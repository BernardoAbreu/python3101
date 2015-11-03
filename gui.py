from ga import *

from tkinter import *
from mapview import *
from menuview import *
from newcitypane import *

root = Tk()
root.config(width=840);
root.resizable(width=FALSE, height=FALSE);

mp = MapView(root);

mmap= Map();
mmap.addCity(City(0,20,"Cidade1"));
mmap.addCity(City(100,0,"Cidade2"));
mmap.addCity(City(80,50,"Cidade3"));
mmap.addCity(City(90,5,"Cidade4"));
mmap.addCity(City(120,100,"Cidade5"));
mmap.addCity(City(50,80,"Cidade6"));
mmap.addCity(City(75,200,"Cidade7"));
mmap.addCity(City(175, 33,"Cidade8"));
mmap.addCity(City(65, 80,"Cidade9"));
mmap.addCity(City(5, 133,"Cidade10"));

mp.drawCities(mmap);

mn = MenuFrame(root);

def test():
	print('hello');
	mn.runButton.config(text='Running',state=DISABLED);

mn.setRunCallback(test);

def newCityEvent():
	print('event');
	NewCityPane(mmap,mp.redrawCities);

mn.setAddCallback(newCityEvent);

# NewCityPane(mmap);


# mp.drawPath([7,6,5,4,3,9,8,2,1,0]);


# f.pack(side=LEFT);
# w.grid(row=1);

root.mainloop();
