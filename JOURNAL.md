# The Nerve - Engineering Logs

Feb 1: Started researching sensors for a custom automation controller. Tested a basic Hall Effect joystick on a breadboard. 

Feb 5: Initial schematic design in EasyEDA. Focused on the power rail. Decided to use a 3.3V LDO to keep the signal clean for the OLED and sensors.
![Schematic](assets/diagrams/Schematic.png)

Feb 10: Major pivot. My browser crashed and I lost an hour of work. This inspired the "Panic Button" idea—a physical Cherry MX switch to force a Git save. 
![Panic Button Concept](assets/journal/Panic.png)

Feb 11: Switched display from I2C to SPI. SPI is faster than I2C for this screen size. 
![OLED Upgrade](assets/journal/Oled.png)

Feb 12: Integrated the ESP32-S3 ProS3 into the design. Chose this board for its built-in LiPo charging circuit and high flash memory.
![ESP32-S3 ProS3](assets/journal/ProS3.jpg)

Feb 13: Decision: No direct soldering of inputs. I will use screw terminals for everything panel-mounted. This protects the PCB from mechanical force.
![Screw Terminals](assets/journal/Terminais.png)

Feb 14: PCB Component placement. Spent a long time trying to keep the high-speed SPI lines away from the analog joystick traces to avoid noise.
![PCB Routing](assets/journal/Trilhas.png)

Feb 15: Finished the 2-layer routing. Added a massive ground pour on the bottom layer. Re-checked pad sizes for SMT assembly compatibility.
![Final PCB Design](assets/journal/PCB_Branca.png)

Feb 18: Started 3D modeling in OnShape. Imported the PCB as a STEP file to check the alignment of the connectors with the case walls.
![3D Mockup](assets/journal/ViewBottom.png)

Feb 22: Finalized the 15-degree wedge case design. Added vertical cooling slots on the back wall.
![Enclosure Render](assets/renders/the_nerve_full_enclosure_render.png)

Mar 5: 3D Print prep. Refined the Cherry MX cutout to exactly 14.05mm for a perfect snap-fit.
![Chamfer Detail](assets/journal/Chanfro.png)

Mar 12: Documentation day. Standardized the 6-pin wiring interface. Exported Gerbers and the final STEP model.

Mar 19: Budget optimization. Found high-quality industrial sensors on AliExpress that are much cheaper than Mouser. Updated the BOM.
![New Cart](assets/journal/AliExpress_Cart_New.png)

Mar 22: Reviewer feedback response. Clarified the battery usage and justified the ESP32-S3. 

Mar 25: Final project sync. Verified that all cart screenshots and shipping methods match. Ready for final review.
![Shipping Verify](assets/journal/JLCPCB_Shipping_Verify.png)
