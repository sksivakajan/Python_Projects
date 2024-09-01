import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MUTTAYA PUDIdaa..")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock for controlling FPS
clock = pygame.time.Clock()

# Load dragon image
dragon_img = pygame.image.load('img.png')
dragon_img = pygame.transform.scale(dragon_img, (100, 100))  # Scale the image

# Dragon class
class Dragon:
    def __init__(self):
        self.image = dragon_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # Keep the dragon on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Prey class
class Prey:
    def __init__(self):
        self.size = 20
        self.rect = pygame.Rect(random.randint(0, WIDTH - self.size), random.randint(0, HEIGHT - self.size), self.size, self.size)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, WIDTH - self.size)
        self.rect.y = random.randint(0, HEIGHT - self.size)

# Main game function
def game():
    dragon = Dragon()
    prey = Prey()
    score = 0
    time_left = 30  # 30 seconds game time
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dragon movement
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1

        dragon.move(dx, dy)

        # Check for collision with prey
        if dragon.rect.colliderect(prey.rect):
            score += 1
            prey.respawn()

        # Draw everything
        dragon.draw(screen)
        prey.draw(screen)

        # Update time
        time_left -= 1 / 60  # 1 second per 60 frames
        if time_left <= 0:
            running = False  # End the game when time is up

        # Display score and time
        score_text = font.render(f"Score: {score}", True, BLUE)
        time_text = font.render(f"Time left: {int(time_left)}", True, BLUE)
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))

        # Update the screen
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    # Game over screen
    screen.fill(WHITE)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, RED)
    screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # Show the final score for 3 seconds

    pygame.quit()

# Run the game
if __name__ == "__main__":
    game()
