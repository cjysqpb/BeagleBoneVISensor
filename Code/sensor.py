import time
import pyupm_grove as grove
import mraa
import Adafruit_BBIO.ADC as ADC
import math

ADC.setup()



def AirRead():
    #air = mraa.Aio(2)
    #airValue = air.read()
    #return airValue
    value = 0;
    return (value);

# Create the temperature sensor object using AIO pin 0
def TemperatureRead():
    #temp = grove.GroveTemp(0)
    #celsius = temp.value()
    #fahrenheit = celsius * 9.0/5.0 + 32.0;
    #return celsius,fahrenheit
    # valueMax = 0.5;
    # valueMin = 0.5;
    # loop = 500;
    # for i in range(0, loop):
    #     value = ADC.read("P9_33")
    #     if (value > valueMax):
    #         valueMax = value
    #     elif (value < valueMin):
    #         valueMin = value
    # current1 = valueMax-valueMin
    #(((valueMax-valueMin)/2.0))*20
    value = 0.0
    loop = 500
    accu = 0.0
    for i in range(0, loop):
        value = ADC.read("P9_33")-0.500
        accu = accu + (value * value)
    meanSQ = accu/loop
    mean = math.sqrt(meanSQ)
    voltage = mean * 1.8
    return voltage,0
    
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