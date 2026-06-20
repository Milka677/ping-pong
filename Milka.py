import pygame
from pygame.key import start_text_input


class Menu:
    def __init__(self,screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.start_btn = pygame.Rect(width//2, height//2, 100, 50)
        self.exit_btn = pygame.Rect(width//2, height//2, -150, 50)

        font = pygame.font.Font(None, 24)
    def draw(self):
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen,self.start_btn)
        pygame.draw.rect(self.screen,self.exit_btn)
        start_text = self.font.rebder("START", True, 255, 255, 255)
        exit_text = self.font.render("EXIT", True, (255,255,255))

        self.screen.blit(start_text, (self.start_btn.x +25, self.start))
        self.screen.blit(exit_text, (self.exit_btn.x +25, self.exit_btn))


    def handl_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.collidepoint(event.pos):
                return "start"
            if self.exit_btn.collidepoint(event.pos):
                return "exit"
        return None
WIDTH, HEIGHT = 800, 600
init()
screen = display.set_mode((WIDTH, HEIGHT))
menu = Menu(screen, WIDTH, HEIGHT)
