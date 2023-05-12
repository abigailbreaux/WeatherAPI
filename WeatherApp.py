import WeatherInfo

WeatherInfo.setKey("ee7c9f2f76474f978171695d26402836")
 
again="Y"
while again=="Y":
  userCity = input("Please enter a city: ")
  WeatherInfo.setCity(userCity)

  success = WeatherInfo.updateWeather()

  if(success == True):
    print("")
  else:
    print("Invalid City")

  description = WeatherInfo.getDescription()
  print("In", userCity, "it is: " + description)

  ktemp = WeatherInfo.getTemp()
  ftemp = (ktemp - 273.15)*(9/5)+32
  ftemp = round(ftemp, 1)
  print("The temperature is " + str(ftemp ) + " degrees fahrenheit")

  feelTempK = WeatherInfo.getFeelsLike()
  feelTempF = (feelTempK - 273.15)*(9/5)+32
  feelTempF = round(feelTempF, 1)
  print("It feels like " + str(feelTempF ) + " degrees fahrenheit")

  humidity = WeatherInfo.getHumidity()
  print("The humidity is " + str(humidity ) + " percent ")

  metersSpeed = WeatherInfo.getWindSpeed()
  milesSpeed = metersSpeed*0.44704
  beaufort = ""
  if milesSpeed <1:
    beaufort = "calm"
  elif 1<= milesSpeed <4:
    beaufort = "light air"
  elif 4<= milesSpeed <8:
    beaufort = "light breeze"
  elif 8<= milesSpeed <13:
    beaufort = "gentle breeze"
  elif 13<= milesSpeed <19:
    beaufort = "moderate speed"
  elif 19<= milesSpeed <25:
    beaufort = "fresh breeze"
  elif 25<= milesSpeed <32:
    beaufort = "strong breeze"
  elif 32<= milesSpeed <39:
    beaufort = "high wind"
  elif 39<= milesSpeed <47:
    beaufort = "gale"
  elif 47<= milesSpeed <55:
    beaufort = "strong gale"
  elif 55<= milesSpeed <64:
    beaufort = "storm"
  elif 64<= milesSpeed <73:
    beaufort = "violent storm"
  elif milesSpeed >=73:
    beaufort = "hurricane"
  milesSpeed= round(milesSpeed, 1)
  print("The wind speed is " + str(milesSpeed ) + " miles per hour - " + str(beaufort) )

  if 55<= feelTempF <65:
    print("You should wear a light jacket")
  if 40<= feelTempF <55:
    print("You should wear a medium jacket")
  if feelTempF < 40:
    print("You should wear a heavy coat")

  if ("mist" in description) or ("drizzle" in description) or ("light rain" in description) or ("rain" in description) or ("heavy rain" in description):
    print("Bring an umbrella")

  again= input("Would you like another weather report? (Y/N): ")
  print("")

print("Thank you, have a good day")
