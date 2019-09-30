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
tempLEDPin = board.A1
numLED = 16
ORDER = neopixel.GRB
tempLED = neopixel.NeoPixel(tempLEDPin, numLED, brightness=0.2, auto_write=False, pixel_order=ORDER)


# SetUp temp range and color range.  range for computer: 25 - 65 or 70?
minBTemp = 23
maxBTemp = 27

midGTemp = 27
rngGTemp = 3

minRTemp = 26
maxRTemp = 30

minRed = 0
maxRed = 150
minGrn = 0
maxGrn = 100
minBlu = 100
maxBlu = 0

# Main loop to print the temperature every second.
while True:

    celc = (ds18.temperature)

    r = int(((celc-minRTemp)/(maxRTemp - minRTemp))*(maxRed-minRed))
    g = int((rngGTemp-(abs(midGTemp - celc)))/(rngGTemp) * (maxGrn-minGrn))
    b = int(minBlu-((celc-minBTemp)/(maxBTemp - minBTemp))*(minBlu-maxBlu))

    if r < minRed:
        r = minRed
    if g < minGrn:
        g = minGrn
    if b < maxBlu:
        b = maxBlu
    if r > maxRed:
        r = maxRed
    if g > maxGrn:
        g = maxGrn
    if b > minBlu:
        b = minBlu

    print('Temp: {0:0.3f}C'.format(ds18.temperature))
    print(r)
    print(g, (rngGTemp-(abs(midGTemp - celc))/(rngGTemp)), sep=", ")
    print(b)
    print()

# not heartbeat to pulse LED(13) for heartbeat
    heartbeat.value = not heartbeat.value
    for i in range(0, numLED, 1):
        tempLED[i] = (r, g, b)

    tempLED.show()
    time.sleep(1.0)
