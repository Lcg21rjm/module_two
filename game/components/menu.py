import pygame
from game.utils.constants import BG, FONT_STYLE, INICIO, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 50)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        self.x_pos_bg = 0
        self.y_pos_bg = 0

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw (self, screen ):
        screen.blit(self.text, self.text_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_TAB: 
                   game.run()
                   
        
    def reset_screen_color(self, screen):
        image = pygame.transform.scale(INICIO, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

    def update_message(self, message):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)