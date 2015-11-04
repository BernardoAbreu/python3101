from tkinter import *
from ga import *

# def inlineTextField(parent,label,entryWidth,row,column):
# 	f = Frame(parent);
# 	f.grid(row=row,column=column);
# 	if(row==0):
# 		f.grid(columnspan=2);
# 	Label(f, text=label).pack(anchor=W,side=LEFT);
# 	v=StringVar();
# 	entry = Entry(f,width=entryWidth,textvariable=v);
# 	entry.pack(anchor=W,side=LEFT);
# 	return v;

class RemoveCityPane:
	def __init__(self,mmap,redrawCallback):
		self.callback = redrawCallback
		self.mmap = mmap;
		self.top = Toplevel();
		self.top.title('Remove city');
		f = Frame(self.top, width=200, height=480, padx=20, pady=20);
		f.pack();
		# self.name = inlineTextField(f,'Name:',20,0,0);
		self.listbox = Listbox(f);

		for item in self.mmap.cityList:
			self.listbox.insert(END,item.name);
		self.listbox.grid(row=0,column=0,sticky=W+E);

		# self.x = inlineTextField(f,'X:',5,1,0);
		# self.y = inlineTextField(f,'Y:',5,1,1);
		self.addButton = Button(f, text="Delete", command=self.handleRemoval);
		# self.runButton.pack(anchor=N,side=TOP,fill=X,pady=15);
		self.addButton.grid(row=1,column=0,pady=10,sticky=W+E);
		# f.grid(row=0,column=1,sticky=N+S,padx=20,pady=20);

	def handleRemoval(self):
		inx = self.listbox.curselection()[0];
		self.mmap.cityList.pop(inx);
		self.callback(self.mmap);
		self.listbox.delete(0,END);
		self.top.destroy();


