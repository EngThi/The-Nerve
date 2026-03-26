# The Nerve – Build Log

---

**Feb 1**

I've been wanting to build some kind of physical control panel for a while. Not a keyboard macro thing, something more serious. Started by testing a Hall Effect joystick I had sitting around. Wired it to a breadboard and read the analog values over serial. It works, but the output is noisy as hell without proper filtering. Already thinking about how to handle that on the PCB.

---

**Feb 5**

Opened EasyEDA and started the schematic from scratch. The power rail took way longer than expected. I kept going back and forth between using an LDO regulator vs. just pulling 3.3V directly from the ESP32 pin. Went with the LDO in the end — the OLED and the analog joystick on the same rail without proper regulation would be asking for noise problems.

![Schematic](assets/diagrams/Schematic.png)

---

**Feb 10**

Browser crashed mid-session and I lost about an hour of routing work. No autosave. That was frustrating enough to make me actually think about the problem instead of just redoing it. If the whole point of this device is to help me work faster and not lose stuff, it should have a physical save button. That became the Panic Button — a Cherry MX switch wired to send a USB HID command that forces a git push. Sounds dumb but it makes sense for how I work.

![Panic Button Concept](assets/journal/Panic.png)

---

**Feb 11**

Switched the display from I2C to SPI. Was using I2C because it's simpler to wire, but the refresh rate was too slow for what I want to show on screen. SPI is faster and the Waveshare 1.5" handles it fine. Had to redo some of the schematic traces but it wasn't a big deal.

![OLED Upgrade](assets/journal/Oled.png)

---

**Feb 12**

Locked in the ESP32-S3 ProS3 as the main MCU. I looked at a few options. The regular ESP32 doesn't have native USB HID, which I need for the Panic Button to actually work as a keyboard. The S3 has it, plus it has a built-in LiPo charger which saves me from adding another IC to the board. More flash too.

![ESP32-S3 ProS3](assets/journal/ProS3.jpg)

---

**Feb 13**

Decided not to solder the inputs directly to the PCB. The joystick, encoder, and switches are all going through screw terminals or JST connectors instead. I kept imagining having to desolder a Cherry MX switch because the firmware has a bug, and that was enough to convince me. The PCB is the brain. The inputs are modular.

![Screw Terminals](assets/journal/Terminais.png)

---

**Feb 14**

Spent most of today on component placement. Keeping the SPI lines (going to the OLED) away from the analog joystick traces is annoying. They run almost parallel on the board and I'm worried about noise coupling. Added some ground traces between them and moved a few components around. Not perfect but better.

![PCB Routing](assets/journal/Trilhas.png)

---

**Feb 15**

Finished the 2-layer routing. Put a full ground pour on the bottom layer. Went back and checked every SMT pad size against the JLCPCB design rules — last time I ordered a board I had an annular ring violation that I only caught after submitting. Not doing that again. The board looks clean.

![Final PCB Design](assets/journal/PCB_Branca.png)

---

**Feb 18**

Started the enclosure in OnShape. Exported the PCB as a STEP file from EasyEDA and imported it to check if the connector positions actually line up with the walls. They didn't — the USB-C port was about 1.5mm off from the cutout I had drawn. Fixed the wall opening. This is exactly why you model in 3D before printing.

![3D Mockup](assets/journal/ViewBottom.png)

---

**Feb 22**

Finalized the case. Went with a 15-degree wedge angle so the panel faces slightly upward when sitting on a desk. Added vertical slots on the back wall for airflow — the ESP32-S3 gets warm under load and I'd rather not cook it inside a sealed box.

![Enclosure Render](assets/renders/the_nerve_full_enclosure_render.png)

---

**Mar 5**

Prep work for when I eventually print this. The Cherry MX cutout needed to be exactly 14.05mm for a snap-fit without glue. Anything looser and the switch wobbles. Went back into OnShape and refined the tolerance. Also added an inner chamfer to the OLED window so the screen doesn't look recessed from the front.

![Chamfer Detail](assets/journal/Chanfro.png)

---

**Mar 10**

Big cleanup day. Added the actual MicroPython firmware file (`firmware/src/main.py`) and a wiring diagram for anyone who wants to hand-wire the inputs to the PCB headers. Also added the KiCad project file that was somehow missing from the repo. Embarrassing but fixed now.

---

**Mar 11**

Replaced all the old PCB files with the final EasyEDA version. The KiCad files I had before were from an earlier iteration and didn't match what I actually submitted to JLCPCB. Uploaded the correct Gerbers, BOM, and Pick & Place files. Should have done this earlier.

---

**Mar 12**

Spent the day on the budget. Went through every item and pulled real checkout prices — not the unit price, the actual price you pay including MOQ and shipping. There's a big difference. The passive components come in packs of 20 or 50, so the real cost is higher than it looks on paper. Updated the BOM and the budget doc to reflect that. Total came out to $87.47 for the JLCPCB order.

---

**Mar 19**

Found that a lot of the external components (joystick, encoder) were way cheaper on AliExpress than on Mouser or Adafruit. The quality on industrial sensors from AliExpress is fine as long as you check the seller. Updated the BOM with the new sources and added a cart screenshot as proof.

![New Cart](assets/journal/AliExpress_Cart_New.png)

---

**Mar 22**

Got reviewer feedback and worked through it. The main questions were about the battery (whether it's necessary) and why specifically the ESP32-S3 and not something cheaper. Added an OnShape link to the README so they can actually see the 3D model. Answered everything in the docs.

---

**Mar 25**

Went through everything one more time. Verified the cart screenshots match the BOM quantities, double-checked the shipping method on the JLCPCB order, and made sure all the files in the repo are the right versions. I think this is actually ready now.

![Shipping Verify](assets/journal/JLCPCB_Shipping_Verify.png)
