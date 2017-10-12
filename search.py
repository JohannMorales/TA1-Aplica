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

######## TAREA ACADEMICA 1: APLICACIONES DE CIENCAS DE LA COMPUTACION ##########

class Node(object):
    def __init__(self, state=None, path_cost=0):
        self.state=state
        self.solution=[]
        self.cost=0

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
   
   
################ INICIO:  DEPTH FIRST SEARCH ################
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



################ INICIO:  BREADTH FIRST SEARCH ################
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


################ INICIO:  ITERATIVE DEPTH SEARCH ################

## Este codigo corresponde a la version que comparte la lista de explorados 
## entre todas las ramas recursivas ya que es el unico que se puede ejecutar
## para los mapas: tinyCorners, mediumCorners y bigCorners sin que se tarde 
## una cantidad de tiempo excesiva

## Si se desean probar las otras versiones, estan en el archivo:
## 		VersionesProfundidadIterativa.py
## Reemplazar el codigo de Iterative Depth Search (lineas 171 a 206) en este 
## archivo (search.py)  por el de la version que se desee probar.
## Se recomienda probar las demas versiones con tinyCorners
## tildes omitidas

def recursiveDLS(node, problem, depth, explored):
    if problem.isGoalState(node.state):
        return node.solution
    elif depth == 0:
        return [1]
    else:
        cutoff_ocurred=False
        explored.add(node.state)
        for action in problem.getSuccessors(node.state):
            child = childNode(node, action)
            if not(child.state in explored):
                result = recursiveDLS(child, problem, depth-1, explored)
                if result == [1]:
                    cutoff_ocurred = True
                elif result != [0]:
                    return result
        if cutoff_ocurred:
            return [1]
        else:
            return [0]

def limitedDepthSearch(problem, depth):
    node = Node(state=problem.getStartState(), path_cost=0)
    explored=set()
    return recursiveDLS(node, problem, depth, explored)

def iterativeDFS(problem):
    depth=0
    while True:
        result = limitedDepthSearch(problem, depth)
        #cutoff=[1]
        #failure=[0]
        if result!= [1]:
            return result
        depth+=1

        


################ INICIO: A* SEARCH ################

## Por defecto esta con la heuristica mas eficiente ManhattanPath, se puede 
## cambiar por la otra heuristica en SearchAgents.py
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
ite = iterativeDFS
