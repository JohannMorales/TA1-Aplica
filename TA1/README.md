## Comandos

```sh
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

```sh
python pacman.py -l bigCorners -p SearchAgent -a fn=bfs,prob=CornersProblem -z 0.5
```

## Resultados experimentales 

### Medium Corners 

||BFS|DFS|A\*|Algoritmo Genetico|
|-|-:|-:|-:|-:|
|Nodos expandidos|1921|371|||
|Costo de solucion|106|221|||

### Big Corners 

||BFS|DFS|A\*|Algoritmo Genetico|
|-|-:|-:|-:|-:|
|Nodos expandidos|7862|504|||
|Costo de solucion|162|302|||

Fuente: http://ai.berkeley.edu/search.html
