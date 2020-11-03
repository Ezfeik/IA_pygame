

class Node(object):
    """docstring for Node."""

    def __init__(self, position, prev):

        self.position = position
        self.prev = prev


    def get_position(self):

        return self.position


    def get_prev(self):

        return self.prev


    def go_back_to(self, c, cc_returning_list):

        if self.prev == c:
            cc_returning_list.append(self.prev)
            print(f"Returned to {self.prev.get_position()}")
            return None
        else:
            cc_returning_list.append(self.prev)
            self.get_prev().go_back_to(c, cc_returning_list)


    def get_solution(self, initial, cc_returning_list):

        if self == initial:
            cc_returning_list.append(self)
            print(f"Returned to {self.get_position()}")
            return None
        else:
            cc_returning_list.append(self)
            self.get_prev().get_solution(initial, cc_returning_list)
