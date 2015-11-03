from tkinter import *

def textField(parent,label,entryWidth):
	f = Frame(parent);
	f.pack(anchor=N,side=TOP,fill=X);
	Label(f, text=label).pack(anchor=W,side=TOP);
	v=StringVar();
	entry = Entry(f,width=entryWidth,textvariable=v);
	entry.pack(anchor=W,side=TOP);
	return v;

class MenuFrame:
	def __init__(self,master):
		self.frame = Frame(master, width=300, height=480);
		self.frame.grid(row=0,column=1,sticky=N+S,padx=20,pady=20);
		self.exButton = Button(self.frame, text="Load example");
		self.exButton.pack(anchor=N,side=TOP,fill=X,pady=5);
		self.addButton = Button(self.frame, text="Add city");
		self.addButton.pack(anchor=N,side=TOP,fill=X,pady=5);
		self.rmButton = Button(self.frame, text="Remove city");
		self.rmButton.pack(anchor=N,side=TOP,fill=X,pady=5);
		Frame(self.frame,height=50).pack(side=TOP);
		self.popEntry = textField(self.frame,'Population Size:',5);
		self.popEntry.set(100);
		self.itEntry = textField(self.frame,'Iterations:',5);
		self.itEntry.set(1000);
		self.mutEntry = textField(self.frame,'Mutation Ratio:',5);
		self.mutEntry.set(0.2);
		self.elitismEntry = textField(self.frame,'Elitism Ratio:',5);
		self.elitismEntry.set(0.6);
		self.runButton = Button(self.frame, text="Run!");
		self.runButton.pack(anchor=N,side=TOP,fill=X,pady=15);

	def setRunCallback(self,callback):
		self.runButton.config(command=callback);

	def setAddCallback(self,callback):
		self.addButton.config(command=callback);

