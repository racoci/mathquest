import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Input Position Test")

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

    # Get the keyboard input
    keys = pygame.key.get_pressed()
    key_x = keys[pygame.K_LEFT] - keys[pygame.K_RIGHT]
    key_y = keys[pygame.K_UP] - keys[pygame.K_DOWN]

    # Fill the window with a color (e.g., white)
    window.fill((255, 255, 255))

    # Render the mouse position text
    mouse_text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (0, 0, 0))
    window.blit(mouse_text, (10, 10))

    # Render the keyboard position text
    keyboard_text = font.render(f"Keyboard Position: ({key_x}, {key_y})", True, (0, 0, 0))
    window.blit(keyboard_text, (10, 40))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
