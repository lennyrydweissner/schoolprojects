import pygame


class TextBox:

    def __init__(self, pos_x_of_txt_box, pos_y_of_txt_box, width, height, color_passive, color_active, font, user_text=''):
        self.rect = pygame.Rect(pos_x_of_txt_box, pos_y_of_txt_box, width, height)
        self.color_passive = color_passive
        self.color_active = color_active
        self.color = color = pygame.Color('blue')  # Border color of the txt box
        self.font = pygame.font.Font(None, 32)
        self.user_text = user_text
        self.txt_surface = font.render(user_text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_passive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.user_text)
                    self.user_text = ''
                    self.active = False
                    self.color = self.color_passive

                elif event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                    print("im in backspace now")

                else:
                    self.user_text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.user_text, True, self.color)

    def update(self):
        # If the user text, is bigger than the textbox resize it, looks kind of ugly but haven't
        # found any better way to do it. (here C# and VB.net is the kings still..)
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, surface):
        # Blit the text to screen
        surface.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect to screen
        pygame.draw.rect(surface, self.color, self.rect, 2)
