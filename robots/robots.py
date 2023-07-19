from gasp import * 
from random import randint


class Robot:
    pass


class Player:
    pass


def place_robot():
    global b, bot
    bot = Robot()
    bot.x = randint(0, 63)
    bot.y = randint(0, 47)
    b = Circle((10 * bot.x +5 , 10 * bot.y + 5), 5 , color =color.RED)


def move_robot():
    print('bot move')
    if bot.y > player.y:
        bot.y -= 1
    if bot.y < player.y:
        bot.y +=1
    if bot.x > player.x:
        bot.x -= 1
    if bot.x < player.x:
        bot.x += 1
    move_to(b, (10 * bot.x, 10 * bot.y))


def place_player():
    global c, player
    player = Player()
    player.x = randint(0, 63) 
    player.y = randint(0, 47)
    c = Circle((10 * player.x + 5 , 10 * player.y + 5), 5, filled = True, color = color.PURPLE)


def move_player():
    print('move')
    key = update_when('key_pressed')
    while key == 'space':
        print('teleport')
        remove_from_screen(c)
        safe_player()
        key = update_when('key_pressed')
    if key == 'Up' and player.y <47:
        player.y += 1
    if key == 'Down' and player.y >1:
        player.y -=1
    if key == 'Left' and player.x >1:
        player.x -= 1
    if key == 'Right' and player.x <63:
        player.x += 1
    
    move_to(c, (10 * player.x, 10 * player.y))


def check_collisions():
    global finished, player
    if player.x == bot.x and player.y == bot.y:
        Text("You've Been Caught", (320, 240), size=40)
        sleep(2)
        finished = True

def safe_player():
    place_player()
    while player.x == bot.x and player.y == bot.y:
        print('safety')
        place_player()


begin_graphics()
finished = False

place_robot()
safe_player()

while not finished:
    move_player()
    move_robot()
    check_collisions()

end_graphics()