# Graph — City Map

A weighted directed graph implemented using an adjacency list, applied to a city navigation problem.

## Files

- `graph.py` — Core `Graph` class
- `vertex.py` — `Vertex` with outgoing edges
- `edge.py` — `Edge` with target vertex and weight
- `city_map.py` — City-specific application layer
- `main.py` — Demo with city data

## Graph Operations

| Method | Description |
|---|---|
| `add_vertex(label)` | Add a city node (no duplicates) |
| `add_edge(src, dest, weight)` | Add weighted directed road |
| `remove_vertex(label)` | Remove city and all connected edges |
| `remove_edge(src, dest)` | Remove a specific road |
| `bfs(start)` | Breadth-first traversal (iterative) |
| `dfs(start)` | Depth-first traversal (iterative, using stack) |
| `dfs_post_order(start)` | DFS post-order traversal |

## Example

```python
from graph import Graph

g = Graph()
for city in ["Ramallah", "Jerusalem", "Jericho", "Nablus"]:
    g.add_vertex(city)

g.add_edge("Ramallah", "Jerusalem", 15)
g.add_edge("Ramallah", "Nablus", 60)
g.add_edge("Jerusalem", "Jericho", 35)

print("BFS from Ramallah:")
g.bfs("Ramallah")

print("\nDFS from Ramallah:")
g.dfs("Ramallah")
```
