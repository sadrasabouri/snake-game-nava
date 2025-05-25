# -*- coding: utf-8 -*-
"""Utilities module."""
from typing import List
import turtle
import time
from settings import NAME, BACKGROUND_COLOR
from settings import SNAKE_COLOR, SNAKE_SHAPE, SNAKE_STEP_SIZE, SNAKE_START_COORDS
from settings import FOOD_COLOR, FOOD_SHAPE, FOOD_START_COORDS
from settings import SEGMENT_COLOR, SEGMENT_SHAPE
from settings import SCORE_DISPLAY_FONT, SCORE_DISPLAY_COLOR
from settings import SCORE_WIDTH, SCORE_HEIGHT
from settings import SCORE_DISPLAY_FORMAT
from settings import WIDTH, HEIGHT


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
    head.goto(*SNAKE_START_COORDS)
    head.direction = "stop"
    return head


def create_food() -> turtle.Turtle:
    """Create the food for the snake."""
    food = turtle.Turtle()
    food.shape(FOOD_SHAPE)
    food.color(FOOD_COLOR)
    food.penup()
    food.goto(*FOOD_START_COORDS)
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


def reset_game(
        head: turtle.Turtle,
        segments: List[turtle.Turtle],
        score: int,
        score_display: turtle.Turtle,
        high_score: int) -> tuple:
    """Reset the game state."""
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for seg in segments:
        seg.goto(1000, 1000)
    segments.clear()
    score = 0
    high_score = update_score(score_display, score, high_score)
    return segments, score, high_score


def update_score(score_display: turtle.Turtle, score: int, high_score: int) -> int:
    """Update the score display."""
    if score > high_score:
        high_score = score
    score_display.clear()
    score_display.write(SCORE_DISPLAY_FORMAT.format(score=score, high_score=high_score),
                        font=SCORE_DISPLAY_FONT,
                        align="center")
    return high_score


def check_wall_collision(head: turtle.Turtle) -> bool:
    """Check if the snake's head collides with the wall."""
    is_x_out = abs(head.xcor()) > WIDTH/2 - 10
    is_y_out = abs(head.ycor()) > HEIGHT/2 - 10
    return is_x_out or is_y_out


def check_food_collision(head, food) -> bool:
    """Check if the snake's head collides with the food."""
    return head.distance(food) < SNAKE_STEP_SIZE


def check_self_collision(segments: List[turtle.Turtle], head: turtle.Turtle) -> bool:
    """Check if the snake collides with itself."""
    for seg in segments:
        if seg.distance(head) < SNAKE_STEP_SIZE:
            return True
    return False


def move_snake(head: turtle.Turtle) -> None:
    """Move the snake's head in the current direction."""
    if head.direction == "up":    head.sety(head.ycor() + SNAKE_STEP_SIZE)
    if head.direction == "down":  head.sety(head.ycor() - SNAKE_STEP_SIZE)
    if head.direction == "left":  head.setx(head.xcor() - SNAKE_STEP_SIZE)
    if head.direction == "right": head.setx(head.xcor() + SNAKE_STEP_SIZE)


def add_segment(segments: List[turtle.Turtle]) -> List[turtle.Turtle]:
    """Add a new segment to the snake."""
    segment = turtle.Turtle()
    segment.shape(SEGMENT_SHAPE)
    segment.color(SEGMENT_COLOR)
    segment.penup()
    segments.append(segment)
    return segments


def update_segments(segments: List[turtle.Turtle], head: turtle.Turtle) -> List[turtle.Turtle]:
    """Update the positions of the snake segments."""
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].pos())
    if segments:
        segments[0].goto(head.pos())
    return segments
