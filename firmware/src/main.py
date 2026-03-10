# The Nerve – firmware/src/main.py
# Symlinked entry: this file is identical to the root firmware.py
# Deploy EITHER this file OR firmware.py to the ESP32-S3 root as 'main.py'
# See README_FIRMWARE.md for flashing instructions

import board
import busio
import analogio
import digitalio
import usb_hid
import time
import math

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import adafruit_displayio_ssd1306
import displayio
import terminalio
from adafruit_display_text import label

# ─── PIN MAP (matches BOM + PCB silkscreen) ──────────────────────────────────
# Joystick (Hall Effect – VGBUS B0CXDTGXZP)
JOY_X       = board.IO1   # Analog X axis
JOY_Y       = board.IO2   # Analog Y axis
JOY_BTN     = board.IO3   # Click button (active LOW)

# Mechanical Encoder (Alps EC11E15244B2) – via LS7183N-S decoder
ENC_A       = board.IO15  # Decoder QU output (CW)
ENC_B       = board.IO16  # Decoder QD output (CCW)
ENC_BTN     = board.IO14  # Encoder push-button

# Switches
SW_CHERRY   = board.IO4   # Cherry MX Blue (active LOW)
SW_MISSILE  = board.IO5   # Illuminated Toggle (Adafruit 3306, active LOW)
SW_POWER    = board.IO6   # SPDT Slide Switch (power rail, not GPIO-controlled)

# RGB LED (common-cathode, 5mm XL-A504RGBW)
LED_R       = board.IO7
LED_G       = board.IO8
LED_B       = board.IO9

# Buzzer (Passive QMB-09B-03)
BUZZER      = board.IO10

# OLED Display (Waveshare 1.5" RGB SPI 128×128)
OLED_MOSI   = board.IO35
OLED_CLK    = board.IO36
OLED_CS     = board.IO37
OLED_DC     = board.IO38
OLED_RST    = board.IO39
# ─────────────────────────────────────────────────────────────────────────────

# ─── HID devices ─────────────────────────────────────────────────────────────
keyboard = Keyboard(usb_hid.devices)
kbd_layout = KeyboardLayoutUS(keyboard)
mouse = Mouse(usb_hid.devices)
# ─────────────────────────────────────────────────────────────────────────────

# ─── Analog joystick setup ───────────────────────────────────────────────────
joy_x = analogio.AnalogIn(JOY_X)
joy_y = analogio.AnalogIn(JOY_Y)

DEADZONE = 2000   # ~3% of 65535 – prevents drift on neutral position

def analog_to_hid(raw):
    """Map 0–65535 analog value to -127..+127 HID mouse delta."""
    centered = raw - 32768
    if abs(centered) < DEADZONE:
        return 0
    return int(centered / 32768 * 127)
# ─────────────────────────────────────────────────────────────────────────────

# ─── Digital inputs ──────────────────────────────────────────────────────────
def make_input(pin):
    d = digitalio.DigitalInOut(pin)
    d.direction = digitalio.Direction.INPUT
    d.pull = digitalio.Pull.UP
    return d

joy_btn_pin    = make_input(JOY_BTN)
enc_a_pin      = make_input(ENC_A)
enc_b_pin      = make_input(ENC_B)
enc_btn_pin    = make_input(ENC_BTN)
cherry_pin     = make_input(SW_CHERRY)
missile_pin    = make_input(SW_MISSILE)
# ─────────────────────────────────────────────────────────────────────────────

# ─── LED helpers ─────────────────────────────────────────────────────────────
def make_led(pin):
    d = digitalio.DigitalInOut(pin)
    d.direction = digitalio.Direction.OUTPUT
    return d

led_r = make_led(LED_R)
led_g = make_led(LED_G)
led_b = make_led(LED_B)

def set_rgb(r, g, b):
    led_r.value = r
    led_g.value = g
    led_b.value = b
# ─────────────────────────────────────────────────────────────────────────────

# ─── Buzzer helpers ──────────────────────────────────────────────────────────
buzz = digitalio.DigitalInOut(BUZZER)
buzz.direction = digitalio.Direction.OUTPUT

def beep(duration=0.05):
    buzz.value = True
    time.sleep(duration)
    buzz.value = False
# ─────────────────────────────────────────────────────────────────────────────

# ─── Encoder state ───────────────────────────────────────────────────────────
last_enc_a = enc_a_pin.value
enc_pos    = 0
# ─────────────────────────────────────────────────────────────────────────────

# ─── Startup feedback ────────────────────────────────────────────────────────
set_rgb(0, 0, 1)   # Blue = booting
beep(0.1)
time.sleep(0.3)
set_rgb(0, 1, 0)   # Green = ready
# ─────────────────────────────────────────────────────────────────────────────

# ─── Main loop ───────────────────────────────────────────────────────────────
while True:
    # --- Joystick mouse movement ---
    dx = analog_to_hid(joy_x.value)
    dy = analog_to_hid(joy_y.value)
    if dx != 0 or dy != 0:
        mouse.move(x=dx, y=dy)

    # --- Joystick click = left mouse button ---
    if not joy_btn_pin.value:
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.2)

    # --- Quadrature encoder (decoded by LS7183N) = scroll wheel ---
    cur_a = enc_a_pin.value
    if cur_a != last_enc_a:
        if enc_b_pin.value != cur_a:
            enc_pos += 1
            mouse.move(wheel=1)
        else:
            enc_pos -= 1
            mouse.move(wheel=-1)
        last_enc_a = cur_a

    # --- Encoder push = Play/Pause (media key) ---
    if not enc_btn_pin.value:
        keyboard.press(Keycode.SPACE)
        keyboard.release_all()
        beep()
        time.sleep(0.25)

    # --- Cherry MX = custom macro (Ctrl+Shift+R: Render shortcut) ---
    if not cherry_pin.value:
        set_rgb(1, 0, 0)   # Red = executing
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.R)
        keyboard.release_all()
        beep(0.05)
        time.sleep(0.1)
        beep(0.05)
        set_rgb(0, 1, 0)
        time.sleep(0.3)

    # --- Missile switch = DANGER action (Ctrl+Alt+D: deploy/export) ---
    if not missile_pin.value:
        set_rgb(1, 0, 1)   # Magenta = armed
        beep(0.2)
        keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.D)
        keyboard.release_all()
        time.sleep(0.5)
        set_rgb(0, 1, 0)

    time.sleep(0.01)  # 100Hz poll rate
# ─────────────────────────────────────────────────────────────────────────────
