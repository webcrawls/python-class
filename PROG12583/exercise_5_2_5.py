from turtle import * # they say this is a code smell but python docs told me!!!!!to!!doit!!!!



def draw_star(verts = 8):
    angle_of_turn = 180 / verts
    while True:
        down()
        forward(100)
        left(180 - angle_of_turn)