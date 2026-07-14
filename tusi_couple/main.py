import pygame, math

class Main():
    """A overall class to handel the program"""

    def __init__(self):

        pygame.init()

        self.clock = pygame.time.Clock()
        self.fps = 60

        #window dimensions
        self.window_width = 1200
        self.window_height = 800

        #color
        self.window_color = '#8B5E3C'
        self.primary_color = '#B8860B'
        self.secondary_color = '#8B5E3C'
        self.dot_color = '#C0C0C0'

        #circle 1
        self.circle_radius = (self.window_height // 2) - 100
        self.circle_x_pos = self.window_width // 2
        self.circle_y_pos = self.window_height // 2

        #circle extras
        self.angle = 0 #in degree
        self.rot_angle = 100

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Tusi Couple")

    def draw_circle(self):
        """draw the extra circles"""

        #big circle calculation
        angle = math.radians(self.angle)
        x_pos = 600 + (self.circle_radius / 2)* math.sin(angle)
        y_pos = 400 - ((self.circle_radius / 2)* math.cos(angle))

        #big circle draw
        pygame.draw.circle(self.window, self.secondary_color, (x_pos, y_pos), (self.circle_radius / 2), 3)

        dot_rad = 10
        height = (self.circle_radius / 2) - (dot_rad / 2)
        for i in range(8):
            dot_angle = math.radians(-self.angle + i * 45)
            dot_x_pos = x_pos + (height * math.sin(dot_angle))
            dot_y_pos = y_pos - (height * math.cos(dot_angle))
            pygame.draw.circle(self.window, self.dot_color, (dot_x_pos, dot_y_pos), dot_rad)

        pygame.display.update()

        time_pass = self.clock.tick(self.fps) / 1000 
        self.angle += self.rot_angle * time_pass

    def run(self):
        """run the program"""
        
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill(self.window_color)

            circle = pygame.draw.circle(self.window, self.primary_color, (self.circle_x_pos, self.circle_y_pos),
                                                         self.circle_radius, 2)
            
            pygame.display.flip()
            
            self.draw_circle()
            
        pygame.quit()

if __name__ == '__main__':
    TusiCouple = Main()
    TusiCouple.run()