import pygame
from sys import exit
from random import randint, choice
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.3)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_frames(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]  

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_frames()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
           fly_frame_1 = pygame.image.load('graphics/fly/Fly1.png').convert_alpha()
           fly_frame_2 = pygame.image.load('graphics/fly/Fly2.png').convert_alpha()
           self.frames = [fly_frame_1, fly_frame_2] 
           y_pos = 210
        else:
            snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.animation_index = 0    
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900, 1100), y_pos))

    def amimation(self):
        self.animation_index += 0.1 
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.amimation()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

#def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else: 
                screen.blit(fly_surf, obstacle_rect)
           
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return(obstacle_list)
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else: 
        return True


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.1)
bg_music.play(loops = -1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

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

#Snail
#snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
#snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
#snail_frames = [snail_frame_1, snail_frame_2]
#snail_frame_index = 0
#snail_surf = snail_frames[snail_frame_index]

#Fly
#fly_frame_1 = pygame.image.load('graphics/fly/Fly1.png').convert_alpha()
#fly_frame_2 = pygame.image.load('graphics/fly/Fly2.png').convert_alpha()
#fly_frames = [fly_frame_1, fly_frame_2]
#fly_frame_index = 0
#fly_surf = fly_frames[fly_frame_index]


obstacle_rect_list = []

player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_grav = 0

#Game off
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
                    start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(random.choice(['fly', 'snail', 'snail'])))

                #if randint(0,2):
                #    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 300)))
                #else:
                #    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 210)))

            #if event.type == snail_animation_timer:
            #    if snail_frame_index == 0:
            #        snail_frame_index = 1
            #    else:
            #        snail_frame_index = 0
            #    snail_surf = snail_frames[snail_frame_index]
        
            #if event.type == fly_animation_timer:
            #    if fly_frame_index == 0:
            #        fly_frame_index = 1
            #    else:
            #        fly_frame_index = 0
            #    fly_surf = fly_frames[fly_frame_index]

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
        #player_grav += 1
        #player_rect.y += player_grav
        #Player ryger ikke under jorden
        #if player_rect.bottom > 300:
        #    player_rect.bottom = 301
        #player_animation()
        #screen.blit(player_surf, player_rect)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # Obstacle movement
        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collisions
        game_active = collision_sprite()
        #game_active = collisions(player_rect, obstacle_rect_list)

        #Collision with snail ending game
        #if snail_rect.colliderect(player_rect):
            #game_active = False
    
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_grav = 0
        
        score_message = test_font.render(f'Your score: {score}', False, (64, 64, 64))
        score_message_rect = score_message.get_rect(center = (400, 350))
        screen.blit(game_title, game_title_rect)

        #bg_music.stop()

        if score == 0:
            screen.blit(game_instr, game_instr_rect)
        else:
            screen.blit(score_message, score_message_rect)

        
    pygame.display.update()
    clock.tick(60)