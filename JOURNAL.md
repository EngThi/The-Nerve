# The Nerve – Build Log

---

**Feb 1** — *~4h*

I've been wanting to build some kind of physical control panel for a while. Not a keyboard macro thing, something more serious. Started by testing a Hall Effect joystick I had sitting around. Wired it to a breadboard and read the analog values over serial. It works, but the output is noisy as hell without proper filtering. Already thinking about how to handle that on the PCB.

---

**Feb 5** — *~4h*

Opened EasyEDA and started the schematic from scratch. The power rail took way longer than expected. I kept going back and forth between using an LDO regulator vs. just pulling 3.3V directly from the ESP32 pin. Went with the LDO in the end — the OLED and the analog joystick on the same rail without proper regulation would be asking for noise problems.

![Schematic](assets/diagrams/Schematic.png)

---

**Feb 10** — *~5h*

Browser crashed mid-session and I lost about an hour of routing work. No autosave. That was frustrating enough to make me actually think about the problem instead of just redoing it. If the whole point of this device is to help me work faster and not lose stuff, it should have a physical save button. That became the Panic Button — a Cherry MX switch wired to send a USB HID command that forces a git push. Sounds dumb but it makes sense for how I work.

![Panic Button Concept](assets/journal/Panic.png)

---

**Feb 11** — *~3h*

Switched the display from I2C to SPI. Was using I2C because it's simpler to wire, but the refresh rate was too slow for what I want to show on screen. SPI is faster and the Waveshare 1.5" handles it fine. Had to redo some of the schematic traces but it wasn't a big deal.

![OLED Upgrade](assets/journal/Oled.png)

---

**Feb 12** — *~3h*

Locked in the ESP32-S3 ProS3 as the main MCU. I looked at a few options. The regular ESP32 doesn't have native USB HID, which I need for the Panic Button to actually work as a keyboard. The S3 has it, plus it has a built-in LiPo charger which saves me from adding another IC to the board. More flash too.

![ESP32-S3 ProS3](assets/journal/ProS3.jpg)

---

**Feb 13** — *~2h*

Decided not to solder the inputs directly to the PCB. The joystick, encoder, and switches are all going through screw terminals or JST connectors instead. I kept imagining having to desolder a Cherry MX switch because the firmware has a bug, and that was enough to convince me. The PCB is the brain. The inputs are modular.

![Screw Terminals](assets/journal/Terminais.png)

---

**Feb 14** — *~6h*

Spent most of today on component placement. Keeping the SPI lines (going to the OLED) away from the analog joystick traces is annoying. They run almost parallel on the board and I'm worried about noise coupling. Added some ground traces between them and moved a few components around. Not perfect but better.

![PCB Routing](assets/journal/Trilhas.png)

---

**Feb 15** — *~6h*

Finished the 2-layer routing. Put a full ground pour on the bottom layer. Went back and checked every SMT pad size against the JLCPCB design rules — last time I ordered a board I had an annular ring violation that I only caught after submitting. Not doing that again. The board looks clean.

![Final PCB Design](assets/journal/PCB_Branca.png)

---

**Feb 18** — *~4h*

Started the enclosure in OnShape. Exported the PCB as a STEP file from EasyEDA and imported it to check if the connector positions actually line up with the walls. They didn't — the USB-C port was about 1.5mm off from the cutout I had drawn. Fixed the wall opening. This is exactly why you model in 3D before printing.

![3D Mockup](assets/journal/ViewBottom.png)

---

**Feb 22** — *~5h*

Finalized the case. Went with a 15-degree wedge angle so the panel faces slightly upward when sitting on a desk. Added vertical slots on the back wall for airflow — the ESP32-S3 gets warm under load and I'd rather not cook it inside a sealed box. Updated the BOM with some components I had been putting off.

![Enclosure Render](assets/renders/the_nerve_full_enclosure_render.png)

---

**Feb 23** — *~5h*

Big day. Updated all the PCB hardware files to the latest revision, generated the new Gerbers, fixed the PCBA BOM for JLCPCB, and corrected a few part URLs that were pointing to the wrong items. The 10uF capacitor was mapped to a part that's out of stock — swapped it to C1713 which is always available.

---

**Feb 24** — *~2h*

Translated the whole journal to English and uploaded all the in-progress photos. The images were sitting on my phone since the first week of the build so it was about time.

---

**Feb 25** — *~1h*

Added a banner and hero image to the README. Small stuff but it makes the project page look less empty when a reviewer opens it for the first time.

---

**Mar 5** — *~3h*

Prep work for when I eventually print this. The Cherry MX cutout needed to be exactly 14.05mm for a snap-fit without glue. Anything looser and the switch wobbles. Went back into OnShape and refined the tolerance. Also added an inner chamfer to the OLED window so the screen doesn't look recessed from the front.

![Chamfer Detail](assets/journal/Chanfro.png)

---

**Mar 10** — *~4h*

Big cleanup day. Added the actual MicroPython firmware file (`firmware/src/main.py`) and a wiring diagram for anyone who wants to hand-wire the inputs to the PCB headers. Also added the KiCad project file that was somehow missing from the repo. Embarrassing but fixed now.

---

**Mar 11** — *~4h*

Replaced all the old PCB files with the final EasyEDA version. The KiCad files I had before were from an earlier iteration and didn't match what I actually submitted to JLCPCB. Uploaded the correct Gerbers, BOM, and Pick & Place files. Updated the cost table with real checkout prices per vendor including shipping and MOQ. Should have done this earlier.

---

**Mar 12** — *~6h*

Spent the day on the budget. Went through every item and pulled real checkout prices — not the unit price, the actual price you pay including MOQ and shipping. There's a big difference. The passive components come in packs of 20 or 50, so the real cost is higher than it looks on paper. Updated the BOM and the budget doc to reflect that. Total came out to $87.47 for the JLCPCB order. Also cleaned up the whole repo structure.

---

**Mar 13** — *~1h*

Finished the README. Added firmware setup instructions, clarified the 3D source files situation, and verified the budget numbers one more time.

---

**Mar 15** — *~1h*

Added a note at the top of the README to help reviewers navigate the project quickly. The repo was getting dense enough that it wasn't obvious where to start.

---

**Mar 17** — *~1h*

Organized the image folders and added the case render photos to the README so reviewers can see the enclosure without having to dig through the repo.

---

**Mar 19** — *~4h*

Found that a lot of the external components (joystick, encoder) were way cheaper on AliExpress than on Mouser or Adafruit. The quality on industrial sensors from AliExpress is fine as long as you check the seller. Updated the BOM with the new sources and added a cart screenshot as proof. Cleaned up the BOM file and moved freight/tax notes to the README.

![New Cart](assets/journal/AliExpress_Cart_New.png)

---

**Mar 21** — *~2h*

Full project overhaul for resubmission. Rewrote parts of the README to be more direct, tightened up the budget doc, and cleaned up the journal format.

---

**Mar 22** — *~6h*

Got reviewer feedback and worked through it. The main questions were about the battery (whether it's necessary) and why specifically the ESP32-S3 and not something cheaper. Added an OnShape link to the README so they can actually see the 3D model. Answered everything in the docs.

---

**Mar 24** — *~1h*

Finalized Tier 3 cost optimization with a cheaper encoder option. Updated the wiring diagram terminology to be consistent. Rewrote the journal entries to raw engineering log format.

---

**Mar 25** — *~1h*

Went through everything one more time. Verified the cart screenshots match the BOM quantities, double-checked the shipping method on the JLCPCB order, and made sure all the files in the repo are the right versions.

![Shipping Verify](assets/journal/JLCPCB_Shipping_Verify.png)

---

**Mar 26** — *~1h*

Final pass on the engineering logs. Added image references throughout, standardized the format, and made sure every entry has enough context to stand on its own.
