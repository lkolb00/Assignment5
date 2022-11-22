# ISQA 3900
# Lucas Kolb
# Working with API and JSON file
# ISQA 3900 Open Weather API
# Sunday, November 21, 2022

from datetime import datetime
import requests
import pytemperature

def output(output_string,output_file):
    if output_file:  #if it is not None (i.e valid output filename)
        print(output_string,file=output_file)  #writing into the file
    print(output_string) #writing into the console



def main():
    api_start = 'https://api.openweathermap.org/data/2.5/weather?q='
    api_key = '&appid=d349ad7bcfd3bf294667ee80d4a82f54'
    now = datetime.now()

    filename = input("\nEnter the output filename: ")
    myfile = None
    try:
        myfile = open(filename, "w")
    except:
        print("Unable to open file " + filename +"\nData will not be saved to a file")
    choice = "y"

    output("ISQA 3900 Open Weather API", myfile)
    output("Lucas Kolb", myfile)
    output(now.strftime("%A, %B %d, %Y"), myfile)

    while choice.lower() == "y":
        # input city and country code
        city = input("Enter city: ")
        print("Use ISO letter country code like: https://countrycode.org/")
        country = input("Enter country code: ")

        # app configures url to generete json data
        url = api_start + city + ',' + country + api_key
        json_data = requests.get(url).json()

        try:
            # getting weather data from json
            weather_description = json_data['weather'][0]['description']
            weather_tempture = json_data['main']['temp']
            weather_humidity = json_data['main']['humidity']
            weather_max = json_data['main']['temp_max']
            weather_min = json_data['main']['temp_min']

            # printing weather information
            output("\nThe Weather Report for " + city + " in " + country + " is:", myfile)
            output("\tCurrent conditions: " + weather_description, myfile)
            print("\tCurrent Temperature in Fahrenheit is:  ", weather_tempture )
            print("\tCurrent Humidity:  ", weather_humidity)
            print("\tExpected High Temperature in Fahrenheit:  ",  weather_max)
            print("\tExpected Low Temperature in Fahrenheit:  ", weather_min)

            # getting expected high temp data from json
            expected_high_temp = json_data['main']['temp_max']
            expected_high_temp = pytemperature.k2f(expected_high_temp)

            # printing expected high temp information #modified
            output("\tExpected high temperature in Fahrenheit: " + str(expected_high_temp), myfile)

            choice = input("Continue (y/n)?: ")
            print()

        except:
            print("Unable to access ", city, " in ", country)
            print("Verify city name and country code")


    if myfile:
        myfile.close()
    print('Thank you - Goodbye')

if __name__ == "__main__":
    main()
