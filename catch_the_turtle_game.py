import turtle
import game_utils

player_score = 0
game_time = 15

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle Game")

gamerTurtle = turtle.Turtle()
game_utils.setup_turtle(gamerTurtle)


def turtle_timer():
    game_utils.send_turtle_to_random_position(turtle_screen, gamerTurtle)
    turtle_screen.ontimer(turtle_timer, t=750)

game_utils.compute_click(turtle_screen, gamerTurtle)
game_utils.score_text(turtle_screen, score=player_score)
game_utils.timer_text(turtle_screen, time=game_time)
turtle_timer()



turtle.mainloop()