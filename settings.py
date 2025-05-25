# -*- coding: utf-8 -*-
"""Settings module."""

NAME = "🐍 Snake Game"
BACKGROUND_COLOR = "black"
SNAKE_COLOR = "green"
SNAKE_SHAPE = "square"
SNAKE_START_COORDS = (0, 0) 

SEGMENT_COLOR = "lightgreen"
SEGMENT_SHAPE = "square"

FOOD_COLOR = "red"
FOOD_SHAPE = "circle"
FOOD_START_COORDS = (0, 100)
FOOD_RAND_RANGE = (-280, 280)
FOOD_SCORE = 10

WIDTH, HEIGHT = 600, 600

SCORE_DISPLAY_COLOR = "white"
SCORE_DISPLAY_FONT = ("Courier", 20, "normal")
SCORE_DISPLAY_FORMAT = "Score: {score}  High Score: {high_score}"
SCORE_WIDTH, SCORE_HEIGHT = 0, 260

GAME_RENDER_RATE = 0.1  # seconds between updates
SNAKE_STEP_SIZE = 20  # pixels the snake moves per step
