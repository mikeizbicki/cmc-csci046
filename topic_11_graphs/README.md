# Graphs

<img src=graphs.jpg width=400px/>

Graphs are one of the key unifying concepts in computer science.
Many problems can be solved by:
1. convert the problem into the language of graphs, and then
2. use an appropriate graph algorithm.

For example:
1. Most [GOFAI](https://en.wikipedia.org/wiki/GOFAI) (Good Old Fashioned Artificial Intelliigence) problems fit this pattern.
    Even in the age of ChatGPT, most "AI" problems are GOFAI problems.
1. Many of the classic SWE (SoftWare Engineer) interview questions fit this pattern.
    (The other common patterns are divide and conquer and dynamic programming.)
    If you go on to take CSCI148 Graph Algorithms with Prof Sarah Cannon,
    you'll cover these concepts in great detail.

Key vocabulary:
1. node
1. edge
1. weight
1. label
1. directed/undirected
1. path
1. shortest path
1. shortest path tree
1. cycle
1. acyclic

We will cover three graph algorithms in this class.
Remarkably, they have essentially the same pseudocode,
but by swapping which data structure we use,
we get different algorithms.

| Algorithm | Data Structure | Run Time |
| --------- | -------------- | -------- |
| Depth First Search (DFS) | Stack (list/deque) | O(V + E) |
| Breadth First Search (BFS) | Queue (deque) | O(V + E) |
| Dijkstra's Algorithm (shortest path) | Priority Queue (heap) | O( (V + E) log V) |

Textbook reference: [chapter 8](https://runestone.academy/runestone/books/published/pythonds/Graphs/toctree.html)

Applications of Dijkstra's algorithm:
1. [Google Maps](https://www.google.com/maps/@39.0188644,125.7397457,13555m/data=!3m1!1e3?hl=en)
1. videogame pathfinding
1. [Internet routing](https://en.wikipedia.org/wiki/Open_Shortest_Path_First)
1. <https://expedia.com>
1. [6 Degrees of Kevin Bacon](https://blogs.ams.org/mathgradblog/2013/11/22/degrees-kevin-bacon/)
1. [Catching criminals](https://www.researchgate.net/profile/Joseph-Olusina-2/publication/335387366_Journey_to_Crime_Using_Dijkstra%27s_Algorithm/links/5f045b90a6fdcc4ca452fdeb/Journey-to-Crime-Using-Dijkstras-Algorithm.pdf)

## Lab

See instructions in [lab-deploying.md](lab-deploting.md)

### Homework

Follow the instructions at <https://github.com/mikeizbicki/risk>

Due date: 25 April
