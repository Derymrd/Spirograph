import turtle

turtle.shape("turtle")
turtle.speed(0)
turtle.bgcolor("black")


for i in range(5):
    for colors in ["red","green","blue","yellow","white"]:
        turtle.color(colors)
        turtle.pensize(3)
        turtle.circle(100)
        turtle.left(15)
        
turtle.exitonclick()