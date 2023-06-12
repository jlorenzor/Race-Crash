import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

pygame.init()

# Set the window size and create a Pygame display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

# Set up the OpenGL perspective
glViewport(0, 0, screen_width, screen_height)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (screen_width / screen_height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)

# Set the initial position and velocity of the sphere
sphere_x, sphere_y, sphere_z = 0.0, 0.0, -5.0
sphere_velocity = 0.1

# Set the number of spheres to be generated on collision
num_spheres = 10

# Generate a list to store the positions of the spheres
spheres = []

def generate_sphere_position():
    # Generate random positions for the spheres
    x = random.uniform(-3.0, 3.0)
    y = random.uniform(-3.0, 3.0)
    z = random.uniform(-10.0, -5.0)
    return x, y, z

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()

    # Handle input to move the sphere left or right
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        sphere_x -= 0.1
    if keys[K_RIGHT]:
        sphere_x += 0.1

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set the sphere position
    glLoadIdentity()
    glTranslatef(sphere_x, sphere_y, sphere_z)

    # Draw the sphere
    quadric = gluNewQuadric()
    gluSphere(quadric, 1.0, 32, 32)
    gluDeleteQuadric(quadric)

    # Check for collision
    if sphere_x < -2.0 or sphere_x > 2.0:
        # Generate new sphere positions on collision
        spheres = [generate_sphere_position() for _ in range(num_spheres)]

    # Draw the collision spheres
    for sphere_pos in spheres:
        glLoadIdentity()
        glTranslatef(sphere_pos[0], sphere_pos[1], sphere_pos[2])

        quadric = gluNewQuadric()
        gluSphere(quadric, 0.5, 16, 16)
        gluDeleteQuadric(quadric)

    # Update the sphere position
    sphere_x += sphere_velocity

    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)
# Wow its running