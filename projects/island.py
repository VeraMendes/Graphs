'''Write a function that takes a 2D binary array and returns
the number of 1 islands. An island consists of 1s that are
connected to the north, south, east or west. For example:

            a  b  c  d  e
            
islands = [[0, 1, 0, 1, 0],   a
           [1, 1, 0, 1, 1],   b
           [0, 0, 1, 0, 0],   c
           [1, 0, 1, 0, 0],   d
           [1, 1, 0, 0, 0]]   e

island_counter(islands) # returns 4'''

# islands consist of - connected components
# connected - neighbors (edges)
# directions, nsew (edges)
# 2D array - graph, more or less?
# returns (shape of solution) - number of islands (int)

# how could we write a get neighbor function that uses this shape?
# offset coordinates

# how can we find the extent of an island?
# either of our travels to find all of the nodes in an island

# how do I explore the larger set?
# loop through and call a traversal if we find an unvisited 1

# UPER

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def get_neighbors(x, y, matrix):
    neighbors = []
    if x > 0 and matrix[y][x - 1] == 1:       # move up
        neighbors.append((x - 1, y))
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:  # move down
        neighbors.append((x + 1, y))
    if y > 0 and matrix[y - 1][x] == 1:       # move left
        neighbors.append((x, y - 1))
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:   # move right
        neighbors.append((x, y + 1))

    return neighbors



def dfs(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    while s.size() > 0:
        v = s.pop()
        if not visited[v[1]][v[0]]:
            visited[v[1]][v[0]] = True
            for neighbor in get_neighbors(v[0], v[1], matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dfs(x, y, matrix, visited)
                    island_count += 1
                else:
                    visited[y][x] = True
    return island_count

def print_matrix(matrix):
    for row in matrix:
        print("".join([str(i) for i in row]))


matrix = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# print_matrix(matrix)
print(get_neighbors(0,1,islands))
print_matrix(islands)
# print(island_counter(matrix))
print(island_counter(islands))