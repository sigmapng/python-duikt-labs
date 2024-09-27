import datetime

from app import *


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Paranoid Android")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500,
                             height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500

        self.bg = PhotoImage(file='img/background.png')
        self.canvas.create_image(0, 0, image=self.bg, anchor='nw')
        self.sprites = []
        self.running = True
        self.game_over = False

    def stop(self):
        self.running = False

    def main_loop(self):
        while self.running:
            if not self.game_over:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)
