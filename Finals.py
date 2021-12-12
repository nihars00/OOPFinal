import arrow
import Tkinter
import requests, json
from arrow import Arrow
from Tkinter import *
#import of all the packages used in the project

utc = arrow.utcnow()
#fetching of utc from the web in aroow package

def usd_to_eur(usd):
    return 0.88*usd;
    #use of method to convert currency

usdi = float(input("Enter your amount in $"))
ute = usd_to_eur(usdi)
print("The Sum of $ {0} in  Euros = {1}".format(usdi, ute))
#object and method call to change the amount provided in $ to Euro

#Getting the desired time and conversion units fr length, volume and currency for the specific ountry
print("Refer to the legend below and get time dialog box and weather of the place")
#UTC+8:00
print("Enter 1 for China-Shanghai") 
#UTC+5:30
print("Enter 2 for India-Kolkata")
#UTC+1:00
print("Enter 3 for France-Paris")
#UTC+9:00
print("Enter 4 for Korea-Seoul") 
#UTC+1:00
print("Enter 5 for Germany-Berlin")
#UTC+2:00
print("Enter 6 for Egypt-Cairo")
#UTC-6:00
print("Enter 7 for Mexico-Mexico City") 
#UTC-3:00
print("Enter 8 for Brazil-Rio De Janerio")
#UTC+1:00
print("Enter 9 for United States-New York City")
#UTC+:9:00
print("Enter 10 for Japan-Tokyo")

input_ft = input()
input_ft = int(input_ft)
#fetching input for the city as an integer

if input_ft == 1:
    local = utc.to('Asia/Shanghai')
    #setting local time to Shanghai from UTC

    window = Tk()
    window.title("Time in Shanghai")
    window.geometry("500x500")
    #description of the dialog box to pop up for the time

    label_title = Label(window,text=local,font=(20))
    label_title.grid(column=0, row=0, columnspan=2)
    #description of text of the time that woould appear

    window.mainloop()

    api_key = "a5252eb0a385c58d58075374ff6f0639"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Shanghai"
    #string variable fo the full URL in parts

    complete_url = base_url + "APPID=" + api_key + "&q=" + city_name
    #foorming the full link of the pllace that we wish to fetch the time for

    print("Weather in Shanghai is as follows")

    response = requests.get(complete_url)
    #using request package to get the data froom the URL

    x = response.json()
    #converting the response of the data fetched into JavaScript

    if x["cod"] != "404":
        #making sure for no errors
 
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
        #determining the weather and its description in a specific place
 
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))
    
elif input_ft == 2:

    local = utc.to('Asia/Kolkata')

    window = Tk()
    window.title("Time in Kolkata")
    window.geometry("500x500")

    label_title = Label(window,text=local,font=(20))
    label_title.grid(column=0, row=0, columnspan=2)

    window.mainloop()

    api_key = "a5252eb0a385c58d58075374ff6f0639"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Kolkata"

    complete_url = base_url + "APPID=" + api_key + "&q=" + city_name

    print("Weather in Kolkata is as follows")

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
 
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))



elif input_ft == 3:
    local = utc.to('Europe/Paris')

    window = Tk()
    window.title("Time in Paris")
    window.geometry("500x500")

    label_title = Label(window,text=local,font=(20))
    label_title.grid(column=0, row=0, columnspan=2)

    window.mainloop()

    api_key = "a5252eb0a385c58d58075374ff6f0639"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Paris"

    complete_url = base_url + "APPID=" + api_key + "&q=" + city_name

    print("Weather in Paris is as follows")

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
 
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))

if input_ft == 4:
    local = utc.to('Asia/Seoul')

    window = Tk()
    window.title("Time in Seoul")
    window.geometry("500x500")

    label_title = Label(window,text=local,font=(20))
    label_title.grid(column=0, row=0, columnspan=2)

    window.mainloop()

    api_key = "a5252eb0a385c58d58075374ff6f0639"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Seoul"

    complete_url = base_url + "APPID=" + api_key + "&q=" + city_name

    print("Weather in Seoul is as follows")

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
 
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))

elif input_ft == 5:
    local = utc.to('Europe/Berlin')

    window = Tk()
    window.title("Time in Berlin")
    window.geometry("500x500")

    label_title = Label(window,text=local,font=(20))
    label_title.grid(column=0, row=0, columnspan=2)

    window.mainloop()

    api_key = "a5252eb0a385c58d58075374ff6f0639"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Berlin"

    complete_url = base_url + "APPID=" + api_key + "&q=" + city_name

    print("Weather in Berlin is as follows")

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
 
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))
    
elif input_ft == 6:

    local = utc.to('Africa/Cairo')

    window = Tk()
    window.title("Time in Cairo")
    window.geometry("500x500")

    label_title = Label(window,text=local,font=(20))
    label_title.grid(column=0, row=0, columnspan=2)

    window.mainloop()

    api_key = "a5252eb0a385c58d58075374ff6f0639"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Cairo"

    complete_url = base_url + "APPID=" + api_key + "&q=" + city_name

    print("Weather in Cairo is as follows")

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
 
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))

if input_ft == 7:

    local = utc.to('US/Central')

    window = Tk()
    window.title("Time in Mexico City")
    window.geometry("500x500")

    label_title = Label(window,text=local,font=(20))
    label_title.grid(column=0, row=0, columnspan=2)

    window.mainloop()

    api_key = "a5252eb0a385c58d58075374ff6f0639"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Mexico City"

    complete_url = base_url + "APPID=" + api_key + "&q=" + city_name

    print("Weather in Mexico City is as follows")

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
 
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))

elif input_ft == 8:

    local = utc.to('Brazil/East')

    window = Tk()
    window.title("Time in Rio de Janeiro")
    window.geometry("500x500")

    label_title = Label(window,text=local,font=(20))
    label_title.grid(column=0, row=0, columnspan=2)

    window.mainloop()


    api_key = "a5252eb0a385c58d58075374ff6f0639"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Rio De Janeiro"

    complete_url = base_url + "APPID=" + api_key + "&q=" + city_name

    print("Weather in Rio De Janeiro is as follows")

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
 
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))
    
elif input_ft == 9:

    local = utc.to('US/Eastern')

    window = Tk()
    window.title("Time in New York")
    window.geometry("500x500")

    label_title = Label(window,text=local,font=(20))
    label_title.grid(column=0, row=0, columnspan=2)

    window.mainloop()


    api_key = "a5252eb0a385c58d58075374ff6f0639"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "New York"

    complete_url = base_url + "APPID=" + api_key + "&q=" + city_name

    print("Weather in New York is as follows")

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
 
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))

elif input_ft == 10:

    local = utc.to('Asia/Tokyo')

    window = Tk()
    window.title("Time in Tokyo")
    window.geometry("500x500")

    label_title = Label(window,text=local,font=(20))
    label_title.grid(column=0, row=0, columnspan=2)

    window.mainloop()

    api_key = "a5252eb0a385c58d58075374ff6f0639"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Tokyo"

    complete_url = base_url + "APPID=" + api_key + "&q=" + city_name

    print("Weather in Tokyo is as follows")

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
 
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))