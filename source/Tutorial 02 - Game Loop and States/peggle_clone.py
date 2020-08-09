
import pygame
import vector
import states

from vector import Vector
from states import GameState, MenuState, PlayState


def update():
    global circle_velocity
    global circle_position

    if circle_following_mouse and states.game_state == GameState.PLAYING:
        mouse_pos_vec = Vector(mouse_position[0], mouse_position[1])
        diff_vec = mouse_pos_vec - circle_position
        normalized_direction = vector.normalize(diff_vec)
        circle_velocity += normalized_direction * 1000 * delta_time

    circle_position += circle_velocity * delta_time


def draw():
    screen.fill((50, 50, 50))

    pygame.draw.circle(screen, (255, 255, 255), circle_position.make_int_tuple(), 10)


pygame.init()

screen = pygame.display.set_mode((960, 720))

app_running = True
delta_time = 0.0
clock = pygame.time.Clock()

circle_position = Vector(0, 0)
circle_velocity = Vector(0, 0)
circle_following_mouse = False

mouse_position = (0, 0)


while app_running:
    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                app_running = False
            elif event.key == pygame.K_SPACE:
                circle_following_mouse = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                circle_following_mouse = False

    update()
    draw()

    pygame.display.flip()

    delta_time = 0.001 * clock.tick(144)

pygame.quit()
