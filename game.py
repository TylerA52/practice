import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

dudeMonster = pygame.image.load('Dude_Monster.png').convert()
dudeMonster = pygame.transform.scale(dudeMonster, (dudeMonster.get_width() * 3, dudeMonster.get_height() * 3))

player_pos = [30, 30]
player_speed = 10

x = 0

running = True

clock = pygame.time.Clock()

font = pygame.font.Font(None, size=30)

while running:
    clock.tick(60)
    screen.fill((255, 255, 255))

    hitbox = pygame.Rect(x, 30, dudeMonster.get_width(), dudeMonster.get_height())
    target = pygame.Rect(300, 0, 160, 280)

    collision = hitbox.colliderect(target)
    pygame.draw.rect(screen, (255 * collision, 255, 0), target)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos[1] -= player_speed
    if keys[pygame.K_a]:
        player_pos[0] -= player_speed
    if keys[pygame.K_s]:
        player_pos[1] += player_speed
    if keys[pygame.K_d]:
        player_pos[0] += player_speed

    screen.blit(dudeMonster, player_pos)
    pygame.display.flip()

pygame.quit()



