## Comandos

### BFS
```sh
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

```sh
python pacman.py -l bigCorners -p SearchAgent -a fn=bfs,prob=CornersProblem -z 0.5
```
### DFS
```sh
python pacman.py -l mediumCorners -p SearchAgent -a fn=dfs,prob=CornersProblem
```

```sh
python pacman.py -l bigCorners -p SearchAgent -a fn=dfs,prob=CornersProblem -z 0.5
```

### A* (Manhattan Path Distance)
```sh
python pacman.py -l mediumCorners -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic -z 0.5
```

```sh
python pacman.py -l bigCorners -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic -z 0.5
```

### IDS (Profundidad iterativa)
```sh
python pacman.py -l tinyCorners -p SearchAgent -a fn=ite,prob=CornersProblem
```
```sh
python pacman.py -l mediumCorners -p SearchAgent -a fn=ite,prob=CornersProblem
```

```sh
python pacman.py -l bigCorners -p SearchAgent -a fn=ite,prob=CornersProblem -z 0.5
```

## Resultados experimentales 

### Medium Corners 

||BFS|DFS|A\*(MPD)|IDS|
|-|-:|-:|-:|-:|
|Nodos expandidos|1921|249|335|95383|
|Costo de solucion|106|221|106|136|

### Big Corners 

||BFS|DFS|A*(MPD)|IDS|
|-|-:|-:|-:|-:|
|Nodos expandidos|7862|504|358|472008|
|Costo de solucion|162|302|162|276|

Fuente: http://ai.berkeley.edu/search.html
