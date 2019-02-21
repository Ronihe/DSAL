## Graph

## A graph data structure consists of a finite (and possibly mutable) set of vertices or nodes or points, together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph

## in a word, graph is like trees except they can contain loops

# It contains nodes + connections

# USES FOR GRAPHS

- Social Networks
- Location / Mapping
- Routing Algorithms
- Visual Hierarchy
- File System Optimizations
- EVERYWHERE!

# Terms

- vertex - a node
- edge - arch connection btw nodes
- weighted/unweighted: a value assigned to distances between vertices
- directed/undirected - directions assigned to distanced between vertices

# Big O

# DIFFERENCES & BIG O

|V| - number of verticles
|E| - number of edges

| OPERATION   |  ADJACENCY LIST  | ADJACENCY MATRIX |
| ----------- | :--------------: | ---------------: |
| Add Vertex  |       O(1)       |   O( \| V^2 \| ) |
| Add Edge    |       O(1)       |             O(1) |
| RemoveVert  | O(\|V\| + \|E\|) |       O(\|V^2\|) |
| Remove Edge |     O(\|E\|)     |             O(1) |
| Query       | O(\|V\| + \|E\|) |             O(1) |
| Storage     | O(\|V\| + \|E\|) |      ​O(\|V^2\|) |
