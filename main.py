import tkinter as tk
import requests
import time


def getWeather(view):
    city = textBox.get()

    # Acquiring data using openweather API.
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9c5484b69c7d724dd164f4d9e324963f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


view = tk.Tk()
view.geometry("600x500")
view.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textBox = tk.Entry(view, justify='center', width=20, font=t)
textBox.pack(pady=20)
textBox.focus()
textBox.bind('<Return>', getWeather)

label1 = tk.Label(view, font=t)
label1.pack()
label2 = tk.Label(view, font=f)
label2.pack()
view.mainloop()