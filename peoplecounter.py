from ubidots import ApiClient
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
try:
    api =ApiClient("e62234c8846318b2962b69c29b62a0b7bbd5ed18")
    people = api.get_variable("578cc74b7625422c4e939b61")
except:
        print("Couldn't connect to the API, check your Internet connection")
counter = 0
peoplecount = 0
while(1):
    presence = GPIO.input(17)
    if(presence):
        peoplecount += 1
        presence = 0
        time.sleep(1.5)
        time.sleep(1)
        counter += 1
if(counter==10):
    print(peoplecount)
people.save_value({'value':peoplecount})
counter = 0
peoplecount = 0
