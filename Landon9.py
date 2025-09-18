# Sets up the libraries and hub
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


# Clear console at start
print("\x1b[H\x1b[2J", end="")


hub = PrimeHub()


# Defines how the ports are used
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
front_motor = Motor(Port.C)
rear_motor = Motor(Port.D)
left_color_sensor = ColorSensor(Port.E)
right_color_sensor = ColorSensor(Port.F)


# Initialize the drive base
# The wheel diameter is 56mm and distance between wheels is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)


# Use the gyro to navigate more accurately
drive_base.use_gyro(True)


###################################
# Mission specific code is below:

# OPTIONAL (add this before driving)
# Default speed is 200, but can change as needed (Minimum = 4, Max = 977)
drive_base.settings(straight_speed=300)

drive_base.straight(500)
drive_base.straight(-200)
drive_base.arc(15, angle=45)
drive_base.straight(-80)

drive_base.settings(straight_speed=200)
drive_base.arc(25, -43)
drive_base.straight(60)
drive_base.settings(straight_speed=500) #changes speed for easier grabe
drive_base.arc(100, 45) #Grabbing brush

drive_base.straight(20)
drive_base.arc(50, -45)
drive_base.straight(220)#going to soil deposit
drive_base.arc(40, -50)
drive_base.straight(155)
drive_base.straight(-255) #backing away from soil deposit after moving 1st slab

drive_base.arc(15, 45) #lining up to get second Slab
drive_base.straight(395)#getting 2nd slab
drive_base.turn(90) #securing 2nd slab
drive_base.arc(50, 90)
print (Turned)
wait(1000)
drive_base.stright(500)
'''
wait(5000)
drive_base.arc(0,-90)
#drive_base.settings(straight_speed=200)
'''

#drive_base.settings(100)
'''
#Allow bot to drive foward messed up lots
drive_base.straight(325)
#drive_base.curve()
'''