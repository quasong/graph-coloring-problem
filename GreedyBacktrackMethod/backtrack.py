from graph import Graph
from .heuristic_order import *
from .constraint_process import *
from .state import *


def backtracking(graph: Graph) -> []:
    domains = graph.domains
    assignments = graph.assignments
    state = graph.state

    if 0 not in assignments:
        return assignments

    variable = minimum_remaining_values(graph)
    for value in least_constraining_value(graph, variable):
        state.value_symmetry(variable, value)
        state.assign(variable, value)
        if constraint_checking(graph, variable, value):
            state.forward()
            result = backtracking(graph)
            if result is not None:
                return result
            state.backward()
        state.unassign(variable)
        state.data_recovery(domains, assignments)
        if not state.targeting(matcher=variable):
            return None
    state.jump_from(launcher=variable)
    return None


def backtrack(graph: Graph) -> []:
    graph.state.tme = time.time()
    solution = backtracking(graph)
    graph.state.update_bar(graph, NONE=solution is None)
    print()
    return solution
