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

# Resultados experimentales 

## Medium Corners 

||BFS|DFS|A\*|Algoritmo Genetico|
|-|-:|-:|-:|-:|
|Nodos expandidos|1921|371|||
|Costo de solucion|106|221|||

## Big Corners 

||BFS|DFS|A\*|Algoritmo Genetico|
|-|-:|-:|-:|-:|
|Nodos expandidos|7862|504|||
|Costo de solucion|162|302|||

Fuente: http://ai.berkeley.edu/search.html