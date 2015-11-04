from ga import *

from tkinter import *
from mapview import *
from menuview import *
from newcitypane import *
from rmcitypane import *

root = Tk()
root.title('Genetic TSP');
root.config(width=840);
root.resizable(width=FALSE, height=FALSE);

mp = MapView(root);

mmap= Map();

mn = MenuFrame(root);

def runEvent():
	mn.runButton.config(text='Running',state=DISABLED);
	root.update();
	p = Population(int(mn.popEntry.get()), mmap);
	p.mutationRatio = float(mn.mutEntry.get());
	p.elitismRatio = float(mn.elitismEntry.get());
	p.crossoverParentRatio = float(mn.crossoverEntry.get());
	p.runGA(int(mn.itEntry.get()));
	mn.runButton.config(text='Run!',state=NORMAL);
	best = p.getBestIndividual();
	mp.redrawCities(mmap);
	mp.drawPath(best[1]);
	mn.updateResultLabel('  '+str(round(best[0],2)));


mn.setRunCallback(runEvent);

def newCityEvent():
	NewCityPane(mmap,mp.redrawCities);

mn.setAddCallback(newCityEvent);

def rmCityEvent():
	RemoveCityPane(mmap,mp.redrawCities);

mn.setRmCallback(rmCityEvent);

def loadExamplesEvent():
	mp.clear();
	mmap.cityList = [];
	mmap.addCity(City(50,20,"Cidade1"));
	mmap.addCity(City(100,0,"Cidade2"));
	mmap.addCity(City(80,50,"Cidade3"));
	mmap.addCity(City(90,5,"Cidade4"));
	mmap.addCity(City(120,100,"Cidade5"));
	mmap.addCity(City(50,80,"Cidade6"));
	mmap.addCity(City(75,120,"Cidade7"));
	mmap.addCity(City(130, 43,"Cidade8"));
	mmap.addCity(City(65, 80,"Cidade9"));
	mmap.addCity(City(5, 133,"Cidade10"));
	mmap.addCity(City(65, 29,"Cidade11"));           
	mmap.addCity(City(30, 90,"Cidade12"));
	mmap.addCity(City(70, 150,"Cidade13"));
	mp.drawCities(mmap);

mn.setLoadExCallback(loadExamplesEvent);

root.mainloop();
