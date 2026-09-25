import pygame
import controls
import rov_connect as rc

pygame.init()
pygame.joystick.init()

#controller = pygame.joystick.Joystick(0)
#controller.init()

clock = pygame.time.Clock()
last = None

port = "COM5"
baudrate = 115200

client = rc.connect_to_rov(port, baudrate)

while True:
    #joysticks, sides = controls.joystick_inputs(controller, last)

    #print("JOYSTICKS:", joysticks)
    #print("STOPPED:", sides)

    rc.send_data(["hi"], client)

    #last = joysticks

    clock.tick(60)