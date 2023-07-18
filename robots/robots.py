from gasp import * 
from random import randint
player_x = 1
player_y = 1
bot_x = randint(0, 63)
bot_y = randint(0, 47)
def place_robot():
    global b
    b = Circle((10 * bot_x +5 , 10 * bot_y + 5), 5 , color =color.RED)
def move_robot():
    global bot_x, bot_y, b
    print('bot move')
    if bot_y > player_y:
        bot_y -= 1
    if bot_y < player_y:
        bot_y +=1
    if bot_x > player_x:
        bot_x -= 1
    if bot_x < player_x:
        bot_x += 1
    move_to(b, (10 * bot_x, 10 * bot_y))
    
def place_player():
    global c, player_x, player_y
    player_x = randint(0, 63) 
    player_y = randint(0, 47)
    c = Circle((10 * player_x + 5 , 10 * player_y + 5), 5, filled = True, color = color.PURPLE)

def move_player():
    global player_x, player_y, c
    print('move')
    key = update_when('key_pressed')
    while key == 'space':
        print('teleport')
        remove_from_screen(c)
        safe_player()
        key = update_when('key_pressed')
    if key == 'Up' and player_y <47:
        player_y += 1
    if key == 'Down' and player_y >1:
        player_y -=1
    if key == 'Left' and player_x >1:
        player_x -= 1
    if key == 'Right' and player_x <63:
        player_x += 1
    
    move_to(c, (10 * player_x, 10 * player_y))
def check_collisions():
    global finished
    if player_x == bot_x and player_y == bot_y:
        Text("You've Been Caught", (320, 240), size=40)
        sleep(2)
        finished = True
def safe_player():
    place_player()
while player_x == bot_x and player_y == bot_y:
    place_player()

begin_graphics()
finished = False

safe_player()
place_robot()
while not finished:
    move_player()
    move_robot()
    check_collisions()
end_graphics()