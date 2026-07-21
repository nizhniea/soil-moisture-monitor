#Version_2.0.py
import serial
pico = serial.Serial("COM7", 115200, timeout=2)
from datetime import datetime
import os


lucky_bamboo = {
    "Very Dry": 20,
    "Dry": 40,
    "Moist": 60,
    "Wet": 80,
    "Soaking in water?": 100
}
dry_soil_mean = 43843.6
moist_soil_mean = 42893.2
water_mean = 23545.8


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

import tkinter as tk

app = tk.Tk()
app.title("Moisture Sensor Monitor")
app.geometry("500x400")
app.configure(bg="#E8F5E9")

title = tk.Label(
    app,
    text="Lucky Bamboo Moisture Monitor",
    font=("Segoe UI", 20, "bold"),
    bg="#E8F5E9",
    fg="#183519",
)
title.pack(pady=(20, 10))

moisture_label = tk.Label(
    app,
    text="0%",
    font=("Segoe UI", 36, "bold"),
    bg="#E8F5E9",
    fg="#1B5E20",
)
moisture_label.pack(pady=10)

status_label = tk.Label(
    app,
    text="Waiting for measurement...",
    font=("Segoe UI", 14),
    bg="#E8F5E9",
    fg="#555555",
)
status_label.pack(pady=10)

def measure():
    pico.write(b"measure\n")

    reading = pico.readline().decode().strip()
    reading = float(reading)
    
    print(f"Reading: {reading}")

    percent = moisture_percent(reading)
    print(f"Percent: {percent}")
    
    percent = moisture_percent(reading)
    moisture_label.config(text=f"{percent}%")

    status = moisture_status(percent)
    status_label.config(text=status)

    save_measurement(reading, percent, status)

def save_measurement(reading, percent, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists("moisture_log_2.csv"):
        with open("moisture_log_2.csv", "a") as file:
            file.write("Timestamp,Reading,Percent,Status\n")

    with open("moisture_log_2.csv", "a") as file:
        file.write(f"{timestamp},{reading},{percent},{status}\n")

def show_graph():
    print("Graph button clicked!")

graph_button = tk.Button(
    app,
    text="View History Graph",
    command=show_graph,
    bg="#EBC2C2",
    font=("Segoe UI", 14, "bold"),
    fg="white",
    activebackground="#7FBA84",
    activeforeground="white",
)
graph_button.pack(pady=10)

measure_button = tk.Button(
    app,
    text="Measure Moisture",
    command=measure,
    bg="#032606",
    font=("Segoe UI", 14, "bold"),
    fg="white",
    activebackground="#0B4D10",
    activeforeground="white",
)
measure_button.pack(pady=20)

app.mainloop()