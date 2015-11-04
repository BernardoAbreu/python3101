from tkinter import *
from ga import *

class RemoveCityPane:
	def __init__(self,mmap,redrawCallback):
		self.callback = redrawCallback
		self.mmap = mmap;
		self.top = Toplevel();
		self.top.title('Remove city');
		f = Frame(self.top, width=200, height=480, padx=20, pady=20);
		f.pack();
		self.listbox = Listbox(f);

		for item in self.mmap.cityList:
			self.listbox.insert(END,item.name);
		self.listbox.grid(row=0,column=0,sticky=W+E);

		self.addButton = Button(f, text="Delete", command=self.handleRemoval);
		self.addButton.grid(row=1,column=0,pady=10,sticky=W+E);

	def handleRemoval(self):
		inx = self.listbox.curselection()[0];
		self.mmap.cityList.pop(inx);
		self.callback(self.mmap);
		self.listbox.delete(0,END);
		self.top.destroy();


