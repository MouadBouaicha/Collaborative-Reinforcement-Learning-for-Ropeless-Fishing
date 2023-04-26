import pygame

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image = pygame.image.load("boat.png")

# Set the initial rotation angle
angle = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle -= 5  # Rotate counter-clockwise
            elif event.key == pygame.K_RIGHT:
                angle += 5  # Rotate clockwise

    # Rotate the image
    rotated_image = pygame.transform.rotate(image, angle)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the rotated image
    screen.blit(rotated_image, (screen_width/2 - rotated_image.get_width()/2, screen_height/2 - rotated_image.get_height()/2))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
