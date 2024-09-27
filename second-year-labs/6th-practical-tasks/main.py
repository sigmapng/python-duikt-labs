from app import *

g = Game()

canvas = g.canvas

platform_1 = PlatformSprite(g, PhotoImage(file="img/platform3.png"), 0, 460, 100, 10)
platform_2 = PlatformSprite(g, PhotoImage(file="img/platform1.png"), 250, 400, 100, 10)
platform_3 = PlatformSprite(g, PhotoImage(file="img/platform1.png "), 100, 340, 100, 10)
moving_platform_1 = MovingPlatformSprite(g, PhotoImage(file="img/platform2.png"), 0, 280, 100, 10, 3)
platform_5 = PlatformSprite(g, PhotoImage(file="img/platform1.png"), 250, 220, 100, 10)
platform_6 = PlatformSprite(g, PhotoImage(file="img/platform1.png"), 100, 160, 100, 10)
platform_7 = PlatformSprite(g, PhotoImage(file="img/platform1.png"), 0, 100, 100, 10)
moving_platform_2 = MovingPlatformSprite(g, PhotoImage(file="img/platform2.png"), 250, 40, 100, 10, 2)
platform_9 = PlatformSprite(g, PhotoImage(file="img/platform1.png"), 200, 280, 100, 10)
platform_10 = PlatformSprite(g, PhotoImage(file="img/platform1.png"), 230, 100, 100, 10)
platform_11 = PlatformSprite(g, PhotoImage(file="img/platform1.png"), 200, 460, 100, 10)
g.sprites.append(platform_1)
g.sprites.append(platform_2)
g.sprites.append(platform_3)
g.sprites.append(moving_platform_1)
g.sprites.append(platform_5)
g.sprites.append(platform_6)
g.sprites.append(platform_7)
g.sprites.append(moving_platform_2)
g.sprites.append(platform_9)
g.sprites.append(platform_10)
g.sprites.append(platform_11)

doorClosed = DoorSprite(g, PhotoImage(file="img/door1.png"), PhotoImage(file="img/door2.png"), 45, 40, 40, 35)

g.sprites.append(doorClosed)

sf = StickFigureSprite(g)

g.sprites.append(sf)

g.main_loop()

g.tk.main_loop()
