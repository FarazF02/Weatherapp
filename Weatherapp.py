import tkinter as tk
import requests
import time


# to get the data from API
# 16200 are the seconds we have to subtract from UTC time zone due to our location(Iran)
def getWeather_name(window):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=2caa626eb5e84edd7462d6e7ea8a9dca"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 16200))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] - 16200))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max temp: " + str(max_temp) + "\n" + "Min temp: " + str(min_temp) + "\n" + "Pressure: " + str(
        pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(
        wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)  # attaching final_info to label1
    label2.config(text=final_data)  # attaching final_data to label2


def getWeather_co(window):
    left_frame = tk.Frame(window)
    left_frame.pack()
    right_frame = tk.Frame(window)
    right_frame.pack()
    lab1 = tk.Label(window, text="Enter altitude: ")
    lab1.pack()
    textfield = tk.Entry(window, font=f2)
    textfield.pack()
    lab2 = tk.Label(window, text="Enter latitude: ")
    textfield = tk.Entry(window, font=f2)
    textfield.pack()
    lab2.pack()

window = tk.Tk()
window.geometry("600x500")
window.title("Weather App")
window.resizable(0,0)

f1 = ("font", 15, "bold")
f2 = ("font", 35, "bold")

label3 = tk.Label(window, font=f1)
label3.pack()
label3.config(text="Please enter city name: ")
textfield = tk.Entry(window, font=f2)
textfield.pack(pady=20)
textfield.focus()  # type city name directly without moving the cursor
textfield.bind('<Return>', getWeather_co())

# to show the data
label1 = tk.Label(window, font=f2)
label1.pack()
label2 = tk.Label(window, font=f1)
label2.pack()

window.mainloop()
