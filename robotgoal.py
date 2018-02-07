import time 
from track import * 
import math

xpos_robot = int(raw_input("Robot x position:"))
Ypos_robot = int(raw_input("Robot Y Position:"))
Xpos_goal = int(raw_input("Goal X position:"))
Ypos_goal= int(raw_input("Goal Y position"))

distance = math.sqrt((Xpos_goal -Ypos_robot)**2 + ( Ypos_goal - Ypos_robot)**2)
angle = round(math.degrees(math.atan2((Ypos_goal - Ypos_robot), (Xpos_goal -xpos_robot))))
if angle < 0 :
    angle = angle + 360
print(angle)
# Turn to the right bearing 	
if (angle) < 180 :
    turn_right(angle)
else:
     turn_left(angle)
print(distance)
forward(distance)	 
	 
	 
	 
	 
	 
	 
	
	
	
