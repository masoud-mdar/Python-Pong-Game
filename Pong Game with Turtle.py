import turtle
window = turtle.Screen()
window.title("OMFG!!!")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

#paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2


    
#pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align = "center", font = ("courier", 24, "normal"))


#score

score_a = 0
score_b = 0


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
    
window.listen()
window.onkeypress(paddle_a_up, "z")


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
window.listen()
window.onkeypress(paddle_a_down, "s")


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
window.listen()
window.onkeypress(paddle_b_up, "Up")


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
window.listen()
window.onkeypress(paddle_b_down, "Down")

def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)

window.listen()
window.onkeypress(paddle_a_right, "d")

def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)
    
window.listen()
window.onkeypress(paddle_a_left, "q")

def paddle_b_right():
    x = paddle_b.xcor()
    x += 20
    paddle_b.setx(x)
    
window.listen()
window.onkeypress(paddle_b_right, "Right")

def paddle_b_left():
    x = paddle_b.xcor()
    x -= 20
    paddle_b.setx(x)
    
window.listen()
window.onkeypress(paddle_b_left, "Left")
    
    

#Game main loop

while True:
    window.update()
    
    #Move the ball
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #checking borders
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align = "center", font = ("courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align = "center", font = ("courier", 24, "normal"))
        
        
    # ball and paddles collisions
    
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1