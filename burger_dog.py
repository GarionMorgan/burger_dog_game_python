import pygame, random

#initialize game
pygame.init()

#set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_HEIGHT))
pygame.display.set_caption("Burger Dog")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#set game values
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = .25
BUFFER_DISTANCE = 100

score = 0
burger_points = 0
burgers_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY

boost_level = STARTING_BOOST_LEVEL

burger_velocity = STARTING_BURGER_VELOCITY

#set colors
ORANGE = (246,170,54)
BLACK = (0,0,0)
WHITE = (255,255,255)

#set fonts
font = pygame.font.Font("./burger_dog_assets/WashYourHand.ttf", 32)

#set text
points_text = font.render("Burger Points: " + str(burger_points), True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft = (10,10)

score_text = font.render("Score: " + str(score), True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10,50)

title_text = font.render("Burger Dog", True, ORANGE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

eaten_text = font.render("Burgers Eaten: " + str(burgers_eaten), True, ORANGE)
eaten_rect = eaten_text.get_rect()
eaten_rect.centerx = WINDOW_WIDTH//2
eaten_rect.y = 50

lives_text = font.render("Lives: " + str(player_lives), True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH-10, 10)

boost_text = font.render("Boost: " + str(boost_level), True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 10, 50)

game_over_text = font.render("FINAL SCORE: " + str(score), True, ORANGE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, ORANGE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2 + 64)

#set sounds and music
bark_sound = pygame.mixer.Sound("./burger_dog_assets/bark_sound.wav")
miss_sound = pygame.mixer.Sound("./burger_dog_assets/miss_sound.wav")
pygame.mixer.music.load("./burger_dog_assets/bd_background_music.wav")

#set images
player_image_right = pygame.image.load("./burger_dog_assets/dog_right.png")
player_image_left = pygame.image.load("./burger_dog_assets/dog_left.png")
player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH//2
player_rect.bottom = WINDOW_HEIGHT

burger_image = pygame.image.load("./burger_dog_assets/burger.png")
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0,WINDOW_WIDTH-32), -BUFFER_DISTANCE)

#main game loop
running = True
while running:
    #check if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#end game
pygame.quit()