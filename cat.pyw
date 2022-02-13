import pygame
from pynput import keyboard, mouse

W, H = (612, 354)
FPS = 25

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Bongo Cat ~by aqur1n~")


clock = pygame.time.Clock()

cat = pygame.image.load('textures/mousebg.png')
mouse_img = pygame.image.load('textures/mouse.png')

pygame.display.set_icon(cat)

left_press, left = (pygame.image.load('textures/left.png'), pygame.image.load('textures/up.png'))

mouse_max_pos_x, mouse_max_pos_y = (W // 3,H // 2)

changed = False

mouse_x = mouse_y = 0

def on_key_down(k):
    global changed
    changed = True

def on_key_up(k):
    global changed
    changed = False

def mouse_move(x, y):
    global mouse_x, mouse_y
    mouse_x, mouse_y = (x, y)

keyboard_listener = keyboard.Listener(
    on_press=on_key_down,
    on_release=on_key_up)

mouse_listener = mouse.Listener(
    on_move=mouse_move)

keyboard_listener.start()
mouse_listener.start()

while True:
    clock.tick(FPS)

    sc.fill((0, 255, 0))
    sc.blit(cat, (0,0))

    mouse_pos = (mouse_max_pos_x-(mouse_x//40 + W//5), mouse_max_pos_y-(mouse_y//40 - H//9))

    sc.blit(mouse_img, mouse_pos)

    [exit() if i.type == pygame.QUIT else ... for i in pygame.event.get()]

    if not changed: sc.blit(left, (0,0))
    else: sc.blit(left_press, (0,0))

    pygame.display.update()