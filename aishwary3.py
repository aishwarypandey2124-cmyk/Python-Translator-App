import pygame
import random

pygame.init()

# Screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font = pygame.font.SysFont(None, 30)

def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [width/6, height/3])

def gameLoop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length = 1

    foodx = random.randint(0, (width - snake_block) // 10) * 10
    foody = random.randint(0, (height - snake_block) // 10) * 10

    while not game_over:

        while game_close:
            screen.fill(black)
            message("Game Over! Q=Quit or C=Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        x += x_change
        y += y_change

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(black)

        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(screen, green, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = random.randint(0, (width - snake_block) // 10) * 10
            foody = random.randint(0, (height - snake_block) // 10) * 10
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()