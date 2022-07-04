import tkinter as tk
import requests
import time
from tkinter.ttk import *


# to get the data from API
# 12600 are the seconds we have to add to UTC time zone due to our location(Iran)
# checking weather by city name
def getWeather_name(window):
    city = textfield.get()
    print(city)
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=2caa626eb5e84edd7462d6e7ea8a9dca"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    print(condition)
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 12600))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] + 12600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max temp: " + str(max_temp) + "\n" + "Min temp: " + str(min_temp) + "\n" + "Pressure: " + str(
        pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(
        wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)  # attaching final_info to label1
    label2.config(text=final_data)  # attaching final_data to label2


# Checking weather by city coordinates
def getWeather_co(window):
    label6 = tk.Label(window, font=f1)
    label6.pack()
    label6.configure(text="Enter city coordinates: ")
    long = textfield.get()
    lat = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?lat= "+ str(lat)+ "&lon=" + str(long) + "appid=2caa626eb5e84edd7462d6e7ea8a9dca&units=metric"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    print(condition)
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 12600))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] + 12600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max temp: " + str(max_temp) + "\n" + "Min temp: " + str(min_temp) + "\n" + "Pressure: " + str(
        pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(
        wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)  # attaching final_info to label1
    label2.config(text=final_data)  # attaching final_data to label2


window = tk.Tk()
window.geometry("600x500")
window.title("Weather App")
window.resizable(0, 0)
combo = Combobox(window)
combo['values']=("City name", "City coordinates")		#adding combobox items using the tuple
combo.pack()
combo['state'] = 'readonly'
combo.current(0)


f1 = ("font", 15, "bold")
f2 = ("font", 35, "bold")


def City_name():
    label3 = tk.Label(window, font=f1)
    label3.pack()
    label3.config(text="Please enter city name: ")
    textfield = tk.Entry(window, font=f2)
    textfield.pack(pady=20)
    textfield.focus()  # type city name directly without moving the cursor
    bt = Button(window, text="Check weather")
    textfield.bind('<Return>', getWeather_name)

def City_coordinates():
    # creating 3 frames
    top_frame = tk.Frame(window).pack()
    middle_frame = tk.Frame(window).pack()
    bottom_frame = tk.Frame(window).pack(side="bottom")
    label7 = tk.Label(window, font=f2)
    label7.pack()
    label7.config(text="Enter longitude: " + "\n")
    textfield =tk.Entry(window, font=f1)
    textfield.pack()
    label8 = tk.Label(window, font=f2)
    label8.pack()
    label8.config(text="Enter latitude: " + "\n")
    textfield = tk.Entry(window, font=f1)
    textfield.pack()
    bt = Button(window, text="Check weather")
    bt.pack()
combo.bind('<Return>', City_coordinates)


# to show the data
label1 = tk.Label(window, font=f2)
label1.pack()
label2 = tk.Label(window, font=f1)
label2.pack()

window.mainloop()
