
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []
 
    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
 
    
    def BellmanFord(self, src):
 
       
        dist = [float("Inf")] * self.V
        dist[src] = 0
 
        
        for _ in range(self.V - 1):
          
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
 
      
 
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
 
     
        self.printArr(dist)
 
 

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge("A", "B", -1)
    g.addEdge("A", "C", 4)
    g.addEdge("B", "C", 3)
    g.addEdge("B", "D", 2)
    g.addEdge("B", "E", 2)
    g.addEdge("D", "C", 5)
    g.addEdge("D", "B", 1)
    g.addEdge("E", "D", -3)
 
    
    g.BellmanFord("A")
