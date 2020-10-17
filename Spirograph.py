import turtle

turtle.speed(0)
turtle.bgcolor("black")


for i in range(100,200):
    for colors in ["red","green","blue","yellow","white"]:
        turtle.color(colors)
        turtle.width(i/100+1)
        turtle.forward(i)
        turtle.left(58)
        

turtle.exitonclick()