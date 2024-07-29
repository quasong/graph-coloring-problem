from graph import Graph
from GreedyBacktrackMethod.backtrack import backtrack


def final_check(graph: Graph, solution: []):
    for var in range(graph.n):
        for neighbor in graph.adj[var]:
            if solution[var] == solution[neighbor]:
                return False
    return True


if __name__ == '__main__':
    firstname = 'le450_'
    filename = firstname + input(f'last name(i.e. 5a, 15b, 25c...) of {firstname} > ')
    graph = Graph(filename)

    print("\033[31m"
          "Warning ⚠️ The following techniques might lead the algorithm to no solution, "
          "use them cautiously.\033[0m\n"
          "Enter 'n' to disable a specific technique.")

    graph.state.RANDOM = input('Random choice from MRV-DHed variables 😨 > ') != 'n'
    graph.state.FILTER = input('Filter values after LCV sorting       😰 > ') != 'n'
    graph.state.JUMPING = input('Enable Conflict-Directed Backjumping  😱 > ') != 'n'

    solution = backtrack(graph)

    if solution:
        print(f'The solution is {final_check(graph, solution)}')
        if input('show solution? y/n ') == 'y':
            print(solution)
    else:
        print('No solution')
