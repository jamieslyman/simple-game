import random
import time
from tkinter import Canvas, Tk, messagebox


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.xmovecounter = 0
        self.ymovecounter = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos):
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        self.xmovecounter += self.x
        self.ymovecounter += self.y


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.xmovecounter = 0
        self.paddlemovespeed = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Left>', self.stopmoving)
        self.canvas.bind_all('<KeyRelease-Right>', self.stopmoving)
        if messagebox.askyesno("Difficulty", "Do you want Easy difficulty?"):
            self.paddlemovespeed = 4
        else:
            self.paddlemovespeed = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
        self.xmovecounter += self.x

    def turn_left(self, evt):
        self.x = -self.paddlemovespeed

    def turn_right(self, evt):
        self.x = self.paddlemovespeed

    def stopmoving(self, evt):
        self.x = 0


# noinspection PyUnusedLocal
class OtherKeybinds:
    def __init__(self):
        self.canvas = canvas
        self.canvas.bind_all('r', self.reset)
        self.ballrelmovex = 0
        self.ballrelmovey = 0
        self.paddlerelmovex = 0

    @staticmethod
    def reset(evt):
        paddle.xmovecounter *= -1
        paddle.canvas.move(paddle.id, paddle.xmovecounter, 0)
        paddle.xmovecounter = 0
        ball.xmovecounter *= -1
        ball.ymovecounter *= -1
        ball.canvas.move(ball.id, ball.xmovecounter, ball.ymovecounter)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        ball.x = starts[0]
        ball.y = -3
        ball.canvas.move(ball.id, ball.x, ball.y)
        ball.xmovecounter = starts[0]
        ball.ymovecounter = -3
        ball.hit_bottom = False


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
otherkeybinds = OtherKeybinds()
while True:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
