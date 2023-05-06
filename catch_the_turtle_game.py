import turtle
import game_utils

player_score = 0
game_time = 15

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle Game")

gamerTurtle = turtle.Turtle()
scoreTurtle = turtle.Turtle()
game_utils.setup_turtle(gamerTurtle)
game_utils.score_text(scoreTurtle, turtle_screen, score=0)

def turtle_timer():
    game_utils.send_turtle_to_random_position(turtle_screen, gamerTurtle)
    turtle_screen.ontimer(turtle_timer, t=500)


def get_click_location(x, y):
    click_distance = game_utils.compute_click(gamerTurtle.pos(), x, y)
    global player_score
    player_score = game_utils.add_score(200, click_distance, player_score)
    scoreTurtle.clear()
    game_utils.score_text(scoreTurtle, turtle_screen, score=player_score)


game_utils.timer_text(turtle_screen, time=game_time)

turtle_screen.onclick(get_click_location)
turtle_timer()



turtle.mainloop()