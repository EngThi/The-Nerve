# 🧠 The Nerve – Custom Workflow Controller

**The Nerve** is a custom USB and Wi-Fi input device designed to trigger automations (n8n, Python scripts, or hotkeys). It uses an ESP32-S3 to act as a standalone controller that can send commands directly to webhooks or act as a standard USB HID keyboard/mouse.

### 🎨 Hardware Overview
![The Nerve Top View](assets/renders/tinkercad_top_view.png)
![The Nerve Back View](assets/renders/tinkercad_back_view.png)

### 🧩 PCB Design
![The Nerve PCB](assets/renders/Frontal_View.png)

> **Project Status:** Hardware Design Complete / Firmware in MicroPython.

---

## 💰 Project Cost & Components

The base cost for components is **$141.22**. For builders in **Brazil**, the total is **$179.27** due to local import taxes and international shipping (see [AliExpress Cart](assets/journal/AliExpress_Cart_New.png)).

| Vendor | Items Purchased | Price | Purpose |
| :--- | :--- | :--- | :--- |
| **Adafruit** | ESP32-S3 ProS3 | $26.50 | Main MCU with native USB and Wi-Fi. |
| **AliExpress** | Optical Encoder | $27.68 | High-precision knob for timeline scrolling/zoom. |
| **AliExpress** | 1.5" RGB OLED | $11.93 | Display for menus and API feedback. |
| **AliExpress** | Hall Joysticks (2x) | $7.39 | Analog XY control for mouse/brush size. |
| **AliExpress** | Cherry MX Switches | $5.74 | Mechanical execution button (Panic/Push). |
| **Amazon** | LiPo Battery | $9.99 | 3000mAh for portable use. |
| **JLCPCB** | PCB + PCBA | $36.04 | Custom board fabrication and SMD assembly. |
| **LCSC** | Connectors/Parts | $12.00 | Terminals and JST headers for wiring. |

### 🛠️ Assembly Strategy
This is **not** a devboard project. I designed the PCB and the case specifically for this use case.
*   **Factory PCBA:** JLCPCB handles the SMT soldering of small passives (0603 resistors/capacitors) and the RGB status LED.
*   **Manual Soldering:** I am hand-soldering all through-hole components, including the ESP32-S3, screw terminals, and JST headers. 
*   **Case Assembly:** All inputs (Joystick, Encoders, OLED) are panel-mounted to the 3D-printed case and hand-wired to the PCB terminals to prevent mechanical stress on the board.

---

## 🔌 Hardware Specs
- **MCU:** ESP32-S3 (Dual-core 240MHz, 16MB Flash).
- **Inputs:** 1x Optical Encoder, 1x Hall Effect Joystick, 1x Mechanical Switch, 1x Toggle Switch.
- **Feedback:** 1.5" RGB OLED (128x128), 1x RGB LED, 1x Passive Buzzer.
- **Connectivity:** USB-C (HID), Wi-Fi (HTTP/JSON), Bluetooth.

---

## 📂 Installation & Structure

### ⚡ Firmware
The device runs **MicroPython**. 
1. Flash the ESP32-S3 with the [MicroPython firmware](https://micropython.org/download/ESP32_GENERIC_S3/).
2. Upload `firmware/main.py` using Thonny or ampy.
3. The device will start sending JSON events over Serial and Wi-Fi.

### 📁 Folders
```text
.
├── the_nerve_bom.csv        # Component list
├── hardware/
│   ├── 3d_models/           # Case STL and STEP files
│   ├── fabrication/         # Gerber and Pick&Place files
│   └── schematics/          # Wiring and PDF Schematic
└── firmware/
    └── main.py              # MicroPython source code
```

_Custom hardware for specific workflows._
