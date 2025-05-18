# -*- coding: utf-8 -*-
"""Utilities module."""
import turtle
from settings import NAME, BACKGROUND_COLOR
from settings import SNAKE_COLOR, SNAKE_SHAPE
from settings import FOOD_COLOR, FOOD_SHAPE
from settings import SCORE_DISPLAY_FONT, SCORE_DISPLAY_COLOR
from settings import SCORE_WIDTH, SCORE_HEIGHT
from settings import SCORE_DISPLAY_FORMAT
from settings import WIDTH, HEIGHT, DELAY


def init_screen() -> turtle.Screen:
    """Initialize the game screen."""
    screen = turtle.Screen()
    screen.title(NAME)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)
    return screen


def create_head() -> turtle.Turtle:
    """Create the snake's head."""
    head = turtle.Turtle()
    head.shape(SNAKE_SHAPE)
    head.color(SNAKE_COLOR)
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"
    return head


def create_food() -> turtle.Turtle:
    """Create the food for the snake."""
    food = turtle.Turtle()
    food.shape(FOOD_SHAPE)
    food.color(FOOD_COLOR)
    food.penup()
    food.goto(0, 100)
    return food


def create_score_display() -> turtle.Turtle:
    """Create the score display."""
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color(SCORE_DISPLAY_COLOR)
    pen.penup()
    pen.hideturtle()
    pen.goto(SCORE_WIDTH, SCORE_HEIGHT)
    pen.write(SCORE_DISPLAY_FORMAT.format(score=0, high_score=0),
              font=SCORE_DISPLAY_FONT,
              align="center")
    return pen
