from turtle import Screen, Turtle
import random


tim = Turtle()

colours = ['HotPink', 'MediumPurple', 'Tomato', 'DarkSlateBlue', 'ForestGreen',
             'DarkTurquoise', 'CornflowerBlue', 'Navy', 'MediumSpringGreen', 'Orchid',
              'SpringGreen', 'Yellow', 'SlateGray', 'RoyalBlue', 'Crimson']
angles = [0, 90, 270]

tim.shape('turtle')
tim.color('DarkSeaGreen4')
# tim.penup()
# tim.sety(100)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

tim.turtlesize(2,2,5)
tim.pendown()
tim.pensize(10)
tim.speed(0)

# for i in range(3, 15):
#     colour = random.choice(colours)
#     colours.remove(colour)
#     tim.pencolor(colour)
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360/i)

# for _ in range(200):
#     colour = random.choice(colours)
#     dir = random.choice(angles)
#     tim.pencolor(colour)
#     tim.forward(30)
#     tim.right(dir)



# for _ in range(72):
#     colour = random.choice(colours)
#     tim.pencolor(colour)
#     tim.circle(100)
#     tim.setheading(tim.heading()+5)















my_screen = Screen()
my_screen.exitonclick()
