
import commons
import pygame
import vector
import states
import entities

from vector import Vector
from states import GameState, MenuState, PlayState
from ball import Ball


def update():
    entities.update_balls()


def draw():
    commons.screen.fill((50, 50, 50))

    entities.draw_balls()


pygame.init()

commons.screen = pygame.display.set_mode((commons.screen_w, commons.screen_h))

pygame.display.set_caption("Peggle Tutorial")

icon_image = pygame.image.load("res/images/icons/ball.png").convert_alpha()
icon_image.set_colorkey((255, 0, 255))
pygame.display.set_icon(icon_image)

app_running = True
delta_time = 0.0
clock = pygame.time.Clock()

mouse_position = (0, 0)

while app_running:
    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                app_running = False
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                entities.balls.append(Ball(Vector(event.pos[0], event.pos[1]), vector.random_vector() * 300))

    update()
    draw()

    pygame.display.flip()

    commons.delta_time = 0.001 * clock.tick(144)

pygame.quit()
