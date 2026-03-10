# Firmware – Flashing Guide

## Overview

The Nerve runs **CircuitPython** on the **Unexpected Maker ESP32-S3 ProS3**.
The main entry point is `firmware.py` (project root) – identical to `firmware/src/main.py`.

## Requirements

- CircuitPython 9.x for ProS3 – download at [circuitpython.org/board/unexpectedmaker_pros3](https://circuitpython.org/board/unexpectedmaker_pros3)
- Required libraries (copy to `CIRCUITPY/lib/`):
  - `adafruit_hid` (keyboard, mouse)
  - `adafruit_displayio_ssd1306`
  - `adafruit_display_text`

## Flashing Steps

1. Hold **BOOT** button on ProS3 while connecting USB
2. A drive called `S3BOOT` (or `UF2BOOT`) appears
3. Drag the CircuitPython `.uf2` file onto the drive – board reboots as `CIRCUITPY`
4. Copy `firmware.py` to the root of `CIRCUITPY/` and rename it `main.py`
5. Unplug and replug – firmware starts automatically

## LED Status

| Color | Meaning |
|---|---|
| 🔵 Blue | Booting |
| 🟢 Green | Ready / Idle |
| 🔴 Red | Executing macro |
| 🟣 Magenta | Missile switch armed |

## Pin Reference

See [`hardware/schematics/WIRING_DIAGRAM.md`](../../hardware/schematics/WIRING_DIAGRAM.md) for the full pinout.
