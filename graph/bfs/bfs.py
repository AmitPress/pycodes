# assignment

from collections import deque  # the built-in library to use queue


def graph_input():
    l = input().strip().split(' ')  # taking input, splitting by space
    N, E = int(l[0]), int(l[1])  # Node and Edge number, saving after converting it to integer number
    adj_list = {}  # adjacent list saved as dictionary that will store the graph with placeholder for 0
    for i in range(0, E):  # all the edges are being taken input
        l = input().strip().split(' ')
        a, b = int(l[0]), int(l[1])  # an edge between a and b
        if adj_list.get(a) is None:  # No entry for node a, creating a key
            adj_list[a] = []  # a: [b, c, d] will be stored from node a, where we can go
        if adj_list.get(b) is None:  # No entry for node a, creating a key
            adj_list[b] = []
        adj_list[a].append(b)
        adj_list[b].append(a)
    l = input().strip().split(' ')
    start_node, dst_node = int(l[0]), int(l[1])
    return N, E, adj_list, start_node, dst_node  # node, edge, adjacent list


"""
Useful functions for a dictionary D = {) 
- Assignment: D[a] = 10 for key a, storing value 10 
- Searching if the key exists: D.get(a), if None no key else returns D[a] 
- Delete del D[a], deletes the concerned entry 
"""

"""
Useful functions for a queue q = deque()
- Add in the end: q.append(a) 
- Pop from the left: u = q.popleft() 
"""


def bfs(adj_list, start_node, dst_node):
    # this function will implement the BFS
    visited = {}  # this indicates which nodes are visited
    parent = {}  # this indicates for each node v, which node u is parent
    distance = {}  # the distance array to store the distance
    parent[start_node] = None  # start node will have no parent
    distance[start_node] = 0  # distance of start_node from start_node is 0
    queue = deque()  # initialization of deque
    queue.append(start_node)  # start_node is being pushed to the queue
    visited[start_node] = True  # tracking which nodes are visited
    while len(queue) > 0:  # continue till the queue is empty
        u = queue.popleft()  # FIFO order popping from the left
        if u == dst_node:  # destination is reached, no more searching/expansion
            break
        if adj_list.get(u) is not None:  # paths from u
            for i in range(0, len(adj_list[u])):  # traverse in the adjacent list of u
                if not adj_list[u][i] in visited:
                    queue.append(adj_list[u][i])
                    visited[adj_list[u][i]] = True
                    parent[adj_list[u][i]] = u
                    
        """
        Task 2: Write Your BFS logic here 
        - Traverse in the adjacent list 
        - Find the nodes which are not visited 
        - Push/Append them in the queue 
        - If the node is already visited, see if its path can be lexicographically made smaller 
        """
        """
        Supporting functions:
        - queue.popleft() # FIFO order popping 
        - visited.get(u) says if you have key for u in the visited array, if returns None then you have no value, 
        otherwise returns visited[u] a value 
        - visited[u] 
        """
    return parent # parent holds the path, track


def print_lexicographical_path(parent, start_node, dst_node):
    if parent.get(dst_node) is None:  # no path exists
        print("INF")
        return
    curr_node = dst_node
    paths = []
    while curr_node != start_node:
        par = parent[curr_node]  # parent of curr_node
        paths.append((par, curr_node))
        """
        Task 3: Write Your logic here to find the whole path 
        """
        curr_node = par
    """
    Task 4: Print the paths maintaining the output format, the number of edges used and the concerned edges  
    """
    for path in sorted(paths):
        print(path, end=' ')


if __name__ == '__main__':
    N, E, adj_list, start_node, dst_node = graph_input()
    parent = bfs(adj_list, start_node, dst_node)
    print_lexicographical_path(parent, start_node, dst_node)

