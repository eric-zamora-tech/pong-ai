import pygame

class PygameButton:
    def __init__(self, x, y, w, h, t):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.t = t
        self.surface = pygame.Surface((self.w, self.h))
        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(t, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.surface.get_width()/2, self.surface.get_height()/2))
        self.button_rect = pygame.Rect(self.x, self.y, w, h)

    def draw(self, screen):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.surface, (127, 255, 212), (2, 2, self.w - 4, self.h - 4))
        else:
            pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, self.w, self.h))
            pygame.draw.rect(self.surface, (255, 255, 255), (2, 2, self.w - 4, self.h - 4))
        
        self.surface.blit(self.text, self.text_rect)
        screen.blit(self.surface, (self.button_rect.x, self.button_rect.y))