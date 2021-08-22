import turtle

wn = turtle.Screen()
wn.title("pong by tokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0


#Sets the current pen state to PENUP. Turtle will move around the screen, but will not draw when its pen state is PENUP. The turtle's default pen state is PENDOWN.
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)#coordenadas da bola no começo
ball.dx = 0.5#Signiifca que cada vez que a bola se mover, ela moverá 2 pixels p/vez
ball.dy = 0.5 #se move para baixo, como a coord.Y esta negativa

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A : 0  player B : 0", align="center", font=("courier", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()#ycor é proprio do modulo, ele retorna a coordenada Y
    y += 20 #adiciona 20 a coordenada y, pra subir#Y na representaçao gráfica da funçao é a coordenada vertical
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, "Q")#sempre que o usuario pressionar "w", a funçao paddle_a_up é ativada
wn.onkeypress(paddle_a_down, "A")
wn.onkeypress(paddle_b_up, "Up")#Seta para cima e para baixo, respectivamente
wn.onkeypress(paddle_b_down, "Down")



while True:
    #enables the window from updating while playing, i think
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390 :
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()#VAI LIMPAR O QUE ESTA NA TELA(atualizar)
        pen.write("player A : {}  player B : {}".format(score_a, score_b), align="center",font=("courier", 24, "normal"))



    elif ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A : {}  player B : {}".format(score_a, score_b), align="center",font=("courier", 24, "normal"))


    #paddle and ball collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):#caso a bola encoste no remo
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1











