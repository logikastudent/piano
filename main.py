import pygame
from settings import *
from sounds import load_sounds
from keys import create_white_keys, create_black_keys, draw_keys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("🎹 Piano")

clock = pygame.time.Clock()

# Звуки
white_sounds = load_sounds(WHITE_KEYS)

white_rects = create_white_keys(WINDOW_WIDTH, len(WHITE_KEYS))
black_rects = create_black_keys(white_rects, BLACK_KEYS_POSITIONS)

white_pressed = set()
black_pressed = set()

running = True
while running:
    screen.fill(DARK_BG)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        # ⌨️ КЛАВІАТУРА
        if e.type == pygame.KEYDOWN:
            for i, (k, _) in enumerate(WHITE_KEYS):
                if pygame.key.name(e.key) == k:
                    white_sounds[k].play()
                    white_pressed.add(i)

        if e.type == pygame.KEYUP:
            white_pressed.clear()
            black_pressed.clear()

        # 🖱️ МИША
        if e.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(white_rects):
                if rect.collidepoint(e.pos):
                    k, _ = WHITE_KEYS[i]
                    white_sounds[k].play()
                    white_pressed.add(i)

            for i, rect in enumerate(black_rects):
                if rect.collidepoint(e.pos):
                    # граємо звук сусідньої білої
                    white_index = BLACK_KEYS_POSITIONS[i]
                    k, _ = WHITE_KEYS[white_index]
                    white_sounds[k].play()
                    black_pressed.add(i)

        if e.type == pygame.MOUSEBUTTONUP:
            white_pressed.clear()
            black_pressed.clear()

    draw_keys(
        screen,
        white_rects,
        black_rects,
        white_pressed,
        black_pressed
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
