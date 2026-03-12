# 🧠 The Nerve – Modular Input Panel

> [!IMPORTANT]
> **REVIEWS NOTE:** The original banner/logo submitted to the Blueprint review appeared disproportionate and did not display the full design as intended. I initially believed I could edit the banner post-submission, but that was not the case.
>
> **The official hero image for the project is actually the board render below:**
>
> ![The Nerve Official Board Render](assets/renders/Board.png)

![The Nerve PCB](assets/renders/Frontal_View.png)

![The Nerve Project Render](assets/renders/the_nerve_render_v2.png)

> **Project Status:** Hardware Frozen / Firmware Development (ESP32-S3)

**The Nerve** is a tactile command center created to bring physical control back to digital workflows. Initially designed to automate video production pipelines (n8n + FFmpeg), its open hardware architecture makes it a powerful universal controller for developers, editors, and creators.

It bridges the gap between a macro pad and a fully programmable cyberdeck interface.

## 💰 Real Project Cost (Actual Checkout Totals)

The table below reflects the **actual amounts paid at checkout per vendor** — not just component unit prices. Each subtotal includes the vendor's shipping fee, any applicable taxes, and minimum order quantities (MOQ) where they apply.

| Vendor | Items Purchased | Checkout Total |
| :--- | :--- | ---: |
| **Adafruit** | ESP32-S3 ProS3 + Illuminated Toggle Switch | $30.45 |
| **Amazon** | Hall Effect Joystick + Silicone Wire Kit + 2× LiPo Batteries | $38.94 |
| **Waveshare** | 1.5" RGB OLED Display | $16.99 |
| **Mouser** | Optical Encoder (Bourns 64PPR) + Mechanical Encoder (Alps 15PPR) | $47.10 |
| **MechanicalKeyboards** | Cherry MX2A Blue Switch | $0.50 |
| **JLCPCB** | PCB Fabrication + PCBA (automated assembly) + Shipping (with coupon) | $107.04 |
| **LCSC (Loose Parts)** | Screw & Expansion Connectors | $17.45 |
| | **TOTAL** | **$258.47** |

### 🛠️ Minimum Cost to Replicate (Hardware Only)
If you want to build this project yourself, the pure cost of the hardware **without shipping fees, import taxes, or JLCPCB engineering fees** is roughly **~$198.62**. This assumes you purchase the exact quantities needed for a single board without extra MOQs where avoidable.
- Pure PCB/PCBA Cost: ~$48.00
- Pure Component Cost: ~$150.62

> **Why is the JLCPCB line so high?**
> The $107.04 JLCPCB cost is not just the bare board. It covers:
> - **PCB fabrication** (5 copies, white solder mask, HASL finish)
> - **PCBA — automated SMD assembly** for all LCSC Basic Parts (passives, connectors, buzzer, decoder IC, RGB LED, capacitors, resistors)
> - **Pick & Place engineering fee** charged per unique component type
> - **International shipping** to Brazil
> - A coupon was applied, reducing the original quote
>
> The LS7183N-S decoder IC was out of stock at JLCPCB during checkout and was **removed from the PCBA order** to avoid halting production — it will be hand-soldered separately after delivery.

> **Why do some unit prices differ from hardware/fabrication/the_nerve_bom.csv?**
> `hardware/fabrication/the_nerve_bom.csv` lists LCSC **reference unit prices** (e.g., Waveshare OLED at $23.99 MSRP). The actual Waveshare storefront checkout came to $16.99, and Mouser BR pricing for the encoders differed from the individual Mouser USA list prices. Real checkout totals always win over catalog estimates.

## 🧱 Hardware Stack
Built around the **ESP32-S3 ProS3** for native USB, Wi-Fi, and Bluetooth capabilities.

- **Core:** Unexpected Maker ESP32-S3 ProS3 (Dual-core 240MHz, 16MB Flash).
- **Visual Feedback:**
  - **OLED:** Waveshare 1.5" RGB SPI (128x128) for real-time status, menus, and API data.
  - **RGB LED:** Immediate visual indications (e.g., server status, active recording).
- **Encoder:** High-precision Optical (Bourns 64PPR) and Mechanical (Alps 15PPR) for diverse tactile feedback prototyping.
- **Hall Effect Joystick:** Analog control without drift (Mouse/XY parameters).
- **Mechanical Switches:** Cherry MX Blue (Clicky) for satisfying execution.
- **Missile Switch:** Safety-covered toggle for critical actions (Deploy/Render).
- **Audio Feedback:** Passive buzzer for audible alerts.

## 🔌 Modular Architecture
**Important Note:** The PCB shown in the renders acts as a "Motherboard". To prevent mechanical stress on the PCB and allow for enclosure flexibility, all major interfaces (Joystick, Encoders, Switches, OLED) are NOT surface-mounted. They are **hand-wired** to the PCB using a flexible silicone wire kit via the onboard screw terminals and JST connectors.

The PCB features **screw terminals and JST connectors**, allowing sensors and inputs to be swapped without desoldering.

- **Universal 6-pin Interfaces (U1–U4):** Supports 3.3V and 5V peripherals.
- **8-pin Expansion Header (U5):** ZX-HY2.0 connector for additional modules.
- **Battery Ready:** Integrated LiPo management for wireless operation (JST 2-Pin).

See [`hardware/schematics/WIRING_DIAGRAM.md`](hardware/schematics/WIRING_DIAGRAM.md) for a complete wiring reference.

## 📂 Firmware, CAD, and Project Structure

To make the project easy to navigate and replicate, please note the following:

- **PCB Design:** The board was designed in **EasyEDA**. The source file (`.json`) is located in the `hardware/pcb/` folder, allowing anyone to open and modify it.

- **Firmware:** The official firmware is written in **MicroPython** for the ESP32-S3. The main entry point is `firmware/main.py`.

- **3D CAD Files:** The `hardware/3d_models/` directory contains all enclosure files, including the original **`.step`** file for modification and **`.stl`** files for 3D printing.

The project is organized as follows:
```text
.
├── hardware/fabrication/the_nerve_bom.csv                  <-- Main Bill of Materials
├── README.md                <-- This file
├── hardware/
│   ├── 3d_models/           # Enclosure .step and .stl files
│   ├── fabrication/         # Gerber, BOM, and Pick & Place files for manufacturing
│   ├── pcb/                 # EasyEDA project source (.json)
│   └── schematics/          # PDF schematic and wiring diagram
├── firmware/
│   └── main.py              # Official MicroPython firmware
└── automation/              # Host integration (e.g., n8n flows)
```

## Manufacturing Preview
![JLCPCB Checkout](hardware/fabrication/JLCPCB_Checkout.png)

_Designed for those who need more than just a keyboard shortcut_
