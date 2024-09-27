from app import *


class PlatformSprite(Sprite):
    def __init__(self, game, platform_img, x, y, width, height):
        Sprite.__init__(self, game)
        self.platform_img = platform_img
        self.image = game.canvas.create_image(x, y, image=self.platform_img,
                                              anchor='nw')
        self.coordinates = Coordinates(x, y, x + width, y + height)


class MovingPlatformSprite(PlatformSprite):
    def __init__(self, game, platform_img, x, y, width, height, speed):
        super().__init__(game, platform_img, x, y, width, height)
        self.speed = speed

    def move(self):
        self.coordinates.x1 += self.speed
        self.coordinates.x2 += self.speed

        if self.coordinates.x1 <= 0:
            self.speed = abs(self.speed)

        elif self.coordinates.x2 >= self.game.canvas_width:
            self.speed = -abs(self.speed)

        self.game.canvas.coords(self.image, self.coordinates.x1, self.coordinates.y1)
