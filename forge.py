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


# Drive forward by 500mm (half a meter)
drive_base.straight(565)

it hits the foge lever to forward damiging setup lower the langth and the turn to a corect angel

# OPTIONAL (add this before driving)
# Default speed is 200, but can change as needed (Minimum = 4, Max = 977)
drive_base.settings(straight_speed=300)
# Drives an arc (a partial circle) with a given radius.
# First value is radius (mm). [positive is right turn; negative is left turn]
# Angle is robot heading end. [positive is forward; negative is backward]
drive_base.arc(-100, angle=90)
# Drive forward by 500mm (half a meter)
drive_base.straight(100)
