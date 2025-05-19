from tiles import *

# Have to load in the spritesheet image

pygame.init()

screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
font = pygame.font.Font(None, size=30)

OVERWORLD = "overworld"
SHOP = "shop"

game_state = OVERWORLD

spritesheet = Spritesheet("basictiles.png")
overworld_map = TileMap('testmap.csv', spritesheet)
overworld_mapL2 = TileMap('testmapl2.csv', spritesheet)

def draw_overworld():
    overworld_map.draw_map(screen)
    overworld_mapL2.draw_map(screen)

def draw_shop():
    screen.fill((0, 0, 0))

dudeMonster = pygame.image.load('Dude_Monster.png').convert()
dudeMonster = pygame.transform.scale(dudeMonster, (dudeMonster.get_width() * 2, dudeMonster.get_height() * 2))

player_pos = [0, 0]
player_speed = 32

x = 0

running = True

pygame.key.set_repeat(300, 100)

while running:
    clock.tick(60)
    screen.fill ((0, 0, 0))

    if game_state == OVERWORLD:
        draw_overworld()
        screen.blit(dudeMonster, player_pos)
    elif game_state == SHOP:
        draw_shop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_pos[1] -= player_speed
            if event.key == pygame.K_a:
                player_pos[0] -= player_speed
            if event.key == pygame.K_s:
                player_pos[1] += player_speed
            if event.key == pygame.K_d:
                player_pos[0] += player_speed
            if event.key == pygame.K_l:
                # printing to console for testing
                print("Shop!")
                game_state = SHOP

    pygame.display.flip()

pygame.quit()



