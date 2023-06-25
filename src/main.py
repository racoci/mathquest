import pygame
import pygame.freetype
import matplotlib.pyplot as plt
from io import BytesIO

# Initialize pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MathQuest Text Editor")

# Set up fonts
pygame.freetype.init()
font = pygame.freetype.SysFont("Arial", 24)

# Text editor variables
text = ""
cursor = "|"
cursor_visible = True
cursor_timer = 0

# Render matplotlib image
def render_equation(text):
    fig, ax = plt.subplots(figsize=(6, 1))
    ax.text(0, 0, text, fontsize=20)
    ax.axis('off')
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
    buffer.seek(0)
    return buffer

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]  # Remove last character
            elif event.key == pygame.K_RETURN:
                text += "\n"  # Add newline character
            else:
                text += event.unicode  # Add typed character

    # Clear the screen
    screen.fill((255, 255, 255))

    # Render text
    rendered_text, _ = font.render(text, (0, 0, 0))
    screen.blit(rendered_text, (20, 20))

    # Render cursor
    if cursor_visible:
        cursor_render, _ = font.render(cursor, (0, 0, 0))
        screen.blit(cursor_render, (20 + rendered_text.get_width(), 20))

    # Render matplotlib image
    equation_image = render_equation(text)
    equation_surface = pygame.image.load(equation_image)
    screen.blit(equation_surface, (20, 60))

    # Update cursor visibility
    cursor_timer += clock.get_time()
    if cursor_timer >= 500:  # Toggle cursor visibility every 500ms
        cursor_visible = not cursor_visible
        cursor_timer = 0

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
