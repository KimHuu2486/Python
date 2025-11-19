import re
from collections import deque

class Graph:
    def __init__(self, directed = True):
        self.directed = directed
        self.adj_list = {}
        self.vertices = []
        self.adj_matrix = []
        self.edge_list = []

    @classmethod
    def read_file(cls, pathFile, directed = True):
        g = cls(directed)

        with open(pathFile, encoding = "utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
            
                nums = list(map(int, re.findall(r"\d+", line)))
                if not nums:
                    continue

                u, *neighbors = nums
                if u not in g.adj_list:
                    g.adj_list[u] = []

                for v in neighbors:
                    g.adj_list[u].append(v)

                    if not directed:
                        if v not in g.adj_list:
                            g.adj_list[v] = []
                        g.adj_list[v].append(u)

        g.vertices = sorted(g.adj_list.keys())
        g.build_adj_matrix()
        g.build_edge_list()

        return g

    def build_adj_matrix(self):
        n = len(self.vertices)

        # ánh xạ tên đỉnh thành chỉ số trong ma trận
        idx = {v: i for i, v in enumerate(self.vertices)}

        self.adj_matrix = [[0] * n for _ in range(n)]

        for u in self.vertices:
            for v in self.adj_list.get(u, []):
                i, j = idx[u], idx[v]
                self.adj_matrix[i][j] = 1

    def build_edge_list(self):
        edges = []
        seen = set()

        for u, neighbors in self.adj_list.items():
            for v in neighbors:
                if self.directed:
                    edges.append((u, v))
                else:
                    e = tuple(sorted((u, v)))
                    if e not in seen:
                        edges.append((u, v))
                        seen.add(e)
        
        self.edge_list = edges

    def print_adj_list(self):
        print("Danh sach ke: ")
        for u, neighbors in self.adj_list.items():
            print(u, ":", neighbors)

    def print_adj_matrix(self):
        print("Ma tran ke: ")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

    def print_edge_list(self):
        print("Danh sach canh: ")
        for u, v in self.edge_list:
            print(f"({u}, {v})")

    def isDirected(self):
        return self.directed
    
    def countEdges(self):
        if self.directed:
            return sum(len(v) for v in self.adj_list.values())
        else:
            return sum(len(v) for v in self.adj_list.values()) // 2
    
    def countVertices(self):
        return len(self.vertices)
    
    def Degree(self, u):
        if self.directed:
            out_deg = len(self.adj_list[u])
            in_deg = sum(u in neighbors for neighbors in self.adj_list.values())
            return in_deg, out_deg
        else :
            return len(self.adj_list[u])
    
    def isolated_vertices(self):
        isolated = []
        for  u in self.vertices:
            deg = self.Degree(u)

            if self.directed:
                in_deg, out_deg = deg
                if in_deg == 0 and out_deg == 0:
                    isolated.append(u)
            else:
                if deg == 0:
                    isolated.append(u)
        return isolated 
    
    def leaf_vertices(self):
        leaf = []
        for u in self.vertices:
            deg = self.Degree(u)

            if self.directed:
                in_deg, out_deg = deg
                if in_deg + out_deg == 2:
                    leaf.append(u)
            else:
                if deg == 1:
                    leaf.append(u)
        return leaf
    
    def to_undirected(self):
        g2 = Graph(directed = False)
        for u in self.vertices:
            for v in self.adj_list[u]:
                g2.adj_list.setdefault(u, [])
                g2.adj_list[u].append(v)
                g2.adj_list.setdefault(v, [])
                if u not in g2.adj_list[v]:
                    g2.adj_list[v].append(u)
        
        g2.vertices = g2.adj_list.keys()
        g2.build_adj_matrix()
        g2.build_edge_list()
        return g2
    
    def complement_graph(self):
        comp = Graph(directed = self.directed)
        V = self.vertices

        neighbor_sets = {u: set(self.adj_list.get(u, [])) for u in V}

        comp.adj_list = {u : [v for v in V if v != u and v not in neighbor_sets[u]] for u in V}

        comp.vertices = V[:]
        return comp

    def converse_graph(self):
        if not self.directed:
            return self.copy()
        
        g2 = Graph(directed = True)
        g2.adj_list = {u: [] for u in self.vertices}
        
        for u in self.vertices:
            for v in self.adj_list[u]:
                g2.adj_list[v].append(u)
                
        g2.vertices = self.vertices[:]
        return g2        
    
    def DFS(self, start):
        visited = set()
        order = []
        
        def go(u):
            visited.add(u)
            order.append(u)
            for v in self.adj_list[u]:
                if v not in visited:
                    go(v)
        
        go(start)
        return order
    

    def BFS(self, start):
        visited = {start}
        q = deque([start])
        order = []
        
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj_list[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        
        return order
    
    def is_complete(self):
        if self.directed:
            return False
        
        n = len(self.vertices)
        for u in self.vertices:
            if len(self.adj_list[u] != n -1):
                return False
        return True
    
    def is_cycle(self):
        for u in self.vertices:
            if len(self.adj_list[u]) != 2:
                return False
        
        visited = set()
        
        def dfs(start):
            visited.add(start)
            for v in self.adj_list[start]:
                if v not in visited:
                    dfs(v)
        
        dfs(self.vertices[0])
        
        return len(visited) == len(self.vertices)
                    
    def is_bipartite(self):
        color = {}
        
        for start in self.vertices:
            if start not in color:
                color[start] = 0
                q = deque([start])
                while q:
                    u = q.popleft()
                    for v in self.adj_list[u]:
                        if v not in color:
                            color[v] = 1 - color[u]
                            q.append(v)
                        elif color[v] == color[u]:
                            return False
        
        return True
    
    def is_complete_bipartite(self):
        if self.directed:
            return False
        
        color = {}
        
        start = self.vertices[0]
        color[start] = 0
        q = deque([start])
        
        while (q):
            u  = q.popleft()
            for v in self.adj_list[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
                
        if (len(color) != len(self.vertices)):
            return False
        
        A = [u for u in self.vertices if color[u] == 0]
        B = [u for u in self.vertices if color[u] == 1]
        
        for u in A:
            if set(self.adj_list[u] != set(B)):
                return False
            
        for v in B:
            if set(self.adj_list[v]) != set(A):
                return False       
        
        return True
                        
    def count_connect_components(self):
        visited = set()
        comps = 0
        
        def dfs(u):
            visited.add(u)
            for v in self.adj_list[u]:
                if v not in visited:
                    dfs(v)
        
        for u in self.vertices:
            if u not in visited:
                comps += 1
                dfs(u)
        
        return comps

    def articulation_points(self):
        comps = self.count_connect_components()
        articulationPoints = []
        
        def dfs(u, banned, visited):
            visited.add(u)
            for v in self.adj_list(u):
                if v == banned:
                    continue
                if v not in visited:
                    dfs(v, banned, visited)
                    
        for banned in self.vertices:
            visited = set([banned])
            cnt = 0
            
            for u in self.vertices:
                if u not in visited:
                    dfs(u, banned, visited)
                    cnt+=1
            
            if cnt > comps:
                articulationPoints.append(banned)
                
        return articulationPoints

    def bridges(self):
        comps = self.count_connect_components()
        bridge = []
        seen = set()
        
        def dfs(u, banned_x, banned_y, visited):
            visited.add(u)
            for v in self.adj_list[u]:
                if (u == banned_x and v == banned_y) or (u == banned_y and v == banned_x):
                    continue
                if v not in visited:
                    dfs(v, banned_x, banned_y, visited)
                    
        for banned_x, banned_y in self.edge_list:
            e  = tuple(sorted((banned_x, banned_y)))
            if e in seen:
                continue
            seen.add(e)
            
            visited = set()
            cnt = 0
            
            for u in self.vertices:
                if u not in visited:
                    dfs(u, banned_x, banned_y, visited)
                    cnt+=1
            
            if cnt > comps:
                bridge.append([banned_x, banned_y])
                
        return bridge

    def euler_hierholzer(self):
        adjList = {u: self.adj_list[u][:] for u in self.vertices}
        
        odd = [u for u in  self.vertices if len(adjList[u]) % 2 == 1]
        
        if len(odd) == 0:
            start = self.vertices[0] # Chu trình Euler
        elif len(odd) == 2:
            start = odd[0] # Đường đi Euler
        else:
            return None
            
        stack = [start]
        path = []
        
        while stack:
            u = stack[-1]
            if adjList[u]:
                v = adjList[u].pop()
                adjList[v].remove(u)
                stack.append(v)
            else:
                path.append(stack.pop())
        
        return path[::-1]
    
    def euler_fleury(self):
        adjList = {u: self.adj_list[u][:] for u in self.vertices}
        
        odd = [u for u in self.vertices if len(adjList[u]) % 2 == 1]
        
        if len(odd) == 0:
            start = self.vertices[0] # chu trình euler
        elif len(odd) == 2:
            start = odd[0] # đường đi euler
        else:
            return None
        
        def dfs(u, visited):
            visited.add(u)
            for v in adjList[u]:
                if v not in visited:
                    dfs(v, visited)
                    
        visited = set()
        dfs(start, visited)
        for u in self.vertices:
            if len(adjList[u]) > 0 and u not in visited:
                return None # Các đỉnh có bậc > 0 phải liên thông
            
        def is_bridge(u, v):
            visited1 = set()
            dfs(u, visited)
            
            adjList[u].remove(v)
            adjList[v].remove(u)
            
            visited2 = set()
            dfs(u, visited2)
            
            adjList[u].insert(0, v)
            adjList[v].insert(0, u)
            
            return len(visited2) < len(visited1)
        
        path = [start]
        u = start
        
        while True:
            if not adjList[u]:
                break
            
            chosen = None
            
            for v in adjList[u]:
                if len(adjList[u] == 1):
                    chosen = v
                    break
                
                if not is_bridge(u, v):
                    chosen = v
                    break
            
            if chosen is None:
                chosen = adjList[u][0]
                
            adjList[u].remove(chosen)
            adjList[chosen].remove(u)
            
            path.append(chosen)
            u = chosen

        return path
        
            
                
                

        

if __name__ == "__main__":
    
    g = Graph.read_file("Graph.txt", directed = True)
    g.print_adj_list()
    print("\n")
    g.print_adj_matrix()
    print("\n")
    g.print_edge_list()
