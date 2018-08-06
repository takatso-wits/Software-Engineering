import random
import time
import matplotlib.pyplot as plt
import timeit

class  Sort:

    def __init__(self, n, key):
        self.n = n
        self.key = key
        self.datastructure = []
        self.x = range(1, n+1, int(n*0.2))
        self.y = []
        self.z = []
        self.comparisons = 0
        self.swaps = 0

    def randomList(self):
        self.datastructure = list(range(self.n)) #random.sample(range(0, self.n), self.n) #[ random.randrange(0, self.n) for i in range(self.n) ]
        random.shuffle(self.datastructure)
        return

    def orderedList(self):
        self.datastructure = list(range(self.n))
        return

    def myorderedList(self):
        self.datastructure = list(range(self.n))
        return


    def swop(self, j, j_):
        hold = self.datastructure[j]
        self.datastructure[j] = self.datastructure[j_]
        self.datastructure[j_] = hold
        return

    def bubbleSort(self):
        for i in range(self.n, 0, -1):
            for j in range(0, i - 1):
                if (self.datastructure[j] > self.datastructure[j+1]):
                    self.swop(j, j+1)
                    self.swaps += 1
                self.comparisons += 1
        return

    def bubbleSortAgain(self):
        i = self.n
        sorting = True
        while (i >= 1 & sorting == True):
            swopped = False
            for j in range(0, i - 1):
                if (self.datastructure[j] > self.datastructure[j + 1]):
                    self.swop(j, j+1)
                    swopped = True
                self.comparisons += 1
            if (swopped == False):
                sorting = False
            else:
                i = i - 1
        return

    def test(self):
        self.n = 10
        self.randomList()
        print (self.datastructure)
        self.bubbleSort()
        print (self.datastructure)
        print (self.swaps)
        print (self.comparisons)
        return

    def noescape(self):
        self.y = []
        self.z = []
        #print self.x
        #return
        print self.x
        for n in self.x:
            #print n
            self.n = n
            self.randomList()
            self.swaps = 0
            self.comparisons = 0
            #print (self.datastructure)

            #self.key = self.datastructure[0]
            #self.bubbleSort()

            #self.y.append(timeit.timeit(lambda: self.bubbleSort()))
            self.bubbleSort()
            self.y.append(self.swaps)
            self.z.append(self.comparisons)
            #print(self.datastructure)
            #print(self.swaps)
        self.plotGraph(self.x, self.y, "b", "no escape - swop operation")
        self.plotGraph(self.x, self.z, "r", "no escape - key comparisons")
        return #self.plotGraph(self.x, self.z, "r")

    def escape(self):
        self.y = []
        self.z = []
        print self.x
        for n in self.x:
            self.n = n
            self.orderedList()
            self.comparisons = 0
            #print (self.datastructure)
            #self.y.append(timeit.timeit(lambda: self.bubbleSortAgain()))
            #print(self.datastructure)
            self.bubbleSortAgain()
            #self.y.append(self.swaps)
            self.z.append(self.comparisons)
            #print(self.swaps)
        self.plotGraph(self.x, self.z, "y", "escape - key comparisons")
        print self.z
        return #self.plotGraph(self.x, self.z, "y")




    def plotGraph(self, x, y, color, key):
        plt.plot(x, y, color, label=key)
        return

sort = Sort(5000, 12)
#sort.noescape()
sort.escape()

plt.legend(bbox_to_anchor=(0.05, 0.95), loc=2, borderaxespad=0.)
plt.ylabel('Operations')
plt.xlabel('Elements')
plt.show()
#n = 10
#print (range(2, n+1, int(n*0.2)))'''

#sort = Sort(10, 12)
#sort.test()
