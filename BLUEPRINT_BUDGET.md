# The Nerve V1.0 - Blueprint Verified Budget

> **Note to Reviewers:** This budget reflects the definitive, non-optional hardware requirements for The Nerve V1.0. All amounts are derived directly from the checkout screenshots provided in the repository assets. The component selection has been optimized to prioritize high-quality, industrial-grade parts via AliExpress while significantly reducing the overall budget compared to domestic US retailers.

## 💡 Engineering Design: The Modular Approach
The design uses screw terminals and JST connectors to allow easy swapping of experimental sensors (Joysticks, Encoders, OLED) without wasting the main PCB or risking trace damage during assembly. 

## 🛠️ Manufacturing & Assembly Strategy
To demonstrate technical skill and ensure repairability:
*   **Factory PCBA (JLCPCB):** Automated SMT assembly of resistors, capacitors, the RGB LED, and small ICs (0603 package).
*   **Manual Assembly (Me):** Hand-soldering of all terminal blocks, JST connectors, the ESP32-S3 ProS3, and wiring all external interfaces to the case.

---

## 1. LCSC Parts (Loose Parts Cart)
*   **Total LCSC Cart (as per `assets/journal/LCSC_Cart.png`)**: **$17.45**
    *   *Includes: Screw Terminals, JST Connectors, Buzzer, Capacitors, LEDs, Shipping ($9.12), and Handling Fees.*

---

## 2. JLCPCB PCBA (Fabrication & Assembly)
*   **Total JLCPCB Quote (as per `assets/journal/JLCPCB_Checkout_Updated.png`)**: **$36.04**
    *   *Covers PCB manufacturing and automated SMD assembly.*

---

## 3. Core Compute
*   **ESP32-S3 ProS3 (`Adafruit.png`)**: **$30.45** (incl. Shipping/Tax)
    *   *High-quality MCU with native USB, Wi-Fi, battery management, and 16MB Flash.*

---

## 4. Front Panel Interfaces (AliExpress Optimization)
*As shown in `assets/journal/AliExpress_Cart_New.png`, these items total **$95.33** at checkout (including $13.17 Freight and $29.42 Import Taxes/ICMS).*

| Component | Source / Link | Base Price | Note |
| :--- | :--- | :--- | :--- |
| **Optical Encoder** | [AliExpress](https://pt.aliexpress.com/item/1005008717897010.html) | $27.68 | Industrial grade (61C221-04-02), high precision. |
| **1.5" RGB OLED** | [AliExpress](https://pt.aliexpress.com/item/1005003754608099.html) | $11.93 | SSD1351 Driver, 128x128 SPI interface. |
| **Hall Joystick (2x)** | [AliExpress](https://pt.aliexpress.com/item/1005008656717678.html) | $7.39 | K-Silver JH16 Electromagnetic (No drift). |
| **Cherry MX Switch (10x)** | [AliExpress](https://pt.aliexpress.com/item/1005008563463707.html) | $5.74 | Genuine Cherry MX2A Blue (Clicky). |
| **Freight & Taxes** | AliExpress Checkout | $42.59 | Included in the final checkout total below. |

**Subtotal External Interfaces:** **$95.33**

---

## Grand Total: $179.27
*(Note: Despite the lower unit prices, Brazilian import taxes (ICMS + Import Tax) add nearly $30 to the AliExpress order, bringing the total back up, but securing vastly superior industrial components).*
