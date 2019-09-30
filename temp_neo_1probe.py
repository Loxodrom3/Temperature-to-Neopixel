# reading from ds18x20 to obtain temperature
# then map a temp range to a color range and display
# color with neopixel
# Jon Proctor: added LED(13) Heartbeat
# and adding neopixel support

import time
import board
import simpleio
import neopixel

from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

heartbeat = simpleio.DigitalOut(board.D13)
heartbeat.value = True

# Initialize one-wire bus on board pin D5.
ow_bus = OneWireBus(board.D5)

# Scan for sensors and grab the first one found.
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

# SetUp NeoPixels
temp_LED_pin = board.A1
num_LED = 16
ORDER = neopixel.GRB
temp_LED = neopixel.NeoPixel(temp_LED_pin, num_LED, pixel_order=ORDER)

n = 0

# Main loop to print the temperature every second.
while True:
    print('Temperature: {0:0.3f}C'.format(ds18.temperature))
    r = int(ds18.temperature *0.8)
    temp_LED[n] = (r, 0, 15)

    time.sleep(1.0)
# not heartbeat to pulse LED(13) for heartbeat
    heartbeat.value = not heartbeat.value
    if n > 14:
        n = 0
        temp_LED.fill((0, 0, 0))
        temp_LED.show()
    else:
        n = n+1

