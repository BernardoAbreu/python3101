import math
import random
import itertools

class City:
    def __init__(self, x, y, name):
        self.x = x;
        self.y = y;
        self.name = name;
        
    def getX(self):
        return self.x;
        
    def getY(self):
        return self.y
        
    def getName(self):
        return self.name;
        
class Map:
    def __init__(self):
        self.cityList = [];
        
    def addCity(self, city):
        self.cityList.append(city);
        
    def size(self):
        return len(self.cityList);
        
    def getDistance(self, city1, city2):
        return math.sqrt((city1.x - city2.x)**2 + (city1.y - city2.y)**2);
        
    def getDistanceFromInx(self, inx1, inx2):
        return self.getDistance(self.cityList[inx1],self.cityList[inx2]);

class Population:
    mutationRatio = 0.2;
    elitismRatio = 0.4; # how many inidividuals kept for the next generation (sorted from best to worst)
    crossoverParentRatio = 0.8; # how many individuals to use for crossover (sorted from best to worst)
    
    def __init__(self, size, cMap):
        self.size = size;
        self.cMap = cMap;
        self.pop = [];
        self.bestIndividual = [];
        self.evaluation = [];
        self.pop.insert(0, []);
        for i in range(size):
            l = list(range(cMap.size()));
            random.shuffle(l);
            self.pop[0].append( l[:] );
        
    def evaluate(self):
        self.evaluation.insert(len(self.pop)-1,0);
        self.lastEvals = [];
        for path in self.pop[-1]:
            distance = 0;
            for i in range(self.cMap.size()-1):
                distance += self.cMap.getDistanceFromInx(path[i],path[i+1]);
            if len(self.pop) > len(self.bestIndividual):
                self.bestIndividual.insert(len(self.pop)-1,[distance, path][:]);                    
            elif distance < self.bestIndividual[-1][0]:
                self.bestIndividual[-1] = [distance, path][:];
            self.lastEvals.append([path, distance]);
            self.evaluation[-1] += distance;
            
    def crossoverFromPrevPop(self):
        parent1 = self.nextGenParents[int(random.random() * len(self.nextGenParents))][:];
        parent2 = self.nextGenParents[int(random.random() * len(self.nextGenParents))][:];
        child = [-1]*self.cMap.size();
        
        begin = int(random.random() * self.cMap.size()-1);
        end = int(random.random() * self.cMap.size()-1);
        if begin>end:
            begin,end = end,begin;
        for i in range(begin,end+1):
            child[i] = parent1[i];
            parent2.remove(parent1[i]);
        for i in range(begin):
            child[i] = parent2.pop(0);
        for i in range(end+1,self.cMap.size()):
            child[i] = parent2.pop(0);        
            
        return child[:];

    def mutateLastAdded(self):
        for i in range(self.cMap.size()):
            if random.random() < self.mutationRatio:
                inx1 = int(random.random() * self.cMap.size()-1);
                inx2 = int(random.random() * self.cMap.size()-1);
                self.pop[-1][-1][inx1],self.pop[-1][-1][inx2] = self.pop[-1][-1][inx2],self.pop[-1][-1][inx1];
            
    def evolve(self):
        self.pop.append([]);
        self.sortedLastGen = [elem[0] for elem in sorted(self.lastEvals,key=lambda d:d[1])];
        parentsNo = int(self.crossoverParentRatio*self.size);
        self.nextGenParents = self.sortedLastGen[:parentsNo];
        elitistsNo = int(self.elitismRatio*self.size);
        if elitistsNo > 0:
            elitists = self.sortedLastGen[:elitistsNo];
            self.pop[-1].extend(elitists);
        for i in range(elitistsNo, self.size):
            self.pop[-1].append(self.crossoverFromPrevPop());
            self.mutateLastAdded();
            
    def discardLastPop(self):
        self.pop.pop(len(self.pop)-1);
        self.bestIndividual.pop(len(self.bestIndividual)-1);
        self.evaluation.pop(len(self.evaluation)-1);
            
            
        
mmap=Map();
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
mmap.addCity(City(65, 29,"Cidade11"));           
mmap.addCity(City(30, 90,"Cidade12"));
mmap.addCity(City(70, 150,"Cidade13"));

import time
if False:
    tbegin = time.clock();
    best = [50000,0];
    perm = list(itertools.permutations(range(mmap.size())));
    print(len(perm));
    for path in perm:
        distance = 0;
        for i in range(mmap.size()-1):
            distance += mmap.getDistanceFromInx(path[i],path[i+1]);                  
        if distance < best[0]:
            best = [distance, path][:];
            
    print(best);
    print(time.clock()-tbegin); 
    print('GAA');   
                                                       

tbegin = time.clock();        
p = Population(200, mmap);
p.evaluate();
##print(p.bestIndividual[-1]);


for i in range(2000):
    p.evolve();
    p.evaluate();
    
    #if len(p.pop) > 50 and p.bestIndividual[-1][0] == p.bestIndividual[-50][0]:
        #print('stopped at iteration'+str(i));
        #break;
        
    if False and len(p.pop) > 1:
        if p.bestIndividual[-1][0] > p.bestIndividual[-2][0]:
            p.discardLastPop();
        elif p.bestIndividual[-1][0] == p.bestIndividual[-2][0] and p.evaluation[-1] > p.evaluation[-2]:
            p.discardLastPop();
#    else:
#        print(p.bestIndividual[-1]);
        
    if p.bestIndividual[-1] == best:
        break;
print(p.bestIndividual[-1]);
    
print(time.clock()-tbegin);        
