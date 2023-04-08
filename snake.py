import pygame, sys, random, time


# variable
clock = pygame.time.Clock()
fps = 5
# display
win_x = 500
win_y = 560
# color
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
# player
player_x = random.randrange(0,win_x -20,20)
player_y = random.randrange(0,win_y -20,20)
player_x_speed = 0
player_y_speed = 0
player_length = 1
player_log = []
# food
food_x = random.randrange(0,win_x -20,20)
food_y = random.randrange(0,win_y -20,20)
food_color = "red"
food_plus = 1
food_luck_spawn = 30

# display
win = pygame.display.set_mode((win_x,win_y))
pygame.display.set_caption("Arcade Game: Snake")

# function
def snake():
    player_log.append([player_x,player_y])
    if len(player_log) > player_length:
        player_log.pop(0)
    for part in player_log:
        pygame.draw.rect(win,green,(part[0],part[1],20,20))
    for part in player_log[:-1]:
        if part == [player_x,player_y]:
            return True
        
def border():
    global player_x,player_y
    if player_x > win_x -20:
        player_x = 0
    elif player_x < 0:
        player_x = win_x -20
    elif player_y > win_y - 20:
        player_y = 0
    elif player_y < 0:
        player_y = win_y -20

def food_spawn():
    global food_x,food_y,player_length,food_color,food_plus
    if player_x == food_x and player_y == food_y:
        player_length += food_plus
        print(player_length)
        food_x = random.randrange(0,win_x -20,20)
        food_y = random.randrange(0,win_y -20,20)
        food_luck = random.randint(1,food_luck_spawn)
        if food_luck != 1:
            food_color = "red"
            food_plus = 1
        else:
            food_color = "yellow"
            food_plus = 5

# main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if player_x_speed != -20:
                    player_x_speed = 20
                    player_y_speed = 0
            if event.key == pygame.K_a:
                if player_x_speed != 20:
                    player_x_speed = -20
                    player_y_speed = 0
            if event.key == pygame.K_w:
                if player_y_speed != 20:
                    player_y_speed = -20
                    player_x_speed = 0
            if event.key == pygame.K_s:
                if player_y_speed != -20:
                    player_y_speed = 20
                    player_x_speed = 0
    clock.tick(fps)
    player_x += player_x_speed
    player_y += player_y_speed
    border()
    # food
    food_spawn()
    win.fill(black)
    pygame.draw.rect(win,food_color,(food_x,food_y,20,20))
    if snake():
        time.sleep(5)
        break
    # pygame.draw.rect(win,green,(player_x,player_y,20,20))
    pygame.display.update()
pygame.quit()
sys.exit()