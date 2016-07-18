import RPi.GPIO as GPIO
import time
from ubidots import ApiClient
 
GPIO.setmode(GPIO.BCM) # use BCM GPIO references
GPIO_PIR = 17 # define GPIO to use on rpi
print "Capture is running (CTRL-C to exit)"
GPIO.setup(GPIO_PIR,GPIO.IN) #set pin as input
 
try:
   api=ApiClient("e62234c8846318b2962b69c29b62a0b7bbd5ed18") # put your own apikey (unique key)
   people= api.get_variable("578cc74b7625422c4e939b61") # pur your own variable's id (one per device)
except:
   print "cant connect. please verify your GPIO connector"
 
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
    if(counter==300): # minimum interval (in sec.) before each sending to Ubidots server (here 5min)
       print peoplecount
       people.save_value({'value':peoplecount})
       counter = 0
       peoplecount = 0
