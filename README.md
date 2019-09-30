# Temperature-to-Neopixel
Jon Proctor : Loxodrom3

A project where I am measuring the temperature and displaying the temp range as colors on neopixels

The goal of this project is to be able to measure air flow into and outof my computer case, and represent the temperature as different colors of LEDs.  The intent is to have colored light responding to the changing temperatures, and to provide the operator with an idea of the amount of heat that is generated and vented through the airflow.

I have chosen to use an Adafruit M0 Express (http://adafru.it/3403) with Ciruitpython as the processor and DC18B20 (http://adafru.it/381).  When deployed, the M0 Express will be inside the computer case and connected to an internal USB so that when hte computer is powered on, the M0 Expres will boot up run the code and start displaying colors that coorospond to the temperature in the airflows.
