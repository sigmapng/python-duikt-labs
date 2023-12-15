from tkinter import *

import time
from ball import Ball
from platform import Platform
from controls import Controls

tk = Tk()
tk.title("chipi chipi chapa chapa")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bg='#1A181B', highlightthickness=0)
canvas.pack()
tk.update()

platform = Platform(canvas, '#B20D30')
ball = Ball(canvas, platform, '#FFFFFF')


def on_escape(event=None):
    tk.destroy()
    print("game over,\nno more chipi chipi chapa chapa")


def start_game(event=None):
    while event_handler.is_active:
        if not ball.hit_bottom:
            ball.draw()
            platform.draw()
        else:
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
            break
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)


tk.bind_all('<Escape>', on_escape)
tk.bind("<Button-1>", start_game)
event_handler = Controls(tk)

tk.mainloop()
