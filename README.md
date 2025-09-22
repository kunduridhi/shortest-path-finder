# Shortest Path Finder

**Project by:** Ridhi Kundu  
**Registration Number:** 24BDE0171  

---

# Shortest Path Finder

## 1. Introduction
Finding the shortest path between two points is one of the most fundamental problems in computer science and mathematics. Graph theory provides an efficient way to model real-world systems such as transportation networks, social networks, and computer communication networks.  

The shortest path problem involves finding the minimum distance or cost between two nodes in a graph. This project implements algorithms such as Breadth-First Search (BFS) for unweighted graphs and Dijkstra’s Algorithm for weighted graphs to solve shortest path problems effectively.

**Applications include:**
- GPS navigation systems (Google Maps, Uber)
- Internet routing (OSPF protocol)
- Airline route planning
- Logistics and supply chain optimization

---

## 2. Problem Statement
In many real-life situations such as road networks, internet routing, and communication systems, it is necessary to find the most efficient route between two points. Without an effective method, navigation and resource allocation may become time-consuming and inefficient.  

This project designs and implements an algorithm that computes the shortest path between two nodes in a graph, solving optimization problems in transportation, networking, and logistics.

---

## 3. Objectives
- To study graph theory concepts and their applications in shortest path problems.  
- To design an algorithmic approach for shortest path computation.  
- To implement BFS for unweighted graphs and Dijkstra’s Algorithm for weighted graphs.  
- To test the algorithms with sample graphs and real-world inspired datasets.  
- To demonstrate how graph-based algorithms can optimize routing and connectivity problems.  

---

## 4. Literature Review
- **Graph Theory:** Introduced by Leonhard Euler in 1736 with the "Seven Bridges of Königsberg" problem.  
- **BFS:** Used for shortest paths in unweighted graphs.  
- **Dijkstra’s Algorithm:** Proposed by Edsger W. Dijkstra in 1956; finds shortest paths in weighted graphs.  
- **Applications:** GPS navigation, transport logistics, and network routing protocols.  

---

## 5. Methodology
1. Represent the network as a graph (nodes = cities/routers, edges = connections).  
2. Implement graph data structures (Adjacency List).  
3. Apply algorithms:  
   - BFS for unweighted graphs  
   - Dijkstra’s Algorithm for weighted graphs  
4. Test with small graphs and real-world inspired datasets.  
5. Visualize results using `networkx` and `matplotlib`.  

---

## 6. Algorithms Used
### 6.1 Breadth-First Search (BFS)
- Works level by level from the source node.  
- Suitable for unweighted graphs.  
- Guarantees the shortest path in terms of number of edges.  

### 6.2 Dijkstra’s Algorithm
- A greedy algorithm that finds the minimum cost path from a source to all other nodes.  
- Suitable for weighted graphs with non-negative weights.  

---

## 7. Working of the Project
1. User inputs the graph (nodes, edges, weights).  
2. Selects the algorithm (BFS for unweighted, Dijkstra for weighted).  
3. Program computes the shortest path:  
   - BFS → minimum number of hops  
   - Dijkstra → minimum total weight  
4. Output shows:  
   - Path taken (e.g., A → B → C → D)  
   - Distance/Cost of the path  
   - Maze with path visualization for BFS example  

---

## 8. Graph Visualization
- **Unweighted Graph:** Nodes connected without edge weights, used in BFS examples.  
- **Weighted Graph:** Nodes connected with weights, used in Dijkstra examples.  

---

## 9. Technology Stack
- **Programming Language:** Python  
- **Libraries:**  
  - `networkx` → Graph representation & visualization  
  - `matplotlib` → Graph plotting  
  - `heapq` → Priority queue for Dijkstra  
- **IDE/Editor:** VS Code / Jupyter Notebook  
- **Version Control:** GitHub  

---

## 10. Results
- BFS successfully finds the shortest path in unweighted graphs.  
- Dijkstra’s Algorithm provides the shortest weighted path.  
- Visualization confirms correctness of paths.  

---

## 11. Applications
- Road navigation systems (Google Maps, Uber)  
- Airline & shipping logistics  
- Internet data packet routing  
- Emergency response planning  

---

## 12. Limitations and Future Work
**Limitations:**  
1. BFS cannot handle weighted graphs.  
2. Dijkstra’s Algorithm does not work with negative weights.  

**Future Enhancements:**  
- Implement A* Algorithm for heuristic search.  
- Apply to real map datasets (OpenStreetMap API).  
- Build a GUI-based navigation system.  

---

## 13. GitHub Repository
[https://github.com/kunduridhi/shortest-path-finder](https://github.com/kunduridhi/shortest-path-finder)  

---

## 14. References
1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.  
2. Dijkstra, E. W. (1959). A note on two problems in connexion with graphs. *Numerische Mathematik*.  
3. NetworkX Documentation: [https://networkx.org/documentation/stable/](https://networkx.org/documentation/stable/)  
4. GeeksforGeeks – Graph Theory: [https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)  
