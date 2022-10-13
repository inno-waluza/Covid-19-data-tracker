from covid import Covid
import pyttsx3
from GetAdvice import advice


engine = pyttsx3.init()
engine1 = pyttsx3.init()

##voice rate
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

##voice options 0 for male 1 for female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

covid = Covid()
covid.get_data()

engine1.say("Welcome to the covid 19 data tracker made by numnet!")
engine1.runAndWait()
while(1):
    engine.say("enter country name")
    engine.runAndWait()
    try:
        country_name = input("Enter Country Name: ")
        covid_data = covid.get_status_by_country_name(country_name)

        country = covid_data["country"]
        comfirmed = covid_data['confirmed']
        active = covid_data['active']
        deaths = covid_data['deaths']
        recovered = covid_data['recovered']

        print("Country", country)
        print("Confirmed Cases " ,comfirmed)
        print("Active Cases " ,active)
        print("Recovered Cases " ,recovered)
        print("Deaths " ,deaths)

        engine.say("Covid 19 data in " + str(country) +"," + "confirmed cases," + str(comfirmed) + "," + "active cases," + str(active) + "," + "recovered cases," + str(recovered) + "," + "Deaths," + str(deaths))
        engine.runAndWait()
        engine.say("random advice" + str(advice))
        engine.runAndWait()
    except:
        engine.say("oops!!!, country not found, try again please")
        print("oops!!!, country not found, try again please")
        engine.runAndWait()  
