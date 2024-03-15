from controller import Robot
from controller import Keyboard
robot = Robot()
kb= Keyboard()

timestep = int(robot.getBasicTimeStep())

motorA = robot.getDevice("A motor")
motorB = robot.getDevice("B motor")
motorC = robot.getDevice("C motor")
motorD = robot.getDevice("D motor")
motorE = robot.getDevice("E motor")
motorF = robot.getDevice("F motor")

pen=robot.getDevice("pen")

kb.enable(timestep)

ds= robot.getDevice("ds")
ds.enable(timestep)
motorA_pos=3.14
motorB_pos=0
motorC_pos=0
motorD_pos=0
motorE_pos=0
motorF_pos=0
draw=True
colors=[0xB04A5A,0x3F2021,0xBA5B3F,0xCB9576,0x7FA0AC ,
        0xB04A5A,0x3F2021,0xBA5B3F,0xCB9576,0x7FA0AC ,
        0xB04A5A,0x3F2021,0xBA5B3F,0xCB9576,0x7FA0AC ]
color_index=0

def halo(color) :
    global motorA_pos , motorB_pos , motorC_pos , draw , color_index
    if ds_val > 400 :
       motorB_pos += 0.001
       motorC_pos += 0.0005
    else : 
       pen.setInkColor(color , 1)
       motorA_pos -=0.002
       if motorA_pos < -3.13 : 
         draw=False
         color_index += 1 
         
def moveback():
    global motorA_pos , motorB_pos , draw
    if ds_val < 1000:
       motorB_pos -= 0.0045
    else : 
       motorA_pos = 3.14
       draw = True
          
while robot.step(timestep) != -1:
    ds_val=ds.getValue()
    if color_index < 12:
       if draw == True : 
         halo(colors[color_index])
       elif draw == False:
         moveback()
     
    motorA.setPosition(motorA_pos)
    motorB.setPosition(motorB_pos)
    motorC.setPosition(motorC_pos)
    motorD.setPosition(motorD_pos)
    motorE.setPosition(motorE_pos)
    motorF.setPosition(motorF_pos)