from gasp import * 
from random import randint
player_x = randint(0, 63) 
player_y = randint(0, 47)
c = Circle(( 200, 200), 5)
def place_robots():
    print('bobot')
def place_player():
    Circle((10 * player_x + 5 , 10 * player_y + 5), 5, filled = True)
    print('sus')
def move_player():
    print('susmovesss')
    update_when('key_pressed')
begin_graphics()
finished = False

place_player()
while not finished:
    move_player()
end_graphics()