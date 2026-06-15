import pygame
import random

pygame.init()


WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 120
car_speed = 7

enemy_width = 50
enemy_height = 100
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100
enemy_speed = 6

score = 0
font = pygame.font.SysFont(None, 40)

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        car_x -= car_speed

    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    if car_x < 0:
        car_x = 0

    if car_x > WIDTH - car_width:
        car_x = WIDTH - car_width

    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)
        score += 1

    if (car_x < enemy_x + enemy_width and
        car_x + car_width > enemy_x and
        car_y < enemy_y + enemy_height and
        car_y + car_height > enemy_y):

        print("Game Over! Score:", score)
        running = False

    screen.fill(BLACK)

    pygame.draw.rect(screen, BLUE,
                     (car_x, car_y, car_width, car_height))

    pygame.draw.rect(screen, RED,
                     (enemy_x, enemy_y,
                      enemy_width, enemy_height))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()