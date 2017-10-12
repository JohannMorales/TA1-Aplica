
### VERSION 1: NORMAL 
def recursiveDLS(node, problem, depth):
    if problem.isGoalState(node.state):
        return node.solution
    elif depth == 0:
        return [1]
    else:
        cutoff_ocurred=False
        for action in problem.getSuccessors(node.state):
            child = childNode(node, action)

            result = recursiveDLS(child, problem, depth-1)
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
    return recursiveDLS(node, problem, depth)

def iterativeDFS(problem):
    depth=0
    while True:
        result = limitedDepthSearch(problem, depth)
        if result!= [1]:
            return result
        depth+=1



### VERSION 2: EXPLORED COMPARTIDO

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

### VERSION 3: EXPLORED NO COMPARTIDO

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
                copy = explored.copy()
                result = recursiveDLS(child, problem, depth-1, copy)
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
        
        
### VERSION 4: INICIALIZANDO DEPTH 

def ManhattanDistance(A, B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1])

def getUnvisited(cornersPosition, cornersState):
    result = set()
    i = 0
    for corner in cornersPosition:
        if cornersState[i] == False: result.add(corner)
        i += 1
    return result
    
def ManhattanPathDistance(pacmanPosition, cornersPosition, cornersState):
    value = 0
    current = pacmanPosition
    unvisitedCorners = getUnvisited(cornersPosition, cornersState)

    while True:
        if(len(unvisitedCorners) == 0): break
        min = 9999999
        for corner in unvisitedCorners:
            if(ManhattanDistance(current, corner) < min):
                min = ManhattanDistance(current, corner)
                minCorner = corner

        current = minCorner
        unvisitedCorners.remove(minCorner)
        value += min

    return value

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
                copy = explored.copy()
                result = recursiveDLS(child, problem, depth-1, copy)
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
    start = problem.getStartState()
    corners = problem.corners
    depth=ManhattanPathDistance(start[0], corners, start[1])
    while True:
        result = limitedDepthSearch(problem, depth)
        if result!= [1]:
            return result
        depth+=1

