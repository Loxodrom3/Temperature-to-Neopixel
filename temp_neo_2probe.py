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
ds18_0 = DS18X20(ow_bus, ow_bus.scan()[0])
ds18_1 = DS18X20(ow_bus, ow_bus.scan()[1])
# devices = ow_bus.scan()
# for device in devices:
#     print("ROM = {} \tFamily = 0x{:02x}".format([hex(i) for i in device.rom], device.family_code))

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

    celc_0 = (ds18_0.temperature)
    celc_1 = (ds18_1.temperature)

    r_0 = int(((celc_0-minRTemp)/(maxRTemp - minRTemp))*(maxRed-minRed))
    g_0 = int((rngGTemp-(abs(midGTemp - celc_0)))/(rngGTemp) * (maxGrn-minGrn))
    b_0 = int(minBlu-((celc_0-minBTemp)/(maxBTemp - minBTemp))*(minBlu-maxBlu))

    r_1 = int(((celc_1-minRTemp)/(maxRTemp - minRTemp))*(maxRed-minRed))
    g_1 = int((rngGTemp-(abs(midGTemp - celc_1)))/(rngGTemp) * (maxGrn-minGrn))
    b_1 = int(minBlu-((celc_1-minBTemp)/(maxBTemp - minBTemp))*(minBlu-maxBlu))

    if r_0 < minRed:
        r_0 = minRed
    if g_0 < minGrn:
        g_0 = minGrn
    if b_0 < maxBlu:
        b_0 = maxBlu
    if r_0 > maxRed:
        r_0 = maxRed
    if g_0 > maxGrn:
        g_0 = maxGrn
    if b_0 > minBlu:
        b_0 = minBlu

    if r_1 < minRed:
        r_1 = minRed
    if g_1 < minGrn:
        g_1 = minGrn
    if b_1 < maxBlu:
        b_1 = maxBlu
    if r_1 > maxRed:
        r_1 = maxRed
    if g_1 > maxGrn:
        g_1 = maxGrn
    if b_1 > minBlu:
        b_1 = minBlu

    print('Temp: {0:0.3f}C'.format(ds18_0.temperature))
    print(r_0)
    print(g_0)
    print(b_0)
    print('Temp: {0:0.3f}C'.format(ds18_1.temperature))
    print(r_1)
    print(g_1)
    print(b_1)
    print()

# not heartbeat to pulse LED(13) for heartbeat
    heartbeat.value = not heartbeat.value
    for i in range(0, (numLED/2), 1):
        tempLED[i] = (r_0, g_0, b_0)
        tempLED[i+8] = (r_1, g_1, b_1)


    tempLED.show()
    time.sleep(1.0)
