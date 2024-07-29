import random


def max_degree(graph, variables: []) -> int:

    adj = graph.adj
    assignments = graph.assignments

    """ Sort the variables list according to the degree of each variable. 
        The degree is determined by counting the number of unassigned neighboring variables.
        Reverse order to have the variable with the highest degree at the beginning of the list.
        variables sorted by number of degrees. """

    degrees = {var: sum(assignments[i] == 0 for i in adj[var])
               for var in variables}
    md = max(degrees.values())
    variables = [var for var in variables if degrees[var] == md]

    if graph.state.RANDOM:
        return random.choice(variables)
    return next(iter(variables))


def minimum_remaining_values(graph) -> int:

    n = graph.n
    domains = graph.domains
    assignments = graph.assignments

    """ Minimum Remaining Values (MRV) heuristic for variable ordering
        The MRV heuristic selects the variable with the smallest domain 
        (i.e., fewest remaining legal values) for assignment next. """

    variables = [var for var in range(n) if assignments[var] == 0]
    mrv = len(domains[min(variables, key=lambda var: len(domains[var]))])
    variables = [var for var in variables if len(domains[var]) == mrv]

    return max_degree(graph, variables)


def least_constraining_value(graph, var: int) -> [int]:

    adj = graph.adj
    domains = graph.domains

    """ Least Constraining Value (LCV) heuristic for value ordering. 
        The LCV heuristic orders the values in the domain of the variable 
        to be assigned based on the number of conflicts each value would 
        create in the remaining unassigned variables. 
        The values that would create fewer conflicts are ordered first. """

    if not graph.state.FILTER:
        values = sorted(domains[var],
                        key=lambda value:
                        sum(value in domains[neighbor] for neighbor in adj[var]))
        return values

    """ to computes a measure of conflict for each possible value of the variable, 
        determines an average conflict level, and then constructs a sorted list 
        of those values that cause less-equal-than-average conflicts. """

    # conflicts as c is a dict
    # for c.key in domains[var]
    # c.value is number of c.key's conflicts
    conflicts = {value: sum(value in domains[neighbor]
                            for neighbor in adj[var])
                 for value in domains[var]}
    average = sum(conflicts.values()) / len(conflicts)
    values = sorted([value for value in conflicts.keys() if conflicts[value] <= average],
                    key=lambda value: conflicts[value])

    return values
