#Calibration_Prep_Version3_Notes

#After testing moisture in the same exact location, back to back, readings came back with variance each time the program ran.
#First run, program gave back:
Reading: 43331.6
Percent: 26.9
Reading: 43230.8
Percent: 32.2
Reading: 43272.4
Percent: 30.1

#Second run, program gave back:
Reading: 42989.2
Percent: 44.9
Reading: 42899.6
Percent: 49.7
Reading: 42878.8
Percent: 50.0

#Variance of about 300-400 units, even though the soil, location of sensor in soil, time, and conditions did not have any obvious changes.
#Possible explanations: Sensor variance, sensor recalibration, sensor malfunction, soil moisture redistribution, 

#How consistent is the sensor in the same conditions?
#Will reconduct what was done above, approx. 30 mins after the previous readings.
#First program run:
Reading: 41834.0
Percent: 52.7
Reading: 41824.4
Percent: 52.8
Reading: 41859.6
Percent: 52.7
Reading: 41821.2
Percent: 52.8
Reading: 41818.0
Percent: 52.8
#Second program run:
Reading: 41762.0
Percent: 52.9
Reading: 41856.4
Percent: 52.7
Reading: 41902.8
Percent: 52.6
Reading: 41808.4
Percent: 52.8
Reading: 41950.8
Percent: 52.4

#Findings are more consistent the second time around, per program run, compared to the first one. This points me away from calling this a 
#sensor malfunction, or that the sensor is coming up with fake values. Thus I will test in lukewarm water and air, to ensure consistent results.

#First *air* program run:
Reading: 44176.4
Percent: 0
Reading: 44125.2
Percent: 0
Reading: 44168.4
Percent: 0
Reading: 44149.2
Percent: 0
Reading: 44205.2
Percent: 0

#Second *air* program run:
Reading: 44091.6
Percent: 0
Reading: 44226.0
Percent: 0
Reading: 44237.2
Percent: 0
Reading: 44123.6
Percent: 0
Reading: 44112.4
Percent: 0

#First *water* program run:
Reading: 17463.2
Percent: 100
Reading: 17480.8
Percent: 100
Reading: 17495.2
Percent: 100
Reading: 17412.0
Percent: 100
Reading: 17490.4
Percent: 100

#Second *water* program run:
#Took out the sensor, patted dry, put back in the water once program loaded back up and measured)
Reading: 17362.4
Percent: 100
Reading: 17316.0
Percent: 100
Reading: 17384.8
Percent: 100
Reading: 17357.6
Percent: 100
Reading: 17293.6
Percent: 100

#consistent results amongst air and water test trials. Possible explanations for inconsistent results for the soil include:
#possible soil changes, or perhaps the sensor needs time to warm up, leading to more inacurate results the first couple of times.
#The problem lies in the fact that the sensor reads consistently per each program run, however, the readings in each program run are not consistent with each other- except for the second experiment, which yeilded consistent results in prgram run #1 and #2.
#To sum up: First experiement program #1 + #2 = not consistent results. 
#Second experiment program #1 + #2 = consistent results
#First experiement program results + Second experiement results = not consistent. 

#High within-run consistency but lower between-run consistency#

#Further Testing:
#I will test if the issue lies in restarting the program or not. This experiement will only target the soil.
#I will run measurments in intervals, keeping the sensor plugged in, every 5 minutes. 

#First measurments:
Reading: 43291.6
Percent: 29.0
Reading: 43245.2
Percent: 31.5
Reading: 43290.0
Percent: 29.1
Reading: 43294.8
Percent: 28.9
Reading: 43291.6
Percent: 29.0

#Second measurment:
Reading: 43000.4
Percent: 44.4
Reading: 43016.4
Percent: 43.5
Reading: 43136.4
Percent: 37.2
Reading: 42998.8
Percent: 44.4
Reading: 42986.0
Percent: 45.1

#Third measurment:
Reading: 42947.6
Percent: 47.1
Reading: 42955.6
Percent: 46.7
Reading: 42920.4
Percent: 48.6
Reading: 42899.6
Percent: 49.7
Reading: 42955.6
Percent: 46.7

#Fourth measurment:
Reading: 42902.8
Percent: 49.5
Reading: 42930.0
Percent: 48.1
Reading: 42890.0
Percent: 50.0
Reading: 42875.6
Percent: 50.0
Reading: 42941.2
Percent: 47.5

#Fifth measurment:
Reading: 43008.4
Percent: 43.9
Reading: 42974.8
Percent: 45.7
Reading: 42805.2
Percent: 50.2
Reading: 42931.6
Percent: 48.0
Reading: 42906.0
Percent: 49.3

#Sixth measurment:
Reading: 42870.8
Percent: 50.1
Reading: 42904.4
Percent: 49.4
Reading: 42846.8
Percent: 50.1
Reading: 42886.8
Percent: 50.0
Reading: 42819.6
Percent: 50.2

#Results are becoming consistent, measurment trials will end here.
#Results show that the differences in results is not due to the program restarting, since the program was kept running all 6 trials.
#Another attempt will be made, this time inserting the sensor in a different position, about halfway up the sensor board, so it will be more emersed in the soil.
#Trial #1:Reading: 35105.6
Percent: 70.1
Reading: 35155.2
Percent: 70.0
Reading: 35212.8
Percent: 69.8
Reading: 35225.6
Percent: 69.8
Reading: 35116.8
Percent: 70.1

#Trail 2, but the program had to be restarted:
Reading: 34820.8
Percent: 70.9
Reading: 34833.6
Percent: 70.8
Reading: 34780.8
Percent: 71.0
Reading: 34804.8
Percent: 70.9
Reading: 34804.8
Percent: 70.9
Reading: 34924.8
Percent: 70.6

#Trial 3:
Reading: 34771.2
Percent: 71.0
Reading: 34881.6
Percent: 70.7
Reading: 34822.4
Percent: 70.9
Reading: 34750.4
Percent: 71.0
Reading: 34793.6
Percent: 70.9

#Results turned out to be consisten amongst all trial groups, in this cohort of testing. 
#Sensor placement test: Previous testing produced substantial variation between measurement sessions when the sensor
#was inserted at a shallower position. To investigate whether sensor placement contributed to this variation, 
#the sensor was repositioned so that approximately half of the sensor board was immersed in soil, unlike just the tip that was recommended. 
#Three trials were conducted. Trial means were approximately 70.0%, 70.9%, and 70.9%, respectively. 
#Individual readings within each trial were also highly consistent. 
#These results suggest that sensor placement within the soil may have been a major source of the variation observed during earlier testing.
#The deeper placement will therefore be standardized for subsequent experimentation.