import time

from ga import *


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
mmap.setStartCity(7);
# mmap.addCity(City(65, 29,"Cidade11"));           
# mmap.addCity(City(30, 90,"Cidade12"));
# mmap.addCity(City(70, 150,"Cidade13"));

tbegin = time.clock();  

p = Population(200, mmap);
p.runGA(1000);

print(p.getBestIndividual());
    
print(time.clock()-tbegin); 