# Example file showing a basic pygame "game loop"
import pygame
from sys import exit
from settings import *
from utility import image_cutter
from player import Player
from monster import Monster, Monster2
from game_object import Coins, Sud
from level import Level

# pygame setup
pygame.init()

def reset_game():
    global player_health
    global game_state

    game_state = "playing"
    player.sprite.lives = 3

#def monster_animation():
#    global monster_surf, monster_index
#    monster_index += 0.1
#    if monster_index > len(monster_images):
#        monster_index = 0
#    monster_surf = monster_images[int(monster_index)]



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

clock = pygame.time.Clock()

running = True

font = pygame.font.Font("assets/fonts/font.ttf", 25)
font_game_over = pygame.font.Font("assets/fonts/font.ttf", 25)

restart_btn_w = 200
restart_btn_h = 60
restart_btn = pygame.Rect(0, 0, restart_btn_w, restart_btn_h)
restart_btn.center = (screen_rect.centerx, screen_rect.centery + 100)
restart_btn_color = "#FF0000"
restart_btn_hover_color = "#FF6060"
restart_btn_text_color = "#FFFFFF"

restart_btn_font = pygame.font.Font("assets/fonts/font.ttf", 25)
restart_btn_text = restart_btn_font.render("RESTART", False, restart_btn_text_color)

player = pygame.sprite.GroupSingle()
player.add(Player())

monsters = pygame.sprite.Group()
monsters.add(Monster(50, 450, 5, "horizontal"), Monster(50, 100, 3, "vertical"))
monsters.add(Monster2(100, 100, "vertical"))

coin_group = pygame.sprite.Group()
sud_group = pygame.sprite.Group()

sprite_groups = {
    "Coins": coin_group,
    "Sud": sud_group
}

level_background = pygame.image.load("assets/world/_composite.png")
level_data = "assets/world/data.json"

level = Level(screen, level_background, level_data, sprite_groups)


#pocatecni hodnota casomiry
#elapse_time = 0
invul_time = 0
game_state = "playing"

coins = pygame.sprite.Group()
coins.add(Coins(120, 300, 16, 16))

sud = pygame.sprite.Group()
sud.add(Sud(400, 300, 16, 16))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        
        if game_state == "game_over":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_btn.collidepoint(event.pos):
                    reset_game()

    key = pygame.key.get_pressed()

    if game_state == "playing":
        #promenna key, pod kterou schovavame stisknutou klavesu

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        text_lives = font.render(f"Lives: {player.sprite.lives}", False, "#FF2CDC")

        screen.blit(text_lives, (SCREEN_WIDTH-120, 10))


#        monster_rect.right += monster_speed
#        if monster_rect.right > SCREEN_WIDTH:
#        elif monster_rect.left < 0:
#            monster_speed = -monster_speed
#        #na obrazovku vykreslit monster - .blit vzdy vykresluje 


#        monster_animation()
        #kulate zavorky = tuple, podobne list, ale efetivnejsi a nelze menit
        #pygame.draw.rect(screen, (255,0,0), player)
        level.draw_objects()

        player.draw(screen)
        player.update(monsters, clock)
        for monster in monsters:
            monster.draw(screen)
        
        for monster2 in monsters:
            monster2.draw(screen)
            
        monsters.update()

        #zapni casomiru
#        elapse_time += clock.get_time()

#        if player.sprite.rect.colliderect(monster_rect):
#            if not invul:
#                player.sprite.lives -= 1
#                print(player.sprite.lives)
#                invul = True
#                elapse_time = 0
#                
#        if elapse_time > 2000:
#            invul = False

        coins.draw(screen)

        if player.sprite.lives <= 0:
            game_state = "game_over"
        
        if game_state == "game_over":
            mouse_pos = pygame.mouse.get_pos()

            screen.fill("black")
            text_game_over = font_game_over.render(f"GAME OVER", False, "#FF2C2C")
            text_game_over_rect = text_game_over.get_rect(center=(SCREEN_WIDTH /2, SCREEN_HEIGHT /2))
            screen.blit(text_game_over, text_game_over_rect)

            if restart_btn.collidepoint(mouse_pos):
                pygame.draw.rect(screen, restart_btn_hover_color, restart_btn, border_radius=15)
            else:
                pygame.draw.rect(screen, restart_btn_color, restart_btn)

            screen.blit(restart_btn_text, (restart_btn.centerx - restart_btn_text.get_width() / 2,
                                           restart_btn.centery - restart_btn_text.get_height() / 2,))


        # RENDER YOUR GAME HERE

    pygame.display.update()
    
    #pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()