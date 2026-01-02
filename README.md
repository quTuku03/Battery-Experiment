
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
* 
## Arduino Setup

The Arduino script and required libraries are already included in this repository.


### Installation

```bash
pip install pyserial
git clone https://github.com/IRNAS/ppk2-api-python
