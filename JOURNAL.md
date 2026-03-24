# The Nerve - Engineering Logs

Feb 1: Breadboarded the core circuit. Tested the Hall joystick and some old encoders. The RP2040 is okay for HID, but I definitely need Wi-Fi for the n8n webhooks. 6 hours spent.

Feb 5: Moved the schematic to EasyEDA. Spent 10 hours creating custom footprints for the screw terminals because the standard ones didn't match the KF128 pitch.

Feb 10: Browser crashed and lost some CAD work. Frustrating. Decided to add a physical "Panic" button (Cherry MX) to force a git push. Switched to SPI for the 1.5" OLED since I2C was lagging. Added a voltage divider for battery monitoring. (14h)

Feb 11: Got the SSD1351 driver working in MicroPython. Wrote some basic classes to draw icons. (8h)

Feb 12: Switched to ESP32-S3 ProS3. The native Wi-Fi and USB HID stack are much better for this. Decided to hand-wire all the panel components to screw terminals. If I solder them to the PCB, the mechanical stress of the joystick will snap the board. (12h)

Feb 14: Finished the 2-layer routing. SPI lines are short and have ground shielding. Added a big ground pour to keep the buzzer noise away from the ADC. (12h)

Feb 15: Hardware freeze. Opted for 0603 parts for the PCBA to keep it small. Using the LS7183N-S to handle the quadrature decoding so the ESP32 doesn't have to bit-bang the phases. (25h)

Feb 18: 3D clearance check in OnShape. The joystick is taller than I thought. Had to increase the case height by 5mm. (8h)

Feb 22: Designed the 15-degree wedge case. Split it into two parts for easier printing. Added ventilation slots in the back because the S3 can get warm when the Wi-Fi is active. (18h)

Feb 25: Coded the main loop. Using uasyncio in MicroPython to handle inputs and OLED refresh without blocking. (15h)

Mar 5: Tightened the tolerances for the Cherry MX cutout. 14.05mm seems to be the sweet spot for a snap-fit. (10h)

Mar 12: Finalized the wiring documentation. Exported everything for manufacturing. (8h)

Mar 19: Budget review. Sourced cheaper parts from AliExpress (Hall joysticks and EC11 encoder). Reduced the base cost significantly. Updated the BOM. (6h)

Mar 22: Final overhaul. Rewrote docs to be clearer and added a functional n8n flow example. (12h)
