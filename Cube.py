import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from Config import *
from Utils import *

class Cube:
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def check_intersection(self, another_cube):
        x, y, z = self.position
        x1, y1, z1 = another_cube.position
        l = self.size

        if (x < x1 + l and x + l > x1 and
            y < y1 + l and y + l > y1 and
            z < z1 + l and z + l > z1):
            return True
        else:
            return False

    def render(self, texture_id):
        x, y, z = self.position

        vertices = [
            (x, y, z),
            (x + self.size, y, z),
            (x + self.size, y, z + self.size),
            (x, y, z + self.size),

            (x, y + self.size, z),
            (x + self.size, y + self.size, z),
            (x + self.size, y + self.size, z + self.size),
            (x, y + self.size, z + self.size)
        ]

        faces = [
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 1, 5, 4),
            (1, 5, 6, 2),
            (2, 6, 7, 3),
            (3, 7, 4, 0)
        ]

        glBegin(GL_QUADS)
        x = 0
        for face in faces:
            for vertex in face:
                # random_color = random.randrange(0, len(colors))
                # glColor3fv(colors[random_color])
                #glColor3fv(colors[vertex])
                #glVertex3fv(vertices[vertex])

                print(text[x])
                glColor3fv((1, 1, 1))
                glTexCoord2f(text[x][0], text[x][1])
                glVertex3fv(vertices[vertex])
                x += 1
        glEnd()

def load_texture(file_name):
    texture_surface = pygame.image.load(file_name)
    texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    glEnable(GL_TEXTURE_2D)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    return texture_id

def Ground():
    glBegin(GL_QUADS)

    x = 0
    for vertex in ground_vertices:
        x += 1
        glColor3fv((0, 1, 1))
        glVertex3fv(vertex)

    glEnd()

cubes = []
current_position = -SIZE_CUBE
while len(cubes) < NUM_CUBES:
    x_value_change = random.randrange(PLAYER_TRACK_LEFT_LIMIT, PLAYER_TRACK_RIGHT_LIMIT)
    y_value_change = 0
    z_value_change = current_position
    current_position -= TRACK_STEP_OBSTACLE

    #position = (x_value_change, y_value_change, z_value_change)
    position = (x_value_change, 0, z_value_change)
    size = SIZE_CUBE
    new_cube = Cube(position, size)

    intersect = False
    for cube in cubes:
        if new_cube.check_intersection(cube):
            intersect = True
            break

    if not intersect:
        cubes.append(new_cube)


def sum_tuples(t1, t2):
    return tuple(map(lambda x, y: x + y, t1, t2))


def main():
    pygame.init()
    display = (WIDTH, HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    camera_current_move = MOVE_ORIGIN
    camera_current_position = (0, -5, 0)
    gluPerspective(78, (display[0] / display[1]), 0.1, 150.0)
    glTranslatef(*camera_current_position)

    cube_texture = load_texture("image/crate.png")

    x_move = 0
    y_move = 0

    object_passed = False

    while not object_passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            time_last_pressed = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:

                    camera_current_move_tmp = sum_tuples(CAMERA_VELOCITY, MOVE_LEFT)
                    camera_current_position_tmp = sum_tuples(camera_current_position, camera_current_move_tmp)

                    print(f"{PLAYER_TRACK_LEFT_LIMIT} - {camera_current_position_tmp[0]} - 0")
                    if PLAYER_TRACK_LEFT_LIMIT <= camera_current_position_tmp[0]:
                        camera_current_position = camera_current_position_tmp
                        camera_current_move = camera_current_move_tmp
                if event.key == pygame.K_RIGHT:
                    camera_current_move_tmp = sum_tuples(CAMERA_VELOCITY, MOVE_RIGHT)
                    camera_current_position_tmp = sum_tuples(camera_current_position, camera_current_move_tmp)

                    print(f"0 - {camera_current_position_tmp[0]} - {PLAYER_TRACK_LEFT_LIMIT}")
                    if camera_current_position_tmp[0] <= PLAYER_TRACK_RIGHT_LIMIT:
                        camera_current_position = camera_current_position_tmp
                        camera_current_move = camera_current_move_tmp

                if event.key == pygame.K_DOWN:
                    camera_current_move = sum_tuples(CAMERA_VELOCITY, MOVE_DOWN)
                if event.key == pygame.K_UP:
                    camera_current_move = sum_tuples(CAMERA_VELOCITY, MOVE_UP)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    camera_current_move = sum_tuples(MOVE_ORIGIN, CAMERA_VELOCITY)
                if event.key == pygame.K_RIGHT:
                    camera_current_move = sum_tuples(MOVE_ORIGIN, CAMERA_VELOCITY)
                if event.key == pygame.K_DOWN:
                    camera_current_move = sum_tuples(MOVE_ORIGIN, CAMERA_VELOCITY)
                if event.key == pygame.K_UP:
                    camera_current_move = sum_tuples(MOVE_ORIGIN, CAMERA_VELOCITY)

        glTranslatef(*camera_current_move)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Ground()
        draw_world_axes()
        for cube in cubes:

            cube.render(cube_texture)
        pygame.display.flip()


main()