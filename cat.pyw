import pygame
from pynput import keyboard, mouse
from os import chdir


chdir("\\".join(__file__.split("\\")[:-1]))

WINDOW_W, WINDOW_H = (612, 354)
MOUSE_MAX_POS_X, MOUSE_MAX_POS_Y = (WINDOW_W // 3, WINDOW_H // 2)
FPS = 30


class Textures:
    def __init__(self) -> None:
        self.cat = pygame.image.load('textures/mousebg.png')
        self.mouse = pygame.image.load('textures/mouse.png')

        self.keyboard_up = pygame.image.load('textures/up.png')
        self.keyboard_press = pygame.image.load('textures/left.png')

class BongoCat:
    def __init__(self) -> None:
        self.running = True
        self.keyboard_pressed = False
        self.mouse_pos = (0, 0)

        self.textures = Textures()
        self.clock = pygame.time.Clock()

    def create_window(self) -> None:
        self.surface = pygame.display.set_mode((WINDOW_W, WINDOW_H))

        pygame.display.set_icon(self.textures.cat)
        pygame.display.set_caption("Bongo Cat ~by aqur1n~")

    def process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def on_mouse_move(self, x: int, y: int) -> None:
        self.mouse_pos = (x, y)

    def on_key_down(self, key) -> None:
        self.keyboard_pressed = True

    def on_key_up(self, key) -> None:
        self.keyboard_pressed = False

    def run(self) -> None:
        self.running = True

        self.create_window()

        keyboard_listener = keyboard.Listener(
            on_press = self.on_key_down,
            on_release = self.on_key_up
        )
        mouse_listener = mouse.Listener(on_move = self.on_mouse_move)

        keyboard_listener.start()
        mouse_listener.start()

        try:
            while self.running:
                self.surface.fill((0, 255, 0))
                self.surface.blit(self.textures.cat, (0,0))

                self.surface.blit(
                    self.textures.mouse, 
                    (
                        MOUSE_MAX_POS_X - (self.mouse_pos[0] // 30 + WINDOW_W // 5), 
                        MOUSE_MAX_POS_Y - (self.mouse_pos[1] // 30 - WINDOW_H // 9)
                    )
                )
                self.surface.blit(
                    self.textures.keyboard_press if self.keyboard_pressed else self.textures.keyboard_up, 
                    (0, 0)
                )

                pygame.display.update()

                self.process_events()
                self.clock.tick(FPS)
        finally:
            keyboard_listener.stop()
            mouse_listener.stop()

def main() -> None:
    pygame.init()

    cat = BongoCat()
    cat.run()

if __name__ == "__main__":
    main()
