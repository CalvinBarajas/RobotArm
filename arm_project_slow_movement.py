### Calvin Barajas
### Robot Arm Project 2019
### Sacramento, California
### SacRobotics.com
### This version is very slow and methodical so I'll 
### create another version that moves the motors faster

import serial
import time
import RPi.GPIO as GPIO

channel = 18
sleep_duration = 3
sleep_duration_on_long_moves = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

ser = serial.Serial("/dev/ttyS0", baudrate=1000000, timeout=3.0)


class Arm():
    def move_far_right(self):
        # SERVO 01:         FAR RIGHT
        # GOAL POSITION:    056[0x038]
        # SPEED:            30[0x1E]
        GPIO.output(channel, GPIO.HIGH)
        ser.write(bytearray.fromhex("FF FF 01 07 03 1E 38 00 1E 00 80"))
        time.sleep(0.1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(sleep_duration_on_long_moves)

    def move_far_left(self):
        # SERVO 01:         FAR LEFT
        # GOAL POSITION:    356[0x164]
        # SPEED:            30[0x1E]
        GPIO.output(channel, GPIO.HIGH)
        ser.write(bytearray.fromhex("FF FF 01 07 03 1E 64 01 1E 00 53"))
        time.sleep(0.1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(sleep_duration_on_long_moves)

    def move_farther_left(self):
        # SERVO 01:         LEFT (FAR LEFT - WOOD BLOCK PERSPECTIVE)
        # GOAL POSITION:    360[0x168]**
        # SPEED:            30[0x1E]
        GPIO.output(channel, GPIO.HIGH)
        ser.write(bytearray.fromhex("FF FF 01 07 03 1E 68 01 1E 00 4F"))
        time.sleep(0.1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(sleep_duration_on_long_moves)

    def correction_left(self): # minor adjustment after releasing gripper
        # SERVO 01:         MOVE ASIDE
        # GOAL POSITION:    365[0x16D]
        # SPEED:            30[0x1E]
        GPIO.output(channel, GPIO.HIGH)
        ser.write(bytearray.fromhex("FF FF 01 07 03 1E 6D 01 1E 00 4A"))
        time.sleep(0.1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(sleep_duration)

    def correction_right(self): # minor adjustment after releasing gripper
        # SERVO 01:         MOVE ASIDE
        # GOAL POSITION:    060[0x3C]
        # SPEED:            30[0x1E]
        GPIO.output(channel, GPIO.HIGH)
        ser.write(bytearray.fromhex("FF FF 01 07 03 1E 3C 00 1E 00 7C"))
        time.sleep(0.1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(sleep_duration)

def gripper_open():
    # SERVO 04:         OPEN (STARTING POSITION)
    # GOAL POSITION:    450[0x1C2]
    # SPEED:            30[0x1E]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 04 07 03 1E C2 01 1E 00 F2")) 
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_duration)

def gripper_closed():
    # SERVO 04:         CLOSED
    # GOAL POSITION:    580[0x244]
    # SPEED:            30[0x1E]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 04 07 03 1E 44 02 1E 00 6F"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_duration)

def servo_02_bottom():
    # SERVO 02:         BOTTOM (STARTING POSITION)
    # GOAL POSITION:    512[0x200]
    # SPEED:            30[0x1E]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 02 07 03 1E 00 02 1E 00 B5"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_duration)
    
def servo_03_bottom():
    # SERVO 03:         BOTTOM (STARTING POSITION)
    # GOAL POSITION:    512[0x200]
    # SPEED:            75[0x4B]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 03 07 03 1E 00 02 4B 00 87"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_duration)

def servo_01_middle():
    # SERVO 01:         MIDDLE (STARTING POSITION)
    # GOAL POSITION:    206[0x0CE]
    # SPEED:            75[0x4B]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 01 07 03 1E CE 00 4b 00 bd"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_duration)

def servo_02_top():
    # SERVO 02:         TOP (HIGHEST POSITION)
    # GOAL POSITION:    356[0x164]
    # SPEED:            30[0x1E]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 02 07 03 1E 64 01 1E 00 52"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_duration)

def servo_03_top():
    # SERVO 03:         TOP (HIGHEST POSITION)
    # GOAL POSITION:    356[0x164]
    # SPEED:            75[0x4B]
    GPIO.output(channel, GPIO.HIGH)
    ser.write(bytearray.fromhex("FF FF 03 07 03 1E 64 01 4B 00 24"))
    time.sleep(0.1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(sleep_duration)

arm = Arm() # instantiate object

for x in range(3):

    ############### MOVE OBJECT FROM RIGHT-TO-LEFT #####################

    # =========== NEUTRAL (START) ================
    servo_02_bottom()
    servo_03_bottom()
    servo_01_middle()
    gripper_closed()
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

    # =========== NEUTRAL (START) ================
    servo_02_bottom()
    servo_03_bottom()
    servo_01_middle()
    gripper_closed()
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
































