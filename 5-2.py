import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

troyka = 13
comp = 14
dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

def number_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def adc():
    x = 0

    x += 128
    val = list(map(int, number_to_bin(x)))
    GPIO.output(dac, val)
    time.sleep(0.001)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 128

    x += 64
    val = list(map(int, number_to_bin(x)))
    GPIO.output(dac, val)
    time.sleep(0.001)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 64

    x += 32
    val = list(map(int, number_to_bin(x)))
    GPIO.output(dac, val)
    time.sleep(0.001)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 32

    x += 16
    val = list(map(int, number_to_bin(x)))
    GPIO.output(dac, val)
    time.sleep(0.001)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 16

    x += 8
    val = list(map(int, number_to_bin(x)))
    GPIO.output(dac, val)
    time.sleep(0.001)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 8

    x += 4
    val = list(map(int, number_to_bin(x)))
    GPIO.output(dac, val)
    time.sleep(0.001)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 4

    x += 2
    val = list(map(int, number_to_bin(x)))
    GPIO.output(dac, val)
    time.sleep(0.001)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 2

    x += 1
    val = list(map(int, number_to_bin(x)))
    GPIO.output(dac, val)
    time.sleep(0.001)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 1

    return x

try:
    while True:
        i = adc()
        v = i * 3.3 / 256.0
        if (i):
            print(f"{i}")
            print(f"{v:.2} V")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
