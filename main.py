import pygame
import controls
import rov_connect as rc

pygame.init()
pygame.joystick.init()

controller = pygame.joystick.Joystick(0)
controller.init()

clock = pygame.time.Clock()
last = None

host = "127.0.0.1"
port = 5001

client = rc.connect_to_rov(port, host)

while True:
    joysticks, sides = controls.joystick_inputs(controller, last)

    print("JOYSTICKS:", joysticks)
    print("STOPPED:", sides)

    rc.send_data([joysticks, sides], client)

    last = joysticks

    clock.tick(60)