import WeatherInfo
import tkinter as tk
from tkinter import messagebox

WeatherInfo.setKey("ee7c9f2f76474f978171695d26402836")


class WeatherApp(tk.Tk): #A simple weather application GUI
    def __init__(self) -> None: #Initialize the WeatherApp
        super().__init__()
        self.title("Weather App")
        self.geometry("400x300")

        self.city_label: tk.Label = tk.Label(self, text="Enter a city:")
        self.city_label.pack()

        self.city_entry: tk.Entry = tk.Entry(self)
        self.city_entry.pack()

        self.get_weather_button: tk.Button = tk.Button(
            self, text="Get Weather", command=self.get_weather
        )
        self.get_weather_button.pack()

        self.weather_info_label: tk.Label = tk.Label(self, text="")
        self.weather_info_label.pack()

        self.check_another_button: tk.Button = tk.Button(
            self, text="Check Another City", command=self.check_another_city
        )
        self.check_another_button.pack()
        self.check_another_button.pack_forget()

        self.mainloop()

    def get_weather(self) -> None: #Fetch and display weather information for the entered city
        user_city = self.city_entry.get()

        if not user_city:
            messagebox.showerror("Error", "Please enter a city name.")
            return

        WeatherInfo.setCity(user_city)
        success = WeatherInfo.updateWeather()

        if success:
            description = WeatherInfo.getDescription()
            ktemp = WeatherInfo.getTemp()
            ftemp = round((ktemp - 273.15) * (9 / 5) + 32, 1)
            feel_temp_k = WeatherInfo.getFeelsLike()
            feel_temp_f = round((feel_temp_k - 273.15) * (9 / 5) + 32, 1)
            humidity = WeatherInfo.getHumidity()
            meters_speed = WeatherInfo.getWindSpeed()
            miles_speed = round(meters_speed * 0.44704, 1)

            attire_suggestions = []
            if 55 <= feel_temp_f < 65:
                attire_suggestions.append("Wear a light jacket")
            if 40 <= feel_temp_f < 55:
                attire_suggestions.append("Wear a medium jacket")
            if feel_temp_f < 40:
                attire_suggestions.append("Wear a heavy coat")

            if (
                "mist" in description
                or "drizzle" in description
                or "light rain" in description
                or "rain" in description
                or "heavy rain" in description
            ):
                attire_suggestions.append("Bring an umbrella")

            attire_suggestions_text = "\n" + "\n".join(attire_suggestions) if attire_suggestions else ""

            self.weather_info_label.config(
                text=f"In {user_city}, it is: {description}\n"
                f"The temperature is {ftemp} degrees Fahrenheit\n"
                f"It feels like {feel_temp_f} degrees Fahrenheit\n"
                f"The humidity is {humidity} percent\n"
                f"The wind speed is {miles_speed} miles per hour"
                f"{attire_suggestions_text}"
            )

            # Hide the city entry, get weather button, and enter a city label
            self.city_entry.pack_forget()
            self.get_weather_button.pack_forget()
            self.city_label.pack_forget()

            # Display the Check Another City button
            self.check_another_button.pack()

        else:
            messagebox.showerror("Error", "Invalid city name.")

        self.city_entry.delete(0, tk.END)  # Clear the city entry box


    def check_another_city(self) -> None: #Reset the UI to enter another city
        self.weather_info_label.config(text="")
        self.city_label.pack()
        self.city_entry.delete(0, tk.END)  #
        self.city_entry.pack()
        self.get_weather_button.pack()
        self.check_another_button.pack_forget()

        self.mainloop()
        def add_item(self, item, quantity):
          item_info = {
            1: {"name": "Cookie", "price": 1.50},
            2: {"name": "Sandwich", "price": 4.00},
            3: {"name": "Water", "price": 1.00},
        }

          if item in item_info:
            item_name = item_info[item]["name"]
            item_price = item_info[item]["price"]

            if item_name in self.cart:
                self.cart[item_name]["quantity"] += quantity
            else:
                self.cart[item_name] = {"quantity": quantity, "price": item_price}

            if quantity == 1:
                messagebox.showinfo("Item Added", f"Added 1 {item_name}")
            else:
                messagebox.showinfo("Item Added", f"Added {quantity} {item_name}s")
          else:
            messagebox.showerror("Invalid Item", "Please select a valid item.")


if __name__ == "__main__":
    WeatherApp()
