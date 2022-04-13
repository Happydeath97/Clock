import pygame
from datetime import datetime
import math
import os

POINT_SIZE = [15, 15]
MID = [300, 300]
R = 170
# ANGLES = [x for x in range(360)]

BACKGROUND = pygame.image.load(os.path.join('graphics', 'background.png'))
CIRCLES = pygame.image.load(os.path.join('graphics', 'circles.png'))
TEXT = pygame.image.load(os.path.join('graphics', 'clock_text.png'))
H_POINT = pygame.transform.scale(pygame.image.load(os.path.join('graphics', 'H_POINT.png')),
                                 (POINT_SIZE[0], POINT_SIZE[1]))
M_POINT = pygame.transform.scale(pygame.image.load(os.path.join('graphics', 'M_POINT.png')),
                                 (POINT_SIZE[0], POINT_SIZE[1]))
S_POINT = pygame.transform.scale(pygame.image.load(os.path.join('graphics', 'S_POINT.png')),
                                 (POINT_SIZE[0], POINT_SIZE[1]))
C_12 = pygame.image.load(os.path.join('graphics', '12.png'))
C_3 = pygame.image.load(os.path.join('graphics', '3.png'))
C_6 = pygame.image.load(os.path.join('graphics', '6.png'))
C_9 = pygame.image.load(os.path.join('graphics', '9.png'))


def rotation_x(sc, r):
    if sc * 6 <= 180:
        y = sc * 6
        x = r * math.sin(math.radians(y))
        z = (x - 1)
        return z
    else:
        y = sc * 6
        x = r * math.sin(math.radians(y))
        z = (x + 1)
        return z


def rotation_y(sc, r):
    if sc * 6 <= 180:
        y = sc * 6
        x = r * math.cos(math.radians(y))
        z = (x + 1) * (-1)
        return z
    else:
        y = sc * 6
        x = r * math.cos(math.radians(y))
        z = (x - 1) * (-1)
        return z


def draw(sc, mn, hr):
    window = pygame.display.set_mode((600, 600))
    window.fill((255, 255, 255))
    window.blit(BACKGROUND, (0, 0))
    window.blit(CIRCLES, (0, 0))
    window.blit(C_12, (300 - 56 // 2, (300 - 230) - 35 // 2))
    window.blit(C_3, ((300 + 230) - 56 // 2, 300 - 35 // 2))
    window.blit(C_6, (300 - 56 // 2, (300 + 230) - 35 // 2))
    window.blit(C_9, ((300 - 230) - 56 // 2, 300 - 35 // 2))

    second = pygame.Rect(((rotation_x(sc, R)) + MID[0]) - (POINT_SIZE[0] // 2),
                         (rotation_y(sc, R) + MID[1]) - (POINT_SIZE[1] // 2),
                         POINT_SIZE[0], POINT_SIZE[1])

    minute = pygame.Rect(((rotation_x(mn, (R + 15))) + MID[0]) - (POINT_SIZE[0] // 2),
                         (rotation_y(mn, (R + 15)) + MID[1]) - (POINT_SIZE[1] // 2),
                         POINT_SIZE[0], POINT_SIZE[1])

    hour = pygame.Rect(((rotation_x((hr * 5), (R + 30))) + MID[0]) - (POINT_SIZE[0] // 2),
                       (rotation_y((hr * 5), (R + 30)) + MID[1]) - (POINT_SIZE[1] // 2),
                       POINT_SIZE[0], POINT_SIZE[1])

    window.blit(S_POINT, (second.x, second.y))
    window.blit(M_POINT, (minute.x, minute.y))
    window.blit(H_POINT, (hour.x, hour.y))

    pygame.draw.line(window, (144, 202, 249), (300, 300),
                     (second.x + (POINT_SIZE[0] // 2), second.y + (POINT_SIZE[1] // 2)), 3)
    pygame.draw.line(window, (61, 90, 254), (300, 300),
                     (minute.x + (POINT_SIZE[0] // 2), minute.y + (POINT_SIZE[1] // 2)), 3)
    pygame.draw.line(window, (26, 35, 126), (300, 300),
                     (hour.x + (POINT_SIZE[0] // 2), hour.y + (POINT_SIZE[1] // 2)), 3)

    window.blit(TEXT, (0, 0))

    pygame.display.update()

def main():
    run = True
    while run:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        now = datetime.now()
        hr = int(now.strftime("%H"))
        mn = int(now.strftime("%M"))
        sc = int(now.strftime("%S"))
        if hr > 12:
            hr -= 12

        draw(sc, mn, hr)


if __name__ == "__main__":
    main()
