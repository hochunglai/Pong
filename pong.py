import turtle

#Variable
sta=False;

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
    global sta;
    sta=True;

#Keyboard bindings
sc.listen()  
sc.onkeypress(paddleright, "d")
sc.onkeypress(paddleleft, "a")
sc.onkeypress(startg, "space")


def start():
    starts = turtle.Turtle()
    starts.speed(0)
    starts.color("white")
    starts.penup()
    starts.hideturtle()
    starts.goto(0, 80)
    while sta==False:
        starts.write("Press SpaceBar To Start",align="center", font=("Courier", 12, "normal"))
    starts.clear()

   

def main():
    start()
  
    while sta==True:
        sc.update()

    turtle.done()
    
main();


