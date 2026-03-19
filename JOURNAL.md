# Development Journal - The Nerve

### Feb 10, 2026: Display upgrade and emergency button
**Time: 14h**

Changed the initial plan after losing data due to a browser crash. I decided the hardware needs a physical backup function.
- **Emergency Button:** Added a Cherry MX switch to trigger a `git push` via USB HID.
- **Display:** Swapped the old OLED for a 1.5" Waveshare RGB (SPI). SPI is faster than I2C for this screen size.
- **Battery:** Added a voltage divider to monitor the LiPo level directly on the ESP32 pins.

### Feb 12, 2026: MCU Switch and Modular Design
**Time: 12h**

- **ESP32-S3:** Switched from RP2040 to ESP32-S3 ProS3. I need native Wi-Fi to send webhooks (n8n) without a PC. The S3 USB HID support is also very reliable.
- **Connectors:** Decided not to solder the encoders/joysticks directly to the PCB. Using screw terminals and JST connectors instead. This prevents mechanical stress from breaking PCB traces and makes it easier to swap parts.

### Feb 15, 2026: Hardware Freeze
**Time: 25h**

Finished the PCB layout in EasyEDA.
- **PCBA:** Used 0603 footprints for passives so JLCPCB can handle the SMT assembly.
- **Encoder Logic:** Kept the LS7183N-S chip to process the optical encoder phases. This saves CPU cycles on the ESP32.

### Feb 22, 2026: Enclosure Design (OnShape)
**Time: 18h**

Designed the case with a focus on assembly and ergonomics.
- **Angle:** 15-degree tilt for better reach.
- **Structure:** Two-part design (main body + bottom cover). The PCB mounts on internal standoffs.
- **Airflow:** Added slots on the back for cooling and buzzer sound.

### Mar 19, 2026: Budget Review and AliExpress Optimization
**Time: 6h**

After the reviewer's feedback on cost, I researched industrial alternatives on AliExpress.
- **Cost reduction:** Swapped Mouser/Amazon parts for high-quality industrial components (K-Silver Hall Joystick and LPD3806 Encoder).
- **Result:** Interface cost dropped from $133 to ~$53. Total budget is now much more efficient.
- **Updates:** Replaced all links and prices in the BOM and README.
