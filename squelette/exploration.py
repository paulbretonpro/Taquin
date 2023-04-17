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

        for n in self.open.values() :
            if node == None or n.f < node.f :
                node = n

        del self.open[node.state]
        return node

    def update_tree(self, new_nodes, open, close):
        """
        Updates the exploration tree with a new node
        """
        for node in new_nodes :
            if node.state in close :
                if node.g < close[node.state].g :
                    del close[node.state]
                    open[node.state] = node
            else :
                if node.state in open :
                    if node.g < open[node.state].g :
                        del open[node.state]
                        open[node.state] = node
                else :
                    open[node.state] = node

    def successors(self,current_node) :
        possible_actions = self.problem.possible_actions(current_node.state)
        nodes = []
        for i in possible_actions:
            nodes.append(current_node.create_child(i, self.problem))
        return nodes

    def explore(self):
        """
        Explores a state space and returns the found path,
        optionally None if no path is found
        """
        
        self.open = {self.problem.initial_state: Node(self.problem.initial_state, criterion=self.criterion)}#Initialisation collection open avec initial state

        while len(self.open) > 0:#tant que open n'est pas vide
            current_node = self.pick()#on selectionne le node courant
            self.close[current_node.state] = current_node #on ajoute le node courant à la collection close
            if self.problem.goal(current_node.state):#si on a atteint le node final attendu
                return current_node.backtrack_path()#on retourne la solution
            else : #sinon
                #on cherche tous les successeurs possibles du node courant
                new_nodes = self.successors(current_node)
                self.update_tree(new_nodes, self.open, self.close)#on met a jour l'arbre d'exploration
        return "Goal not achievable"

  