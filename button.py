import pygame


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # Method to draw the button to the screen
    def draw_button_to_screen(self, surface1):
        action = False

        # Look for mouse pos
        pos = pygame.mouse.get_pos()

        # Check for mouse over and the clicked coordinate conditions
        if self.rect.collidepoint(pos):

            button = pygame.mouse.get_pressed()  # Button 0 = left mousebutton , 1 = clicked
            if button[0] == 1:
                if not self.clicked:
                    self.clicked = True
                    action = True

            if button[0] == 0:
                if self.clicked:
                    self.clicked = False

        # Draw the button on the screen
        surface1.blit(self.image, (self.rect.x, self.rect.y))

        return action
