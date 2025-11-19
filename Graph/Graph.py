import re

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


if __name__ == "__main__":
    g = Graph.read_file("Graph.txt", directed = True)
    g.print_adj_list()
    print("\n")
    g.print_adj_matrix()
    print("\n")
    g.print_edge_list()
