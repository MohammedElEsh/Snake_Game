import turtle
import time
import random


segments = []

score = 0
high_score = 0
delay = 0.1




# Screen
s = turtle.Screen()
s.title('Snake Game')
s.bgcolor("black")
s.setup(width=700, height=700)
s.tracer(0)  # Turns off screen updates




# words
title_pen = turtle.Turtle()
title_pen.hideturtle()
title_pen.color('white')
title_pen.penup()
title_pen.goto(-300, 310)
title_pen.write(f"Score: {score} High Score: {high_score}", align="left", font=("Fixedsys", 20))


def update_score():
    title_pen.clear()
    title_pen.write(f"Score: {score} High Score: {high_score}", align='left', font=('Fixedsys', 20))



# Border
b = turtle.Turtle()
b.color('white')
b.penup()
b.hideturtle()
b.goto(310,310)
b.pendown()
b.goto(-310,310)
b.goto(-310,-310)
b.goto(310,-310)
b.goto(310,310)
b.penup()



# Snake head
head = turtle.Turtle()
head.shape("square")
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'stop'



# Snake Food
food = turtle.Turtle()
food.shape("square")
food.color('red')
food.penup()
food.goto(0,100)









def move():
    # Move the end segments first in reverse order
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
        
        
    # Move segment 0 to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
        
        
    # Keep the snake moving in the same direction
    if head.direction == 'up':
        head.sety(head.ycor() + 10)
    if head.direction == 'down':
        head.sety(head.ycor() - 10)
    if head.direction == 'left':
        head.setx(head.xcor() - 10)
    if head.direction == 'right':
        head.setx(head.xcor() + 10)





# Functions that move snake in response to keyboard keys
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'







def collision():
    time.sleep(0.5)
    head.goto(0,0)
    head.direction = 'stop'
    
    
    # Hide the segments
    for segment in segments:
        segment.hideturtle()
        
    # Clear the segments list
    segments.clear()
    
    
    # Reset the score
    global score
    score = 0
    update_score()
    
    
    # Reset the delay
    global delay
    delay = 0.1





### Keyboard bindings
s.listen()
s.onkeypress(go_up, 'Up')
s.onkeypress(go_down, 'Down')
s.onkeypress(go_left, 'Left')
s.onkeypress(go_right, 'Right')











while True:
    # Updates the window repeatedly
    s.update()

    # Check for collision with border
    if (   head.xcor()>290
        or head.xcor()<-290
        or head.ycor()>290
        or head.ycor()<-290):
        
        collision()






    # Check if the snake eats the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        food.goto(random.randint(-290,290),random.randint(-290,290))
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.shape('square')
        new_segment.color("grey")
        new_segment.penup()
        
        segments.append(new_segment)
        
        
        
        # Shorten the delay - this increases speed of snake as it gets longer
        delay -= 0.001
        # Increase the score
        score += 1
        
        
        
        if score > high_score:
            high_score = score
        update_score()

    # Move the snake in the game
    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 10:
            collision()
            
            
            
            
            
            
            
            
            
    # Delay so that we can see things move
    time.sleep(delay)