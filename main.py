import pygame as pg

pg.init()
screen = pg.display.set_mode((1000, 600))
#screen.set_at((50, 100), "green")

def display_ground():
    pg.draw.rect(screen, "green", pg.Rect(100, 100, 800, 400))
    pg.draw.rect(screen, "black", pg.Rect(480, 100, 10, 400))
    pg.draw.rect(screen, "white", pg.Rect(490, 100, 20, 400))
    pg.draw.rect(screen, "black", pg.Rect(510, 100, 10, 400))

    pg.draw.rect(screen, "red", pg.Rect(460, 200, 20, 200))
    pg.draw.rect(screen, "red", pg.Rect(440, 220, 20, 160))
    pg.draw.rect(screen, "red", pg.Rect(420, 240, 20, 120))
    pg.draw.rect(screen, "red", pg.Rect(400, 260, 20, 80))

    pg.draw.rect(screen, "black", pg.Rect(480, 270, 40, 10))
    pg.draw.rect(screen, "black", pg.Rect(480, 300, 40, 10))

    pg.draw.rect(screen, "white", pg.Rect(520, 200, 20, 200))
    pg.draw.rect(screen, "white", pg.Rect(540, 220, 20, 160))
    pg.draw.rect(screen, "white", pg.Rect(560, 240, 20, 120))
    pg.draw.rect(screen, "white", pg.Rect(580, 260, 20, 80))


def main():
    done = False
    display_ground()
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        pg.display.flip()

if __name__ == "__main__":
    main()