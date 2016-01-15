from tkinter import *
from ga import *

class ChangeStartPane:
	def __init__(self,mmap,callback):
		self.callback = callback
		self.mmap = mmap;
		self.top = Toplevel();
		self.top.title('Change Start city');
		f = Frame(self.top, width=200, height=480, padx=20, pady=20);
		f.pack();
		self.listbox = Listbox(f);

		for item in self.mmap.cityList:
			self.listbox.insert(END,item.name);
		self.listbox.grid(row=0,column=0,sticky=W+E);

		self.addButton = Button(f, text="Change", command=self.handleRemoval);
		self.addButton.grid(row=1,column=0,pady=10,sticky=W+E);

	def handleRemoval(self):
		inx = self.listbox.curselection()[0];
		self.mmap.start = inx;
		self.callback();
		self.listbox.delete(0,END);
		self.top.destroy();


