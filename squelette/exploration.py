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
        # À implémenter on le pioche en function de l'algo parcourir open chopé le plus petit g,
        small_g = -1
        node_picked = None
        for node in self.open:
            if (small_g == -1):
                node_picked = node
                small_g = node.g
            else:
                if (small_g > node.g):
                    node_picked = node

        return node_picked

    def update_tree(self, new_nodes):
        """
        Updates the exploration tree with a new node
        """
        # À implémenter

    def explore(self):
        """
        Explores a state space and returns the found path,
        optionally None if no path is found
        """
        # init OPEN and CLOSE dict
        self.open[self.problem.initial_state] = Node(
            self.problem.initial_state, 0, self.criterion, None, None)

        while len(self.open) != 0:
            current_node = self.pick()
            if current_node.state == self.problem.final_state:
                return current_node
            else:

        return None

    def successeur(self, current_node):
        # prochaine noeud, lister les actions possible, pour chaque action possible créer un fils (combiner possible action et createChild)
        action_possibles = self.problem.possible_actions(current_node.state)
        for action in action_possibles:
            new_node = current_node.create_child(action, self.problem)
            self.open[new_node.state] = new_node

        return action_possibles
