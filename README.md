# The Nerve Automation Motherboard

> ![IMPORTANT]
> Reviewer, this project of mine is a custom board, I've placed it in Tier 3. And to fit within the $100 budget, I removed the PCBA service, so I'll solder everything by hand.

[![Hardware License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

I created The Nerve to control my automation and video systems/pipelines because keeping everything on the web was kind of **boring**, and also because I like n8n, I thought of using it to control my workflows from webhooks. Being an ESP32, it has native Wi-Fi and Bluetooth. And in the case of this S3 version, having more memory and better processing, I can orchestrate more complex pipelines and workflows. With the OLED I can get instant visual feedback on the things I'm working with, and being RGB I can test assets and different types of renderings without needing an external monitor, in addition to other modes. The HID interface via USB allows me to control and debug a server or homelab (I decided I'm going to have one soon, I don't know when, but I will). Testing and querying data with greater precision.

The parts outside the PCB serve as physical and tactile nodes for different things: sending important things that need double confirmation (the Missile Switch), the Joystick and Encoder allow me to have fine control over video editing, control other hardware, and the mechanical feedback, which is cool. This last one is through the MX switch.

[Specs](#hardware) | [Logs](JOURNAL.md) | [Budget](BLUEPRINT_BUDGET.md) | [Production](hardware/production/)

---
## What is this? 

I like modularity and preparing the groundwork for future upgrades and changes. That's why I designed **The Nerve** as a modular node where, through JSTs and screw terminals, it's possible to replace components if they break or reach the end of their lifespan. Whether you're in a different mood at a certain time or simply want to experiment with variations of those parts (as long as they fit and are compatible with the main system's electrical system). The 3000mAh battery allows you to work on all of this without needing to be plugged into an outlet.

## Hardware Design

I designed the PCB in EasyEDA and the enclosure in OnShape. The board acts as a central hub for panel-mounted sensors and possible external components.

### PCB Layout
![PCB Layers](assets/journal/Trilhas.png)
![PCB Render](assets/renders/Board.png)

### Parts
| Part | Why |
| :--- | :--- |
| **ESP32-S3 ProS3** | Native USB HID + built-in LiPo charging. |
| **K-Silver JH16** | Hall Effect sensor (no drift). |
| **LS7183N-S IC** | Hardware quadrature decoder to offload the MCU. |
| **3000mAh Battery** | Required for standalone wireless operation. |

---

## Build & Budget

The hardware cost is **$**.

I optimized the budget by removing the factory assembly service (PCBA). I will be hand-soldering every component myself—including the 0603 SMT resistors and capacitors—to demonstrate technical proficiency and keep the project within the $100 limit.

### External Wiring Guide
![External Wiring Guide](assets/diagrams/EXTERNAL_WIRING_GUIDE.png)
*Detailed map for hand-connecting external components*

---

_Designed by @EngThi for Hack Club Blueprint._