import pygame
from pygame import locals


class RewrittenTextbox:
    # Adding my constructor
    def __init__(self, textbox_pos_x, textbox_pos_y, textbox_width, textbox_height, color_passive, color_active
                 , base_font, surface1, active, user_text=''):

        pushed_return_key = True
        first_state = 0
        self.input_rect = pygame.Rect(textbox_pos_x, textbox_pos_y, textbox_width, textbox_height)
        self.color_passive = color_passive
        self.color_active = color_active
        self.color = pygame.Color('grey')
        self.user_text = user_text
        self.base_font = base_font
        self.surface = surface1
        self.active = active
        self.written_word = self.user_text
        self.pushed_return_key = pushed_return_key
        self.first_state = first_state

    def catch_user_events(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.pushed_return_key:
                if self.first_state == 0:
                    self.pushed_return_key = False
            else:
                self.pushed_return_key = False
                self.first_state = 1

                if self.input_rect.collidepoint(event.pos):
                    self.active = True
                    self.color = pygame.Color("blue")
                else:
                    self.active = False
                    self.color = pygame.Color("grey")

        if event.type == pygame.KEYDOWN:
            if self.pushed_return_key:
                pass
            else:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    self.user_text = self.user_text[:-1]
                else:
                    self.user_text += event.unicode

                if event.key == pygame.K_RETURN:
                    print(self.user_text)
                    self.written_word = self.user_text
                    self.user_text = ''
                    self.active = False
                    self.color = self.color = pygame.Color("grey")
                    self.pushed_return_key = True

    def what_user_wrote(self):
        self.written_word = self.written_word.strip()
        return self.written_word

    def clear_written_word(self):
        self.written_word = ""
        return self.written_word

    def update(self):
        if self.active:
            color = self.color_active
        else:
            color = self.color_passive

        self.input_rect = pygame.draw.rect(self.surface, self.color, self.input_rect)

        text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))

        self.surface.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

        self.input_rect.w = max(200, text_surface.get_width() + 10)

    def draw(self):
        self.input_rect = pygame.draw.rect(self.surface, self.color, self.input_rect)

    def reset_mouseclick(self):
        self.pushed_return_key = False

