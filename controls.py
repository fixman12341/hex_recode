import pygame

pygame.init()
pygame.joystick.init()

controller = pygame.joystick.Joystick(0)
controller.init()

# Returns the x and y value for each joystick
# l = left joystick, r = right joystick
def get_joystick_value(controller):
    lx = controller.get_axis(0)
    ly = controller.get_axis(1)
    rx = controller.get_axis(3)
    ry = controller.get_axis(2)
    return {"l":[lx,ly],"r":[rx,ry]}

clock = pygame.time.Clock()

while True:
    pygame.event.pump()
    print(get_joystick_value(controller))
    clock.tick(10)