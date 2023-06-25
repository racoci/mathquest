import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pygame Test")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with a color (e.g., white)
    window.fill((255, 255, 255))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
