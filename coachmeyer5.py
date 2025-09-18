#Sets up the libraries and hub
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
hub = PrimeHub()
#Defines the ports
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
front_motor = Motor(Port.C)
rear_motor = Motor(Port.D)
left_color_sensor = ColorSensor(Port.E)
right_color_sensor = ColorSensor(Port.F)
# Initialize the drive base. The wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
#Use the gyro to navigate
drive_base.use_gyro(True)
# Clear console
print("\x1b[H\x1b[2J", end="")
#########Mission code is below:

print(123)
#drive_base.straight(500)
#drive_base.turn(90)
#drive_base.arc(100, angle=-90)
#First value is speed (deg/sec). Second value is amount of rotation (deg.)
'''
left_motor.run_target(500,0)
right_motor.run_target(500,0)
front_motor.run_target(500,0)
rear_motor.run_target(500,0)
wait(2000)
#new
#left_motor.run_angle(500,360)
#print(straight_speed)

drive_base.straight(500)
left_color_sensor.lights.on(10)
right_color_sensor.lights.on(66)
drive_base.settings(straight_speed=200)
drive_base.straight(500)
#drive_base.settings(300)

drive_base.settings(straight_speed=977)
drive_base.arc(-56, angle=90)
'''
red=Color(h=0, s=100, v=100)
hub.light.on(red)
wait(10000)