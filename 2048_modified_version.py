import pygame
import random
import copy

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 500
GRID_SIZE = 4
TILE_SIZE = 100
MARGIN = 5
FONT = pygame.font.SysFont("arial", 24)
FONT_GAME_OVER = pygame.font.SysFont("arial", 72)

# Colors
BACKGROUND_COLOR = (187, 173, 160)
EMPTY_TILE_COLOR = (205, 193, 180)
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}
TEXT_COLOR = (119, 110, 101)
WHITE = (255, 255, 255)

# Game variables
board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
score = 0
undo_stack = []

# Functions
def reset_board():
    global board, score, undo_stack
    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    score = 0
    undo_stack = []
    add_random_tile()
    add_random_tile()

def add_random_tile():
    empty_tiles = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if board[r][c] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        board[r][c] = 4 if random.random() < 0.1 else 2

def draw_board():
    screen.fill(BACKGROUND_COLOR)
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = board[r][c]
            color = TILE_COLORS.get(value, EMPTY_TILE_COLOR)
            pygame.draw.rect(screen, color, (c * (TILE_SIZE + MARGIN) + MARGIN, r * (TILE_SIZE + MARGIN) + MARGIN, TILE_SIZE, TILE_SIZE))
            if value != 0:
                text_surface = FONT.render(str(value), True, TEXT_COLOR)
                text_rect = text_surface.get_rect(center=(c * (TILE_SIZE + MARGIN) + MARGIN + TILE_SIZE / 2, r * (TILE_SIZE + MARGIN) + MARGIN + TILE_SIZE / 2))
                screen.blit(text_surface, text_rect)

    # Draw Score
    score_surface = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, HEIGHT - 50))

    # Draw buttons
    reset_surface = FONT.render("Restart", True, WHITE)
    reset_rect = reset_surface.get_rect(center=(WIDTH - 70, HEIGHT - 50))
    pygame.draw.rect(screen, (128, 128, 128), reset_rect.inflate(20, 10))
    screen.blit(reset_surface, reset_rect)

    undo_surface = FONT.render("Undo", True, WHITE)
    undo_rect = undo_surface.get_rect(center=(WIDTH - 200, HEIGHT - 50))
    pygame.draw.rect(screen, (128, 128, 128), undo_rect.inflate(20, 10))
    screen.blit(undo_surface, undo_rect)

def move_left():
    global score
    moved = False
    for r in range(GRID_SIZE):
        tiles = [tile for tile in board[r] if tile != 0]
        for i in range(len(tiles) - 1):
            if tiles[i] == tiles[i + 1]:
                tiles[i] *= 2
                score += tiles[i]
                tiles[i + 1] = 0
        tiles = [tile for tile in tiles if tile != 0]
        while len(tiles) < GRID_SIZE:
            tiles.append(0)
        if board[r] != tiles:
            moved = True
        board[r] = tiles
    return moved

def move_right():
    global score
    moved = False
    for r in range(GRID_SIZE):
        tiles = [tile for tile in board[r] if tile != 0]
        for i in range(len(tiles) - 1, 0, -1):
            if tiles[i] == tiles[i - 1]:
                tiles[i] *= 2
                score += tiles[i]
                tiles[i - 1] = 0
        tiles = [tile for tile in tiles if tile != 0]
        while len(tiles) < GRID_SIZE:
            tiles.insert(0, 0)
        if board[r] != tiles:
            moved = True
        board[r] = tiles
    return moved

def move_up():
    global score
    moved = False
    for c in range(GRID_SIZE):
        tiles = [board[r][c] for r in range(GRID_SIZE) if board[r][c] != 0]
        for i in range(len(tiles) - 1):
            if tiles[i] == tiles[i + 1]:
                tiles[i] *= 2
                score += tiles[i]
                tiles[i + 1] = 0
        tiles = [tile for tile in tiles if tile != 0]
        while len(tiles) < GRID_SIZE:
            tiles.append(0)
        if [board[r][c] for r in range(GRID_SIZE)] != tiles:
            moved = True
        for r in range(GRID_SIZE):
            board[r][c] = tiles[r]
    return moved

def move_down():
    global score
    moved = False
    for c in range(GRID_SIZE):
        tiles = [board[r][c] for r in range(GRID_SIZE) if board[r][c] != 0]
        for i in range(len(tiles) - 1, 0, -1):
            if tiles[i] == tiles[i - 1]:
                tiles[i] *= 2
                score += tiles[i]
                tiles[i - 1] = 0
        tiles = [tile for tile in tiles if tile != 0]
        while len(tiles) < GRID_SIZE:
            tiles.insert(0, 0)
        if [board[r][c] for r in range(GRID_SIZE)] != tiles:
            moved = True
        for r in range(GRID_SIZE):
            board[r][c] = tiles[r]
    return moved

def can_move():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c] == 0:
                return True
            if c < GRID_SIZE - 1 and board[r][c] == board[r][c + 1]:
                return True
            if r < GRID_SIZE - 1 and board[r][c] == board[r + 1][c]:
                return True
    return False

def undo():
    global board, score
    if undo_stack:
        board, score = undo_stack.pop()

# Main game loop
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My2048")

reset_board()

running = True
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                undo_stack.append((copy.deepcopy(board), score))
                if event.key == pygame.K_LEFT:
                    moved = move_left()
                elif event.key == pygame.K_RIGHT:
                    moved = move_right()
                elif event.key == pygame.K_UP:
                    moved = move_up()
                elif event.key == pygame.K_DOWN:
                    moved = move_down()
                if moved:
                    add_random_tile()
                if not can_move():
                    screen.fill(BACKGROUND_COLOR)
                    game_over_surface = FONT_GAME_OVER.render("Game Over!", True, WHITE)
                    game_over_rect = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                    screen.blit(game_over_surface, game_over_rect)
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    reset_board()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            reset_rect = pygame.Rect(WIDTH - 70 - 40, HEIGHT - 50 - 20, 80, 40)
            undo_rect = pygame.Rect(WIDTH - 200 - 40, HEIGHT - 50 - 20, 80, 40)
            if reset_rect.collidepoint(x, y):
                reset_board()
            elif undo_rect.collidepoint(x, y):
                undo()

pygame.quit()
