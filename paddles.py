import turtle

win = turtle.Screen()
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

# Paddle A

class paddle(turtle.Turtle):
    
    def __init__(self, x, y, shape, stretch_wid = 1, stretch_len = 1):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape(shape)
        self.color("white")
        self.shapesize(stretch_wid, stretch_len)
        self.penup()
        self.goto(x,y)
        self.y = y
        
    def paddle_up(self):
        self.y += 20
        self.sety(self.y)
    
    def paddle_down(self):
        self.y -= 20
        self.sety(self.y)

# Paddles

paddleA = paddle(-350, 0, "square", 5, 1)
paddleA.color("blue")
paddleB = paddle(350, 0, "square", 5, 1)
paddleB.color("blue")

# Ball

ball = paddle(0, 0, "circle")
ball.color("red")
ball.dx = 0.4
ball.dy = 0.4

# Keyboard Input

win.listen()
win.onkeypress(paddleA.paddle_up, "w")
win.onkeypress(paddleA.paddle_down, "s")
win.onkeypress(paddleB.paddle_up, "Up")
win.onkeypress(paddleB.paddle_down, "Down")    
    
# Score Kepping

scoreA = 0
scoreB = 0
pen = paddle(0, 260, "square")
pen.hideturtle()
pen.write("Player A : {}  Player B : {} ".format(scoreA, scoreB), align = "center", font =("Times New Roman", 24, "normal"))

# Starting the Game
start = False
    
def startGame(start):
    win.onkeypress(startGame,"Enter")
    return True

while True:
    win.update()

    #Moving the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {} ".format(scoreA, scoreB), align = "center", font =("Times New Roman", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {} ".format(scoreA, scoreB), align = "center", font =("Times New Roman", 24, "normal"))

    # Ball Paddle colossion
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        
