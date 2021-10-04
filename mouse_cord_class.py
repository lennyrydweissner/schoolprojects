import pygame


class MouseCords:
    def __init__(self, mx, my):
        self.mouse_x = mx
        self.mouse_y = my

    def hunt_cords(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def write_out_cords(self):
        print(f"Mouse X cords: {self.mouse_x} and Mouse Y cords: {self.mouse_y}")
