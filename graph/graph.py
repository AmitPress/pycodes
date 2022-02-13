class G:
    def __init__(self):
        self.neighbours = []
        self.name2node = {}
        self.node2name = []
        self.weight = []
    def __len__(self):
        return len(self.node2name)
    def __getitem__(self, value):
        return self.neighbours[value]
    def add_node(self, name):
        assert name not in self.name2node
        self.name2node[name] = len(self.name2node)
        self.node2name.append(name)
        self.neighbours.append([])
        self.weight.append({})
        return self.name2node[name]
    def add_edge(self, name_u, name_v, weight_uv=None):
        self.add_arc(name_u, name_v, weight_uv)    
        self.add_arc(name_v, name_u, weight_uv)
    def add_arc(self, name_u, name_v, weight_uv=None):
        u = self.name2node[name_u]
        v = self.name2node[name_v]
        self.neighbours[u].append(v)
        self.weight[u][v] = weight_uv

# test the graph
g = G()
g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')
g.add_edge('a','b')
g.add_edge('a','c')
g.add_edge('a','d')
g.add_edge('b','d')
g.add_edge('c','d')
print(g[2])