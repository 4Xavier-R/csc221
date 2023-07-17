from gasp import * 
from random import randint
player_x = randint(0, 63) 
player_y = randint(0, 47)
 
def place_robots():
    print('bobot')
def place_player():
    global c
    c = Circle((10 * player_x + 5 , 10 * player_y + 5), 5, filled = True)
def move_player():
    global player_x, player_y, c
    print('move')
    key = update_when('key_pressed')
    if key == 'Up' and player_y <480:
        player_y += 20
    if key == 'Down' and player_y >0:
        player_y -=20
    if key == 'Left' and player_x >0:
        player_x -= 20
    if key == 'Right' and player_x <630:
        player_x += 20
    move_to(c, (player_x, player_y))

    
begin_graphics()
finished = False

place_player()
while not finished:
    move_player()
end_graphics()