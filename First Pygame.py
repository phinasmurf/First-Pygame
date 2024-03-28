import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

#def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x 

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype(1).ttf', 50)
game_active = False
start_time = 0
score = 0

Sky_surface = pygame.image.load('graphics/Sky.png').convert()
Ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surf = test_font.render('My game', False, (64, 64, 64))
#score_rect = score_surf.get_rect(center = (400, 50))

#Game title 
game_title = test_font.render('Pixel Runner', False, (111, 196, 169))
game_title_rect = game_title.get_rect(center = (400, 50))

#game instructions
game_instr = test_font.render('Press space to start', False, (64, 64, 64))
game_instr_rect = game_instr.get_rect(center = (400, 350))

#Obstacles
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800, 300))

obstacle_rect_list = []

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_grav = 0

#Game off
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.bottom == 301:
                if player_rect.collidepoint(event.pos):
                    player_grav = -20
 
        if event.type == pygame.KEYDOWN:
            if player_rect.bottom == 301:
                if event.key == pygame.K_SPACE:
                    player_grav = -20
        #else:
            #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: game_active = True

                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active == False:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
           obstacle_rect_list.append(snail_surface.get_rect(bottomright = randint(900-1100, 300)))

    if game_active:        
        #Sky and ground 
        screen.blit(Sky_surface, (0, 0))
        screen.blit(Ground_surface, (0, 300))

        #Top text
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surf, score_rect)
        score = display_score()

        #snail movement
        #snail_rect.left -= 4
        #if snail_rect.right <= 0:
        #    snail_rect.left = 800
        #screen.blit(snail_surface, snail_rect)
        
        #Player
        #Før player tegnes, ryger gravity 1 op
        player_grav += 1
        player_rect.y += player_grav
        #Player ryger ikke under jorden
        if player_rect.bottom > 300:
            player_rect.bottom = 301
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        #obstacle_movement(obstacle_rect_list)

        #Collision with snail ending game
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        
        score_message = test_font.render(f'Your score: {score}', False, (64, 64, 64))
        score_message_rect = score_message.get_rect(center = (400, 350))
        screen.blit(game_title, game_title_rect)

        if score == 0:
            screen.blit(game_instr, game_instr_rect)
        else:
            screen.blit(score_message, score_message_rect)

        
    pygame.display.update()
    clock.tick(60)