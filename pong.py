import turtle
import random

#Variable
sta=False;
score=0;

#Screen Setup
sc = turtle.Screen()
sc.setup(600,800)
sc.bgcolor("black")
sc.title("Classic Pong")
    
#Paddle Setup
paddle = turtle.Turtle()
turtle.setworldcoordinates(-100, -25, 100, 100)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=4)
paddle.penup()


#Ball setup
ball = turtle.Turtle()
ball.speed(0)
ball.hideturtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 10)
ball.showturtle()

#Start Setup
starts = turtle.Turtle()
starts.speed(0)
starts.color("white")
starts.penup()
starts.hideturtle()
starts.goto(0, 80)
starts.write("Press SpaceBar To Start",align="center", font=("Courier", 12, "normal"))

def paddleright():
    if sta==True:
        x = paddle.xcor()
        x += 10
        paddle.setx(x)

def paddleleft():
    if sta==True:
        x = paddle.xcor()
        x -= 10
        paddle.setx(x)

def startg():
    starts.clear()
    starts.write("Score - {}".format(score), align="center",font=("Courier", 12, "normal"))
    global sta;
    sta=True;
    main()

def scoreup():
    global score
    score+=1
    starts.clear()
    starts.write("Score - {}".format(score), align="center",font=("Courier", 12, "normal"))

#Keyboard bindings
sc.listen()  
sc.onkeypress(paddleright, "d")
sc.onkeypress(paddleleft, "a")
sc.onkeypress(startg, "space")

def main():
    #Ball Random x
    sx=0;
    while sx == 0:
        sx = random.randrange(-2,5)

    #Ball Shoot y
    sy=1;
    while True:
        sc.update()
        print(sx)
        #Set ball initial x shooting angle
        x = ball.xcor()
        x = x + sx;
        ball.setx(x)

        #Set ball initial y shooting angle
        y = ball.ycor()
        y = y + sy
        ball.sety(y)

        # Checking borders
        if y > 98:
            ball.sety(98)
            sy = -1
            scoreup()

        if x < -100:
            ball.setx(-100)
            sx = sx*(-1)

        if y < -25:
            ball.sety(-25)
            sy = 1

        if x > 98:
            ball.setx(98)
            sx = sx*(-1)

       #Collisions


turtle.done()
    



