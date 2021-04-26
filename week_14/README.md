# More Graphs/Wrap up

## Homework: conquer the world with Risk

You will implement several graph algorithms to develop a tool for the game of Risk.

**Learning Objectives:**

1. implement graph traversal algorithms
1. understand how graph traversals relate to real-world AI problems
1. use someone else's complex code

### Background

Risk is the classic board game of world domination.
The website https://warzone.com has a free online game.
If you've never played before, they provide a short tutorial with the rules.

Here's a picture of the board:

<p align=center>
<img width=500px src=img/board5.png>
</p>

We can model the game board as a graph by creating a vertex for each country,
and drawing an edge between two countries whenever the two countries are adjacent:

<p align=center>
<img width=500px src=img/board5_graph.png>
</p>

In the game of Risk, armies from one territory attack another territory following paths along this graph,
and so you must implement algorithms that would help an AI determine which are the best paths to attack along.

### Path verification

The first three functions you should implement are: `is_valid_path`, `is_valid_attack_path`, and `cost_of_attack_path`.
These functions are fairly straightforward to implement and full descriptions are provided in the starter code.

### Breadth First Search for shortest path

The first complicated function you will have to implement is the `shortest_path` function,
which uses a breadth first search.
The algorithm is:

```
Create a stack
Push the source territory onto the stack
Create a queue
Enqueue the stack onto the queue

While the queue is not empty
    Dequeue a stack from the queue
    For each territory on the board 
        If the territory is adjacent to the top of the stack
            If this territory is the target territory
                You are done!
                The front stack plus this territory is your shortest path
            Make a copy of the stack
            Push the found territory onto the copy
            Enqueue the copy
            Delete the territory from the board
```

This algorithm should look very familiar, because you've already implemented it!
The pseudocode above is taken exactly from the word ladder assignment (hw4),
except I've run the commands `s/word/territory/g` and `s/dictionary/board/g`
(these are the find and replace commands in vim, and you will frequently see programmers talk like this in online forums.)

To see how the word ladder algorithm was just breadth first search on a graph,
I've created a small subgraph of the word ladder problem:

<p align=center>
<img src=img/words.png>
</p>

In this graph, words are the nodes, and an edge exists between nodes if the words differ by only 1 letter.

Now that we know how this algorithm relates to breadth first search,
it will be a bit easier on this problem to use the following pseudocode to implement the `shortest_path` function:

```
Create a dictionary whose keys are territories and values are path
Set dictionary[source] = [source]
Create a queue
Enqueue source onto the queue
Create a set of visited territories
Add source to the set

While the queue is not empty
    Dequeue current_territory from the queue
    If current_territory is the target
        return the dictionary[current_territory]
    For each territory in the neighbors of current_territory that is not in the visited set
        Make a copy of dictionary[current_territory]
        Push territory onto the copy
        Set dictionary[territory] = copy + territory
        Enqueue territory
    Add current_territory to the visited set
```

The `can_fortify` function also uses breadth first search but with two modifications.
1. We are not returning a path, but instead only returning `True` or `False` depending on whether a path exists.
    We will still have to calculate the path to determine if one exists,
    you'll just discard this information.
2. We are searching over only a subgraph of the original graph.
    All the nodes remain the same, but there are only edges between territories if they are owned by the same player.
    The pseudocode for `can_fortify` function is the same as the pseudocode for the `shortest_path`,
    except that in the line
    ```
        For each territory in the neighbors of current_territory that is not in the visited set
    ```
    the meaning of `neighbors` is different.
    In `shortest_path`, two territories are neighbors if they are adjacent,
    but in `can_fortify`, two territories are neighbors is they are adjacent and are owned by the same player.

### Depth first search

In this homework, you don't have to implement the depth first search algorithm,
but notice that depth first search is the same as breadth first search if you replace `s/queue/stack/g`, `s/enqueue/push/g`, `s/dequeue/pop/g`.
The choice of data structure determine the algorithm!

### Djikstra's algorithm

Dijkstra's algorithm finds shortest paths in a graph where the nodes or edges have non-negative weights.
(The breadth first search algorithm above for shortest path considers all nodes/edges to have weight 1.)
The key idea is that Dijkstra's algorithm uses a priority queue instead of a queue to keep track of these weights.

You will use Dijkstra's algorithm to implement the `cheapest_attack_path` function.
The pseudocode follows the same pattern as the BFS pseudocode,
but is modified to use a priority queue instead of a regular queue:
```
    Create a dictionary whose keys are territories and values are path
    Set dictionary[source] = [source]
++  Create a PRIORITY queue
++  Enqueue source onto the PRIORITY queue WITH PRIORITY 0
    Create a set of visited territories
    Add source to the set

++  While the PRIORITY queue is not empty
++      Dequeue current_territory from the PRIORITY queue
        If current_territory is the target
            return the dictionary[current_territory]
        For each territory in the neighbors of current_territory that is not in the visited set
            Make a copy of dictionary[current_territory]
            Push territory onto the copy
++          CALCULATE THE PRIORITY OF THE PATH AS PRIORITY OF CURRENT_TERRITORY + NUMBER OF ARMIES ON TERRITORY
++          IF TERRITORY NOT IN THE PRIORITY QUEUE
                Set dictionary[territory] = copy + territory
++              Enqueue territory WITH PRIORITY 
++          ELSE, IF THE NEW PRIORITY IS LESS THEN THE PRIORITY IN THE QUEUE
                Set dictionary[territory] = copy + territory
++              UPDATE THE TERRITORY'S PRIORITY IN THE PRIORITY QUEUE WITH THE NEW PRIORITY
        Add current_territory to the visited set
```

Notice that the `cheapest_attack_path` function requires that the returned path not pass through any friendly nodes.
To ensure this is the case, you will have to modify the set of neighbors in the inner for loop so that only enemy territories are returned.

### Tasks

Complete the following tasks:

1. Fork the [risk repo](https://github.com/mikeizbicki/risk) and enable travis
1. Update the `README.md` file so that the github actions badge points to your repo
1. Implement the `is_valid_path`, `is_valid_attack_path`, `cost_of_attack_path`, `shortest_path`, `can_reinforce`, `cheapest_attack_path`, and `can_attack` functions.
1. Submit the link to your github repo into sakai.

