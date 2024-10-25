import requests
import tkinter as tk
from config import WEATHER_API_KEY
from tkinter import messagebox, font



def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        # Raise HTTPError if the response was bad
        response.raise_for_status()  
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"Error: {data.get('message', 'City not found')}")
            return

        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Displaying the weather data in a messagebox
        messagebox.showinfo("Weather Info", f"Weather in {city}:\n"
        f"Description: {weather}\n"
        f"Temperature: {temperature:.0f}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed} m/s")
    
   
    except Exception as err:
        messagebox.showerror("Error", f"Error occurred: {err}")

def on_submit():
    city = city_entry.get()
    api_key = os.getenv("WEATHER_API_KEY")  # Replace with your OpenWeatherMap API key
    get_weather(city, api_key)

# Setting up the GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
root.configure(bg="#87CEEB") 
# Setting a custom font
custom_font = font.Font(family="Helvetica", size=12)

# Create a label and entry for the city
label = tk.Label(root, text="Enter City Name:", bg="#87CEEB", font=custom_font)
label.pack(pady=10)
city_entry = tk.Entry(root, font=custom_font)
city_entry.pack(pady=10)

# Create a submit button
submit_btn = tk.Button(root, text="Get Weather", command=on_submit, bg="#FF4500", fg="white", font=custom_font)
submit_btn.pack(pady=20)

# Run the GUI event loop
root.mainloop()
