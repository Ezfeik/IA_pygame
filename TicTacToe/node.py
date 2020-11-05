

class Node(object):
    """docstring for Node."""

    def __init__(self, value, prev, level, move):
        self.value = value
        self.prev = prev
        self.level = level
        self.move = move
        self.heuristic = None


    def set_heuristic(self, heuristic):
        self.heuristic = heuristic


    def get_value(self):
        return self.value


    def get_level(self):
        return self.level


    def get_move(self):
        return self.move


    def get_heuristic(self):
        return self.heuristic


    def print_matrix(self):
        for i in range(3):
            print(self.value[i])
