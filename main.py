import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city_name, api_key):
    # URL API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        # Wysyłanie żądania GET
        response = requests.get(url)
        response.raise_for_status()  # Sprawdzenie poprawności odpowiedzi
        data = response.json()

        # Pobieranie danych z odpowiedzi API
        city = data['name']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        # Wyświetlenie wyników w oknie
        result = (
            f"Pogoda w {city}:\n"
            f"Temperatura: {temperature}°C\n"
            f"Temperatura odczuwalna: {feels_like}°C\n"
            f"Wilgotność: {humidity}%\n"
            f"Wiatr: {wind_speed} m/s\n"
            f"Opis: {weather.capitalize()}"
        )
        messagebox.showinfo("Pogoda", result)

    except requests.exceptions.HTTPError as http_err:
        messagebox.showerror("Błąd HTTP", f"HTTP error: {http_err}")
    except Exception as err:
        messagebox.showerror("Błąd", f"Inny błąd: {err}")

def fetch_weather():
    city = city_entry.get()
    if city:
        api_key = "ac50e6033cd78af94115bb526d8033a8"  # Twój klucz API
        get_weather(city, api_key)
    else:
        messagebox.showwarning("Brak danych", "Wprowadź nazwę miasta!")

# Tworzenie okna głównego
root = tk.Tk()
root.title("Pogoda")

# Etykieta i pole tekstowe
tk.Label(root, text="Podaj nazwę miasta:").pack(pady=80)
city_entry = tk.Entry(root, width=40)
city_entry.pack(pady=80)

# Przycisk
tk.Button(root, text="Pobierz pogodę", command=fetch_weather).pack(pady=40)

# Uruchomienie okna
root.mainloop()
