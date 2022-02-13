g = {
    'a' : ['b', 'c'],
    'b' : ['d', 'e'],
    'c' : ['f', 'g'],
    'd' : [],
    'f' : [],
    'e' : [],
    'g' : []
}
q = []
def bfs(start):
    q.append(start)
    while len(q):
        v = q.pop(0)
        print(v, end=" ")
        for n in g[v]:
            q.append(n)
bfs('a')