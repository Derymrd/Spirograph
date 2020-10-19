import turtle

turtle.shape("turtle")
turtle.speed(3)
turtle.bgcolor("black")


for i in range(5):
    for colors in ["red","green","blue","yellow","white"]:
        turtle.color(colors)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
turtle.exitonclick()
