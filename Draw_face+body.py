from gasp import *

def drawface(x ,y):
    for r in x-40, x + 40:
        Circle((r, y+20), 10)
    Circle((x, y), 100)
    Line((x, y+10), (x-20, y-30))
    Line((x-20, y-30), (x+10, y-30))
    Arc((x, y-40) , 30, 225, 315)
    for r in x-40, x+40:
        Arc((r, y+30), 20, 30, 150)

def drawbody(x, y):
    Line((x, y-100), (x, y-500))
    Line((x, y-130), (x+70, y-250))
    Line((x, y-130), (x-70, y-250))

begin_graphics()  
drawface(300, 300)
drawbody(300, 300)
update_when('key_pressed')
end_graphics()
