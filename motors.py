import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

motorLeftForward = 10
motorLeftBackward = 12
motorRightForward = 24
motorRightBackward = 26

GPIO.setup(motorLeftForward, GPIO.OUT)
GPIO.setup(motorLeftBackward, GPIO.OUT)
GPIO.setup(motorRightForward, GPIO.OUT)
GPIO.setup(motorRightBackward, GPIO.OUT)

def reverse():
    GPIO.output(motorLeftBackward, GPIO.HIGH)
    GPIO.output(motorLeftForward, GPIO.LOW)
    GPIO.output(motorRightBackward, GPIO.HIGH)
    GPIO.output(motorRightForward, GPIO.LOW)

def forward():
    GPIO.output(motorLeftBackward, GPIO.LOW)
    GPIO.output(motorLeftForward, GPIO.HIGH)
    GPIO.output(motorRightBackward, GPIO.LOW)
    GPIO.output(motorRightForward, GPIO.HIGH)

def left():
    GPIO.output(motorLeftBackward, GPIO.HIGH)
    GPIO.output(motorLeftForward, GPIO.LOW)
    GPIO.output(motorRightBackward, GPIO.LOW)
    GPIO.output(motorRightForward, GPIO.HIGH)

def right():
    GPIO.output(motorLeftBackward, GPIO.LOW)
    GPIO.output(motorLeftForward, GPIO.HIGH)
    GPIO.output(motorRightBackward, GPIO.HIGH)
    GPIO.output(motorRightForward, GPIO.LOW)

def stop():
    GPIO.output(motorLeftBackward, GPIO.LOW)
    GPIO.output(motorLeftForward, GPIO.LOW)
    GPIO.output(motorRightBackward, GPIO.LOW)
    GPIO.output(motorRightForward, GPIO.LOW)