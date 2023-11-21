import turtle
import random


score = 0
high_score = 0
delay = 0.1


# Screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("black")
s.setup(width=700, height=700)


# words
title_pen = turtle.Turtle()
title_pen.hideturtle()
title_pen.color("white")
title_pen.penup()
title_pen.goto(-300, 310)
title_pen.write(f"Score: {score} High Score: {high_score}", align="left", font=("Fixedsys", 20))


def update_score():
    title_pen.clear()
    title_pen.write(f"Score: {score} High Score: {high_score}", align="left", font=("Fixedsys", 20))


# Border
b = turtle.Turtle()
b.color("white")
b.penup()
b.hideturtle()
b.goto(310, 310)
b.pendown()
b.goto(-310, 310)
b.goto(-310, -310)
b.goto(310, -310)
b.goto(310, 310)
b.penup()


# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# Snake Food
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 10)
    if head.direction == "down":
        head.sety(head.ycor() - 10)
    if head.direction == "left":
        head.setx(head.xcor() - 10)
    if head.direction == "right":
        head.setx(head.xcor() + 10)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def collision():
    head.goto(0, 0)
    head.direction = "stop"

    # Reset the score
    global score
    score = 0
    update_score()

    # Reset the delay
    global delay
    delay = 0.1


### Keyboard bindings
s.listen()
s.onkeypress(go_up, "Up")
s.onkeypress(go_down, "Down")
s.onkeypress(go_left, "Left")
s.onkeypress(go_right, "Right")


while True:
    # Updates the window repeatedly
    s.update()

    # Check for collision with border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        collision()

    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # increases speed
        delay -= 0.001
        # Increase the score
        score += 1

        if score > high_score:
            high_score = score
        update_score()






    move()