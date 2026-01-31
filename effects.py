import pygame

def draw_white_key(screen, rect, pressed):
    color = (200, 200, 200) if pressed else (245, 245, 245)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)

def draw_black_key(screen, rect, pressed):
    color = (60, 60, 60) if pressed else (0, 0, 0)
    pygame.draw.rect(screen, color, rect, border_radius=4)
