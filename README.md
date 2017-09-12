# TA1-Aplica

## Clases adicionales necesarias

### Node 
Nodo del arbol de busqueda 

```python
class Node(object):
    def __init__(self):
        self.state=None
        self.solution=[]
        self.cost=0
```

## Entregables

### Estrategias de Busqueda 

#### Deep First Search
Busqueda en profundidad
```python
def depthFirstSearch(problem):
    node = Node()
    node.state=problem.getStartState()
    frontier=util.Stack()
    frontier.push(node)
    explored=Set([])
    while True:
        if frontier.isEmpty():
            return []
        node=frontier.pop()
        if problem.isGoalState(node.state):
            return node.solution
        explored.add(node.state)
        for action in problem.getSuccessors(node.state):
            child=Node()
            child.cost=node.cost + action[2]
            child.solution=list(node.solution)
            child.solution.append(action[1])
            child.state=action[0]
            if not (child.state) in explored:
                frontier.push(child)
```
#### Breadth First Search
Busqueda en amplitud
```python
def breadthFirstSearch(problem):
    node = Node()
    node.state=problem.getStartState()
    frontier=util.Queue()
    frontier.push(node)
    explored=Set([])
    while True:
        if frontier.isEmpty():
            return []
        node=frontier.pop()
        if problem.isGoalState(node.state):
            return node.solution
        explored.add(node.state)
        successors = problem.getSuccessors(node.state)
        random.shuffle(successors)
        for action in successors:
            child=Node()
            child.cost=node.cost + action[2]
            child.solution=list(node.solution)
            child.solution.append(action[1])
            child.state=action[0]
            if not (child.state) in explored:
                frontier.push(child)
```
Fuente: http://ai.berkeley.edu/search.html