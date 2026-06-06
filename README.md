# The Nerve Automation Motherboard

![The Nerve Hero Render](assets/renders/tinkercad_top_view.png)

> [!IMPORTANT]
> Reviewer, this project is a custom board placed in Tier 3. To stay within the $100 budget including international shipping fees and taxes, Version A (Round TFT) is the primary build configuration. All components are hand-soldered.

[![Hardware License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

The Nerve is a modular controller for automation workflows and video pipelines. It uses an ESP32-S3 for native Wi-Fi, Bluetooth, and USB HID support.

[Specs](#hardware) | [Logs](JOURNAL.md) | [Budget](BLUEPRINT_BUDGET.md) | [Production](hardware/production/)

---

## Hardware Design

The PCB was designed in EasyEDA and the enclosure in OnShape.

### Enclosure Design
![Enclosure Back View](assets/renders/tinkercad_back_view.png)
- [OnShape Public Link](https://cad.onshape.com/documents/f5fe8f1a3f0d54ab7cd3f1d7/w/a16133ebbda184e0e50a9073/e/bf72140826f3054b8f947155?renderMode=0&uiState=6a2071693fc56d9f8f5e1dc7)

### PCB Layout
![PCB Bottom Layout](assets/journal/PCB_Layout_Bottom.png)
![PCB Render](assets/renders/Board.png)

### Core Parts (Version A)
| Part | Description |
| :--- | :--- |
| **ESP32-S3 Olimex** | Native USB HID and built-in LiPo charging. |
| **K-Silver JH16** | Hall Effect joystick sensor. |
| **LS7183N-S IC** | Hardware quadrature decoder. |
| **GC9A01 Round TFT** | 1.28 inch SPI display. |
| **1800mAh Battery** | Standalone power source. |

---

## Schematic

![Schematic Diagram](assets/diagrams/Schematic.png)

---

## Build and Budget

The total delivered cost for Version A is **$99.77**.

Detailed evidence can be found in the [Hardware Budget](BLUEPRINT_BUDGET.md).

### Evidence Gallery
![AliExpress Proof](assets/final_proofs/AliExpress_Final_Cart.png)
![JLCPCB Proof](assets/final_proofs/JLCPCB_Final_Cart.png)
![LCSC Proof](assets/final_proofs/LCSC_Final_Cart.png)
![Shopee Proof](assets/final_proofs/Shopee_Final_Cart.png)

---

_Designed by ChefThi for Hack Club Blueprint._
