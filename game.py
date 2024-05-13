import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

# Define player class
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 5  # Adjust speed as needed
        self.health = 100  # Initial health

    def move(self, direction):
        if direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed
        elif direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed

        # Implement boundary checking to prevent going off-screen
        self.x = max(0, self.x)  # Don't go off left side
        self.x = min(WIDTH - 32, self.x)  # Don't go off right side (assuming player is 32x32 pixels)
        self.y = max(0, self.y)  # Don't go off top
        self.y = min(HEIGHT - 32, self.y)  # Don't go off bottom

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 32, 32))  # Draw a green square for the player
        # Draw health bar
        pygame.draw.rect(screen, RED, (self.x, self.y - 5, 32, 5))  # Red health bar behind player
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 5, int(self.health * 0.32), 5))  # Green health bar based on health

# Define a simple map (replace with your own level design)
def draw_map():
    # Here i would define obstacles, walls, etc. using rectangles or other shapes
    pygame.draw.rect(screen, BLACK, (100, 100, 200, 200))  # Example obstacle

# Create player object
player = Player()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle key presses for movement (**customizable controls**)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: 
                player.move("up")
            if event.key == pygame.K_s:
                player.move("down")
            if event.key == pygame.K_a: 
                player.move("left")
            if event.key == pygame.K_d: 
                player.move("right")

    # Clear the screen
    screen.fill(WHITE)

    # Draw the map
    draw_map()

    # Draw the player with health bar
    player.draw()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()