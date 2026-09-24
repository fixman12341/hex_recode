import pygame

def get_joystick_value(controller):
    lx = controller.get_axis(0)
    ly = controller.get_axis(1)
    rx = controller.get_axis(3)
    ry = controller.get_axis(2)
    return {"l":[lx,ly],"r":[rx,ry]}

def get_stopped(    difference,last,now):
    sides = []

    for side in now:
        times = 0

        for i in range(2):
            if abs(now[side][i] - last[side][i]) <= difference:
                if -0.5 <= now[side][i] <= 0.5:
                    times += 1

        if times == 2:
            sides.append(side)

    return sides

def joystick_inputs(controller,last):
    pygame.event.pump()

    joysticks = get_joystick_value(controller)

    if last is None:
        return joysticks, []

    sides = get_stopped(0.05,last,joysticks)

    return joysticks,sides