from ga import *

from tkinter import *
from mapview import *
from menuview import *
from newcitypane import *
from rmcitypane import *
from changestartpane import *

root = Tk()
root.title('Genetic TSP');
root.config(width=840);
root.resizable(width=FALSE, height=FALSE);

mp = MapView(root);

mmap= Map();

mn = MenuFrame(root);

def runEvent():
	if(len(mmap.cityList)<2):
		return;
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

def redrawHelper(mmap):
	mp.redrawCities(mmap);
	showNewStart();
	root.update();

mn.setRunCallback(runEvent);

def newCityEvent():
	NewCityPane(mmap,redrawHelper);

mn.setAddCallback(newCityEvent);

def rmCityEvent():
	RemoveCityPane(mmap,redrawHelper);

mn.setRmCallback(rmCityEvent);

def loadExamplesEvent():
	mp.clear();
	mmap.start = 0;
	mmap.cityList = [];
	mmap.addCity(City(50,20,"Dummy 1"));
	mmap.addCity(City(100,0,"Dummy 2"));
	mmap.addCity(City(80,50,"Dummy 3"));
	mmap.addCity(City(90,5,"Dummy 4"));
	mmap.addCity(City(120,100,"Dummy 5"));
	mmap.addCity(City(50,80,"Dummy 6"));
	mmap.addCity(City(75,120,"Dummy 7"));
	mmap.addCity(City(130, 43,"Dummy 8"));
	mmap.addCity(City(65, 90,"Dummy 9"));
	mmap.addCity(City(5, 133,"Dummy 10"));
	mmap.addCity(City(65, 29,"Dummy 11"));           
	mmap.addCity(City(30, 90,"Dummy 12"));
	mmap.addCity(City(70, 150,"Dummy 13"));
	mp.drawCities(mmap);
	showNewStart();

mn.setLoadExCallback(loadExamplesEvent);

def showNewStart():
	if(len(mmap.cityList)>0):
		label = mmap.cityList[mmap.start].name;
	else:
		label = '(no cities)';
	mn.updateStartLabel(label);

def changeStartEvent():
	ChangeStartPane(mmap,showNewStart);

mn.setChangeStartCallback(changeStartEvent);


root.mainloop();
