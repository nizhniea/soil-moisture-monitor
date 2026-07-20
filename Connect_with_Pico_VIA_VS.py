import serial

print("Opening connection...")

pico = serial.Serial("COM7", 115200, timeout=2)

print("Connected!")

pico.write(b"measure\n")
print("Command sent!")

reading = pico.readline().decode().strip()
reading = float(reading)

print("Raw reading:", reading)
