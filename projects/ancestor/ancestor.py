# directed acyclic graph

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):

    # level in the graph
    max_level = 0
    # current min value (if node has no parents, min value is -1)
    min_value = -1

    # instantiate a queue
    q = Queue()
    # enqueue tuple with the starting value and starting level
    q.enqueue((starting_node, 0))

    # process queue while queue is not empty
    while q.size() > 0:
        current = q.dequeue()

        for tup in ancestors:
            # check ancestors tup[1] for all relationships with current[0]
            if tup[1] == current[0]:
                next_level = current[1] + 1
                # if neighbor is found
                if next_level > max_level:
                    # max level increments
                    max_level = next_level
                    # min value will be set to a new value from tup
                    min_value = tup[0]
                # otherwise compare neighbor at the same level, if lower than current min value
                elif tup[0] < min_value:
                    # min value only change if new value found is lower than min value in this level
                    min_value = tup[0]
                # enqueue the neighbor tup as tup[0] and next level
                q.enqueue((tup[0], next_level))
    
    return min_value

# ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]