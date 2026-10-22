
# 심전도 파형 그리기

import turtle

screen = turtle.Screen()
screen.title("심전도 모니터")
screen.bgcolor("black")
screen.setup(width=800, height=400)

pen = turtle.Turtle()
pen.color("lime")
pen.pensize(3)
pen.speed(3)

# 심박 한 번의 모양 (x 이동량, y 높이)
beat = [(20, 0), (10, 15), (10, 0), (15, 0),
        (5, -15), (8, 120), (8, -40), (6, 0),
        (20, 0), (15, 30), (15, 0), (30, 0)]

pen.penup()
pen.goto(-380, 0)
pen.pendown()

for _ in range(4):
    for dx, y in beat:
        pen.goto(pen.xcor() + dx, y)

pen.hideturtle()
turtle.done()



