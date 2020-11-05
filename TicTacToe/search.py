from node import Node


class Search(object):
    """docstring for Search."""

    def __init__(self, matrix, player, opponent):
        self.initial_node = Node(matrix, None, 0, None)
        self.to_max = player
        self.to_min = opponent
        self.solution_node = None


    def someone_wins(self, matrix):
        return self.player_wins(matrix, self.to_max) or self.player_wins(matrix, self.to_min)


    def player_wins(self, matrix, player):
        for i in range(3):
            if matrix[i][0] == matrix[i][1] == matrix[i][2] == player:
                return True
            if matrix[0][i] == matrix[1][i] == matrix[2][i] == player:
                return True
        if matrix[0][0] == matrix[1][1] == matrix[2][2] == player:
            return True
        if matrix[0][2] == matrix[1][1] == matrix[2][0] == player:
            return True

        return False


    def make_move(self, node, move, letter):
        new_matrix = [row[:] for row in node.get_value()]#copia el valor, no la referencia
        new_matrix[move[0]][move[1]] = letter

        return Node(new_matrix, node, node.get_level() + 1, move)


    def pos_free_spaces(self, node):
        m = node.get_value()
        p = []
        for i in range(3):
            for j in range(3):
                if m[i][j] == " ":
                    p.append([i,j])
        return p


    def calc_score(self, matrix, letter):
        score = 0
        m = matrix
        l = letter
        if not self.player_wins(m, l):
            for i in range(3):
                if m[i][0] in [l," "] and m[i][1] in [l," "] and m[i][2] in [l," "]:
                    score += 1
                if m[0][i] in [l," "] and m[1][i] in [l," "] and m[2][i] in [l," "]:
                    score += 1
            if m[0][0] in [l," "] and m[1][1] in [l," "] and m[2][2] in [l," "]:
                score += 1
            if m[0][2] in [l," "] and m[1][1] in [l," "] and m[2][0] in [l," "]:
                score += 1
        else:
            score = float("inf")
        return score


    def calc_heuristic(self, matrix):
        if self.calc_score(matrix, self.to_max) == self.calc_score(matrix, self.to_min):
            return 0
        return self.calc_score(matrix, self.to_max) - self.calc_score(matrix, self.to_min)


    def game_over(self, node):
        matrix = node.get_value()
        count = 0
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == " ":
                    count += 1

        if count == 0:
            return True

        return False


    def minimax_algorithm(self, current_node, deep_level, mode):
        if deep_level == 0 or self.game_over(current_node) or self.someone_wins(current_node.get_value()):
            current_node.set_heuristic(self.calc_heuristic(current_node.get_value()))
            return current_node.get_heuristic()
        elif mode:  	#max
            next_nodes = []
            max = -float("inf")
            max_node = None
            moves = self.pos_free_spaces(current_node)
            for move in moves:
                next_nodes.append(self.make_move(current_node, move, self.to_max))
            for node in next_nodes:
                eval = self.minimax_algorithm(node, deep_level-1, False)
                if eval >= max:
                    max = eval
                    max_node = node
            self.solution_node = max_node
            return max
        else:           #min
            next_nodes = []
            min = float("inf")
            min_node = None
            moves = self.pos_free_spaces(current_node)
            for move in moves:
                next_nodes.append(self.make_move(current_node, move, self.to_min))
            for node in next_nodes:
                eval = self.minimax_algorithm(node, deep_level-1, True)
                if eval <= min:
                    min = eval
                    min_node = node
            self.solution_node = min_node
            return min

    def find(self):
        self.minimax_algorithm(self.initial_node, 20, True)
        return self.solution_node.get_value()
