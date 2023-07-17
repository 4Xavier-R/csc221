from gasp import * 
from random import randint
player_x = randint(0, 63) 
player_y = randint(0, 47)
bot_x = 1
bot_y = 1 
def place_robots():
    print('bobot')
    b = Box((10 * bot_x +5 , 10 * bot_y + 5), 5 , color =color.RED)
def move_robot():
    print('bot move')
    if bot_y > player_y:
        bot_y -= 1
    if bot_y < player_y:
        bot_y +=1
    if bot_x > player_x:
        bot_x -= 1
    if bot_x < player_x:
        bot_x += 1
def place_player():
    global c
    c = Circle((10 * player_x + 5 , 10 * player_y + 5), 5, filled = True, color = color.PURPLE)

def move_player():
    global player_x, player_y, c
    print('move')
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

    
begin_graphics()
finished = False

place_player()
while not finished:
    move_player()
end_graphics()