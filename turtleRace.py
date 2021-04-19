import turtle
import time
import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

WIDTH, HEIGHT = 500, 1000
COLORS = ["red", "green", "blue", "yellow", "magenta", "cyan"]


def get_number_of_racers():  # ask user for the number of turtles they want to race
    racers = 0
    while True:
        racers = input("Please input the number of racers (2-6): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric, please try Again")
            continue

        if 2 <= racers <= 6:
            return racers
        else:
            print("Number not in range 2-10. Try Again!")


def race():  # main race loop
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):  # creates list of turtle object
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, - HEIGHT // 2 + 20)
        racer.pendown()

        turtles.append(racer)

    return turtles


def init_turtle():  # initialize Turtle
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race()

winner_fore = getattr(Fore, (winner.upper()))
print(f"{winner_fore}The winner is the {winner} turtle!")

time.sleep(5)
