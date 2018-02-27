from tkinter import Canvas
from tkinter import Tk
import random
import time

class Ball:
	def __init__(self, canvas, paddle, color):
		self.canvas = canvas
		self.paddle = paddle
		self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
		self.canvas.move(self.id, 245, 100)
		starts = [-3, -2,-1, 1, 2, 3]
		random.shuffle(starts)
		self.x = starts[0]
		self.y = -3
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()
		self.hit_bottom = False
	def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True
		return False
	def draw(self):
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <=0:
			self.y = 3
		if pos[3] >= self.canvas_height:
			self.hit_bottom - True
		if self.hit_paddle(pos) == True:
			self.y = -3
		if pos[0] <= 0:
			self.x = 3
		if pos[2] >= self.canvas_width:
			self.x = -3
class Paddle:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
		self.canvas.move(self.id, 200, 300 )
		self.x = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
		self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
		self.canvas.bind_all('<KeyRelease-Left>', self.stopmoving)
		self.canvas.bind_all('<KeyRelease-Right>', self.stopmoving)
	def draw(self):
		self.canvas.move(self.id, self.x, 0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = 0
		elif pos[2] >= self.canvas_width:
			self.x = 0
	def turn_left(self, evt):
		self.x = -2
	def turn_right(self, evt):
		self.x = 2
	def stopmoving(self, evt):
		self.x = 0
class OtherKeybinds:
	def __init__(self):
		self.canvas = canvas
		self.canvas.bind_all('r', self.reset)
		self.ballrelmovex = 0
		self.ballrelmovey = 0
		self.paddlerelmovex = 0
	def reset(self, evt):
		self.ballrelmovex = ball.x - 245
		self.ballrelmovey = ball.y - 100
		self.paddlerelmovex = paddle.x - 200
		ball.canvas.move(ball.id, self.ballrelmovex, self.ballrelmovey)
		starts = [-3, -2,-1, 1, 2, 3]
		random.shuffle(starts)
		ball.x = starts[0]
		ball.y = -3
		paddle.x = 0
		paddle.canvas.move(paddle.id, self.paddlerelmovex, 0)
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
	if ball.hit_bottom == False:
		ball.draw()
		paddle.draw()
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)