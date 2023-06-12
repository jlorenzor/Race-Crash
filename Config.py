# Configuraciones del juego
WIDTH = 1080
HEIGHT = 900

CAMERA_INITIAL_POSITION = (0, -5, 0)
CAMERA_VELOCITY = (0, 0, 0.2)

NUM_CUBES = 50
SIZE_CUBE = 6


KEY_PRESSED_TIME_LIMIT = 200
MOVE_ORIGIN = (0, 0, 0)
MOVE_LEFT = (SIZE_CUBE/2, 0, 0)
MOVE_RIGHT = (-SIZE_CUBE/2, 0, 0)
MOVE_DOWN = (0, SIZE_CUBE/2, 0)
MOVE_UP = (0, -SIZE_CUBE/2, 0)

# SIZE_CUBE + 2*SIZE_CUBE + SIZE_CUBE/2 + SIZE_CUBE/2 + 2*SIZE_CUBE + SIZE_CUBE/2 + SIZE_CUBE
TRACK_WIDTH_LIMIT = 8*SIZE_CUBE
TRACK_DEPTH_LIMIT = 200*SIZE_CUBE
TRACK_STEP_OBSTACLE = 3*SIZE_CUBE

PLAYER_TRACK_LEFT_LIMIT = -int(TRACK_WIDTH_LIMIT/2) + SIZE_CUBE/2
PLAYER_TRACK_RIGHT_LIMIT = int(TRACK_WIDTH_LIMIT/2) - 3*SIZE_CUBE/2

ground_vertices = (
    (-TRACK_WIDTH_LIMIT / 2, 0.0, TRACK_DEPTH_LIMIT),
    (-TRACK_WIDTH_LIMIT / 2, 0.0, -TRACK_DEPTH_LIMIT),
    (TRACK_WIDTH_LIMIT / 2, 0.0, TRACK_DEPTH_LIMIT),
    (TRACK_WIDTH_LIMIT / 2, 0.0, -TRACK_DEPTH_LIMIT)
)


vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)

ground_surfaces = (0, 1, 2, 3)

max_distance = 300

text = [
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0],
    [0.0, 0.0],
    [0.0, 1.0],
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [1.0, 1.0],
    [0.0, 1.0],
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [1.0, 0.0],
    [0.0, 1.0],
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [0.0, 0.0],
    [1.0, 1.0]
]