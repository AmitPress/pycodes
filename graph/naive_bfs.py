g = {
    'a' : ['b', 'c'],
    'b' : ['d', 'e'],
    'c' : ['f', 'g'],
    'd' : [],
    'f' : [],
    'e' : [],
    'g' : []
}
# here we are not considering any optimisation
q = []
def bfs(start):
    q.append(start)
    while len(q):
        v = q.pop(0)
        print(v, end=" ")
        for n in g[v]:
            q.append(n)
# bfs('a') it  works

# lets consider some optimisation - add a flagging system

def smart_bfs(start):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)
    while len(queue):
        v = queue.pop(0)
        print(v, end=" ")
        for n in g[v]:
            if n not in visited:
                queue.append(n)
                visited.append(n)

# smart_bfs('a') works fine

# test for `in` and `not in`
# x = [1, 3, 4]
# y = [1, 3, 7]
# for nc in x:
#     if nc not in y:
#         print(nc)