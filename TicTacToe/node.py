

class Node(object):
    """docstring for Node."""

    def __init__(self, value, prev, level, heuristic):
        self.value = value
        self.prev = prev
        self.level = level
        self.heuristic = heuristic


    def set_heuristic(self, heuristic):
        self.heuristic = heuristic
