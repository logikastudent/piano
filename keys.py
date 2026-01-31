import pygame
from effects import draw_white_key, draw_black_key

WHITE_W = 80
WHITE_H = 300
BLACK_W = 50
BLACK_H = 180
KEY_Y = 150

def create_white_keys(screen_width, count):
    total_width = count * WHITE_W
    start_x = (screen_width - total_width) // 2

    rects = []
    for i in range(count):
        rects.append(
            pygame.Rect(
                start_x + i * WHITE_W,
                KEY_Y,
                WHITE_W,
                WHITE_H
            )
        )
    return rects

def create_black_keys(white_rects, positions):
    rects = []
    for i in positions:
        r = white_rects[i]
        x = r.right - BLACK_W // 2
        rects.append(
            pygame.Rect(x, KEY_Y, BLACK_W, BLACK_H)
        )
    return rects

def draw_keys(screen, white_rects, black_rects, white_pressed, black_pressed):
    for i, rect in enumerate(white_rects):
        draw_white_key(screen, rect, i in white_pressed)

    for i, rect in enumerate(black_rects):
        draw_black_key(screen, rect, i in black_pressed)
