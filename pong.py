
import turtle #library for graphics
from playsound import playsound

win = turtle.Screen()
win.title("PONG")
win.bgcolor("white")
win.setup(width=500, height=500)
win.tracer(0) # not sure what this is yet

scoreA = 0
scoreB = 0

# Pad A

padA = turtle.Turtle()
padA.speed(0)
padA.shape("square")
padA.color("black")
padA.penup()
padA.goto(-200,0)
padA.shapesize(stretch_wid=5, stretch_len=1)

# Pad B

padB = turtle.Turtle()
padB.speed(0)
padB.shape("square")
padB.color("black")
padB.penup()
padB.goto(200,0)
padB.shapesize(stretch_wid=5, stretch_len=1)


# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0,0)

ball.dx = 1
ball.dy = 1

# Pen 

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("{} {}".format(scoreA,scoreB), align="center", font=("Courier", 15, "normal"))

# Functions

def padA_up():
    y = padA.ycor()
    y += 30
    padA.sety(y)

def padA_dn():
    y = padA.ycor()
    y -= 30
    padA.sety(y)

def padB_up():
    y = padB.ycor()
    y += 30
    padB.sety(y)

def padB_dn():
    y = padB.ycor()
    y -= 30
    padB.sety(y)

# Keyboard Bindings

win.listen()
win.onkey(padA_up, "w")
win.onkey(padA_dn, "s")
win.onkey(padB_up, "Up")
win.onkey(padB_dn, "Down")


# Main game loop


while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check the border

    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1
        playsound("bounce.wav",False)


    if ball.ycor() < -230:
        ball.sety(-230)
        ball.dy *= -1
        playsound("bounce.wav",False)



    if ball.xcor() > 230:
        ball.goto(0,0)
        if ball.dx > 0:
            ball.dx = -1
        else:
            ball.dx = 1

        
        scoreA += 1
        pen.clear()
        pen.write("{} {}".format(scoreA,scoreB), align="center", font=("Courier", 15, "normal"))

    if ball.xcor() < -240:
        ball.goto(0,0)
        if ball.dx > 0:
            ball.dx = -1
        else:
            ball.dx = 1
        scoreB += 1
        pen.clear()
        pen.write("{} {}".format(scoreA,scoreB), align="center", font=("Courier", 15, "normal"))

    # Ball and Paddle collisions

    if (ball.xcor() > 180 and ball.xcor() < 190) and (ball.ycor() < padB.ycor() + 50 and ball.ycor() > padB.ycor() - 50):
        ball.setx(180)
        ball.dx *= -1.00
        ball.dy *= 1.05
        playsound("bounce.wav",False)



    if (ball.xcor() < -180 and ball.xcor() > -190) and (ball.ycor() < padA.ycor() + 50 and ball.ycor() > padA.ycor() - 50):
        ball.setx(-180)
        ball.dx *= -1.05
        playsound("bounce.wav",False)


        


