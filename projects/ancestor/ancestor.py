# directed acyclic graph

class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None



def earliest_ancestor(ancestors, node):

    # instantiate graph
    graph = Graph()
    # create graph
    # add node to graph
    # node = graph.add_vertex(node)
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
    # check if node has parents
    # if yes with 1 parent
    if len(graph.get_neighbors(node)) == 1:
        parent = graph.get_neighbors(node)
        earliest_ancestor(ancestors, parent)
    # if yes with 2 parents
    # choose the smallest parent id
    elif len(graph.get_neighbors(node)) == 2:
        smallest_id_parent = min(graph.get_neighbors(node))
        earliest_ancestor(ancestors, smallest_id_parent)
    # if not, we found the earliest ancestor
    else:
        return node


    # If the input individual has no parents, returns -1
    return -1