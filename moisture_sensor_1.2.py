#Version 1.2
from datetime import datetime
import os
now = datetime.now()

import serial
pico = serial.Serial("COM7", 115200, timeout=2)


lucky_bamboo = {
    "Very Dry": 20,
    "Dry": 40,
    "Moist": 70,
    "Wet": 90,
    "Soaking in water?": 100
}

dry_soil_mean = 43843.6
moist_soil_mean = 42893.2
water_mean = 23545.8

# Garden-friendly calibration
# Dry soil = 0%
# Moist soil = 50%
# Water? = 100%

def moisture_percent(reading):

    first_range = dry_soil_mean - moist_soil_mean
    second_range = moist_soil_mean - water_mean

    if reading >= dry_soil_mean:
        return 0

    elif moist_soil_mean < reading < dry_soil_mean:
        return round(((dry_soil_mean - reading) / first_range) * 50, 1)

    elif water_mean < reading <= moist_soil_mean:
        return round(50 + ((moist_soil_mean - reading) / second_range) * 50, 1)

    else:
        return 100
    
def moisture_status(percent):
    if percent <= lucky_bamboo["Very Dry"]:
        return "Needs Water ASAP!"
    elif percent <= lucky_bamboo["Dry"]:
        return "Should Water"
    elif percent <= lucky_bamboo["Moist"]:
        return "Happy :)"
    elif percent <= lucky_bamboo["Wet"]:
        return "Wet"
    else:
        return "Soaking in water?"
    
print("=============")
print("Bamboo Moisture Monitor!")
print("=============")

while True:
    choice = input("Measure moisture? (yes/no): ").strip().lower()

    if choice == "yes":
        pico.write(b"measure\n")
        print("Command sent!")

        reading = pico.readline().decode().strip()
        reading = float(reading)

        percent = moisture_percent(reading)
        status = moisture_status(percent)
        timestamp = now.strftime("%Y-%m-%d, %H:%M")

        print("-----------------------")
        print(f"Timestamp: {timestamp}")
        print(f"Sensor Reading: {reading}")
        print(f"Moisture: {percent}%")
        print(f"Status: {status}")
        print("-----------------------")

        if not os.path.exists("moisture_log_2.csv"):
            with open("moisture_log_2.csv", "a") as file:
                file.write("Timestamp,Reading,Percent,Status\n")

        with open("moisture_log_2.csv", "a") as file:
            file.write(f"{timestamp},{reading},{percent},{status}\n")

    elif choice == "no":
        pico.close()
        print("Okay, have a nice day!")
        break
    else:
        print("Please enter 'yes' or 'no'.")