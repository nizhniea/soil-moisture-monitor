#Using previously established calibrated values and statistics to convert moisture readings to percentages.
air_mean = 44063.33
water_mean = 23545.8

calibration_range = air_mean - water_mean
def moisture_percent(reading):
    if reading >= air_mean:
        return 0
    elif reading <= water_mean:
        return 100
    else:
        return round(((air_mean - reading) / calibration_range * 100),1)
    
#Test the function
print(moisture_percent(44063.33))  # Should return 0
print(moisture_percent(23545.8))   # Should return 100
print(moisture_percent(30000))     # Should return a value between 0 and 100
#Mental calculation for the 30000 reading:
#air mean- water mean = 44063.33 - 23545.8 = 20517.53
#(44063.33 - 30000)= 14063.33 / 20517.53 ≈ 0.685 * 100 = 68.5%

#Turning the % into categories
lucky_bamboo = {
    "Very Dry": 20,
    "Dry": 40,
    "Moist": 60,
    "Wet": 80,
    "Way Overdone": 100
}

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
    
#Testing------

reading = 30000

percent = moisture_percent(reading)
status = moisture_status(percent)

print(f"Sensor Reading: {reading}")
print(f"Moisture: {percent}%")
print(f"Status: {status}")




