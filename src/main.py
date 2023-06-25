import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mouse Position Test")

# Set up the font
font = pygame.font.Font(None, 24)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Fill the window with a color (e.g., white)
    window.fill((255, 255, 255))

    # Render the mouse position text
    text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (0, 0, 0))
    window.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
