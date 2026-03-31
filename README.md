# The Nerve – ESP32-S3 Wireless Automation Node

**The Nerve** is a standalone hardware controller built to trigger webhooks and macros over Wi-Fi. It uses an ESP32-S3 to send commands directly to services like n8n or local APIs, and also works as a USB HID device (keyboard/mouse) for PC shortcuts.

[Technical Specs](#specs) | [Build Logs](JOURNAL.md) | [Budget](BLUEPRINT_BUDGET.md) | [Wiring Diagram](hardware/schematics/WIRING_DIAGRAM.md)

---

![Top View](assets/renders/tinkercad_top_view.png)
![Back View](assets/renders/tinkercad_back_view.png)

---

## What it does

Most macro pads need a computer and background software running to do anything. I built The Nerve to be independent. It connects to Wi-Fi and talks to my automation server (n8n) directly.

- **Standalone triggers:** Hit the mechanical switch to start a server-side pipeline.
- **Hybrid control:** Hall Effect joystick for XY movement, encoder for precise scrolling.
- **Portable:** Runs on a 3000mAh LiPo battery, so it works anywhere without a USB cable.

---

## Hardware Breakdown <a name="specs"></a>

| Component | Choice | Why |
| :--- | :--- | :--- |
| **MCU** | ESP32-S3 ProS3 | Needed native USB HID for the Panic Button and built-in LiPo charging. |
| **Joystick** | K-Silver JH16 Hall Effect | Analog joysticks drift badly over time; this one stays centered. |
| **Display** | SSD1351 1.5" OLED (SPI) | SPI version for fast refreshes to show API feedback and battery level. |
| **Encoder logic** | LS7183N-S IC | Dedicated chip to count encoder pulses so the ESP32 doesn't skip steps under load. |
| **Main button** | Cherry MX Blue | The "Panic Button". Loud, tactile click for critical commands. |
| **Power** | 3000mAh LiPo | Required for standalone wireless operation away from a desk. |

---

## Assembly & Wiring

### Making the Board

- **PCB:** 2-layer custom board from JLCPCB. Small 0603 passives are factory-soldered (PCBA). Through-hole parts (ESP32-S3, JST connectors, screw terminals) are hand-soldered by me.
- **Connectors:** KF128 screw terminals and JST-PH headers. Nothing is permanently glued or soldered to the case, so individual parts can be swapped without desoldering the whole board.

### Wiring Diagram

The PCB is the central hub. All external inputs (joystick, screen, buttons) mount to the 3D-printed case and connect back to the board via wires.

> [View the external wiring map](hardware/schematics/WIRING_DIAGRAM.md) — shows exactly which wire goes where for assembly.

---

## Budget

Total build cost: **$122.27** (merchandise only).

Tier 3 optimization: swapped boutique parts for LCSC/AliExpress alternatives (EC11 encoder, K-Silver joystick) to stay under the limit without compromising function. Full breakdown with cart screenshots in [BLUEPRINT_BUDGET.md](BLUEPRINT_BUDGET.md).

| Vendor | Amount | What |
| :--- | :--- | :--- |
| Adafruit | $30.45 | ESP32-S3 ProS3 + Missile Switch |
| AliExpress | $38.33 | Encoder, OLED, Joystick, Cherry MX, Battery |
| JLCPCB | $48.00 | PCB fabrication + SMT assembly |
| LCSC | $5.49 | Terminals, JST connectors, passives |

---

## Project Structure

- `/firmware` — MicroPython code for Wi-Fi webhooks and USB HID
- `/hardware` — Gerber files, 3D STLs, wiring diagram, OnShape enclosure link
- `/assets` — Renders, journal photos, cart screenshots
- `JOURNAL.md` — Full build log with time spent per session
- `BLUEPRINT_BUDGET.md` — Itemized budget with proof-of-purchase screenshots

---

_Developed for Hack Club Blueprint 2026. Designed by @EngThi._
