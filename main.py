from typing import Any
from functools import cmp_to_key
import copy

def union(lst1, lst2):
    return list(set(lst1) & set(lst2))

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def difference(lst1, lst2):
    return [x for x in lst1 if x not in lst2]

def compare(x, y):
    return x[0] - y[0]

def quadratic_function(arg):
    x = arg[1]
    arg = arg[0]
    return arg[0] * x*x + arg[1]*x + arg[2]

class LIFO():

    __list = []

    def __init__(self, elements) -> None:
      
      for el in elements:
          self.__list.append(el)

    
    def push(self, el):
        self.__list.append(el)

        return self.__list
    
    def pop(self):
        last = self.__list[-1]

        self.__list = self.__list[:-1]

        return last
    
    def empty(self):
        if len(self.__list) == 0:
            return True
        else: return False

    def length(self):
        return len(self.__list)

class FIFO():
    
    __list = []

    def __init__(self, elements) -> None:
      
      for el in elements:
          self.__list.append(el)

    
    def push(self, el):
        self.__list.append(el)

        return self.__list
    
    def pop(self):
        first = self.__list[0]

        self.__list = self.__list[1:]

        return first
    
    def empty(self):
        if len(self.__list) == 0:
            return True
        else: return False

    def length(self):
        return len(self.__list)

def create_square_matrix(n): 
 return [[0 for _ in range(n)] for _ in range(n)] 

class Graph():

    matrix = []
    
    vertNames = []
    namenum = {}
    numname = {}

    def __init__(self, matrix, vertNames):
        
        self.vertNames = copy.deepcopy(vertNames)
        self.matrix = copy.deepcopy(matrix)

        for i in range(len(self.matrix)):
            self.namenum[vertNames[i]] = i
            self.numname[i] = vertNames[i]

    def vertAmount(self):
        return len(self.matrix)
    
    def edgeAmount(self):
        
        ans = 0

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != 0:
                    ans += 1

        return ans

    def neighbors(self, vertName) -> list:

        vertNum = self.namenum[vertName]

        ans = []

        for i in range(self.vertAmount()):
            if self.matrix[vertNum][i] != 0:
                ans.append(self.numname[i])
        
        return ans

    def BFS(self, vertName):
        vertNum = self.namenum[vertName]

        stack = FIFO([vertNum])

        visited = [0] * self.vertAmount()
        visited[vertNum] = 1

        ans = [vertName]

        while(stack.empty() == False):
            now = stack.pop()

            for i in range(self.vertAmount()):

                if visited[i] == 0 and self.matrix[now][i] != 0:
                    stack.push(i)

                    visited[i] = 1
                    ans.append(self.numname[i])

        return ans
    
    def DFS(self, vertName):
        
        vertNum = self.namenum[vertName]

        queue = LIFO([vertNum])
        visited = [0] * self.vertAmount()
        visited[vertNum] = 1

        ans = []

        while(queue.empty() == False):
            now = queue.pop()
            ans.append(self.numname[now])
            for i in range(self.vertAmount()):
                if self.matrix[now][i] != 0 and visited[i] == 0:
                    queue.push(i)
                    visited[i] = 1
                    
        
        return ans
    
    def successors(self, vertName):
        vertNum = self.namenum[vertName]
        ans = []
        for i in range(self.vertAmount()):
            if self.matrix[vertNum][i] != 0:
                ans.append(self.numname[i])
        return ans

    def predecessors(self, vertName):
        vertNum = self.namenum[vertName]
        ans = []

        for i in range(self.vertAmount()):
            if self.matrix[i][vertNum] != 0:
                ans.append(self.numname[i])

        return ans

    def Kahn(self):
        
        ans = []

        g = copy.deepcopy(self)
        g.numname = copy.deepcopy(self.numname)

        while g.vertAmount() > 0:
            
            for vert in g.vertNames:
                if len(g.predecessors(vert)) == 0:
                    ans.append(vert)
                    g.remove_vert(vert)
                    break
        return ans

    def creat_edge(self, vertName_x, vertName_y, weight = 1):
        vertNum_x = self.namenum[vertName_x]
        vertNum_y = self.namenum[vertName_y]
        self.matrix[vertNum_x][vertNum_y] = weight
    
    def remove_edge(self, vertName_x, vertName_y):
        vertNum_x = self.namenum[vertName_x]
        vertNum_y = self.namenum[vertName_y]
        self.matrix[vertNum_x][vertNum_y] = 0   

    def create_vert(self, vertName):
        
        self.vertNames.append(vertName)

        self.namenum[vertName] = self.vertAmount()
        self.numname[self.vertAmount()] = vertName

        self.matrix.append([])
        for i in range(self.vertAmount()):
            self.matrix[-1].append(0)

        for i in range(self.vertAmount()):
            self.matrix[i].append(0)

    def remove_vert(self, vertName):
        vertNum = self.namenum[vertName]
        self.vertNames.remove(vertName)

        for i in range(vertNum, self.vertAmount() - 1):
            self.numname[i] = self.numname[i + 1] 
        
        self.numname.pop(self.vertAmount() - 1)
        self.namenum = dict(zip(self.numname.values(), self.numname.keys()))

        for i in range(self.vertAmount()):
            self.matrix[i] = self.matrix[i][:vertNum] + self.matrix[i][vertNum + 1:]
        self.matrix = self.matrix[:vertNum] + self.matrix[vertNum + 1:]
    
    #Maybe don't work
    def Lawlera(self, P, f, ABC):

        ans = []
        PSum = sum(P)

        g = copy.deepcopy(self)
        g.numname = copy.deepcopy(self.numname)
        g.namenum = copy.deepcopy(self.namenum)

        while g.vertAmount() > 0:
            
            succFree = []

            for vert in g.vertNames:
                if len(g.successors(vert)) == 0:
                    succFree.append(vert)
            succFreeABC = [ABC[succ - 1] for succ in succFree]

            fValues = list(map(f, list(zip(succFreeABC, [PSum] * len(ABC)))))
            minValue = min(fValues)
            minValueInd = fValues.index(minValue)
            nextVert = succFree[minValueInd]
            ans = [nextVert] + ans
            g.remove_vert(nextVert)
            PSum -= P[nextVert - 1]

        maxLoss = 0
        time = 0
        for i in range(len(ans) - 1):
            vertnum = ans[i] - 1
            time += P[vertnum]
            maxLoss = max(maxLoss, f((ABC[vertnum], time)))
        return maxLoss

            



    
