import pygame
import random
import math

pygame.init()

# Dimensions
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Shark Game')

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
SEABLUE = (0, 122, 165)
GRAY = (169, 169, 169)
DARK_GRAY = (105, 105, 105)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)

# ---------------------------
# Initialize global variables
Score = 0
Lives = 3

# List to store regular fish and poison fish positions
fish_positions = []
poisonfish_positions = []
shark_x = 100
shark_y = 100

# Score and Lives Display Font
font = pygame.font.SysFont("RussoOne", 30)

# Function to draw a regular fish
def fish(x, y):
    pygame.draw.ellipse(screen, LIGHT_BLUE, (x, y, 50, 25))
    tail_points = [(x, y + 12), (x - 15, y), (x - 15, y + 25)]
    pygame.draw.polygon(screen, ORANGE, tail_points)
    pygame.draw.circle(screen, BLACK, (x + 35, y + 7), 3)
    pygame.draw.arc(screen, BLACK, (x + 27, y + 15, 10, 5), 3.14, 0, 3)

# Function to draw a poison fish
def poison_fish(x, y):
    pygame.draw.ellipse(screen, RED, (x, y, 50, 25))  # Poison fish is red
    tail_points = [(x, y + 12), (x - 15, y), (x - 15, y + 25)]
    pygame.draw.polygon(screen, ORANGE, tail_points)  # Orange tail
    pygame.draw.circle(screen, BLACK, (x + 35, y + 7), 3)  # Black eye
    pygame.draw.arc(screen, BLACK, (x + 27, y + 15, 10, 5), 3.14, 0, 3)  # Fish mouth

# Function to generate a new random position for a fish, avoiding the shark's initial position
def generate_new_fish(avoid_shark=True):
    safe_zone = 150 
    while True:
        x = random.randint(20, WIDTH - 100)
        y = random.randint(20, HEIGHT - 50)

        # If the fish is too close to the shark's initial position, try again
        if avoid_shark and (abs(x - shark_x) < safe_zone and abs(y - shark_y) < safe_zone):
            continue
        
        return (x, y)

# Generate Random Positions for regular fish and poison fish
for i in range(4):  # Regular fish
    fish_positions.append(generate_new_fish())

for i in range(2):  # 2 poison fish
    poisonfish_positions.append(generate_new_fish(avoid_shark=True))

# ---------------------------
# Function to display the game over screen
def game_over_screen():
    font = pygame.font.SysFont("RussoOne", 50)
    message = "You Lost! Press C to Play Again or Q to Quit"
    text_surface = font.render(message, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()

# Function to reset the game
def reset_game():
    global shark_x, shark_y, Score, Lives, fish_positions, poisonfish_positions
    shark_x = 100
    shark_y = 100
    Score = 0
    Lives = 3  
    fish_positions = []
    poisonfish_positions = []

    # Generate random positions for regular fish and poison fish
    for i in range(4):
        fish_positions.append(generate_new_fish())

    for i in range(2):
        poisonfish_positions.append(generate_new_fish(avoid_shark=True))

# ---------------------------
# Main game loop
def game_loop():
    global shark_x, shark_y, Score, Lives, fish_positions, poisonfish_positions
    running = True
    game_over = False

    # Shark speed and direction
    shark_speed = 10
    x1_change = shark_speed
    y1_change = 0

    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x1_change = -shark_speed
            y1_change = 0
        if keys[pygame.K_RIGHT]:
            x1_change = shark_speed
            y1_change = 0
        if keys[pygame.K_UP]:
            y1_change = -shark_speed
            x1_change = 0
        if keys[pygame.K_DOWN]:
            y1_change = shark_speed
            x1_change = 0

        # Update shark position
        shark_x += x1_change
        shark_y += y1_change

        # Shark eating fish
        for fish_x, fish_y in fish_positions[:]:
            distance = math.sqrt((shark_x - fish_x) ** 2 + (shark_y - fish_y) ** 2)
            if distance < 200:  # Collision with regular fish
                Score += 10
                fish_positions.remove((fish_x, fish_y))  # Remove fish
                shark_speed += 1
                fish_positions.append(generate_new_fish())  # Add a new fish in a random position
                break  

        # Shark eats a poison fish
        for poison_x, poison_y in poisonfish_positions[:]:
            distance = math.sqrt((shark_x - poison_x) ** 2 + (shark_y - poison_y) ** 2)
            if distance < 100:  # Collision with poison fish
                poisonfish_positions.remove((poison_x, poison_y))  # Remove poison fish
                Lives -= 1
                poisonfish_positions.append(generate_new_fish(avoid_shark=True))  # Add a new poison fish in a random position
                break
            
        # End the game if all lives are lost
        if Lives == 0:
            game_over = True

        # End the game if the shark hits the border
        if shark_x < 0 or shark_x + 200 > WIDTH or shark_y < 0 or shark_y + 70 > HEIGHT:
            game_over = True  

        # Update Score and Lives display
        score_text = f"Score: {Score}  Lives: {Lives}"
        text_surface = font.render(score_text, True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 30))

        # DRAWING
        screen.fill(SEABLUE)

        # Load the shark image
        shark = pygame.image.load("miku_image")
        shark = pygame.transform.scale(shark, (200, 70))
        screen.blit(shark, (shark_x, shark_y))

        # Draw Fish
        for pos in fish_positions:
            fish(pos[0], pos[1])

        # Draw poison fish
        for pos in poisonfish_positions:
            poison_fish(pos[0], pos[1])

        # Display the score and lives
        screen.blit(text_surface, text_rect)

        # Game over display
        if game_over:
            game_over_screen()
            shark_speed = 10
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                running = False  # Quit the game if Q is pressed
            if keys[pygame.K_c]:
                reset_game()  # Reset the game if C is pressed
                game_over = False  

        # Update the display
        pygame.display.flip()
        clock.tick(15)

    pygame.quit()

# Start the game loop
game_loop()