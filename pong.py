import turtle
import random

#Variable
sta=False;
score=0;
rx=0;
ry=0;

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
while rx ==0:
    rx = random.randrange(-1,1)
ball.dx = rx
ball.dy = 0.8

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

    while True:
        sc.update()

        #Set ball initial x shooting angle
        ball.goto((ball.xcor()+ball.dx), (ball.ycor()+ball.dy))
        print("x-",ball.xcor(),"y-", ball.ycor())
        # Checking borders
        if ball.ycor() > 98:
            ball.sety(98)
            ball.dy *= -1

        if ball.xcor() < -100:
            ball.setx(-100)
            ball.dx *= -1

        if ball.ycor() < -25:
            exit()

        if ball.xcor() > 98:
            ball.setx(98)
            ball.dx *= -1

       #Collisions
        if ((ball.ycor() < (paddle.ycor()+5))) & ((ball.xcor()< (paddle.xcor()+20))) & ((ball.xcor()) > (paddle.xcor()-20)):
            ry = float(random.randrange(110,135)/100)
            ball.dy = ball.dy * -1 * ry
            scoreup()

            
turtle.done()
    



