# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
# print(rgb_colors)

import turtle as t
import random

COLOR_LIST = [(208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), 
              (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), 
              (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), 
              (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), 
              (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), 
              (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), 
              (65, 33, 43), (104, 43, 59)]

screen = t.Screen()
screen.title("Hirst Painting")
screen.colormode(255)
screen.setup(width=800, height=800)
tim = t.Turtle()
tim.speed(0)

def draw_painting(cols=10, dot_size=20, dist=50):
    '''Draws a painting of dots with random colors.
    Args:
        cols (int): Number of columns.
        dot_size (int): Size of dots.
        dist (int): Distance between dots.
        '''
    coord = ((cols - 1) * dist) / 2
    x, y = (-coord, -coord)
    tim.hideturtle()
    tim.penup()
    tim.goto(x, y)

    for _ in range(cols):
        for _ in range(cols):
            tim.dot(dot_size, random.choice(COLOR_LIST))
            tim.fd(dist)
        y = y+dist
        tim.goto(x, y)


if __name__=='__main__':
    draw_painting()
    screen.exitonclick()
