import pygame
import numpy as np
from math import sin, cos

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
FPS = 60
VERTICES_RADIUS = 5
SCALE = 100

COLORS = {'bg': '#000000',
          'vertices': "#C51515",
          'line': '#FFFFFF'}

POINTS = np.array([[[1], [1], [1]],
                    [[1], [1], [-1]],
                    [[1], [-1], [1]],
                    [[1], [-1], [-1]],
                    [[-1], [1], [1]],
                    [[-1], [1], [-1]],
                    [[-1], [-1], [1]],
                    [[-1], [-1], [-1]]])

EDGES = [
    (0,1), (0,2), (0,4),
    (1,3), (1,5),
    (2,3), (2,6),
    (3,7),
    (4,5), (4,6),
    (5,7),
    (6,7)
]


PROJECTION_MATRIX = np.array([[1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 0]])