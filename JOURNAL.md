> *Disclaimer: Initially, I was only using the Blueprint platform to document progress. I am compiling past logs here to reflect the true project timeline and translating everything to English for the Hack Club reviewers.*

# Development Journal - The Nerve

This document records the evolution, engineering decisions, and challenges faced during the development of **The Nerve V1**, aligned with the posts made on the Blueprint platform.

---

### Feb 10, 2026: The "Panic" That Became a Feature (Project Reboot)
**Time spent: 14.4h**

What was supposed to be a productive Saturday turned into a technical nightmare when a 6-hour timelapse upload got stuck at 60%. Instead of just accepting the loss, I used the frustration as fuel to create the **"Panic Save Module"**: now THE NERVE's hardware has a physical emergency button to force backups and save the project state before any digital error happens again.

**What was done:**
- **Hacker Investigation:** I opened the console and discovered the browser database was corrupted due to a server request limit. I decided the project cannot depend 100% on the cloud or browser.
- **Display Upgrade:** I replaced the simple OLED with a 1.5" Waveshare SPI. It's much faster and makes the interface look much more professional.
- **Power Management:** I implemented a voltage monitor for the LiPo battery. Now the system warns if the battery is dying.
- **Panic Module:** I designed the circuit for a mechanical switch (Cherry MX style). When pressed, it sends a USB command to the computer to `git push` and save everything instantly.
- **Validation:** Tested the logic of the new Optical Encoder in Wokwi. The precision is infinitely better than standard mechanical ones.

*The design in EasyEDA evolved from basic to combat-ready hardware. The project is now an autonomous and resilient workstation.*

---

### Feb 12, 2026: Hardware Pivot & Transition to Modular Architecture
**Time spent: 12.0h**

This phase marked the transition from breadboard theory to actual hardware design. The focus was making the board robust and modular.

**1. Microcontroller Pivot (RP2040 -> ESP32-S3):**
The original plan used the RP2040. It was cheap, but lacking connectivity would limit the scope to cable-bound automations. I migrated to the **ESP32-S3 ProS3**. Besides native USB HID (essential for simulating input peripherals), the built-in Wi-Fi opened doors to fire HTTP webhooks directly to n8n, bypassing host PC scripts entirely.

**2. The Optical Encoder Dilemma:**
I spent a long time trying to create a footprint from scratch for an absolute optical encoder. Halfway through, I realized that soldering it directly to the board was a trap: any mechanical stress on the "dial" could snap the PCB.
**The Fix:** I abandoned fixed mounting and implemented universal **JST connectors and KF128 screw terminals**. Now the project is modular! I can swap the Dial or Joystick without resoldering the whole board.

**3. Pinout & Signal Integrity:**
Standardized the input interface: `VCC | GND | SIG_A | SIG_B | SW | LED`. I placed a solid GND copper pour to avoid EMI interference between the analog Joystick signals and the fast SPI OLED lines.

---

### Feb 15, 2026: Hardware Freeze
**Time spent: 25.0h**

After dozens of hours tweaking placements and routing (and losing several timelapse recordings due to browser crashes), I reached the "Hardware Freeze" for version 1.0.

- **DFM (Design for Manufacturing):** Selected components that LCSC has in stock (Basic Parts) so JLCPCB can deliver it partially assembled.
- **Decoder IC:** Kept the **LS7183N-S**. It takes the heavy processing load of the high-resolution encoder off the ESP32's shoulders.
- **Passives:** Everything is 0603. It’s the smallest size I can reasonably hand-solder if I need to fix a trace later.

*(Note: The `hardware/` and `firmware/` directory structure was organized in this session).*

---

### Feb 22, 2026: 3D CAD Modeling & The Slim Premium Case
**Time spent: 18.0h**

After the Hardware Freeze, I thought the hardest part was over. I was wrong. Moving from electronic theory to real-world physics in **OnShape** was a massive challenge. I spent 18 straight hours designing the enclosure to ensure everything fit perfectly without sketchy workarounds.

**The Complete OnShape Model:**
I designed a 15-degree wedge enclosure with 3mm walls. Tolerances were strict:
- **1.5" OLED:** A 40x40mm window with a 45° inner chamfer so the screen doesn't look deeply sunken into the plastic.
- **Cherry MX (Execute):** A precise 14.05x14.05mm cutout designed for a perfect press-fit without glue.
- **Missile Switch (Panic):** An M12 (12.5mm) hole with 50mm of clearance so the red safety cover can open without hitting the joystick.

**The Structural Leap: Flush-Inside Bottom Cover**
Trying to design everything as a single piece would ruin printability and maintenance. I split the case into a main body and a flush-inside bottom cover. The PCB screws directly into the bottom cover standoffs, making assembly incredibly clean.

**Thermals and Acoustics (The Stealth Approach):**
The ESP32-S3 gets warm, and I have a buzzer on the board. I refused to drill ugly holes in the front face. Instead, I designed 7 vertical slots (2x30mm) on the rear wall. They act as thermal exhaust and acoustic grills, keeping the front aesthetic completely stealthy.

---

### Feb 23, 2026: Fixing the BOM & LCSC PCBA Checkout

I thought the Gerbers and CAD were ready, but when attempting to checkout the automated assembly (PCBA) at JLCPCB, the system threw massive `item does not found` and `shortfall` errors.

**The Fixes for PCBA:**
1. **Clean BOM for JLCPCB:** Generated a dedicated 16-column CSV from EasyEDA, stripping out all mechanical/external components (Cherry MX, Joystick, ESP32-S3, OLED) that aren't sold by LCSC.
2. **MOQ (Minimum Order Quantity) Corrections:** Fixed generic Buzzer and RGB LED errors by mapping them to exact LCSC stock codes (`QMB-09B-03` and `XL-A504RGBW`) and adjusting the BOM math to match tray/pack minimums.
3. **Connector Swaps:** Swapped "Unmatched" THT connectors to in-stock LCSC equivalents (`B2B-PH-K-S` and `ZX-HY2.0-8PZZ`).
4. **LS7183N-S Decoder:** JLCPCB reported a stock shortfall for this IC. Rather than halting the entire production for one chip, I removed it from the automated assembly. I'll buy it separately and hand-solder it.

The new `BOM_JLCPCB_PCBA.csv` passed the system checks perfectly.

---

### Feb 24, 2026: Blueprint Grant Submission! 🚀

Today is the day! After weeks of pivoting from breadboards to CAD, debugging corrupted browser databases, surviving JLCPCB checkout errors, and calculating costs down to the cent, **The Nerve has officially been submitted to the Hack Club Blueprint for funding.**

The final requested budget is **$171.92**, covering the custom JLCPCB manufacturing, the Adafruit ESP32-S3, and all the premium interface hardware (Hype Dial, Hall Joystick, Cherry MX switch). 

I spent significant time writing the "Note to Reviewer," ensuring complete transparency about why the JLCPCB quote ($68) differs from the total request (since I'll be hand-wiring the expensive interfaces for maximum modularity).

Now, the waiting game begins. If funded, the next phase is physical assembly and writing the MicroPython firmware!