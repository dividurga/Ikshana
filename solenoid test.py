import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
while True:
    
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    print("On")
    
    time.sleep(1)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(16,GPIO.HIGH)
    
    print("Off")
    
    time.sleep(1)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    print("On")
    
    time.sleep(1)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(17,GPIO.HIGH)
    
    print("Off")
    time.sleep(1)
    GPIO.output(24,GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    print("On")
    
    time.sleep(1)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    
    print("Off")
    time.sleep(1)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)
    print("On")
    
    time.sleep(1)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(19,GPIO.HIGH)
    
    print("Off")
    time.sleep(1)
   
    GPIO.output(26,GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    print("On")
    
    time.sleep(1)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(20,GPIO.HIGH)
    
    print("Off")
    time.sleep(1)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(21, GPIO.LOW)
    print("On")
    
    time.sleep(1)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)
    
    print("Off")
    time.sleep(1)                         