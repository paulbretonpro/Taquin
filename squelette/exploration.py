import collections
import sys
from node import *


class Exploration:
    """
    Exploration algorithm
    - problem: Formalized problem to be solved
    - criterion: function that associates a node with a score, the lowest being the best
    - open: collection of nodes known but not yet explored
    - close: collection of nodes already explored
    - n_explores: number of nodes explored (useful for statistics at the end)
    """

    def __init__(self, problem, criterion):
        self.problem = problem
        self.criterion = criterion
        self.open = dict()
        self.close = dict()
        self.n_explores = 0

    def pick(self):
        """
        Return a new node to explore
        """
        node = None

        for n in self.open.values():
            if node == None or n.f < node.f:
                node = n

        del self.open[node.state]
        return node

    def update_tree(self, new_nodes, open, close):
        """
        Updates the exploration tree with a new node
        """
        for node in new_nodes:
            if node.state in close:
                if node.g < close[node.state].g:
                    del close[node.state]
                    open[node.state] = node
            else:
                if node.state in open:
                    if node.g < open[node.state].g:
                        del open[node.state]
                        open[node.state] = node
                else:
                    open[node.state] = node

    def explore(self):
        """
        Explores a state space and returns the found path,
        optionally None if no path is found
        """
        # init OPEN and CLOSE dict
        self.open[self.problem.initial_state] = Node(
            self.problem.initial_state, 0, self.criterion, None, None)

        while len(self.open) > 0:
            current_node = self.pick()
            self.close[current_node.state] = current_node
            if self.problem.goal(current_node.state):
                return current_node.backtrack_path()
            else:
                possible_actions = self.problem.possible_actions(
                    current_node.state)
                new_nodes = []
                for i in possible_actions:
                    new_nodes.append(
                        current_node.create_child(i, self.problem))

                self.update_tree(new_nodes, self.open, self.close)
        return "Goal not achievable"

    def successeur(self, current_node):
        action_possibles = self.problem.possible_actions(current_node.state)
        for action in action_possibles:
            new_node = current_node.create_child(action, self.problem)
            self.open[new_node.state] = new_node

        return action_possibles
