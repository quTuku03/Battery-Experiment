# 24/7/2025
# Read Voltage and Discharge Current of Tested Battery
import serial
import time
import csv
from ppk2_api.ppk2_api import PPK2_API

# Settings for Arduino serial port
ser = serial.Serial("COMX", 115200, timeout=0)  # Change COMX to actual port
time.sleep(1)

# Defining csv file
file_name = "battery_data_" + time.strftime("%H_%M_%S") + ".csv"
start_time = time.time()  #  Elapsed time (seconds)

with open(file_name, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Timestamp", "Elapsed Time (s)", "Voltage (V)", "Current (uA)"])

# PPK2 settings
ppk2s_connected = PPK2_API.list_devices()
ppk2_port = ppk2s_connected[0]
ppk2 = PPK2_API(ppk2_port, timeout=1, write_timeout=1, exclusive=True)
ppk2.get_modifiers()
ppk2.set_source_voltage(3300)  # Dummy voltage
ppk2.use_ampere_meter()
ppk2.toggle_DUT_power("ON")
ppk2.start_measuring()

# End condition; ought to be adjusted in each battery case
Vmin = 1.05

stop = False
bad_lines = []  # 'Bad' lines from Arduino

#Main loop
reference_time = time.time()  # Initial time reference
while not stop:
    current_time = time.time()

    if (current_time - reference_time) < 5.0:
        continue # Waits 5secs
    reference_time = current_time

    #Voltage from Arduino
    data = ser.readline()

    if data:
        serial_line = data.decode("utf-8").strip()
        timestamp = time.strftime("%H:%M:%S")
        elapsed_time = int(time.time() - start_time)

        # Safe convert to float,just in case 'bad' lines occur during operation
        try:
            voltage = float(serial_line)
        except ValueError:
            print("'Bad' line:", serial_line)
           # bad_lines.append(serial_line)  #Saving 'bad' lines
            continue

        # Current from PPK2
        read_data = ppk2.get_data()
        current = 0.0
        if read_data != b'':
            samples, _ = ppk2.get_samples(read_data)
            if len(samples) > 0:
                current = sum(samples) / len(samples)

        # Print and save
        print(f"{timestamp} | {elapsed_time}s | {voltage}V | {current}uA")
        with open(file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([timestamp, elapsed_time, round(voltage, 3), round(current, 5)])


        if voltage <= Vmin:
            print("Battery reached cut-off")
            stop = True

# Closing PPK2 & Arduino
ppk2.toggle_DUT_power("OFF")
ppk2.stop_measuring()
ppk2.ser.close()
ser.close()

