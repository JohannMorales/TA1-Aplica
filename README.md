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
    def __eq__(self, other):
        return self.state == other.state and self.parent == other.parent and self.cost == other.cost
```
Fuente: http://ai.berkeley.edu/search.html