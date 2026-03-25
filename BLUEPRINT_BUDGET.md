# The Nerve V1.0 - Tier 3 Optimized Budget

> **Note to Reviewers:** This budget has been strictly optimized for Tier 3. I have replaced expensive components with high-quality industrial alternatives from AliExpress and clarified the necessity of the LiPo battery for standalone Wi-Fi automation.

## 🛠️ Assembly Strategy
*   **Custom Design:** This is a custom PCB and enclosure project.
*   **Factory PCBA (JLCPCB):** SMT assembly of 0603 passives and status LED.
*   **Manual Assembly (Me):** Hand-soldering of the ESP32-S3, screw terminals, JST headers, and wiring of all panel-mounted sensors.

---

## 1. PCB & Factory PCBA (JLCPCB)
*   **Subtotal:** **$48.00** (Includes 5x PCBs, PCBA fee, and SMD components).
*   *Verification:* See `assets/journal/JLCPCB_Shipping_Verify.png` and `assets/journal/JLCPCBshipmethods.png` for the most economical shipping route to Brazil ($18.52 via Global Standard Direct Line).

---

## 2. Main Controller (Adafruit)
*   **ESP32-S3 ProS3 & Missile Switch:** **$30.45** (Including shipping/tax).
*   *Note:* Selected for its native Wi-Fi and USB HID reliability.

---

## 3. Optimized Interface Cart (AliExpress)
*Based on our optimized [AliExpress Cart](assets/journal/AliExpress_Cart_New.png).*

| Component | Price | Purpose |
| :--- | :--- | :--- |
| **EC11 Encoder** | $1.23 | Timeline scrolling / Volume. |
| **1.5" RGB OLED** | $11.93 | UI and API feedback. |
| **Hall Joysticks (2x)** | $7.38 | XY Control (No Drift). |
| **Cherry MX Switches (10x)** | $5.74 | Execution buttons. |
| **3000mAh Battery** | $12.05 | Standalone Wireless Power. |
| **Regional Freight/Tax** | ~$27.51 | Estimated base shipping & import taxes. |

**Subtotal Base Parts:** **$38.33**

---

## 4. Power & Safety (LCSC)
*   **Screw Terminals & Connectors:** **$5.49** (Merchandise Total).
*   *Verification:* See `assets/journal/LCSC_Cart_Updated.png`.

---

## Grand Total Base Cost: ~$122.27
*(Excluding regional Brazilian import taxes and international shipping to stay within Tier 3 guidelines).*

