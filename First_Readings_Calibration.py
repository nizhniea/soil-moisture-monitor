#First readings in air
Moisture: 18084    #Huge outlier
Moisture: 43930
Moisture: 43994
Moisture: 43978
Moisture: 43978
Moisture: 44314
Moisture: 44186
Moisture: 44170
Moisture: 44010
Moisture: 44010
#Finished

#First readings in dry soil
Moisture: 44090
Moisture: 43786
Moisture: 43802
Moisture: 43818
Moisture: 43818
Moisture: 43818
Moisture: 43818
Moisture: 43802
Moisture: 43850
Moisture: 43834
#Finished

#First reading in barely moist soil
Moisture: 42858
Moisture: 42826
Moisture: 42938
Moisture: 42970
Moisture: 42922
Moisture: 42906
Moisture: 42890
Moisture: 42858
Moisture: 42922
Moisture: 42842
#Finished

#First reading in water
Moisture: 23557
Moisture: 23525
Moisture: 23525
Moisture: 23525
Moisture: 23525
Moisture: 23493
Moisture: 23509
Moisture: 23493
Moisture: 23749
Moisture: 23557
#Finished

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

air = [18084, 43930, 43994, 43978, 43978, 44314, 44186, 44170, 44010, 44010]
dry_soil = [44090, 43786, 43802, 43818, 43818, 43818, 43818, 43802, 43850, 43834]
barely_moist_soil = [42858, 42826, 42938, 42970, 42922, 42906, 42890, 42858, 42922, 42842]
water = [23557, 23525, 23525, 23525, 23525, 23493, 23509, 23493, 23749, 23557]

#Calculate the statistics
#Mean:
mean_air = np.mean(air)
mean_dry_soil = np.mean(dry_soil)
mean_barely_moist_soil = np.mean(barely_moist_soil)
mean_water = np.mean(water)
#Standard Deviation:
std_air = np.std(air)
std_dry_soil = np.std(dry_soil)
std_barely_moist_soil = np.std(barely_moist_soil)
std_water = np.std(water)
## Minimum and Maximum:
min_air = np.min(air)
min_dry_soil = np.min(dry_soil)
min_barely_moist_soil = np.min(barely_moist_soil)
min_water = np.min(water)

max_air = np.max(air)
max_dry_soil = np.max(dry_soil)
max_barely_moist_soil = np.max(barely_moist_soil)
max_water = np.max(water)
#Print Results for all statistics:
print("Mean values:")
print(f"Air: {mean_air}")
print(f"Dry Soil: {mean_dry_soil}")
print(f"Barely Moist Soil: {mean_barely_moist_soil}")
print(f"Water: {mean_water}")

print("\nStandard Deviations:")
print(f"Air: {std_air}")
print(f"Dry Soil: {std_dry_soil}")
print(f"Barely Moist Soil: {std_barely_moist_soil}")
print(f"Water: {std_water}")

print("\nMinimum values:")
print(f"Air: {min_air}")
print(f"Dry Soil: {min_dry_soil}")
print(f"Barely Moist Soil: {min_barely_moist_soil}")
print(f"Water: {min_water}")

print("\nMaximum values:")
print(f"Air: {max_air}")
print(f"Dry Soil: {max_dry_soil}")
print(f"Barely Moist Soil: {max_barely_moist_soil}")
print(f"Water: {max_water}")


#Results:
#Mean values:
#Air: 41465.4    <--Will be updated.
#Dry Soil: 43843.6
#Barely Moist Soil: 42893.2
#Water: 23545.8

#Standard Deviations:
#Air: 7794.64739677171  <--Will be updated.
#Dry Soil: 83.8131254637363
#Barely Moist Soil: 43.992726671576065
#Water: 70.8530874415505

## Minimum values:
#Air: 18084   <--Will be updated.
#Dry Soil: 43786
#Barely Moist Soil: 42826
#Water: 23493

#Maximum values:
## Air: 44314   
## Dry Soil: 44090
## Barely Moist Soil: 42970
## Water: 23749


#The water is going to be 100% moisture 
#Air is 0% moisture
#Percentages will be calculated based on these values to get a range. 

#The outlier in the first Air reading needs to be addressed.
air = np.delete(air, 0)  # Remove the outlier from the first Air reading
# Updated air values after removing the outlier.
print(f"Updated Air values: {air}")
#All of the updated air values after removing the outlier are:
print(f"Updated Air mean: {np.mean(air)}")
print(f"Updated Air standard deviation: {np.std(air)}")
print(f"Updated Air minimum: {np.min(air)}")
print(f"Updated Air maximum: {np.max(air)}")

#So the updated air values provide a more accurate representation of the sensor readings.
#New calculations based on the updated air values:
#Air values: [43930 43994 43978 43978 44314 44186 44170 44010 44010]
#Updated Air mean: 44063.333333333336
#Updated Air standard deviation: 121.15004471040584
#Updated Air minimum: 43930
#Updated Air maximum: 44314
