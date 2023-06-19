import os
import time
import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.spaceship import Spaceship

from game.utils.constants import BG, FONT_STYLE, GAME_OVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, IMG_DIR, VIDA
from game.components.spaceship import Spaceship

class Game:
    
    def __init__(self):
        pygame.init()
        SOUND1 = pygame.mixer_music.load(os.path.join(IMG_DIR,'Other/Sonido_de_Galaxias.mp3'))
        SOUND1 = pygame.mixer.music.play(-1)
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.deat_count = 0
        self.score = 0
        self.intervalo = time.time()
        self.incremento = 5
        self.intervalo_se = 5

        self.menu = Menu ('Press TAB to start...', self.screen)
        
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.score = 0
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.power_up_manager.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
        
        


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(self,user_input)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        
        
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        half_creen_width = SCREEN_WIDTH // 2
        half_creen_height = SCREEN_HEIGHT // 2
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
        if self.deat_count == 0:
          vida1 = pygame.transform.scale(VIDA,(20,20))
          self.screen.blit(vida1, (half_creen_width - 500, half_creen_height - 300))
          vida2 = pygame.transform.scale(VIDA,(20,20))
          self.screen.blit(vida2, (half_creen_width - 480, half_creen_height - 300))
          vida3 = pygame.transform.scale(VIDA,(20,20))
          self.screen.blit(vida3, (half_creen_width - 460, half_creen_height - 300))
        elif self.deat_count == 1:
          vida1 = pygame.transform.scale(VIDA,(20,20))
          self.screen.blit(vida1, (half_creen_width - 500, half_creen_height - 300))
          vida2 = pygame.transform.scale(VIDA,(20,20))
          self.screen.blit(vida2, (half_creen_width - 480, half_creen_height - 300))
        elif self.deat_count == 2:
          vida1 = pygame.transform.scale(VIDA,(20,20))
          self.screen.blit(vida1, (half_creen_width - 500, half_creen_height - 300))

    def show_menu(self):
        half_creen_width = SCREEN_WIDTH // 2
        half_creen_height = SCREEN_HEIGHT // 2

        self.menu.reset_screen_color(self.screen)
        if self.deat_count >= 3:
            self.menu.update_message(f"Su Puntaje Fue: {self.score} ")
            self.deat_count = 0
            game_over = pygame.transform.scale(GAME_OVER,(250,90))
            self.screen.blit(game_over, (half_creen_width - 50, half_creen_height - 300))
            
            
            
            
        icon = pygame.transform.scale(ICON,(80,120))
        self.screen.blit(icon, (half_creen_width - 1, half_creen_height - 140))
        self.menu.draw(self.screen)
        self.menu.update(self)
        


    def update_score(self):
           self.score += 1
           
           

    def draw_score(self):
        if time.time() - self.intervalo >= 5:
          self.score += self.incremento
          self.intervalo = time.time()
         
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100, 50)
        self.screen.blit(text, text_rect)
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000,2)
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 30)
                text = font.render(f"{self.player.power_up_type.capitalize()} is neable for {time_to_show} seconds", True, (255,255,255))
                text_rect = text.get_rect()
                self.screen.blit(text,(540,50))
            else:
                self.player_has_power_up  = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()


        
    

        
