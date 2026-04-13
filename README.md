# 🧠 The Nerve — Standalone Automation Node

> [!IMPORTANT]
> **Note to Reviewers:** This is a **custom hardware** project (Tier 3). I designed the PCB and the 3D enclosure from scratch. The components in the cart (Joystick, Encoder, OLED) are panel-mounted to the case and hand-wired to the motherboard terminals to prevent mechanical stress on the board. The 3000mAh battery is required for **standalone Wi-Fi automation** (sending webhooks without a host PC).

[![Hardware License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/EngThi/The-Nerve?include_prereleases)](https://github.com/EngThi/The-Nerve/releases)

The Nerve is a custom hardware controller I built to trigger webhooks and macros over Wi-Fi. It uses an ESP32-S3 to talk directly to n8n or local APIs without needing a PC turned on.

[Specs](#hardware) | [Logs](JOURNAL.md) | [Budget](BLUEPRINT_BUDGET.md) | [Production](hardware/production/)

---

![Front](assets/renders/tinkercad_top_view.png)
![Back](assets/renders/tinkercad_back_view.png)

---

## What it is

Most macro pads are just USB keyboards. I designed The Nerve to be a standalone Wi-Fi device. It runs on a 3000mAh battery so I can use it as a remote for my server-side video pipelines.

- **Direct Triggers:** Hits n8n webhooks directly via Wi-Fi.
- **Precision Control:** Hall Effect joystick (no drift) and an EC11 encoder.
- **Visuals:** SSD1351 RGB OLED for real-time API feedback.

---

## Hardware Design <a name="hardware"></a>

I designed the PCB in EasyEDA and the enclosure in OnShape. The board acts as a central hub for panel-mounted sensors.

### PCB Layout
![PCB Layers](assets/journal/Trilhas.png)
![PCB Render](assets/renders/Board.png)

### Parts
| Part | Why |
| :--- | :--- |
| **ESP32-S3 ProS3** | Has native USB HID and built-in LiPo charging. |
| **K-Silver JH16** | Hall Effect sensor. Analog joysticks drift; this one doesn't. |
| **LS7183N-S IC** | Hardware quadrature decoder so the MCU doesn't miss pulses. |
| **3000mAh Battery** | Required for standalone wireless operation. |

---

## Build & Budget

The raw hardware cost is **$122.27**. 

I optimized the budget for Tier 3 by using industrial parts from AliExpress and LCSC. I am hand-soldering all connectors and the MCU, while JLCPCB handles the small SMT passives.

> [!NOTE]
> **Wiring:** All inputs are panel-mounted and hand-wired to the PCB terminals to prevent mechanical stress on the traces. See the [Wiring Guide](assets/diagrams/EXTERNAL_WIRING_GUIDE.png).

---

_Designed by @EngThi for Hack Club Blueprint._
