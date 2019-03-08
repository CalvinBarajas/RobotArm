### Calvin Barajas
### Robot Arm Project 2019 rev 001
### Sacramento, California
### SacRobotics.com
### This version is faster (motors move faster). If you are a beginner, start with the 
### slower motor code because you don't want to have any accidents and destroy your motors.

import serial
import time
import RPi.GPIO as GPIO

channel = 18 # PIN NUMBER ON RASPBERRY PI

sleep_short = 0.5
sleep_long = 1
sleep_ultra_long = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

# Use ttyS0 or ttyAMA0
ser = serial.Serial("/dev/ttyS0", baudrate=1000000, timeout=3.0)

class Arm():
    def move_far_right(self): # method 001
        # SERVO 01:         FAR RIGHT
        # GOAL POSITION:    056[0x038]
        # SPEED:            150[0x96]
        GPIO.output(channel, GPIO.HIGH)
        ser.write(bytearray.fromhex("FF FF 01 07 03 1E 38 00 96 00 08"))
        time.sleep(0.1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(sleep_long)

    def move_far_left(self): # method 002
        # SERVO 01:         FAR LEFT
        # GOAL POSITION:    356[0x164]
        # SPEED:            150[0x96]
        GPIO.output(channel, GPIO.HIGH)
        ser.write(bytearray.fromhex("FF FF 01 07 03 1E 64 01 96 00 DB"))
        time.sleep(0.1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(sleep_long)

    def move_farther_left(self): # method 003
        # THE FOLLOWING CODE IS USED FOR CORRECTING POSITION
        # SERVO 01:         LEFT (FAR LEFT - WOOD BLOCK PERSPECTIVE)
        # GOAL POSITION:    360[0x168]**
        # SPEED:            150[0x96]
        GPIO.output(channel, GPIO.HIGH)
        ser.write(bytearray.fromhex("FF FF 01 07 03 1E 68 01 96 00 D7"))
        time.sleep(0.1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(sleep_long)

    def correction_left(self): # minor adjustment after releasing gripper
        # SERVO 01:         MOVE ASIDE
        # GOAL POSITION:    365[0x16D]
        # SPEED:            30[0x1E]
        GPIO.output(channel, GPIO.HIGH)
        ser.write(bytearray.fromhex("FF FF 01 07 03 1E 6D 01 1E 00 4A"))
        time.sleep(0.1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(sleep_short)

    def correction_right(self): # minor adjustment after releasing gripper
        # SERVO 01:         MOVE ASIDE
        # GOAL POSITION:    060[0x3C]
        # SPEED:            30[0x1E]
        GPIO.output(channel, GPIO.HIGH)
        ser.write(bytearray.fromhex("FF FF 01 07 03 1E 3C 00 1E 00 7C"))
        time.sleep(0.1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(sleep_short)

def gripper_open():
    # SERVO 04:         OPEN (STARTING POSITION)
    # GOAL POSITION:    450[0x1C2]
    # SPEED:            150[0x96]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 04 07 03 1E C2 01 96 00 7A")) 
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_short)

def gripper_closed():
    # SERVO 04:         CLOSED
    # GOAL POSITION:    580[0x244]
    # SPEED:            150[0x96]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 04 07 03 1E 44 02 96 00 F7"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_short)

def servo_02_bottom():
    # SERVO 02:         BOTTOM (STARTING POSITION)
    # GOAL POSITION:    512[0x200]
    # SPEED:            150[0x96]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 02 07 03 1E 00 02 96 00 3D"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_long)
    
def servo_03_bottom():
    # SERVO 03:         BOTTOM (STARTING POSITION)
    # GOAL POSITION:    512[0x200]
    # SPEED:            75[0x4B]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 03 07 03 1E 00 02 4B 00 87"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_ultra_long)

def servo_01_middle():
    # SERVO 01:         MIDDLE (STARTING POSITION)
    # GOAL POSITION:    206[0x0CE]
    # SPEED:            75[0x4B]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 01 07 03 1E CE 00 4b 00 bd"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_long)

def servo_02_top():
    # SERVO 02:         TOP (HIGHEST POSITION)
    # GOAL POSITION:    356[0x164]
    # SPEED:            150[0x96]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 02 07 03 1E 64 01 96 00 DA"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_short)

def servo_03_top():
    # SERVO 03:         TOP (HIGHEST POSITION)
    # GOAL POSITION:    356[0x164]
    # SPEED:            150[0x96]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 03 07 03 1E 64 01 96 00 D9"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_short)

arm = Arm() # instantiate object

# RESET ALL MOTORS AND PLACE IN NEUTRAL/START POSITION
servo_01_middle()
servo_02_bottom()
servo_03_bottom()
gripper_closed()

for x in range(3):

    ############### MOVE OBJECT FROM RIGHT-TO-LEFT #####################

    # =========== MOVE ARM UP ================
    servo_02_top()
    servo_03_top()
    # =========== MOVE TO THE RIGHT ================
    arm.move_far_right()
    # =========== MOVE ARM DOWN ================
    gripper_open()
    servo_02_bottom()
    servo_03_bottom()
    gripper_closed()
    # =========== MOVE ARM UP ================
    servo_02_top()
    servo_03_top()
    # =========== MOVE FAR LEFT ================
    arm.move_far_left()
    # =========== MOVE ARM DOWN ================
    servo_02_bottom()
    servo_03_bottom()
    gripper_open()
    arm.correction_left()
    # =========== MOVE ARM UP ================
    servo_02_top()
    servo_03_top()
    gripper_closed()
    # =========== NEUTRAL (START) ================
    servo_01_middle()
    servo_02_bottom()
    servo_03_bottom()

    ############### MOVE OBJECT FROM LEFT-TO-RIGHT #####################

    # =========== MOVE ARM UP ================
    servo_02_top()
    servo_03_top()
    # =========== MOVE FAR LEFT ================
    arm.move_farther_left()
    # =========== MOVE ARM DOWN ================
    gripper_open()
    servo_02_bottom()
    servo_03_bottom()
    gripper_closed()
    # =========== MOVE ARM UP ================
    servo_02_top()
    servo_03_top()
    # =========== MOVE TO THE RIGHT ================
    arm.move_far_right()
    # =========== MOVE ARM DOWN ================
    servo_02_bottom()
    servo_03_bottom()
    gripper_open()
    arm.correction_right()
    # =========== MOVE ARM UP ================
    servo_02_top()
    servo_03_top()
    gripper_closed()
    # =========== NEUTRAL (START) ================
    servo_01_middle()
    servo_02_bottom()
    servo_03_bottom()

    print('iteration completed')

ser.close()
GPIO.cleanup()


