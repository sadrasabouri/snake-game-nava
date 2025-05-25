# -*- coding: utf-8 -*-
"""Main module."""
import time
import random
from utils import init_screen, create_head, create_food
from utils import reset_game 
from utils import create_score_display, update_score
from utils import update_segments, add_segment
from utils import check_wall_collision, check_self_collision, check_food_collision
from utils import move_snake
from settings import GAME_RENDER_RATE
from settings import FOOD_RAND_RANGE, FOOD_SCORE

if __name__ == "__main__":
    score = 0
    high_score = 0
    segments = []

    screen = init_screen()
    head = create_head()
    food = create_food()
    score_display = create_score_display()

    # Prevents the snake from going back on itself
    def go_up(): head.direction = "up" if head.direction != "down" else None
    def go_down(): head.direction = "down" if head.direction != "up" else None
    def go_left(): head.direction = "left" if head.direction != "right" else None
    def go_right(): head.direction = "right" if head.direction != "left" else None

    while True:
        screen.listen()
        screen.onkeypress(go_up, "Up")
        screen.onkeypress(go_down, "Down")
        screen.onkeypress(go_left, "Left")
        screen.onkeypress(go_right, "Right")
        screen.update()

        if check_wall_collision(head) or check_self_collision(segments, head):
            segments, score, high_score = reset_game(head, segments, score, score_display, high_score)
            continue

        if check_food_collision(head, food):
            food.goto(random.randint(*FOOD_RAND_RANGE),
                      random.randint(*FOOD_RAND_RANGE))
            segments = add_segment(segments)
            score += FOOD_SCORE
            high_score = update_score(score_display, score, high_score)

        segments = update_segments(segments, head)
        move_snake(head)
        time.sleep(GAME_RENDER_RATE)
