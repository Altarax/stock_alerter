import time
import RPi.GPIO as GPIO

# Définit le mode de numérotation (Board)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Définit le numéro du port GPIO qui alimente la led
LED = 4

# Active le contrôle du GPIO
GPIO.setup(LED, GPIO.OUT)

# Lit l'état actuel du GPIO, vrai si allumé, faux si éteint
state = GPIO.input(LED)


def on_off():
    var = 1

    while var < 11:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        var += 1
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)
