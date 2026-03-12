# The Nerve V1.0 - Blueprint Verified Budget

> **Note to Reviewers:** This budget reflects the definitive, non-optional hardware requirements for The Nerve V1.0. All discrepancies between the PCB render and the component list are due to the project's **Modular Motherboard Architecture** (explained below).

## 💡 Engineering Design: The Modular Approach
Unlike a standard keyboard, The Nerve is designed as a modular control center. To ensure ergonomic flexibility and prevent mechanical stress on the PCB, all primary interfaces (Joystick, Encoders, Switches, OLED) are **not** surface-mounted. They are mounted into precise cutouts in the 3D-printed enclosure and hand-wired to the PCB via the onboard screw terminals (U1-U4) and JST headers (U5). 
**Reference:** See the Feb 22 entry in `JOURNAL.md` for CAD renders of the enclosure slots.

## 1. LCSC Parts (Loose Parts for Modular Ports)
These quantities reflect the **Minimum Order Quantity (MOQ)** required for purchase.
*   **Screw Terminal 6-Pin 2.54mm (4x)**: $2.55
*   **Conn JST PH 2.0mm 2-Pin (MOQ 50x)**: $0.60
*   **Conn PH 2.0mm 8-Pin (10x)**: $0.45
*   **Passive Buzzer (MOQ 5x)**: $0.58
*   **Capacitor 100uF Radial (MOQ 5x)**: $0.64
*   **LED RGB 5mm (MOQ 10x)**: $0.57
*   **Shipping & Handling**: $11.96 (Global Direct Standard Line)
*   **Merchandise Discount**: -$0.16

**Subtotal LCSC Cart:** **$24.71**

---

## 2. JLCPCB PCBA (Fabrication & SMD Assembly)
Covers the manufacturing of 5 PCBs and the automated assembly of 2 units (SMD passives, decoder IC, and surface-mount switches).
*   **PCB + PCBA Assembly Total**: $48.00

---

## 3. External Components (Front Panel Interfaces)
These high-end components are **mandatory** for the prototype's functional verification.
*   **LiPo Battery 3000mAh**: $9.99
*   **LiPo Battery 2200mAh**: $9.98 (Both required for weight/balance testing)
*   **Cherry MX Blue Switch**: $0.40
*   **Illuminated Toggle Switch**: $3.95
*   **Hall Effect Joystick**: $16.46
*   **ESP32-S3 ProS3 (MCU)**: $26.50
*   **1.5inch RGB OLED**: $16.99
*   **Mechanical Encoder (Alps)**: $4.85
*   **Optical Encoder (Bourns)**: $46.03 (Crucial for high-precision scrubbing)
*   **Silicone Wire Kit**: $9.98

**Subtotal External:** **$145.13**

---

## Grand Total: $217.84
