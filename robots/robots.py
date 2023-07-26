from gasp import * 
from random import randint

telecount = 0
class Robot:
    pass


class Player:
    pass


def place_robots():
    global robots
    robots = []
    while len(robots) < numbot:
        bot = Robot()
        bot.x = randint(0, 63)
        bot.y = randint(0, 47)
        if not collided(bot, robots):
            bot.shape = Circle((10 * bot.x + 5 , 10 * bot.y + 5 ), 5, color =color.RED)
            robots.append(bot)


def move_robots():
    global robots
    print('bot move')
    for bot in robots:
        if bot.y > player.y:
            bot.y -= 1
        if bot.y < player.y:
            bot.y +=1
        if bot.x > player.x:
            bot.x -= 1
        if bot.x < player.x:
            bot.x += 1
        move_to(bot.shape, (10 * bot.x + 5, 10 * bot.y + 5))


def place_player():
    global c, player
    player = Player()
    player.x = randint(0, 63) 
    player.y = randint(0, 47)
    c = Circle((10 * player.x + 5 , 10 * player.y + 5), 5, filled = True, color = color.PURPLE)


def move_player():
    global telecount
    print('move')
    key = update_when('key_pressed')
    while key == 'space':
        print('teleport')
        telecount = telecount +1 
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
    move_to(c, (10 * player.x + 5, 10 * player.y + 5))

def collided(player, robots):
    for bot in robots:
        if player.x == bot.x and player.y == bot.y:
            return True
    return False
    


def check_collisions():
    global finished, player, collided
    if collided(player, robots):
        Text("You've Been Caught", (315, 235), size=40)
        sleep(2)
        finished = True

def safe_player():
    place_player()
    if collided(player, robots):           
        print('safety')
        remove_from_screen(c)
        place_player()


begin_graphics()
finished = False
numbot = 10

place_robots()
safe_player()

while not finished:
    move_player()
    move_robots()
    check_collisions()

end_graphics()