import pygame
import sys
import random
import os

# --- Initialization ---
pygame.init()
pygame.mixer.init() # Initialize the sound mixer

# --- Game Constants ---
# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
DARK_GREEN = (0, 100, 0)
RED = (200, 0, 0)
PURPLE = (128, 0, 128) # Color for the poison
GOLD = (255, 215, 0) # Color for high score text
GREY = (128, 128, 128) # Color for obstacles
BLUE = (0, 0, 255) # Color for start menu text

# Game speed
INITIAL_SPEED = 10

# High score file
HIGH_SCORE_FILE = "snake_highscore.txt"

# --- Game Setup ---
# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ultimate Python Snake')
clock = pygame.time.Clock()

# --- Load Sound Effects ---
# NOTE: Create a 'sounds' folder and place these .wav files inside it.
# You can find free sound effects on websites like freesound.org.
try:
    eat_sound = pygame.mixer.Sound(os.path.join('sounds', 'eat.wav'))
    game_over_sound = pygame.mixer.Sound(os.path.join('sounds', 'game_over.wav'))
except (pygame.error, FileNotFoundError): # MODIFIED: Catches FileNotFoundError as well
    print("Warning: Sound files not found. The game will run without sound.")
    eat_sound = None
    game_over_sound = None

# --- High Score Functions ---
def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, 'r') as f: return int(f.read())
        except ValueError: return 0
    return 0

def save_high_score(score):
    with open(HIGH_SCORE_FILE, 'w') as f: f.write(str(score))

# --- Drawing and UI Functions ---
def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (SCREEN_WIDTH, y))

def draw_snake(snake_segments):
    for i, segment in enumerate(snake_segments):
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def draw_food(food_position):
    pygame.draw.rect(screen, RED, pygame.Rect(food_position[0], food_position[1], GRID_SIZE, GRID_SIZE))

def draw_poison(poison_position):
    pygame.draw.rect(screen, PURPLE, pygame.Rect(poison_position[0], poison_position[1], GRID_SIZE, GRID_SIZE))

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREY, pygame.Rect(obstacle[0], obstacle[1], GRID_SIZE, GRID_SIZE))

def randomize_position(exclude_positions=[]):
    while True:
        position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                    random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
        if position not in exclude_positions:
            return position

def show_start_screen():
    screen.fill(BLACK)
    title_font = pygame.font.SysFont('Arial', 60)
    instr_font = pygame.font.SysFont('Arial', 30)

    title_text = title_font.render("SNAKE", True, GREEN)
    instr_text = instr_font.render("Press any key to start", True, WHITE)

    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(instr_text, (SCREEN_WIDTH // 2 - instr_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def show_game_over_screen(score, high_score):
    if game_over_sound: game_over_sound.play()
    screen.fill(BLACK)
    font = pygame.font.SysFont('Arial', 50)
    score_font = pygame.font.SysFont('Arial', 30)
    
    game_over_text = font.render("GAME OVER", True, RED)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 4))

    if score > high_score:
        new_high_score_text = score_font.render("New High Score!", True, GOLD)
        screen.blit(new_high_score_text, (SCREEN_WIDTH // 2 - new_high_score_text.get_width() // 2, SCREEN_HEIGHT // 3 + 20))

    score_text = score_font.render(f"Your Score: {score}", True, WHITE)
    high_score_text = score_font.render(f"High Score: {high_score}", True, WHITE)
    restart_text = score_font.render("Press 'R' to Restart or 'Q' to Quit", True, WHITE)

    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
    
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: pygame.quit(); sys.exit()
                if event.key == pygame.K_r: waiting = False

# --- Main Game Loop ---
def game_loop(high_score):
    # Game state variables
    snake_segments = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)
    obstacles = []
    
    all_positions = snake_segments + obstacles
    food_position = randomize_position(all_positions)
    poison_position = randomize_position(all_positions + [food_position])
    
    score = 0
    speed = INITIAL_SPEED
    paused = False
    
    running = True
    while running:
        # --- 1. Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: # Pause the game
                    paused = not paused
                if not paused:
                    if event.key == pygame.K_UP and direction != (0, GRID_SIZE): direction = (0, -GRID_SIZE)
                    elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE): direction = (0, -GRID_SIZE)
                    elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0): direction = (-GRID_SIZE, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0): direction = (GRID_SIZE, 0)

        if paused:
            # Draw a pause overlay and skip the rest of the game loop
            pause_font = pygame.font.SysFont('Arial', 50)
            pause_text = pause_font.render("PAUSED", True, BLUE)
            screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2 - pause_text.get_height() // 2))
            pygame.display.flip()
            clock.tick(5) # Tick slowly while paused
            continue

        # --- 2. Update Game State ---
        current_head = snake_segments[0]
        moved_head = (current_head[0] + direction[0], current_head[1] + direction[1])
        
        x, y = moved_head
        if x >= SCREEN_WIDTH: x = 0
        elif x < 0: x = SCREEN_WIDTH - GRID_SIZE
        if y >= SCREEN_HEIGHT: y = 0
        elif y < 0: y = SCREEN_HEIGHT - GRID_SIZE
        new_head = (x, y)

        if new_head in snake_segments or new_head in obstacles or new_head == poison_position:
            running = False
        
        snake_segments.insert(0, new_head)

        if new_head == food_position:
            if eat_sound: eat_sound.play()
            score += 1
            if score % 5 == 0 and score > 0:
                speed += 1
                # Add a new obstacle every 5 points
                new_obstacle = randomize_position(snake_segments + obstacles + [food_position, poison_position])
                obstacles.append(new_obstacle)
            
            all_positions = snake_segments + obstacles
            food_position = randomize_position(all_positions)
            poison_position = randomize_position(all_positions + [food_position])
        else:
            snake_segments.pop()

        # --- 3. Drawing ---
        screen.fill(BLACK)
        draw_grid()
        draw_obstacles(obstacles)
        draw_snake(snake_segments)
        draw_food(food_position)
        draw_poison(poison_position)
        
        score_font = pygame.font.SysFont('Arial', 24)
        score_text = score_font.render(f'Score: {score}', True, WHITE)
        high_score_text = score_font.render(f'High Score: {high_score}', True, GOLD)
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (SCREEN_WIDTH - high_score_text.get_width() - 10, 10))

        pygame.display.flip()
        clock.tick(speed)
    
    return score

# --- Game Execution ---
high_score = load_high_score()
while True:
    show_start_screen()
    final_score = game_loop(high_score)
    if final_score > high_score:
        high_score = final_score
        save_high_score(high_score)
    show_game_over_screen(final_score, high_score)

