from CollisionCheck import CollisionCheck
from app import *


class DoorSprite(Sprite):

    def __init__(self, game, door_img_closed, door_img_opened, x, y, width, height):
        Sprite.__init__(self, game)
        self.door_img_closed = door_img_closed
        self.door_img_opened = door_img_opened
        self.image = game.canvas.create_image(x, y,
                                              image=self.door_img_closed,
                                              anchor='nw')
        self.coordinates = Coordinates(x, y, x + (width / 2), y + height)
        self.endgame = True


"""
    def animate(self):
        # Метод для анімації дверей при потраплянні чоловічка
        if self.game.sf and CollisionCheck.bottom_part_collide(0, self.game.sf.coords(), self.coordinates):
            self.game.canvas.itemconfig(self.image, image=self.game.sf.images_left[0])

            # Зачекайте трошки
            sleep(1)

            # Приховати чоловічка
            self.game.canvas.itemconfig(self.game.sf.image, state='hidden')

            # Переключити зображення дверей на відкрите
            self.game.canvas.itemconfig(self.image, image=self.door_img_opened)

            # Зачекайте ще трошки
            sleep(1)

            # Показати чоловічка знову
            self.game.canvas.itemconfig(self.game.sf.image, state='normal')

            # Переключити зображення дверей на закрите
            self.game.canvas.itemconfig(self.image, image=self.door_img_closed)

            # Оновити координати дверей
            self.coordinates = Coordinates(self.x, self.y, self.x + (self.width / 2), self.y + self.height)
"""
