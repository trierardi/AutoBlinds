import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPIO_PINS = (-1, -1)
DIRECTION_PIN = 27
STEP_PIN = 4


def motor_up():
    motor = RpiMotorLib.A3967EasyNema(DIRECTION_PIN, STEP_PIN, GPIO_PINS)
    motor.motor_move(.004, 600, False, True, "Full", .05)
    GPIO.cleanup()


def motor_down():
    motor = RpiMotorLib.A3967EasyNema(DIRECTION_PIN, STEP_PIN, GPIO_PINS)
    motor.motor_move(.004, 600, False, True, "Full", .05)
    GPIO.cleanup()

# TESTING FUNCTIONS
# Uncomment these (and comment the other ones) if you are testing locally (not on the pi).
# def motor_up():
#     pass
#
#
# def motor_down():
#     pass
