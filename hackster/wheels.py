import sys
import time
import cv2
import RPi.GPIO as GPIO
import serial
from RPIO import PWM
from flask import Flask, render_template, request

mode=GPIO.getmode()

GPIO.cleanup()

Forward=26
fwd = 19
backward=20
bkd = 16
sleeptime=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(fwd, GPIO.OUT)
GPIO.setup(backward, GPIO.OUT)
GPIO.setup(bkd, GPIO.OUT)

    

def forward(x):
	GPIO.output(Forward, GPIO.HIGH)
	GPIO.output(fwd, GPIO.HIGH)
	print("Moving Forward")
	time.sleep(x)
	GPIO.output(Forward, GPIO.LOW)
	GPIO.output(fwd, GPIO.LOW)
	

def left(x):
    GPIO.output(Forward, GPIO.HIGH)
    print(" moving left ")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)
    
def right(x):
    GPIO.output(fwd, GPIO.HIGH)
    print("Moving right")
    time.sleep(x)
    GPIO.output(fwd, GPIO.LOW)
    
    
    

def reverse(x):
	GPIO.output(backward, GPIO.HIGH)
	GPIO.output(bkd, GPIO.HIGH)
	print("Moving Backward")
	time.sleep(x)
	GPIO.output(backward, GPIO.LOW)
	GPIO.output(bkd, GPIO.LOW)
	

    

    

while (1):

	forward(1)
	left(0.5)
	right(0.5)
	reverse(1)
	
	GPIO.cleanup()