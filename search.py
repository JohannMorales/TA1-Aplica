# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from sets import Set
import util
import random

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

class Node(object):
    def __init__(self, state=None, path_cost=0):
        self.state=state
        self.solution=[]
        self.cost=0

    def create_child(self, state, addSolution, addCost):
        child = Node(state=None, path_cost = 0)
        child.state = tuple(state)
        child.solution = list(self.solution)
        child.solution.append(addSolution)
        child.cost = self.cost + addCost
        return child

def childNode(parent, action):
    result = action[0]
    step = action[1]
    step_cost = action[2]
    
    child = Node()
    child.state = tuple(result)
    child.solution = list(parent.solution)
    child.solution.append(step)
    child.cost = parent.cost + step_cost

    return child
   
def depthFirstSearch(problem):
    node = Node(state=problem.getStartState(), path_cost=0)
    frontier=util.Stack()
    frontier.push(node)
    explored=set()

    while True:

        if frontier.isEmpty():
            return [] #failure 

        node = frontier.pop()
        
        if node.state in explored:
            continue
            
        if problem.isGoalState(node.state):
            return node.solution

        explored.add(node.state)

        for action in problem.getSuccessors(node.state):
            child = childNode(node, action)
            if not child.state in explored and not child.state in frontier.list:
                frontier.push(child)


def breadthFirstSearch(problem):
    node = Node(state=problem.getStartState(), path_cost=0)
    frontier=util.Queue()
    frontier.push(node)
    explored=set()
    
    while True:

        if frontier.isEmpty():
            return [] # failure

        node=frontier.pop()
        
        #Limpio a los repetidos en el frontier que no fueron limpiados abajo
        #debido a que Queue no tiene una funcion que permita validar que hay
        #un elemento en ella en O(1)
        if node.state in explored:
           continue

        explored.add(node.state)

        for action in problem.getSuccessors(node.state):
            child = childNode(node, action)

            if not child.state in explored:
                if problem.isGoalState(child.state):
                    return child.solution
                frontier.push(child)

def depthIterative(problem):
    node = Node(state=problem.getStartState(), path_cost=0)
    frontier=util.Stack()
    frontier.push(node)
    explored=set()
    num = 0
    while True:
        #if frontier.isEmpty() or (num > limit):
        if frontier.isEmpty():
			print "Si no hay solucion, la huelga continua :v"
			return [] #failure 

        node = frontier.pop()
        num = num - 1
        
        if node.state in explored:
            continue
            
        if problem.isGoalState(node.state):
            return node.solution

        explored.add(node.state)
        for action in problem.getSuccessors(node.state):
            child = childNode(node, action)
            if not child.state in explored and not child.state in frontier.list:
                frontier.push(child)
                num = num + 1
        print num

def iterativeDFS(problem):
	limite = 10000
	depthIterative(problem)
	print limite
	
	

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def obtenerCantTrue(lista):
    cont = 0
    for i in lista:
        if i == True:
            cont += 1
    return cont

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()#
    node = Node()
    node.state = problem.getStartState()
    frontier = []
    frontier.append((node.state,node.solution,node.cost))
    explored = set()
    cantTrue=0
    cantTrueAux=0
    while True:
        if len(frontier) == 0:
            print "No hay solucion"
            return []

        #Se escoge el nodo con el valor mas pequenio de distancia
        node.state = frontier[0][0]
        node.solution = frontier[0][1]
        node.cost = frontier[0][2]

        if problem.isGoalState(node.state):
            return node.solution

        del frontier[0]

        if node.state in explored:
            continue

        #Si no ha sido explorado entonces lo pone como explorado
        explored.add(node.state)

        #Insertamos a todos los hijos con su heuristica
        nodeChild=[]
        for action in problem.getSuccessors(node.state):
            child = childNode(node, action)
            if not child.state in explored:

                cantTrue=obtenerCantTrue(child.state[1])
                if cantTrue == (cantTrueAux + 1):
                    cantTrueAux += 1
                    nodeChild = []
                    #print("SE ENCONTRO UNA NUEVA ESQUINA")
                    #print(child.state[1])
                    #print(frontier)
                    frontier = []
                dManhattan=heuristic(child,problem)
                nodeChild.append((child.state,child.solution,child.cost,dManhattan+child.cost))
        if len(nodeChild) >0:
            #nodeChild=sorted(nodeChild, key=lambda dist:dist[3], reverse=False)
            frontier.extend(nodeChild)
            frontier=sorted(frontier, key=lambda dist:dist[3], reverse=False)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
dep = depthIterative
ite = iterativeDFS
