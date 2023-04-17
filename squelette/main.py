import time
from node import Node
from exploration import Exploration
from taquin.problem import Problem
from taquin.state import State


###############################################
# Taquin
###############################################

board = [
    [1, 2, 3],
    [4, 5, 0],
    [6, 7, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

target_state = State(goal)

initial_state = State(board)
# OU
# initial_state = State(board) = Probleme.mix_up(target_state)

problem = Problem(initial_state=initial_state, final_state=target_state)

# Dijkstra


def score_function(node): return node.g

###############################################
# Exploration (generic)
###############################################


exploration = Exploration(problem=problem, criterion=score_function)
path = exploration.explore()

###############################################
# Result
###############################################
print("=====================================================")
steps = -1
print("Initial state:\t" + str(problem.initial_state))
if len(path) > 0:
    last = None
    for node in path:
        print(node.action)
        node.state.print_state()
        time.sleep(0.2)
        last = node
        steps += 1
        print(last)
    print("Final state:\t\t" + str(last.state))
    print("Total cost:\t\t" + str(last.g))
else:
    print("Goal not achievable")

print("Number of nodes explored:" + str(exploration.n_explores))
print("Number of steps: " + str(steps))
print("Exploration duration: " + str(time_end - time_begin) + " second(s)")
