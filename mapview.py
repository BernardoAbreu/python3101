from tkinter import *

class MapView:
	def __init__(self,master):
		self.canvas = Canvas(master, width=640, height=480);
		self.canvas.grid(row=0,column=0);

		self.canvas.create_line(0, 0, 640, 480)

	def drawCities(self,mmap):
		for c in mmap.cityList:
			self.canvas.create_oval(c.x-2,c.y-2,c.x+2,c.y+2);

	