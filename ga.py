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
        self.start = 0;
        
    def addCity(self, city):
        self.cityList.append(city);
        
    def size(self):
        return len(self.cityList);
        
    def getDistance(self, city1, city2):
        return math.sqrt((city1.x - city2.x)**2 + (city1.y - city2.y)**2);
        
    def getDistanceFromInx(self, inx1, inx2):
        return self.getDistance(self.cityList[inx1],self.cityList[inx2]);

    def setStartCity(self,inx):
        self.start = inx;

    def clear(self):
        self.cityList = [];

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
            l = list(range(self.cMap.size()));
            l.remove(self.cMap.start);
            random.shuffle(l);
            l.insert(0,self.cMap.start);
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
        
        begin = random.randint(1,self.cMap.size()-1);
        end = random.randint(1,self.cMap.size()-1);
        
        if begin>end:
            begin,end = end,begin;
        child[0] = self.cMap.start;
        # print('begin ' + str(begin));
        # print('end ' + str(end));
        for i in range(begin,end+1):
            # print('par1' + str(parent1));
            # print('par2' + str(parent2));
            # print('chl' + str(child));
            child[i] = parent1[i];
            # print(parent1[i]);
            parent2.remove(parent1[i]);
        parent2.pop(0);
        for i in range(1,begin):
            child[i] = parent2.pop(0);
        for i in range(end+1,self.cMap.size()):
            child[i] = parent2.pop(0);
        
        # child.remove(self.start);
        # child.insert(0,self.start);

        return child[:];

    def mutateLastAdded(self):
        for i in range(self.cMap.size()-1):
            if random.random() < self.mutationRatio:
                inx1 = random.randint(1,self.cMap.size()-1);
                inx2 = random.randint(1,self.cMap.size()-1);
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

    def getBestIndividual(self):
        return self.bestIndividual[-1];

    def runGA(self,iterations):
        self.evaluate();
        for i in range(iterations):
            self.evolve();
            self.evaluate();
                
            if False and len(self.pop) > 1:
                if self.bestIndividual[-1][0] > self.bestIndividual[-2][0]:
                    self.discardLastPop();
                elif self.bestIndividual[-1][0] == self.bestIndividual[-2][0] and self.evaluation[-1] > self.evaluation[-2]:
                    self.discardLastPop();
            
            
        



# if False:
#     tbegin = time.clock();
#     best = [50000,0];
#     perm = list(itertools.permutations(range(mmap.size())));
#     print(len(perm));
#     for path in perm:
#         distance = 0;
#         for i in range(mmap.size()-1):
#             distance += mmap.getDistanceFromInx(path[i],path[i+1]);                  
#         if distance < best[0]:
#             best = [distance, path][:];
            
#     print(best);
#     print(time.clock()-tbegin); 
#     print('GAA');   
                                                       

      

##print(p.bestIndividual[-1]);




       
