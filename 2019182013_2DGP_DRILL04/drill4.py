import turtle

count = 1
while count < 7:
    turtle.forward(500)
    turtle.penup()
    turtle.goto(0,100*count)
    turtle.pendown()
    count += 1

count = 1
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.left(90)
while count < 7:
    turtle.forward(500)
    turtle.penup()
    turtle.goto(100 * count,0)
    turtle.pendown()
    count += 1

turtle.exitonclick()
