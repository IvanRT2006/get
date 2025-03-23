import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

troyka = 13
comp = 14
dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = 1)


def number_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def adc():
    for i in range(0, 256):
        GPIO.output(dac, number_to_bin(i) )
        time.sleep(0.001)
        if (GPIO.input(comp) == 1):
            return i


    return 256


try:
    while True:
        voltage = adc() / 256 * 3.3
        print(f'Voltage = {voltage:.2f} B')



finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
