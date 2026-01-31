import pygame

class Button:
    def __init__(self, rect, text, font):
        self.rect = rect
        self.text = text
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen, (210, 210, 210), self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        text_surf = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(
            text_surf,
            text_surf.get_rect(center=self.rect.center)
        )

    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(event.pos)
        )
