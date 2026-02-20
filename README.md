![The Nerve PCB](assets/renders/Frontal_View.png)

# 🧠 The Nerve – Modular Input Panel
![The Nerve Project Render](assets/renders/the_nerve_render_v2.png)

> **Project Status:** Hardware Frozen / Firmware Development (ESP32-S3)

**The Nerve** is a tactile command center created to bring physical control back to digital workflows. Initially designed to automate video production pipelines (n8n + FFmpeg), its open hardware architecture makes it a powerful universal controller for developers, editors, and creators.

It bridges the gap between a macro pad and a fully programmable cyberdeck interface.

## 💰 Detailed Project Cost (Excluding Shipping)
Total cost considering all components and hardware options listed in the BOM.

| ID | Item Name | Qty | Unit Price | Subtotal |
| :--- | :--- | :---: | :--- | :--- |
| - | **Custom PCB (JLCPCB)** | 1 | $9.37 | **$9.37** |
| 1 | Capacitor 10uF 0805 | 1 | $0.01 | $0.01 |
| 2 | Resistor 220Ω (Set of 3) | 3 | $0.01 | $0.03 |
| 3 | Resistor 330Ω | 1 | $0.01 | $0.01 |
| 4 | Resistor 2kΩ | 1 | $0.01 | $0.01 |
| 5 | Screw Terminals 6-Pin (Set of 4) | 4 | $0.64 | $2.56 |
| 6 | JST 2-Pin Battery Conn | 1 | $0.01 | $0.01 |
| 7 | PH 8-Pin 2.00mm Header | 1 | $0.04 | $0.04 |
| 8 | Passive Buzzer | 1 | $0.01 | $0.01 |
| 9 | Capacitor 100nF (Set of 2) | 2 | $0.01 | $0.02 |
| 10 | Capacitor 100uF Radial | 1 | $0.01 | $0.01 |
| 11 | LED RGB 5mm | 1 | $0.01 | $0.01 |
| 12 | Decoder IC LS7183N-S | 1 | $6.32 | $6.32 |
| 13 | SPDT Slide Switch | 1 | $0.08 | $0.08 |
| 14 | LiPo Battery 3000mAh (Option 1) | 1 | $9.99 | $9.99 |
| 15 | LiPo Battery 2200mAh (Option 2) | 1 | $9.98 | $9.98 |
| 16 | Cherry MX Blue Switch | 1 | $0.50 | $0.50 |
| 17 | Illuminated Toggle Switch | 1 | $3.95 | $3.95 |
| 18 | Hall Effect Joystick | 1 | $16.46 | $16.46 |
| 19 | ESP32-S3 ProS3 MCU | 1 | $26.50 | $26.50 |
| 20 | 1.5" RGB OLED Display | 1 | $23.99 | $23.99 |
| 21 | Mechanical Encoder (Alps) | 1 | $4.85 | $4.85 |
| 22 | Optical Encoder (Bourns) | 1 | $46.03 | $46.03 |
| | **TOTAL** | | | **$160.70** |

## 🧱 Hardware Stack
Built around the **ESP32-S3 ProS3[D]** for native USB, Wi-Fi, and Bluetooth capabilities.

- **Core:** Unexpected Maker ESP32-S3 ProS3[D] (Dual-core 240MHz, 16MB Flash).
- **Visual Feedback:**
    - **OLED:** Waveshare 1.5" RGB SPI (128x128) for real-time status, menus, and API data.
    - **RGB LED:** Immediate visual indications (e.g., server status, active recording).
- **Encoder:** High-precision Optical/Mechanical scrolling options.
- **Hall Effect Joystick:** Analog control without drift (Mouse/XY parameters).
- **Mechanical Switches:** Cherry MX Blue (Clicky) for satisfying execution.
- **Missile Switch:** Safety-covered toggle for critical actions (Deploy/Render).
- **Audio Feedback:** Passive buzzer for audible alerts.

## 🔌 Modular Architecture
The PCB features **screw terminals and JST connectors**, allowing sensors and inputs to be swapped without desoldering.
- **Universal 6-pin Interfaces:** Supports 3.3V and 5V peripherals.
- **Battery Ready:** Integrated LiPo management for wireless operation.

## 📂 Project Structure
```text
├── BOM.csv <-- Official Bill of Materials (LCSC + External modules)
├── README.md <-- System documentation
├── hardware/
│   ├── schematics/   # Design files and PDF
│   ├── pcb/          # Board layout and routing (KiCad)
│   ├── fabrication/  # Production files (Gerbers, PnP, Checkout)
│   └── 3d_models/    # Enclosure concept (STEP files)
├── firmware/         # ESP32 Logic (Rust/MicroPython)
│   └── src/          # Input handling and display drivers
└── automation/       # Host integration (n8n flows)
```

## Manufacturing Preview
![JLCPCB Checkout](hardware/fabrication/JLCPCB_Checkout.png)

_Designed for those who need more than just a keyboard shortcut_
