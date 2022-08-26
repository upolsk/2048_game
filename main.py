from logics import *
import pygame
import sys


def draw_interface(score, delta = 0):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont("stxingkai", 70)
    font_score = pygame.font.SysFont("stxingkai", 48)
    font_delta = pygame.font.SysFont("stxingkai", 45)
    score_text = font_score.render("Score: ", True, RED)
    score_text_value = font_score.render(f"{score}", True, NAVY)

    screen.blit(score_text, (20, 35))
    screen.blit(score_text_value, (150, 35))
    if delta > 0:
        delta_value = font_delta.render(f"+{delta}", True, NAVY)
        screen.blit(delta_value, (150, 80))
    pretty_print(mas)
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))


mas = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

BLACK = (0, 0, 0)
GRAY = (130, 130, 130)
WHITE = (255, 255, 255)
LIME = (0, 255, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
AQUA = (0, 255, 255)
PURPLE = (128, 0, 128)
NAVY = (0, 0, 128)
MAROON = (128, 0, 0)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
GREEN = (0, 128, 0)
COLORS = {
    0: GRAY,
    2: WHITE,
    4: LIME,
    8: YELLOW,
    16: MAGENTA,
    32: AQUA,
    64: PURPLE,
    128: NAVY,
    256: MAROON,
    512: RED,
    1028: SILVER,
    2048: GREEN
}
score = 0
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)

mas[1][2] = 2
mas[3][0] = 4

print(get_empty_list(mas))
pretty_print(mas)

pygame.init()    #initializes all pygame modules
screen = pygame.display.set_mode((WIDTH, HEIGHT))  #setting screen size
pygame.display.set_caption("2048")

draw_interface(score)
pygame.display.update()

while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            delta = 0
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            elif event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta
            empty = get_empty_list(mas)  # get empty elements
            random.shuffle(empty)  # shuffle them
            random_num = empty.pop()  # random number is going to be the one which is going to be popped out
            x, y = get_index_from_number(random_num)  # shows empty element's indexes
            mas = insert_2_or_4(mas, x, y)  # inserts 2 or 4 into the massive
            print(f'We inserted element into: {random_num}')
            draw_interface(score, delta)
            pygame.display.update()


