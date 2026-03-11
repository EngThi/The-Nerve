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
| | **TOTAL** | **$241.02** |

> **Why is the JLCPCB line so high?**
> The $107.04 JLCPCB cost is not just the bare board. It covers:
> - **PCB fabrication** (5 copies, white solder mask, HASL finish)
> - **PCBA — automated SMD assembly** for all LCSC Basic Parts (passives, connectors, buzzer, decoder IC, RGB LED, capacitors, resistors)
> - **Pick & Place engineering fee** charged per unique component type
> - **International shipping** to Brazil
> - A coupon was applied, reducing the original quote
>
> The LS7183N-S decoder IC was out of stock at JLCPCB during checkout and was **removed from the PCBA order** to avoid halting production — it will be hand-soldered separately after delivery.

> **Why do some unit prices differ from BOM.csv?**
> `BOM.csv` lists LCSC **reference unit prices** (e.g., Waveshare OLED at $23.99 MSRP). The actual Waveshare storefront checkout came to $16.99, and Mouser BR pricing for the encoders differed from the individual Mouser USA list prices. Real checkout totals always win over catalog estimates.

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

## 📂 Firmware, CAD, and Project Structure

To resolve ambiguity and make the project easier to navigate, please note the following:

- **Firmware:** The official firmware is written in **MicroPython** for the ESP32-S3. The main entry point is `firmware/main.py`. This provides a lightweight and easily modifiable foundation. The previous Rust-based firmware has been removed to avoid confusion.

- **3D CAD Files:** The `hardware/3d_models/` directory contains all necessary files for the enclosure, including the original **`.step`** file for easy modification and **`.stl`** files for direct 3D printing.

The project is organized as follows:
```text
.
├── BOM.csv                  <-- Official Bill of Materials (LCSC + External parts)
├── README.md                <-- This file
├── hardware/
│   ├── 3d_models/           # Enclosure source (.step) and print-ready (.stl) files
│   ├── fabrication/         # Production files (Gerbers, BOM, Pick & Place)
│   ├── pcb/                 # PCB project files (KiCad)
│   └── schematics/          # PDF schematic + wiring diagram
├── firmware/
│   └── main.py              # Official MicroPython firmware for the ESP32-S3
└── automation/              # Host integration (e.g., n8n flows)
```

## Manufacturing Preview
![JLCPCB Checkout](hardware/fabrication/JLCPCB_Checkout.png)

_Designed for those who need more than just a keyboard shortcut_
