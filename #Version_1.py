#Version_1.0
import serial
pico = serial.Serial("COM7", 115200, timeout=2)

air_mean = 44063.33
water_mean = 23545.8

lucky_bamboo = {
    "Very Dry": 20,
    "Dry": 40,
    "Moist": 60,
    "Wet": 80,
    "Way Overdone": 100
}

calibration_range = air_mean - water_mean
def moisture_percent(reading):
    if reading >= air_mean:
        return 0
    elif reading <= water_mean:
        return 100
    else:
        return round(((air_mean - reading) / calibration_range * 100),1)
    
def moisture_status(percent):
    if percent <= lucky_bamboo["Very Dry"]:
        return "Very Dry"
    elif percent <= lucky_bamboo["Dry"]:
        return "Dry"
    elif percent <= lucky_bamboo["Moist"]:
        return "Moist"
    elif percent <= lucky_bamboo["Wet"]:
        return "Wet"
    else:
        return "Way Overdone"
    
print("=============")
print("Bamboo Moisture Monitor")
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