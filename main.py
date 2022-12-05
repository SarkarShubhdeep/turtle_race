import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

# A dictionary to hold all players
turtles = {}

# List of colors that will be assigned to other players
color_list = ['green', 'blue', 'black', 'brown',  'violet', 'red', 'magenta', 'blue']

# Getting color as user input
user_bet = screen.textinput(title="Make your bet", prompt="Enter your turtle's color: ")

# User's turtle
foli = Turtle()
foli.color(user_bet)
# print(foli.pos()[0])

turtles['player'] = foli


def generating_runners():
    # Generating 4 random color from color_list
    jumbled_colors = []
    ct = 0
    for color in color_list:
        if ct == 4:
            break

        if color != user_bet.lower():
            jumbled_colors.append(color)
            ct += 1

    random.shuffle(jumbled_colors)
    # print(jumbled_colors)

    # Creating new turtles with 👆the 4 colors
    for i in range(4):
        new_turtle = Turtle()
        new_turtle.color(jumbled_colors[i])
        turtles[jumbled_colors[i]] = new_turtle



generating_runners()


# setting turtles on the start line
def set_players_positions():
    turtles_names = [_ for _ in turtles.keys()]
    for t in turtles.keys():
        turtles[t].penup()

    turtles['player'].goto(x=-230, y=0)
    turtles[turtles_names[1]].goto(x=-230, y=60)
    turtles[turtles_names[2]].goto(x=-230, y=30)
    turtles[turtles_names[3]].goto(x=-230, y=-30)
    turtles[turtles_names[4]].goto(x=-230, y=-60)

    for t in turtles.keys():
        turtles[t].pendown()

set_players_positions()
# print(foli.pos()[0])

finish_mark = Turtle()
finish_mark.penup()
finish_mark.color('grey')
finish_mark.goto(x=230, y=0)
finish_mark.right(180)



def forward_random():
    while 1:
        for t in turtles.keys():
            if turtles[t].pos()[0] >= 230.00:
            # print(f"{turtles[t]}:{turtles[t].pos()[0]}", end=" | ")
                print(f"Winner: {t}")
                exit(0)
            r_dis = random.randint(0, 50)
            turtles[t].forward(r_dis)
            # print(f"{t} moves {r_dis}")
            # break

        # print()

forward_random()
    # set_random_pace()
    # move_all_forward()





screen.exitonclick()
