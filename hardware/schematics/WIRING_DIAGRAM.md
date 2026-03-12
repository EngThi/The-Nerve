# The Nerve – Wiring Diagram

Complete wiring reference for all components listed in `BOM.csv`. All signal levels are **3.3V** unless noted.

---

## MCU: ESP32-S3 ProS3 (U_MCU)

> Unexpected Maker ProS3 – [Adafruit #6398](https://www.adafruit.com/product/6398)

All peripherals connect to the ESP32-S3 ProS3 via its labeled GPIO header.

---

## 1. Hall Effect Joystick (JOY1 – VGBUS B0CXDTGXZP)

| Joystick Pin | ESP32-S3 Pin | Notes |
|---|---|---|
| VCC | 3.3V | Regulated from onboard LDO |
| GND | GND | |
| X-AXIS (Analog) | IO1 | ADC Channel |
| Y-AXIS (Analog) | IO2 | ADC Channel |
| BTN (Click) | IO3 | Internal Pull-UP; active LOW |

> **Pull-up:** IO3 uses the ESP32-S3 internal pull-up (enabled in firmware).

---

## 2. Quadrature Encoder (ENC_MECH or ENC_OPT) + LS7183N-S Decoder (U_DEC)

The raw encoder output feeds through the **LS7183N-S** (ID 12 in BOM) quadrature decoder IC before reaching the ESP32-S3. This offloads pulse counting from the firmware.

### Encoder → LS7183N-S

| Encoder Pin | LS7183N-S Pin | Notes |
|---|---|---|
| A (Phase A) | QA (Pin 3) | |
| B (Phase B) | QB (Pin 4) | |
| VCC | VDD (Pin 8) | 3.3V (Alps) or 5V (Bourns—use level shifter) |
| GND | GND (Pin 1) | |

> ⚠️ **Optical Encoder (Bourns ENA1J-B28):** Requires 5V supply (Pin 8). Use a 3.3V↜5V level shifter on A/B lines going into LS7183N-S if using 3.3V logic side.

### LS7183N-S → ESP32-S3

| LS7183N-S Pin | ESP32-S3 Pin | Notes |
|---|---|---|
| QU (CW pulse, Pin 5) | IO15 | Pull-UP; CW tick |
| QD (CCW pulse, Pin 6) | IO16 | Pull-UP; CCW tick |

### Encoder Push-Button

| Encoder BTN Pin | ESP32-S3 Pin | Notes |
|---|---|---|
| BTN | IO14 | Internal Pull-UP; active LOW |
| GND | GND | |

---

## 3. OLED Display (DISP1 – Waveshare 1.5" RGB SPI 128×128)

| OLED Pin | ESP32-S3 Pin | Notes |
|---|---|---|
| VCC | 3.3V | |
| GND | GND | |
| DIN (MOSI) | IO35 | SPI Data |
| CLK | IO36 | SPI Clock |
| CS | IO37 | Chip Select (active LOW) |
| DC | IO38 | Data/Command select |
| RST | IO39 | Reset (active LOW) |

---

## 4. RGB LED (LED_RGB – XL-A504RGBW, Common Cathode)

Each channel uses a current-limiting resistor per BOM.

| LED Pin | Resistor | ESP32-S3 Pin | Notes |
|---|---|---|---|
| R (Anode) | R1 – 220Ω | IO7 | Active HIGH |
| G (Anode) | R3 – 220Ω | IO8 | Active HIGH |
| B (Anode) | R7 – 220Ω | IO9 | Active HIGH |
| Cathode | — | GND | Common cathode |

---

## 5. Passive Buzzer (BUZ – QMB-09B-03)

| Buzzer Pin | Connection | Notes |
|---|---|---|
| + | IO10 (via R5 – 330Ω) | Active HIGH |
| − | GND | |

> **R5 (330Ω)** limits current and protects the GPIO output.

---

## 6. Cherry MX Blue Switch (SW_MECH)

| Switch Pin | ESP32-S3 Pin | Notes |
|---|---|---|
| Pin 1 | IO4 | Internal Pull-UP; active LOW |
| Pin 2 | GND | |

---

## 7. Illuminated Toggle Switch – Missile Switch (SW_MISSILE – Adafruit 3306)

| Toggle Pin | Connection | Notes |
|---|---|---|
| COM | GND | |
| NO (Normally Open) | IO5 | Internal Pull-UP; active LOW |
| LED + | 3.3V (via R4 – 2kΩ) | Built-in LED |
| LED − | GND | R4 limits LED current |

---

## 8. SPDT Power Slide Switch (SW1)

The slide switch interrupts the **battery positive rail** directly – not connected to any GPIO.

| Switch Pin | Connection |
|---|---|
| COM | LiPo Battery (+) via JST 2-Pin |
| NO | VIN / 5V rail of ESP32-S3 ProS3 |
| NC | Not connected |

---

## 9. LiPo Battery

| Battery Pin | Connection | Notes |
|---|---|---|
| + | SW1 COM | Through power slide switch |
| − | GND | |

> **Configuration A (3000mAh, JST 1.25mm):** Requires a JST 1.25mm → JST 2.0mm adapter cable.
> **Configuration B (2200mAh, JST 2.0mm):** Plugs directly into onboard JST connector (B2B-PH-K-S, ID 6 in BOM).

---

## 10. Decoupling & Filter Capacitors

| Designator | Value | Placement |
|---|---|---|
| C1 (qty 20 available) | 10µF 0805 | One across each VCC/GND near IC power pins |
| C2, C3 | 100nF 0603 | Across VCC/GND at LS7183N-S and joystick |
| C4 | 100µF radial | Main bulk cap on 3.3V rail |

---

## 11. Screw Terminals (U1–U4) and Expansion Header (U5)

Four **6-pin screw terminals (KEFA KF128-2.54-6P)** and one **8-pin ZX-HY2.0 connector** provide break-out points for additional modules.

| Connector | Typical Use |
|---|---|
| U1 | Encoder interface (A, B, BTN, VCC, GND, NC) |
| U2 | Joystick interface (X, Y, BTN, VCC, GND, NC) |
| U3 | Switch breakout (Cherry, Missile, spare GPIOs) |
| U4 | LED + Buzzer interface (R, G, B, BUZ, VCC, GND) |
| U5 (8-pin ZX-HY2.0) | Expansion (I2C, extra ADC, future sensors) |

---

## Summary Pinout Table

| ESP32-S3 Pin | Signal | Component |
|---|---|---|
| IO1 | JOY_X (analog) | Hall Effect Joystick X |
| IO2 | JOY_Y (analog) | Hall Effect Joystick Y |
| IO3 | JOY_BTN | Joystick click |
| IO4 | SW_CHERRY | Cherry MX Blue |
| IO5 | SW_MISSILE | Illuminated Toggle |
| IO7 | LED_R | RGB LED Red (via 220Ω) |
| IO8 | LED_G | RGB LED Green (via 220Ω) |
| IO9 | LED_B | RGB LED Blue (via 220Ω) |
| IO10 | BUZZER | Passive Buzzer (via 330Ω) |
| IO14 | ENC_BTN | Encoder push-button |
| IO15 | ENC_A (QU) | LS7183N-S CW output |
| IO16 | ENC_B (QD) | LS7183N-S CCW output |
| IO35 | OLED_MOSI | SPI Data |
| IO36 | OLED_CLK | SPI Clock |
| IO37 | OLED_CS | OLED Chip Select |
| IO38 | OLED_DC | OLED Data/Command |
| IO39 | OLED_RST | OLED Reset |
| 3.3V | VCC | All 3.3V peripherals |
| GND | GND | Common ground |
