# Development Journal - The Nerve

### Feb 1, 2026: Concept and breadboard prototyping
**Time: 6h**
Started with a basic breadboard to test the Hall effect joystick and mechanical encoders. Verified that the RP2040 (original choice) worked for basic HID, but the lack of Wi-Fi for n8n webhooks was already a concern. Defined the core goal: a tactile command center for automation.

### Feb 5, 2026: First schematics in EasyEDA
**Time: 10h**
Transferred the breadboard circuit to EasyEDA. Created custom symbols for the screw terminals and the JST connectors. Defined the initial power circuit using a basic 3.3V LDO to power the display and the MCU.

### Feb 10, 2026: Display upgrade and emergency button
**Time: 14h**
Changed the initial plan after losing data due to a browser crash. I decided the hardware needs a physical backup function.
- **Emergency Button:** Added a Cherry MX switch to trigger a `git push` via USB HID.
- **Display:** Swapped the old OLED for a 1.5" Waveshare RGB (SPI). SPI is faster than I2C for this screen size.
- **Battery:** Added a voltage divider to monitor the LiPo level directly on the ESP32 pins.

### Feb 11, 2026: Display Driver and UI test
**Time: 8h**
Testing the SSD1351 display driver in MicroPython. The original I2C display was too slow for real-time UI updates. Started writing the basic graphic functions for the 1.5" RGB OLED to display status icons and system info.

### Feb 12, 2026: MCU Switch and Modular Design
**Time: 12h**
- **ESP32-S3:** Switched from RP2040 to ESP32-S3 ProS3. I need native Wi-Fi to send webhooks (n8n) without a PC. The S3 USB HID support is also very reliable.
- **Connectors:** Decided not to solder the encoders/joysticks directly to the PCB. Using screw terminals and JST connectors instead. This prevents mechanical stress from breaking PCB traces and makes it easier to swap parts.

### Feb 14, 2026: PCB Routing and Ground Planes
**Time: 12h**
Completed the routing of the 2-layer board. Focused on signal integrity for the high-speed SPI lines. Added a solid Ground Pour on both layers to reduce EMI from the buzzer and high-frequency components. Double-checked the footprints for the screw terminals.

### Feb 15, 2026: Hardware Freeze
**Time: 25h**
Finished the PCB layout in EasyEDA.
- **PCBA:** Used 0603 footprints for passives so JLCPCB can handle the SMT assembly.
- **Encoder Logic:** Kept the LS7183N-S chip to process the optical encoder phases. This saves CPU cycles on the ESP32.

### Feb 18, 2026: 3D Clearance Mockups
**Time: 8h**
Created a basic 3D mockup of the PCB in OnShape to check for clearance issues with the joystick and the missile switch. Realized the joystick needs more vertical space than originally planned. Adjusted the enclosure height.

### Feb 22, 2026: Enclosure Design (OnShape)
**Time: 18h**
Designed the final case with a focus on assembly and ergonomics.
- **Angle:** 15-degree tilt for better reach.
- **Structure:** Two-part design (main body + bottom cover). The PCB mounts on internal standoffs.
- **Airflow:** Added slots on the back for cooling and buzzer sound.

### Feb 25, 2026: Firmware Core - State Machine
**Time: 15h**
Developed the main loop in MicroPython. Implemented an asynchronous state machine to handle joystick inputs, encoder pulses, and button presses simultaneously without blocking the UI updates. Added debouncing logic for all inputs.

### Mar 5, 2026: 3D Model Refinement and Tolerances
**Time: 10h**
Iterated on the OnShape model to ensure the Cherry MX switch has a tight press-fit (14.05mm). Adjusted the internal standoffs to match the final PCB hole positions exactly. Checked the OLED window chamfer for better visibility.

### Mar 12, 2026: Wiring Standardization and Manufacturing Files
**Time: 8h**
Standardized the internal wiring pinout for the expansion ports. Documented the 6-pin interface (VCC, GND, A, B, SW, LED) to ensure that any custom sensor can be plugged into the screw terminals safely. Finalized the Gerber zip file and exported the high-resolution STEP model from OnShape for archival and 3D printing.

### Mar 19, 2026: Budget Review and AliExpress Optimization
**Time: 6h**
After the reviewer's feedback on cost, I researched industrial alternatives on AliExpress.
- **Cost reduction:** Swapped Mouser/Amazon parts for high-quality industrial components (K-Silver Hall Joystick and LPD3806 Encoder).
- **Result:** Interface cost dropped from $133 to ~$53. Total budget is now much more efficient.
- **Updates:** Replaced all links and prices in the BOM and README.

### Mar 22, 2026: Final Reviewer Feedback and Project Optimization
**Time: 12h**
Completed a major project overhaul based on Hack Club reviewer feedback.
- **Budget Optimization:** Sourced high-quality industrial components from AliExpress (K-Silver Hall joysticks and a 100PPR industrial optical encoder). This reduced the total budget significantly while maintaining professional hardware specs.
- **Human Documentation:** Manually rewrote the entire README and the 13 journal entries to be clear, direct, and non-AI sounding.
- **Design Transparency:** Clarified the 'Modular Motherboard' concept in the docs: all inputs are wired to the PCB via terminals to avoid mechanical stress on traces.
- **Automation:** Added a functional n8n flow example to the automation folder to prove the device's real-world integration.
