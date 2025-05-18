import pygame, csv, os

class Tile(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

SCALE = 2

class Spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()
    def get_sprite(self, x, y, width, height, scale=1):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        if scale != 1:
            sprite = pygame.transform.scale(sprite, (width * scale, height * scale))
        return sprite

class TileMap():
    def __init__(self, filename, spritesheet):
        self.tile_size = 16
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            reader = csv.reader(data, delimiter=',')
            for row in reader:
                map.append(row)
        return map

    def load_tiles(self, filename):
        tiles = []
        map_data = self.read_csv(filename)
        tile_size = self.tile_size
        tiles_per_row = self.spritesheet.sheet.get_width() // tile_size

        y = 0
        for row in map_data:
            x = 0
            for tile_id in row:
                tile_id = tile_id.strip()
                if tile_id.isdigit() and tile_id != '-1':  # ignore empty/invalid tiles
                    tile_id = int(tile_id)
                    tile_x = (tile_id % tiles_per_row) * tile_size
                    tile_y = (tile_id // tiles_per_row) * tile_size
                    sprite = self.spritesheet.get_sprite(tile_x, tile_y, tile_size, tile_size, scale=SCALE)
                    tiles.append(Tile(sprite, x * tile_size * SCALE, y * tile_size * SCALE))
                x += 1
            y += 1

        self.map_w, self.map_h = x * tile_size * SCALE, y * tile_size * SCALE
        return tiles
