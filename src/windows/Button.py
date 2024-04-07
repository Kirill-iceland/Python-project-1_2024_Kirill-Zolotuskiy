import pygame


class Button:
    color: tuple[int, int, int]
    text_color: tuple[int, int, int]
    text: str
    rect: pygame.rect.Rect
    clicked: bool
    my_font: pygame.font.Font

    def __init__(self, pos_x: int, pos_y: int, size_x: int, size_y: int, font_size: int):
        self.rect = pygame.rect.Rect(pos_x, pos_y, size_x, size_y)
        self.clocked = True
        self.my_font = pygame.font.SysFont('Consolas', font_size)

    def set_color(self, color: tuple[int, int, int]):
        self.color = color

    def set_text(self, text: str):
        self.text = text

    def set_text_color(self, color: tuple[int, int, int]):
        self.text_color = color

    def draw(self, screen: pygame.Surface) -> bool:
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            pygame.draw.rect(screen, self.text_color, self.rect)
            text = self.my_font.render(self.text, False, self.color)
            screen.blit(
                text, (self.rect.center[0] - (text.get_size()[0] / 2), self.rect.center[1] - 15))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            text = self.my_font.render(self.text, False, self.text_color)
            screen.blit(text, (self.rect.center[0] - (text.get_size()[
                        0] / 2), self.rect.center[1] - 15 - (text.get_size()[1] / 2)))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
