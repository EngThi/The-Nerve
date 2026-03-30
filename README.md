# 🧠 The Nerve – Custom Wireless Automation Controller

[![Hardware License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/EngThi/The-Nerve?include_prereleases)](https://github.com/EngThi/The-Nerve/releases)

**The Nerve** is a custom hardware input device designed for standalone workflow automation. Powered by an ESP32-S3, it triggers webhooks (n8n/API) and executes complex macros via Wi-Fi or USB HID without requiring a host computer.

[**Project Vision**](#vision) | [**Technical Specs**](#specs) | [**Manufacturing**](#production) | [**Build Logs**](JOURNAL.md) | [**BOM**](the_nerve_bom.csv)

---

### 🎨 Design & Ergonomics
![The Nerve Top View](assets/renders/tinkercad_top_view.png)
![The Nerve Back View](assets/renders/tinkercad_back_view.png)

---

## 🛠️ Technical Specifications <a name="specs"></a>

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

## 💰 Budget & Cost (Tier 3 Optimized)

The total requested base budget is **$122.27**. 
*Note: Regional Brazilian import taxes (~$40) are documented in the [AliExpress Cart](assets/journal/AliExpress_Cart_New.png).*

| Vendor | Price | Note |
| :--- | :--- | :--- |
| **Adafruit** | $30.45 | ESP32-S3 ProS3 + Missile Switch. |
| **AliExpress** | $38.33 | Encoder + OLED + Joystick + Cherry MX + Battery. |
| **JLCPCB** | $48.00 | Custom PCB Fabrication + SMT PCBA Service. |
| **LCSC** | $5.49 | Terminals, JST Connectors, and Passive components. |

---

## 🔌 Manufacturing & Assembly <a name="production"></a>

### 📁 Production Files
Ready-to-order files are located in [**`hardware/production/`**](hardware/production/):
*   **Gerber:** `the_nerve_gerber.zip` (PCB Manufacturing).
*   **Pick & Place:** `the_nerve_pickandplace.csv` (Automated Assembly).
*   **BOM:** Full list in root [**`the_nerve_bom.csv`**](the_nerve_bom.csv).

### 🛠️ Assembly Strategy
*   **Factory PCBA:** JLCPCB handles the SMT soldering of small 0603 passives and the status LED.
*   **Hand-Wiring:** All major inputs (Joystick, Encoder, OLED) are panel-mounted to the 3D case and hand-wired to the PCB terminals to ensure mechanical durability.
*   **Manual Soldering:** Through-hole parts (ESP32-S3, JST connectors, terminals) are hand-soldered by the designer.

---

## 📜 Wiring Reference
![Wiring Reference](assets/diagrams/Schematic.png)
*Detailed wiring reference for hand-connecting external sensors to the motherboard.*

---

_Designed for standalone automation and tactile control._
