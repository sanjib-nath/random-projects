from settings import *

class Main:

    def __init__(self):
        #baisc setup
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(("3D CUBE"))
        self.clock = pygame.time.Clock()
        self.running = True

        self.angle_x = self.angle_y = self.angle_z = 0

    def run(self):

        while self.running:

            self.clock.tick(FPS)

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.running = False

            #rotation_matrices
            rotation_x = np.array([[1, 0, 0],
                                 [0, cos(self.angle_x), -sin(self.angle_x)],
                                 [0, sin(self.angle_x), cos(self.angle_x)]])

            rotation_y = np.array([[cos(self.angle_y), 0, sin(self.angle_y)],
                                [0, 1, 0],
                                [-sin(self.angle_y), 0, cos(self.angle_y)]])

            rotation_z = np.array([[cos(self.angle_z), -sin(self.angle_z), 0],
                                 [sin(self.angle_z), cos(self.angle_z), 0],
                                 [0, 0, 1]])

            self.angle_x += 0.01
            self.angle_y += 0.01
            self.angle_z += 0.01

            #draw
            self.window.fill(COLORS['bg'])

            #points
            points = []
            for point in POINTS:
                rotate_x = np.dot(rotation_x, point)
                rotate_y = np.dot(rotation_y, rotate_x)
                rotate_z = np.dot(rotation_z, rotate_y)
                point_2d = np.dot(PROJECTION_MATRIX, rotate_z)

                x_pos = (point_2d[0][0] * SCALE) + WINDOW_WIDTH / 2
                y_pos = (point_2d[1][0] * SCALE) + WINDOW_HEIGHT / 2

                points.append((x_pos, y_pos))

                pygame.draw.circle(self.window, COLORS['vertices'], (x_pos, y_pos), VERTICES_RADIUS)

            for edge in EDGES:
                pygame.draw.line(self.window, COLORS['line'], points[edge[0]], points[edge[1]])

            #update
            pygame.display.update()


        pygame.quit()

if __name__ == '__main__':
    cube = Main()
    cube.run()
            