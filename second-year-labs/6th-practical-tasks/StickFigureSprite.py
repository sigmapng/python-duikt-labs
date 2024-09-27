from CollisionCheck import CollisionCheck
from app import *


class StickFigureSprite(Sprite):
    def __init__(self, game):
        self.canvas = game.canvas

        Sprite.__init__(self, game)

        self.images_left = [
            PhotoImage(file="img/figure-L1.png"),
            PhotoImage(file="img/figure-L2.png"),
            PhotoImage(file="img/figure-L3.png")
        ]

        self.images_right = [
            PhotoImage(file="img/figure-R1.png"),
            PhotoImage(file="img/figure-R2.png"),
            PhotoImage(file="img/figure-R3.png")
        ]

        self.image = game.canvas.create_image(200, 370, image=self.images_left[0], anchor='nw')

        self.x = -2
        self.y = 2
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coordinates()

        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<KeyPress-Up>', self.jump)
        game.canvas.bind_all('<Escape>', self.on_escape)

    def on_escape(self, event=None):
        self.canvas.destroy()
        self.game.game_over = True
        self.game.stop()
        print("game over :(")

    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2

    def turn_right(self, evt):
        if self.y == 0:
            self.x = 2

    def jump(self, evt):
        if self.y == 0:
            self.y = -4
            self.jump_count = 0

    def animate(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.last_time > 0.1:
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1

        if self.x < 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_left[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_right[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_right[self.current_image])

    def coords(self):
        xy = self.game.canvas.coords(self.image)

        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]

        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30

        return self.coordinates

    def move(self):
        self.animate()

        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4

        if self.y > 0:
            self.jump_count -= 1

        co = self.coords()

        left = True
        right = True
        top = True
        bottom = True
        falling = True

        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False

        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False

        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right = False

        elif self.x < 0 and co.x1 < 0:
            self.x = 0
            left = False
        for sprite in self.game.sprites:
            if sprite == self:
                continue

            sprite_co = sprite.coords()

            if top and self.y < 0 and CollisionCheck.top_part_collide(co, sprite_co):
                self.y = -self.y
                top = False

            if bottom and self.y > 0 and CollisionCheck.bottom_part_collide(self.y, co, sprite_co):
                self.y = 0
                bottom = False
                top = False

            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and CollisionCheck.bottom_part_collide(
                    1, co,
                    sprite_co):
                falling = False

            if left and self.x < 0 and CollisionCheck.left_side_collide(co, sprite_co):
                self.x = 0
                left = False

                if sprite.endgame:
                    self.game.game_over = True
                    self.game.canvas.create_text(250, 250, text="you won :)", fill='pink')

            if right and self.x > 0 and CollisionCheck.right_side_collide(co, sprite_co):
                self.x = 0
                right = False

                if sprite.endgame:
                    self.game.game_over = True

        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
            self.y = 4

        self.game.canvas.move(self.image, self.x, self.y)

    def disappear(self):
        pass
