from gasp import *
begin_graphics()
c = Circle((200, 100), 5)
update_when('key_pressed')
move_to(c, ( 300, 200))