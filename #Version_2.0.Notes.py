#Version_2.0.py Notes

#Attempting to work with Tkinter to make a seperate application for the sensor.
#Adding more features and improving the user interface.
#Using Tkinter to create a more interactive and user-friendly interface for the moisture monitoring system.
#This will include an application window.
#The window will give users the option to see the current moisture levels, historical data, and graphs.
#Need to connect this back with CSV file.
#Made a semi-permenant color for the background of the GUI- *Add custom designed background via Canvas in future*


def measure():
    pico.write(b"measure\n")

    reading = pico.readline().decode().strip()

    reading = float(reading)
    
    percent = moisture_percent(reading)
    moisture_label.config(text=f"{percent}%")
    status_label.config(text=moisture_status(percent))

measure_button = tk.Button(
    app,
    text="Measure Moisture",
    command=measure
)
measure_button.pack(pady=20)
app.mainloop()