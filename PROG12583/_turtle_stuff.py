import turtle
import random

def draw_star(verts = None):
    turtle.speed(100)
    turtle.pensize(3)
    turtle.color()
    if verts is None:
        verts = random.randrange(1, 20)
    angle_of_turn = 180 / verts
    angle = 0
    while angle < 180:
        turtle.forward(100)
        turtle.left(180 - angle_of_turn)
        angle += angle_of_turn / 2

def draw_crazy_circle_shape(radius = 100, angle = 10, circles = 36):
    turtle.speed(10000)
    for _ in range(circles):
        turtle.circle(radius)
        turtle.left(angle)

OPTIONS = [
    draw_crazy_circle_shape,
    draw_star
]

while True:
    turtle.up()
    width_range = (turtle.window_width() - 200) / 2
    height_range = (turtle.window_height() - 200) / 2
    turtle.goto(round(random.randrange(round(0 - width_range), round(width_range))),
                round(random.randrange(round(0 - height_range), round(height_range))))
    option = random.choice(OPTIONS)
    turtle.down()
    option()
