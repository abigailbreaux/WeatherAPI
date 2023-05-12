Final Project - Weather API

The goal of the code is to create a weather reporting application that utilizes the OpenWeatherMap API to retrieve and display weather information for a specified city. The code prompts the user to enter a city, retrieves the weather data using the API, and presents details such as weather description, temperature, humidity, pressure, and wind speed. It also includes additional features like converting temperature units and providing recommendations based on weather conditions. The code aims to provide users with an easy-to-use interface to obtain accurate and up-to-date weather information for their desired location.

1. The code begins by importing the necessary libraries: `urllib.request` for making HTTP requests and `json` for working with JSON data.

2. Global variables are defined to store the user's API key, the city for which weather information is requested, and various weather data such as description, temperature, humidity, pressure, and wind speed.

3. The `setKey(key)` function is defined to set the user's API key.

4. The `setCity(city)` function is defined to set the city for which weather information is requested. The city name is URL-encoded by replacing spaces with "%20".

5. The `updateWeather()` function is defined to retrieve weather data from the OpenWeatherMap API. It constructs the API URL using the user's API key and the city, and then makes a request to the API. If the request is successful, the JSON response is parsed and weather data is extracted and stored in the global variables.

6. Several getter functions (`getDescription()`, `getTemp()`, `getFeelsLike()`, `getHumidity()`, `getPressure()`, `getWindSpeed()`) are defined to retrieve the weather data stored in the global variables.

7. The main code starts by setting the user's API key using `WeatherInfo.setKey("ee7c9f2f76474f978171695d26402836")`. Replace the empty string with your actual API key.

8. A while loop is used to repeatedly ask the user for a city and retrieve weather information until the user chooses to stop.

9. Inside the loop, the user is prompted to enter a city.

10. The `setCity()` function is called to set the city based on the user's input.

11. The `updateWeather()` function is called to retrieve weather data for the specified city. If the retrieval is successful, the program continues; otherwise, an error message is displayed.

12. The `getDescription()` function is called to retrieve the weather description and print it.

13. The temperature is retrieved using `getTemp()`, converted from Kelvin to Fahrenheit, rounded to one decimal place, and printed.

14. The "feels like" temperature is retrieved using `getFeelsLike()`, converted from Kelvin to Fahrenheit, rounded to one decimal place, and printed.

15. The humidity is retrieved using `getHumidity()` and printed.

16. The wind speed is retrieved using `getWindSpeed()`, converted from meters per second to miles per hour, rounded to one decimal place, and printed. Additionally, the wind speed is classified into different Beaufort scale categories based on its value.

17. Based on the "feels like" temperature, different jacket recommendations are printed.

18. Based on the weather description, if it contains keywords related to precipitation, a message to bring an umbrella is printed.

19. The user is prompted to choose whether they want another weather report. If they enter 'Y', the loop continues; otherwise, the loop ends.

20. Finally, a closing message is displayed.

The code essentially retrieves weather data from the OpenWeatherMap API for a user-specified city and presents it in a user-friendly format, providing information such as description, temperature, humidity, pressure, and wind speed.
