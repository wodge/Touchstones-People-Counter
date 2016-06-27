from ubidots import ApiClient

import RPi.GPIO as GPIO 

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)

try: 

    api =ApiClient("from ubidots import ApiClient")

    import RPi.GPIO as GPIO 

    import time

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(7, GPIO.IN)

    try: 

        api =ApiClient("e62234c8846318b2962b69c29b62a0b7bbd5ed18")

        people = api.get_variable("wY36NjEfLRQ3Y1OlTmGLcm9zHKAVQk") 

    except: print "Couldn't connect to the API, check your Internet connection"

    counter = 0

    peoplev = 0

    while(1): 

        presence = GPIO.input(7)
	peoplecount = 0 

    if(presence): 

        peoplecount =+ 1 

        presence = 0

        time.sleep(1.5)

        time.sleep(1)

        counter += 1

    if(counter==10):

        print peoplecount 

        people.save_value({'value':peoplecount})

        counter = 0

        peoplev = 0

        people = api.get_variable("5238cec3f91b282c7357a140") 

except: print "Couldn't connect to the API, check your Internet connection"

counter = 0

peoplev = 0

while(1): 

    presence = GPIO.input(17) 

    if(presence): 

        peoplecount += 1 

        presence = 0

        time.sleep(1.5)

        time.sleep(1)

        counter += 1

    if(counter==10):

        print peoplecount 

        people.save_value({'value':peoplecount})

        counter = 0

        peoplev = 0
