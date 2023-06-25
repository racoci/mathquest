import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)  # Make the window resizable
pygame.display.set_caption("Theorem Prover")
# Set up the font
font = pygame.font.Font(None, 24)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:  # Handle window resize event
            window_width = event.w
            window_height = event.h
            window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Get the keyboard input
    key_x = 0
    key_y = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        key_x -= 1
    if keys[pygame.K_RIGHT]:
        key_x += 1
    if keys[pygame.K_UP]:
        key_y -= 1
    if keys[pygame.K_DOWN]:
        key_y += 1

    # Get the key being pressed
    key_name = ""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)

    # Fill the window with a color (e.g., white)
    window.fill((0, 0, 0))
    # Render the mouse position text
    mouse_text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (255, 0, 0))
    window.blit(mouse_text, (10, 10))

    # Render the keyboard position text
    keyboard_text = font.render(f"Keyboard Position: ({key_x}, {key_y})", True, (255, 0, 0))
    window.blit(keyboard_text, (10, 40))

    # Render the key being pressed text
    key_text = font.render(f"Key Pressed: {key_name}", True, (255, 0, 0))
    window.blit(key_text, (10, 100))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
