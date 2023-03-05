import RPi.GPIO as GPIO

relay1 = 37
relay2 = 38
relay3 = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)

GPIO.output(relay1, GPIO.LOW)
GPIO.output(relay2, GPIO.LOW)
GPIO.output(relay3, GPIO.LOW)

def control_relays(command):
    if command == "S4_1":
        GPIO.output(relay1, GPIO.HIGH)
    if command == "S4_0":
        GPIO.output(relay1, GPIO.LOW)
    if command == "S5_1":
        GPIO.output(relay2, GPIO.HIGH)
    if command == "S5_0":
        GPIO.output(relay2, GPIO.LOW)
    if command == "S7_1":
        GPIO.output(relay3, GPIO.HIGH)
    if command == "S7_0":
        GPIO.output(relay3, GPIO.LOW)
