from tkinter import *
from ga import *

def inlineTextField(parent,label,entryWidth,row,column):
	f = Frame(parent);
	f.grid(row=row,column=column);
	if(row==0):
		f.grid(columnspan=2);
	Label(f, text=label).pack(anchor=W,side=LEFT);
	v=StringVar();
	entry = Entry(f,width=entryWidth,textvariable=v);
	entry.pack(anchor=W,side=LEFT);
	return v;

class NewCityPane:
	def __init__(self,mmap,redrawCallback):
		self.callback = redrawCallback
		self.mmap = mmap;
		self.top = Toplevel();
		self.top.title('New city');
		f = Frame(self.top, width=200, height=480, padx=20, pady=20);
		f.pack();
		self.name = inlineTextField(f,'Name:',20,0,0);
		self.x = inlineTextField(f,'X:',5,1,0);
		self.y = inlineTextField(f,'Y:',5,1,1);
		self.addButton = Button(f, text="Save", command=self.handleAddition);
		self.addButton.grid(row=2,columnspan=2,pady=10,sticky=W+E);

	def handleAddition(self):
		self.mmap.addCity(City(int(self.x.get()),int(self.y.get()),self.name.get()));
		self.callback(self.mmap);
		self.top.destroy();


