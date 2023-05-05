import turtle
from random import randrange


def score_text(screen, score=0):
    score_turtle = turtle.Turtle()
    score_turtle.hideturtle()
    score_turtle.speed(0)
    score_turtle.penup()
    score_turtle.setpos(0, (screen.window_height() // 2) * 0.8)
    score_turtle.write(f"Score: {score}", False, align="center", font=('Arial', 30, 'normal'))


def setup_turtle(gamerTurtle):
    gamerTurtle.speed(0)
    gamerTurtle.penup()
    gamerTurtle.shape("turtle")
    gamerTurtle.shapesize(2,2)
    gamerTurtle.color("dark green")


def timer_text(screen, time=15):
    score_turtle = turtle.Turtle()
    score_turtle.hideturtle()
    score_turtle.speed(0)
    score_turtle.penup()
    score_turtle.setpos(0, (screen.window_height() // 2) * 0.7)
    score_turtle.write(f"{time} seconds left", False, align="center", font=('Arial', 20, 'normal'))


def send_turtle_to_random_position(screen, gamerTurtle):
    gamerTurtle.hideturtle()
    turtle_random_x = randrange(-int((screen.window_width() // 2) * 0.8), int((screen.window_width() // 2) * 0.9))
    turtle_random_y = randrange(-int((screen.window_height() // 2) * 0.6), int((screen.window_height() // 2) * 0.6))

    gamerTurtle.setpos(turtle_random_x, turtle_random_y)
    gamerTurtle.showturtle()


def compute_click(screen, gamerTurtle):
    click_x, click_y = 0, 0
    screen.onclick((click_y, click_y))
    print(click_x, click_y)
