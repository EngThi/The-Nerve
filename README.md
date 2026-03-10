# 🧠 The Nerve – Modular Input Panel

> [!IMPORTANT]
> **REVIEWS NOTE:** The original banner/logo submitted to the Blueprint review appeared disproportionate and did not display the full design as intended. I initially believed I could edit the banner post-submission, but that was not the case.
>
> **The official hero image for the project is actually the board render below:**
>
> ![The Nerve Official Board Render](Board.png)

![The Nerve PCB](assets/renders/Frontal_View.png)

![The Nerve Project Render](assets/renders/the_nerve_render_v2.png)

> **Project Status:** Hardware Frozen / Firmware Development (ESP32-S3)

**The Nerve** is a tactile command center created to bring physical control back to digital workflows. Initially designed to automate video production pipelines (n8n + FFmpeg), its open hardware architecture makes it a powerful universal controller for developers, editors, and creators.

It bridges the gap between a macro pad and a fully programmable cyberdeck interface.

## 💰 Detailed Project Cost (Excluding Shipping)
Total cost considering all components, hardware options, and wiring listed in the BOM.

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
| 8 | Passive Buzzer QMB-09B-03 (Tray of 5) | 5 | $0.12 | $0.58 |
| 9 | Capacitor 100nF (Set of 2) | 2 | $0.01 | $0.02 |
| 10 | Capacitor 100uF Radial | 1 | $0.01 | $0.01 |
| 11 | LED RGB 5mm XL-A504RGBW (Pack of 10) | 10 | $0.06 | $0.64 |
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
| 23 | Silicone Wire Kit 24AWG BNTECHGO | 1 | $9.98 | $9.98 |
| | **TOTAL** | | | **$171.92** |

## 🧱 Hardware Stack
Built around the **ESP32-S3 ProS3** for native USB, Wi-Fi, and Bluetooth capabilities.

- **Core:** Unexpected Maker ESP32-S3 ProS3 (Dual-core 240MHz, 16MB Flash).
- **Visual Feedback:**
  - **OLED:** Waveshare 1.5" RGB SPI (128x128) for real-time status, menus, and API data.
  - **RGB LED:** Immediate visual indications (e.g., server status, active recording).
- **Encoder:** High-precision Optical (Bourns 64PPR) or Mechanical (Alps 15PPR) scrolling options.
- **Hall Effect Joystick:** Analog control without drift (Mouse/XY parameters).
- **Mechanical Switches:** Cherry MX Blue (Clicky) for satisfying execution.
- **Missile Switch:** Safety-covered toggle for critical actions (Deploy/Render).
- **Audio Feedback:** Passive buzzer for audible alerts.

## 🔌 Modular Architecture
The PCB features **screw terminals and JST connectors**, allowing sensors and inputs to be swapped without desoldering.

- **Universal 6-pin Interfaces (U1–U4):** Supports 3.3V and 5V peripherals.
- **8-pin Expansion Header (U5):** ZX-HY2.0 connector for additional modules.
- **Battery Ready:** Integrated LiPo management for wireless operation (JST 2-Pin).

See [`hardware/schematics/WIRING_DIAGRAM.md`](hardware/schematics/WIRING_DIAGRAM.md) for a complete wiring reference.

## 📂 Project Structure
```text
├── BOM.csv                  <-- Official Bill of Materials (LCSC + External modules)
├── README.md                <-- System documentation
├── hardware/
│   ├── schematics/          # Design files, PDF schematic + wiring diagram
│   ├── pcb/                 # Board layout and routing (KiCad)
│   ├── fabrication/         # Production files (Gerbers, BOM, Pick & Place)
│   └── 3d_models/           # Enclosure STEP + STL files
├── firmware/
│   ├── firmware.py          # Main MicroPython entry point (deploy to ESP32-S3)
│   └── src/                 # Module source files
│       ├── main.py          # Core loop (input handling + display drivers)
│       └── README_FIRMWARE.md
└── automation/              # Host integration (n8n flows)
```

## Manufacturing Preview
![JLCPCB Checkout](hardware/fabrication/JLCPCB_Checkout.png)

_Designed for those who need more than just a keyboard shortcut_
