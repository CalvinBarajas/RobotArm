import serial
import time
import RPi.GPIO as GPIO

channel = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

ser = serial.Serial("/dev/ttyS0", baudrate=1000000, timeout=3.0)

# [01][04 ][03  ][03][02][F2   ]
# [ID][LEN][INST][P0][P1][C.SUM]
# write new ID
GPIO.output(channel, GPIO.HIGH)
ser.write(bytearray.fromhex("FF FF 01 04 03 03 02 F2"))
time.sleep(0.1)
GPIO.output(channel, GPIO.LOW)
time.sleep(1)
   
ser.close()
GPIO.cleanup()









