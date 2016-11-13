import time
import pyupm_grove as grove
import mraa
import Adafruit_BBIO.ADC as ADC

ADC.setup()



def AirRead():
    #air = mraa.Aio(2)
    #airValue = air.read()
    #return airValue
    value = ADC.read("P9_33")
    return (value/2.275)*1.8;

# Create the temperature sensor object using AIO pin 0
def TemperatureRead():
    #temp = grove.GroveTemp(0)
    #celsius = temp.value()
    #fahrenheit = celsius * 9.0/5.0 + 32.0;
    #return celsius,fahrenheit
    return 10,6;
    
# Read the temperature ten times, printing both the Celsius and
# equivalent Fahrenheit temperature, waiting one second between readings

def ControlRelay(flag):
    relay = mraa.Gpio(62) # GPIO_51
    relay.dir(mraa.DIR_OUT)
    if flag == 1:
        relay.write(1)
    else:
        relay.write(0)
    

if __name__ == "__main__":
    while True:
        print(AirRead())
        print(TemperatureRead())
        #ControlRelay(1)
        time.sleep(1)
        #ControlRelay(0)
        time.sleep(1)