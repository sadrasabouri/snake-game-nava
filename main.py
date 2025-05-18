# -*- coding: utf-8 -*-
"""Main module."""
import turtle
import time
import random
from utils import init_screen, create_head, create_food
from utils import create_score_display
from settings import WIDTH, HEIGHT

DELAY = 0.1
SCORE = 0
HIGH_SCORE = 0
SEGMENTS = []

screen = init_screen()
head = create_head()
food = create_food()
score_display = create_score_display()

def go_up():    head.direction = "up"    if head.direction != "down" else None
def go_down():  head.direction = "down"  if head.direction != "up" else None
def go_left():  head.direction = "left"  if head.direction != "right" else None
def go_right(): head.direction = "right" if head.direction != "left" else None

def move_snake() -> None:
    if head.direction == "up":    head.sety(head.ycor() + 20)
    if head.direction == "down":  head.sety(head.ycor() - 20)
    if head.direction == "left":  head.setx(head.xcor() - 20)
    if head.direction == "right": head.setx(head.xcor() + 20)

def check_wall_collision():
    return (abs(head.xcor()) > WIDTH/2 - 10 or abs(head.ycor()) > HEIGHT/2 - 10)

def reset_game():
    global SCORE
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for seg in SEGMENTS:
        seg.goto(1000, 1000)
    SEGMENTS.clear()
    SCORE = 0
    update_score()

def check_food_collision():
    return head.distance(food) < 20

def add_segment():
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color("lightgreen")
    segment.penup()
    SEGMENTS.append(segment)

def update_segments():
    for i in range(len(SEGMENTS)-1, 0, -1):
        SEGMENTS[i].goto(SEGMENTS[i-1].pos())
    if SEGMENTS:
        SEGMENTS[0].goto(head.pos())

def check_self_collision():
    for seg in SEGMENTS:
        if seg.distance(head) < 20:
            return True
    return False

def update_score():
    global HIGH_SCORE
    if SCORE > HIGH_SCORE:
        HIGH_SCORE = SCORE
    score_display.clear()
    score_display.write(f"Score: {SCORE}  High Score: {HIGH_SCORE}", align="center", font=("Courier", 20, "normal"))

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# --- Game loop ---
while True:
    screen.update()

    if check_wall_collision(head) or check_self_collision():
        reset_game()

    if check_food_collision():
        x, y = random.randint(-280, 280), random.randint(-280, 280)
        food.goto(x, y)
        add_segment()
        SCORE += 10
        update_score()

    update_segments()
    move_snake()
    time.sleep(DELAY)
