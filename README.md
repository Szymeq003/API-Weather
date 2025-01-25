# Aplikacja Pogodowa

## Opis
Aplikacja Pogodowa to prosty program napisany w Pythonie, który pobiera i wyświetla aktualne dane pogodowe dla wybranego miasta. Aplikacja korzysta z API OpenWeatherMap do pozyskiwania danych.

## Wymagania
- Python 3.x
- Moduł `requests`
- Moduł `tkinter`
- Konto na [OpenWeatherMap](https://openweathermap.org/) i klucz API

## Instalacja
1. Sklonuj repozytorium na swój komputer.
    ```bash
    git clone https://twoje-repozytorium.git
    cd twoje-repozytorium
    ```
2. Zainstaluj wymagane moduły.
    ```bash
    pip install requests
    ```

## Konfiguracja
1. Utwórz plik `config.py` w głównym katalogu projektu.
2. Dodaj swój klucz API z OpenWeatherMap do pliku `config.py`.
    ```python
    API_KEY = 'Twój_klucz_API'
    ```

## Użycie
1. Uruchom aplikację.
    ```bash
    python app.py
    ```
2. Wprowadź nazwę miasta i kliknij przycisk "Pobierz pogodę", aby wyświetlić aktualne dane pogodowe.

## Kod
```python
import requests
import tkinter as tk
from tkinter import messagebox
from config import API_KEY

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        city = data['name']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

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
        get_weather(city, API_KEY)
    else:
        messagebox.showwarning("Brak danych", "Wprowadź nazwę miasta!")

root = tk.Tk()
root.title("Pogoda")

tk.Label(root, text="Podaj nazwę miasta:").pack(pady=80)
city_entry = tk.Entry(root, width=40)
city_entry.pack(pady=80)

tk.Button(root, text="Pobierz pogodę", command=fetch_weather).pack(pady=40)

root.mainloop()
