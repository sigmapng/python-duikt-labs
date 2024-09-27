class Controls:

    def __init__(self, tk_instance):
        self.tk = tk_instance
        self.is_active = True
        self.tk.bind_all('<Escape>', self.on_escape)

    def on_escape(self, event=None):
        self.is_active = False
        self.tk.destroy()
        print("game over,\nno more chipi chipi chapa chapa")

    def on_click(self, event):
        self.is_active = True
