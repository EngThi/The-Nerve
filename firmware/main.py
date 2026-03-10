import machine
import time
import json
from machine import Pin, ADC, PWM

# --- CONFIGURAÇÃO DE PINAGEM (MAPA OFICIAL PROS3) ---

# 1. Joystick (ADC1 - WiFi Safe)
# No ESP32-S3, os ADC1 são os pinos 1 a 10. O range é 12-bits (0 a 4095).
joy_x = ADC(Pin(1))
joy_y = ADC(Pin(2))
joy_sw = Pin(3, Pin.IN, Pin.PULL_UP)

# Atenuação de 11DB permite ler até ~3.1V (Perfeito para Joystick de 3.3V)
joy_x.atten(ADC.ATTN_11DB)
joy_y.atten(ADC.ATTN_11DB)

# 2. Encoder Óptico via LS7183N-S (Pulsos de Hardware)
# O chip LS7 entrega pulsos de UP e DOWN limpos. Não precisamos de debounce de hardware aqui.
enc_up = Pin(15, Pin.IN, Pin.PULL_UP)
enc_dn = Pin(16, Pin.IN, Pin.PULL_UP)
enc_sw = Pin(14, Pin.IN, Pin.PULL_UP)

# 3. Gatilhos Modulares JST
mx_switch = Pin(4, Pin.IN, Pin.PULL_UP)     # Execute (Cherry MX)
missile_sw = Pin(5, Pin.IN, Pin.PULL_UP)    # Safety Toggle
missile_led = Pin(21, Pin.OUT)              # LED da capa do switch

# 4. Feedbacks On-Board (PWM)
# No MicroPython do ESP32, o duty_u16 vai de 0 a 65535 (16 bits)
buzzer = PWM(Pin(18), freq=1000, duty_u16=0)
led_r = PWM(Pin(38), freq=5000, duty_u16=0)
led_g = PWM(Pin(39), freq=5000, duty_u16=0)
led_b = PWM(Pin(40), freq=5000, duty_u16=0)

# --- ESTADO DO SISTEMA ---
hype_level = 50
system_armed = False

def set_led(r, g, b):
    """
    Define a cor do LED RGB.
    Recebe (r,g,b) de 0 a 255 e converte para duty_u16 (0-65535).
    Se o seu LED for Cátodo Comum, maior valor = mais luz.
    Se for Ânodo Comum (como na maioria das devboards), inverta a lógica.
    """
    # Ex: r=255 -> 255 * 257 = 65535
    led_r.duty_u16(int(r * 257))
    led_g.duty_u16(int(g * 257)) 
    led_b.duty_u16(int(b * 257))

def play_alert(freq, duration):
    """Toca um tom no buzzer usando duty_u16 (50% = 32768)"""
    buzzer.freq(freq)
    buzzer.duty_u16(32768) # 50% de duty cycle (volume máximo)
    time.sleep(duration)
    buzzer.duty_u16(0)     # Desliga

# --- LÓGICA DO ENCODER LS7183N (PULSOS) ---
last_up = enc_up.value()
last_dn = enc_dn.value()

print("🎬 THE NERVE V1.0 - PROS3 EDITION ONLINE")
play_alert(2000, 0.2)
set_led(0, 50, 200) # Inicia Azul Cyperpack

while True:
    # 1. Gerenciamento de Segurança (Missile Switch)
    # Supondo que ligado (capa pra cima) feche para GND (0)
    system_armed = not missile_sw.value()
    missile_led.value(1 if system_armed else 0) # Acende LED do Missile se armado

    # 2. Hype Dial (Lógica para o chip LS7183N)
    curr_up = enc_up.value()
    curr_dn = enc_dn.value()
    
    # Detecta a borda de descida (quando o pino vai de 1 para 0)
    if curr_up == 0 and last_up == 1: 
        hype_level = min(100, hype_level + 5)
        # Gradient: 0 = Azul (0,0,255), 100 = Vermelho (255,0,0)
        set_led(int((hype_level/100)*255), 0, int(((100-hype_level)/100)*255)) 
    elif curr_dn == 0 and last_dn == 1: 
        hype_level = max(0, hype_level - 5)
        set_led(int((hype_level/100)*255), 0, int(((100-hype_level)/100)*255))
        
    last_up, last_dn = curr_up, curr_dn

    # 3. Timeline Scrubbing (Joystick)
    # ESP32-S3 ADC retorna 0 a 4095 (12 bits). Centro é ~2048.
    # Lemos read_u16 para ter mais precisão (0-65535) mas read() simples basta.
    # Normalizando ADC (0-4095) para Range de -100 a +100
    try:
        raw_x = joy_x.read()
        raw_y = joy_y.read()
        x_val = int((raw_x - 2048) / 20.48)
        y_val = int((raw_y - 2048) / 20.48)
        
        # Deadzone (ignora movimentos pequenos do dedo)
        if abs(x_val) < 10: x_val = 0
        if abs(y_val) < 10: y_val = 0
    except Exception as e:
        x_val, y_val = 0, 0

    # 4. Gatilho Final (Absolute Cinema Execution - Cherry MX)
    if not mx_switch.value():
        if system_armed:
            msg = {
                "event": "RENDER_NOW",
                "params": {
                    "hype": hype_level,
                    "scrub_x": x_val,
                    "scrub_y": y_val
                },
                "meta": "SHIP_IT"
            }
            print(json.dumps(msg)) # Envia para o n8n via Serial
            set_led(255, 255, 255) # Flash Branco (Cinema effect)
            play_alert(1500, 0.3)
            time.sleep(1) # Impede duplo clique acidental
        else:
            # Alerta de Segurança: Tentativa sem armar
            print(json.dumps({"warning": "SAFETY_LOCK_ACTIVE"}))
            set_led(255, 0, 0)
            play_alert(400, 0.1)
            time.sleep(0.5)

    time.sleep(0.01) # Loop a 100Hz para capturar o encoder rápido