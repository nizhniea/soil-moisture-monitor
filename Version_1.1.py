#Version_1.1
import serial
pico = serial.Serial("COM7", 115200, timeout=2)

lucky_bamboo = {
    "Very Dry": 20,
    "Dry": 40,
    "Moist": 70,
    "Wet": 90,
    "Water?": 100
}

dry_soil_mean = 43843.6
moist_soil_mean = 42893.2
Water_mean = 23545.8

# Garden-friendly calibration
# Dry soil = 0%
# Moist soil = 50%
# Water? = 100%

def moisture_percent(reading):

    first_range = dry_soil_mean - moist_soil_mean
    second_range = moist_soil_mean - Water_mean

    if reading >= dry_soil_mean:
        return 0

    elif moist_soil_mean < reading < dry_soil_mean:
        return round(((dry_soil_mean - reading) / first_range) * 50, 1)

    elif Water_mean < reading <= moist_soil_mean:
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
        return "Water?"
    
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
        print(f"Sensor Reading: {reading}")
        print(f"Moisture: {percent}%")
        print(f"Status: {status}")

    elif choice == "no":
        pico.close()
        print("Okay, have a nice day!")
        break
    else:
        print("Please enter 'yes' or 'no'.")
