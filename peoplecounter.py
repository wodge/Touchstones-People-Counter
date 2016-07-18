from ubidots import ApiClient
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)
try:
    api = ApiClient("04856548e100d631985d3e9bd9d112c1846ff8da")
    people = api.get_variable("55b2b19376254219c59334c0")
except:
        print("Couldn't connect to the API, check your Internet connection")
counter = 0
peoplecount = 0
while(1):
    presence = GPIO.input(7)
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
