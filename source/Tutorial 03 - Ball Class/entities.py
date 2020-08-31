from ball import Ball

balls = []


def update_balls():
    for i in range(len(balls) - 1, -1, -1):
        balls[i].update()
        if not balls[i].alive:
            balls.pop(i)


def draw_balls():
    for i in range(len(balls)):
        balls[i].draw()
