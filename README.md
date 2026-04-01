# The Nerve – Custom Wireless Automation Controller

> [!IMPORTANT]
> **Note to Reviewers:** This is a **custom hardware** project (Tier 3). I designed the PCB and the 3D enclosure from scratch. The components in the cart (Joystick, Encoder, OLED) are panel-mounted to the case and hand-wired to the motherboard terminals to prevent mechanical stress on the board. The 3000mAh battery is required for **standalone Wi-Fi automation** (sending webhooks without a host PC).

[![Hardware License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/EngThi/The-Nerve?include_prereleases)](https://github.com/EngThi/The-Nerve/releases)

**The Nerve** is a standalone hardware controller built to trigger webhooks and macros over Wi-Fi. It uses an ESP32-S3 to send commands directly to services like n8n or local APIs, and also works as a USB HID device (keyboard/mouse) for PC shortcuts.

[**Technical Specs**](#specs) | [**Build Logs**](JOURNAL.md) | [**Budget**](BLUEPRINT_BUDGET.md) | [**Manufacturing**](#production)

---

![Top View](assets/renders/tinkercad_top_view.png)
![Back View](assets/renders/tinkercad_back_view.png)

---

## Technical Specifications <a name="specs"></a>

| Component | Part / Protocol | Purpose |
| :--- | :--- | :--- |
| **MCU** | **ESP32-S3 ProS3** (Dual-core 240MHz) | Native Wi-Fi for Webhooks + USB HID Keyboard/Mouse. |
| **Quadrature Decoder** | **LS7183N-S** IC | Offloads high-speed pulse counting from the MCU. |
| **Display** | **SSD1351** 1.5" RGB OLED (SPI) | High-speed UI for menus and API status feedback. |
| **Primary Input** | **K-Silver JH16** Hall Effect Joystick | Zero-drift electromagnetic XY control. |
| **Rotation** | **EC11** Quadrature Encoder | Precision scroll wheel for timeline/parameter control. |
| **Execution** | **Cherry MX Blue** Mechanical Switch | Tactile feedback for critical command execution. |
| **Power** | **3000mAh LiPo** (3.7V) | Mandatory for standalone wireless operation. |

---

## Budget & Cost (Tier 3 Optimized)

The total requested base budget is **$122.27**. 
*Note: Regional Brazilian import taxes (~$40) and international shipping are documented in the [BLUEPRINT_BUDGET.md](BLUEPRINT_BUDGET.md).*

| Vendor | Price | Note |
| :--- | :--- | :--- |
| **Adafruit** | $30.45 | ESP32-S3 ProS3 + Missile Switch. |
| **AliExpress** | $38.33 | Encoder + OLED + Joystick + Cherry MX + Battery. |
| **JLCPCB** | $48.00 | Custom PCB Fabrication + SMT PCBA Service. |
| **LCSC** | $5.49 | Terminals, JST Connectors, and Passive components. |

---

## Assembly & Wiring

### Strategy
This is a **Custom Hardware** project. I designed the PCB and the 3D enclosure specifically for this use case.
*   **Factory PCBA:** JLCPCB handles the SMT soldering of small 0603 passives and the status LED.
*   **Hand-Wiring:** All major inputs (Joystick, Encoder, OLED) are panel-mounted to the 3D case and hand-wired to the PCB terminals to ensure mechanical durability.
*   **Manual Soldering:** Through-hole parts (ESP32-S3, JST connectors, terminals) are hand-soldered by me.

### Wiring Diagram
![The Nerve External Wiring Guide](assets/diagrams/EXTERNAL_WIRING_GUIDE.png)
*Detailed wiring reference for hand-connecting external sensors to the motherboard. See [WIRING_DIAGRAM.md](hardware/schematics/WIRING_DIAGRAM.md) for pinout details.*

---

## Manufacturing & Files <a name="production"></a>

Ready-to-order files and 3D models:
*   **Production:** [Gerbers & Pick&Place](hardware/production/)
*   **3D Models:** [STL & STEP](hardware/3d_models/)
*   **Firmware:** [MicroPython Source](firmware/)

---

_Developed for Hack Club Blueprint 2026. Designed by @EngThi._
