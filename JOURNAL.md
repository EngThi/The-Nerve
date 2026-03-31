# The Nerve – Build Log

---

### Feb 1 — Initial Concept

I want to build a physical control panel that isn't just another macro pad. Tested a Hall Effect joystick on a breadboard today. The analog values from these electromagnetic sensors are much more stable than cheap pot-based sticks, but the raw signal is still a bit noisy. Spent some time writing a basic moving average filter in software to smooth the jitter before I even think about the PCB.

---

### Feb 5 — Power & Footprints

Started the schematic. The standard terminal footprints in the library didn't match the KF128 connectors I'm using, so I had to draw a custom 2.54mm pitch footprint. Also decided to add a dedicated LDO regulator. Putting the OLED and the analog joystick on the same power rail without regulation is just asking for noise interference.

![Schematic](assets/diagrams/Schematic.png)

---

### Feb 10 — The "Panic Button" & Battery

My browser crashed and I lost an hour of routing. That's why this thing needs a physical "Save/Push" button. Wired a Cherry MX switch to test a USB HID command that forces a `git push`. Also added a voltage divider with high-value resistors to the schematic so the ESP32 can monitor the LiPo level without draining it.

![Panic Button Concept](assets/journal/Panic.png)

---

### Feb 11 — SPI Over I2C

Switched the display from I2C to SPI. I2C is easier to wire, but the refresh rate is too sluggish for a dynamic UI. Tested a 1.5" Waveshare OLED via SPI and the difference is huge. I had to redo several traces for the extra pins (MOSI, CLK, CS, etc.), but it's worth it for the performance.

![OLED Upgrade](assets/journal/Oled.png)

---

### Feb 12 — MCU Choice

Locked in the ESP32-S3 ProS3. The standard ESP32 doesn't have native USB HID support, which I need for the hardware macros to work properly as a keyboard. Plus, the ProS3 has a built-in LiPo charger, so I don't need an extra TP4056 chip on the board.

![ESP32-S3 ProS3](assets/journal/ProS3.jpg)

---

### Feb 13 — Modular Design

Decided not to solder the inputs directly to the PCB. Everything (joystick, encoder, switches) will connect via screw terminals or JST headers. If a switch fails or I want to change the joystick, I don't want to have to desolder the whole board. The PCB is the brain; the sensors are modular.

![Screw Terminals](assets/journal/Terminais.png)

---

### Feb 14 — Routing & Noise

Spent the day routing the SPI lines. Kept them as short as possible and far away from the analog joystick traces. I also added ground guard traces between them to prevent the high-speed data lines from leaking noise into the analog signals.

![PCB Routing](assets/journal/Trilhas.png)

---

### Feb 15 — Ground Planes & DRC

Finished the 2-layer routing. Added a full ground pour on the bottom and stitched it to the top with vias for a solid reference plane. Ran the Design Rule Check (DRC) and had to fix a few clearance issues on the SMT pads to match JLCPCB's manufacturing limits. The board is ready for the factory.

![Final PCB Design](assets/journal/PCB_Branca.png)

---

### Feb 18 — CAD & Mechanical Fit

Exported the PCB as a STEP file and moved to OnShape. Good thing I did — the USB-C port was 1.5mm off from my enclosure cutout. Adjusted the 3D model wall to match the actual board position.

![3D Mockup](assets/journal/ViewBottom.png)

---

### Feb 22 — Ergonomics & Heat

Finalized the case with a 15-degree angle. It's much easier to read the screen on a desk this way. Added ventilation slots on the back because the ESP32-S3 can get warm when the Wi-Fi is constantly hitting webhooks.

![Back Ventilation Slots](assets/journal/BackView.png)

---

### Mar 12 — BOM Audit & Cost

Audited the budget. The prices for parts like the joystick and encoder are much better on AliExpress than on Mouser. Swapped the sources in the BOM and updated the total cost. It's now optimized for Tier 3 without losing the Hall Effect precision.

![AliExpress Cart](assets/journal/AliExpress_Cart_New.png)

---

### Mar 22 — Reviewer Feedback

Got feedback asking why the battery is necessary and why the ESP32-S3 instead of something cheaper. The battery question is fair — the whole point of the standalone mode is that it sends webhooks and triggers automations without needing a PC open. If it had to be tethered to USB for power, half the use case disappears. Wrote detailed justifications in the README and added the public OnShape link so the reviewer can inspect the CAD natively.

---

### Mar 24 — Final Refinements

Simplified the encoder setup. Replaced the expensive optical version with a standard EC11. It's cheaper and does the job for menu navigation. Polished the README and verified all shipping/tax proof for the submission.

![JLCPCB Shipping Verification](assets/journal/JLCPCB_Shipping_Verify.png)

---

### Mar 25 — Final Verification

Went through everything one last time. Verified that the cart screenshots match the BOM quantities exactly, double-checked the shipping method on the JLCPCB order, and made sure all the files in the repo are the latest versions.
