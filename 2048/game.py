import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
ROWS, COLS = 4, 4

FPS = 60

RECT_WIDTH = WIDTH // COLS
RECT_HEIGHT = HEIGHT // ROWS

COLOR = (187, 173, 160)
THICKNESS = 10
BACKGROUND_COLOR = (250, 248, 239)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont('arial', 60, bold=True)
MOVE_VEL = 10

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')


class Game:

    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, value, row, col) : 
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT
        
    def get_color(self) : 
        index = math.log2(self.value) - 1
        return self.COLORS[int(index)]
    
    def draw(self, window) : 
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            text,
            (
                self.x + RECT_WIDTH // 2 - text.get_width() // 2,
                self.y + RECT_HEIGHT // 2 - text.get_height() // 2,
            ),
        )

    def set_pos(self, ceil = False) : 
        if ceil :
            self.row = math.ceil(self.y / RECT_HEIGHT)
            self.col = math.ceil(self.x / RECT_WIDTH)
        else :
            self.row = math.floor(self.y / RECT_HEIGHT)
            self.col = math.floor(self.x / RECT_WIDTH)

    def move(self, delta) :
        self.x += delta[0]
        self.y += delta[1]


def draw_grid() :
    for row in range(1, ROWS) :
        y = row * RECT_HEIGHT
        pygame.draw.line(WINDOW, COLOR, (0, y), (WIDTH, y), THICKNESS)
    
    for col in range(1, COLS) :
        x = col * RECT_WIDTH
        pygame.draw.line(WINDOW, COLOR, (x, 0), (x, HEIGHT), THICKNESS)
    
    pygame.draw.rect(WINDOW, COLOR, (0, 0, WIDTH, HEIGHT), THICKNESS)


def draw(window, tiles) : 
    window.fill(BACKGROUND_COLOR)
    
    for tile in tiles.values() : 
        tile.draw(window)

    draw_grid()

    pygame.display.update()


def get_random_pos(tiles) : 
    row = None
    col = None

    while True : 
        row = random.randint(0, ROWS)
        col = random.randint(0, COLS)

        if f"{row}{col}" not in tiles : 
            break

    return row, col


def move_tiles(window, tiles, clock, direction) :
    updated = True
    blocks = set()

    if direction == "left" :
        sort_function = lambda x : x.col
        reverse = False
        delta = (-MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col - 1}")
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOVE_VEL
        )

        ceil = True

    elif direction == "right" :
        sort_function = lambda x : x.col
        reverse = True
        delta = (MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == COLS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col + 1}")
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x < next_tile.x - RECT_WIDTH - MOVE_VEL
        )

        ceil = False

    elif direction == "up" :
        sort_function = lambda x : x.row
        reverse = False
        delta = (0, -MOVE_VEL)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row - 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y > next_tile.y + RECT_HEIGHT + MOVE_VEL
        )

        ceil = True

    elif direction == "down" :
        sort_function = lambda x : x.row
        reverse = True
        delta = (0, MOVE_VEL)
        boundary_check = lambda tile: tile.row == ROWS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row + 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y < next_tile.y - RECT_HEIGHT - MOVE_VEL
        )

        ceil = False

    while updated :

        clock.tick(FPS)

        updated = False

        sorted_tiles = sorted(tiles.values(), key=sort_function, reverse=reverse)

        for i, tile in enumerate(sorted_tiles) : 
            if boundary_check(tile) :
                continue

            next_tile = get_next_tile(tile)
            if not next_tile :
                tile.move(delta)
            elif (tile.value == next_tile.value and tile not in blocks and next_tile not in blocks) :
                if merge_check(tile, next_tile) :
                    tile.move(delta)
                else :
                    tile.value *= 2
                    sorted_tiles.pop(i)
                    blocks.add(next_tile)
            elif move_check(tile, next_tile) :
                tile.move(delta)
            else :
                continue

            tile.set_pos(ceil)
            updated = True
        
        updated_tiles(window, tiles, sorted_tiles)

    return end_move(tiles)


def end_move(tiles) : 
    if len(tiles) == 16 :
        return "Lost"
    
    row, col = get_random_pos(tiles)
    tiles[f"{row}{col}"] = Game(random.choice([2, 4]), row, col)
    return "Continue"

def updated_tiles(window, tiles, sorted_tiles) : 
    tiles.clear()
    for tile in sorted_tiles : 
        tiles[f"{tile.row}{tile.col}"] = tile
    draw(window, tiles)

def generate_tiles() : 
    tiles = {}
    for _ in range(2) : 
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Game(2, row, col)
    return tiles

def main(window) :

    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()

    while run :
        clock.tick(FPS)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                break

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    result = move_tiles(WINDOW, tiles, clock, "left")
                if event.key == pygame.K_RIGHT :
                    result = move_tiles(WINDOW, tiles, clock, "right")
                if event.key == pygame.K_UP :
                    result = move_tiles(WINDOW, tiles, clock, "up")
                if event.key == pygame.K_DOWN :
                    result = move_tiles(WINDOW, tiles, clock, "down")

        draw(window, tiles)

    pygame.quit()

if __name__ == "__main__" : 
    main(WINDOW)
                