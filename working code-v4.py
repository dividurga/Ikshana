import pytesseract
import cv2
import numpy as np
from pytesseract import Output
from PIL import Image
from picamera.array import PiRGBArray
from picamera import PiCamera
import os
import time
import RPi.GPIO as GPIO

button = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
'''
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

while True:
    camera.start_preview()
    if input()=='a':
        camera.capture('/home/pi/Desktop/0.jpg')
        camera.stop_preview()
        time.sleep(0.3)
        break

img_source = cv2.imread('/home/pi/Desktop/WhatsApp Image 2022-06-08 at 4.15.14 PM.jpeg')
 '''
cap = cv2.VideoCapture(0)
focus = 15  # min: 0, max: 255, increment:5
cap.set(28, focus) 
img1 = 0
while True:
   
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    img1 = frame
    if cv2.waitKey(1) & GPIO.input(button)==True: 
        status = cv2.imwrite('/home/pi/Desktop/0.jpg',img1)
        #print(status)
        break
    
 
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
 
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
 
 
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
 
 
def canny(image):
    return cv2.Canny(image, 100, 200)
 
 
gray = get_grayscale(img1)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)
 
for img in [img1, gray, thresh, opening, canny]:
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    scanlst=d['text']
    #string manipulation to cleanup data and get output as string
    #print(scanlst)
    scannogap=[x for x in scanlst if x !='']
    #print(scannogap)
    scanstr=""
    for i in scannogap:
        scanstr+=i
        scanstr+=' '
    
    print(scanstr)
    
    #text to braille

    timeglow=1

    timeblank=0.5

   
    dict_braille = {'a': [1,0,0,0,0,0], 'b': [1,0,1,0,0,0], 'c': [1,1,0,0,0,0], 'd': [1,1,0,1,0,0], 'e': [1,0,0,1,0,0], 'f': [1,1,1,0,0,0], 'g': [1,1,1,1,0,0], 'h': [1,0,1,1,0,0], 'i': [0,1,1,0,0,0], 'j': [0,1,1,1,0,0], 'k': [1,0,0,0,1,0], 'l': [1,0,1,0,1,0], 'm': [1,1,0,0,1,0], 'n': [1,1,0,1,1,0], 'o': [1,0,0,1,1,0], 'p': [1,1,1,0,1,0], 'q': [1,1,1,1,1,0], 'r': [1,0,1,1,1,0], 's': [0,1,1,0,1,0], 't': [0,1,1,1,1,0], 'u': [1,0,0,0,1,1], 'v': [1,0,1,0,1,1], 'w': [0,1,1,1,0,1], 'x': [1,1,0,0,1,1], 'y': [1,1,0,1,1,1], 'z': [1,0,0,1,1,1], ' ': [0,0,0,0,0,0], '0': [0,1,0,1,1,1], '1': [1,0,0,0,0,1], '2': [1,0,1,0,0,1], '3': [1,1,0,0,0,1], '4': [1,1,0,1,0,1], '5': [1,0,0,1,0,1], '6': [1,1,1,0,0,1], '7': [1,1,1,1,0,1], '8': [1,0,1,1,0,1], '9': [0,1,1,0,0,1],'?':[0,0,1,0,1,1],'.':[0,0,1,1,0,1],'!':[0,0,1,1,1,0],'-':[0,0,0,0,1,1],',':[0,0,1,0,0,0],';':[0,0,1,0,1,0],':':[0,0,1,1,0,0],'/':[0,1,0,0,1,0],'"':[0,0,1,0,1,1],"()":[0,0,1,1,1,1],"'":[0,0,0,0,1,0], 'test':[0,0,0,0,0,0]}
    def braille_func(scanstr, dict_braille):
    
        for l in range(0, 1):
            k=22
            a=0
            n=16
            #print(l)
            for i in scanstr.lower():
                for key, value in zip(dict_braille.keys(), dict_braille.values()):
                    if i==key:
                        print(i)
                        print(dict_braille[key])
                        for j in range(len(dict_braille[key])):
                            '''
                            print(k)
                            print(n)
                            print(j)
                            '''
                            if dict_braille[key][j]==1:
                                GPIO.output(k, GPIO.HIGH)
                                GPIO.output(n, GPIO.LOW)
                                #print("high")
                            '''k=22
                            n=16
                            '''
                            k=k+1
                            n=n+1
                time.sleep(timeglow)
                GPIO.output(22,GPIO.LOW)
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(23,GPIO.LOW)
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(24,GPIO.LOW)
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(25,GPIO.LOW)
                GPIO.output(19, GPIO.HIGH)
                GPIO.output(26,GPIO.LOW)
                GPIO.output(20, GPIO.HIGH)
                GPIO.output(27,GPIO.LOW)
                GPIO.output(21, GPIO.HIGH)
                time.sleep(timeblank)
                k=22
                a=0
                n=16
    braille_func(scanstr, dict_braille)

    n_boxes = len(d['text'])
 
    # back to RGB
    if len(img.shape) == 2:
    
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
 
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (text, x, y, w, h) = (d['text'][i], d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            # don't show empty text
            if text and text.strip() != "":
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                img = cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
 
    cv2.imshow('img', img)
    
    cv2.waitKey(0)
    #print(text)
   
