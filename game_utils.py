import turtle
from random import randrange
from math import sqrt



def score_text(score_turtle ,screen, score=0):
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


def timer_text(timer_turtle, screen, time=15):
    timer_turtle.hideturtle()
    timer_turtle.speed(0)
    timer_turtle.penup()
    timer_turtle.setpos(0, (screen.window_height() // 2) * 0.7)
    timer_turtle.write(f"{time} seconds left", False, align="center", font=('Arial', 20, 'normal'))


def send_turtle_to_random_position(screen, gamerTurtle):
    gamerTurtle.hideturtle()
    turtle_random_x = randrange(-int((screen.window_width() // 2) * 0.8), int((screen.window_width() // 2) * 0.9))
    turtle_random_y = randrange(-int((screen.window_height() // 2) * 0.6), int((screen.window_height() // 2) * 0.6))

    gamerTurtle.setpos(turtle_random_x, turtle_random_y)
    gamerTurtle.showturtle()


def compute_click(turtlePos, coord_x, coord_y):
    turtle_x, turtle_y = turtlePos

    click_distance = sqrt((turtle_x - coord_x) ** 2 + (turtle_y - coord_y) ** 2)
    return click_distance


def add_score(max_distance, click_distance, player_score, prize_point=1):
    if click_distance < max_distance:
        player_score += prize_point
    return int(player_score)


def game_over(score):
    game_over_turtle = turtle.Turtle()
    game_over_turtle.speed(0)
    game_over_turtle.penup()
    game_over_turtle.hideturtle()
    game_over_turtle.write(f"Game over!\n Score {score}", False, align="center", font=('Arial', 50, 'bold'))