
# Battery Discharge Logger & Profiler 

## Overview

This repository contains the Python control software **(read_data.py)** developed for my Bachelor of Science thesis. The tool automates the process of recording battery discharge curves by synchronizing voltage readings and current measurements.

It integrates two hardware components:
1.  **Arduino:** Acts as a voltmeter to read the battery's terminal voltage.
2.  **Nordic Power Profiler Kit II (PPK2):** Measures from micro-ampere to ~1ampere level discharge current.

The script logs `Time`, `Voltage (V)`, and `Current (µA)` to a CSV file until the battery reaches a defined cutoff voltage.

##  Hardware Architecture

To replicate this setup, you need:
* **Nordic PPK2:** Connected via USB (Data/Power).
* **Arduino (Any model):** Connected via USB. Must be running a sketch that prints voltage floats to Serial @ 115200 baud.
* **Device Under Test (DUT):** The battery being discharged.

## Dependencies

This project relies on Python 3 and the following external libraries:

* `pyserial`: For communicating with the Arduino.
* `ppk2-api`: For controlling the Power Profiler Kit II.
## Arduino Firmware Setup

The Arduino acts as a digitizer, reading the battery voltage and sending it to the Python script via Serial.

###  Wiring
* [cite_start]**Input Pin:** `A0` [cite: 1]
* **Circuit:** Use a **voltage divider** connecting the battery's positive terminal to `A0`.
    * [cite_start]**Resistors:** R1 & R2 must be **10kΩ** each[cite: 2].
    * [cite_start]**Note:** Ensure both resistors have identical resistance values for accuracy[cite: 2].

### Installation & Dependencies
1.  **Library:** This project relies on the `Vcc` library (included as `Vcc.h` and `Vcc.cpp`). [cite_start]Ensure these files are placed in your Arduino project folder or libraries directory before compiling[cite: 2].
2.  **Upload:** Flash the `READ_BATTERY_VOLTAGE.ino` sketch to your board.
3.  **Settings:**
    * [cite_start]**Baud Rate:** `115200` (Must match Python script)[cite: 8].
    * [cite_start]**Calibration:** You may need to adjust the `VccCorrection` float in the code (Line 18) to match your specific hardware regulator[cite: 5].


### Installation

```bash
pip install pyserial
git clone https://github.com/IRNAS/ppk2-api-python
