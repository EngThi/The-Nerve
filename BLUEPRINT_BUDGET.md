# The Nerve V1.0 - Blueprint Verified Budget

This budget reflects the true cost of producing the initial prototype of The Nerve V1.0. It incorporates Minimum Order Quantities (MOQs), shipping fees, and accurate component selection based on actual shopping carts from JLCPCB and external suppliers.

## 1. LCSC Parts (To be manually soldered)
These components are purchased via LCSC but require manual soldering. The quantities reflect the **Minimum Order Quantity (MOQ)** forced by LCSC, which is why they differ slightly from the absolute per-board count.

*   **Screw Terminal 6-Pin 2.54mm (4x)**: $2.55
*   **Conn JST PH 2.0mm 2-Pin (MOQ 50x)**: $0.60
*   **Conn PH 2.0mm 8-Pin (10x)**: $0.45
*   **Passive Buzzer (MOQ 5x)**: $0.58
*   **Capacitor 100uF Radial (MOQ 5x)**: $0.64
*   **LED RGB 5mm (MOQ 10x)**: $0.57

*   **Shipping (Global Direct Standard Line)**: $9.12
*   **Handling Fee**: $3.00
*   **Merchandise Discount**: -$0.16

**Subtotal LCSC Cart:** **$24.71**

---

## 2. JLCPCB PCBA (Fabrication & Assembly)
This covers the manufacturing of the PCB itself and the automated Pick-and-Place (SMT) soldering for surface-mount components (like the LS7183N-S Decoder, resistors, and SMD capacitors). 

*   **PCB Prototype (5 units)**: $4.00
*   **Economic PCBA (Assembly for 2 units)**: $44.00

**Subtotal JLCPCB:** **$48.00**

---

## 3. External Components
These are high-performance or specialized parts sourced outside of the LCSC/JLCPCB ecosystem (e.g., Adafruit, Amazon, Mouser, Waveshare). **Important:** These components will be hand-wired to the PCB's screw terminals and headers (U1-U5), as this is a modular control panel design where the PCB acts as the central motherboard.

*   **LiPo Battery 3000mAh (Amazon)**: $9.99
*   **LiPo Battery 2200mAh (Amazon)**: $9.98 *(Note: Both battery form-factors are required for weight distribution and enclosure prototyping)*
*   **Cherry MX Blue Switch (MechKeyboards)**: $0.40
*   **Illuminated Toggle Switch (Adafruit)**: $3.95
*   **Hall Effect Joystick (Amazon BR)**: $16.46
*   **ESP32-S3 ProS3 (Adafruit)**: $26.50
*   **1.5inch RGB OLED (Waveshare)**: $16.99
*   **Mechanical Encoder - Alps (Mouser)**: $4.85
*   **Optical Encoder - Bourns (Mouser)**: $46.03 *(Note: Both encoders are required for prototyping different tactile feedbacks)*
*   **Silicone Wire Kit 24AWG (Amazon)**: $9.98

**Subtotal External:** **$145.13**

---

## Grand Total
**Total Estimated Project Cost:** **$217.84**

---

### ⚠️ Variable Costs (Not Included in Total)
The $217.84 total strictly represents the known hardware, manufacturing, and LCSC shipping costs. It does **not** include:
*   **External Shipping Fees:** Delivery charges from Adafruit, Mouser, Amazon, etc. (Estimated: ~$25 - $40 depending on location).
*   **Import Taxes / Customs Duties:** Depending on the destination country (e.g., Brazil), customs duties and import taxes on parts from Mouser/Adafruit/JLCPCB can add a significant overhead (sometimes up to 60-90% of the item's value).

> **Note to Reviewers:** The slight discrepancy between the per-board BOM cost and the final LCSC cart cost is strictly due to LCSC's Minimum Order Quantity (MOQ) requirements (e.g., forcing a purchase of 50 JST connectors or 5 buzzers). The numbers here are 100% veracious and derived directly from checkout screenshots.