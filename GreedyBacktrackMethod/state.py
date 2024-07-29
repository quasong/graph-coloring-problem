import time
import sys


class State:
    def __init__(self, graph):
        self.graph = graph
        self.btk = 0                # backtracking
        self.tme = time.time()      # time
        self.level = 0              # recursion stack depth
        self.jumpto = None
        self.assign_stack = []
        self.assign_log = [[] for _ in range(graph.n)]
        self.domain_log = [[] for _ in range(graph.n)]
        self.RANDOM = True
        self.FILTER = True
        self.JUMPING = True

    def update_bar(self, graph, NONE=False):
        level = len([value for value in graph.assignments if value != 0])
        depth = graph.n
        emoji = '😪'
        if level == depth:
            emoji = '🥳'
        elif NONE:
            emoji = '😵'
        p = int(level / depth * 100)
        q = 99 - p
        r = '-'
        if p <= 50:
            left = r * (p // 2) + " " * ((q // 2) - 24)
            right = " " * 25
        else:
            left = r * 25
            right = r * ((p // 2) - 24) + ' ' * (q // 2)
        if p < 10:
            left += ' '
        elif p == 100:
            right = right.replace('--', '', 1)
        bar = '[' + left + str(p) + "%" + emoji + right + ']'
        tme = time.time() - self.tme
        state = ' ' + str(round(tme, 1)) + 's'
        state += ' ⤴ ' + str(self.btk)
        sys.stdout.write('\033[1;32m ' + bar + state + '\r\033[0m')
        sys.stdout.flush()

    def value_symmetry(self, variable, value):
        if value not in self.graph.assignments:
            self.graph.domains[variable] = {value}

    def forward(self):
        self.update_bar(self.graph)
        self.level += 1

    def backward(self):
        self.level -= 1
        self.btk += 1

    def data_recovery(self, domains, assignments):
        while self.assign_log[self.level]:
            assignments[self.assign_log[self.level].pop()] = 0
        while self.domain_log[self.level]:
            (var, val) = self.domain_log[self.level].pop()
            domains[var].add(val)

    def jump_from(self, launcher):
        if self.JUMPING:
            self.jumpto = next(iter(var for var in self.assign_stack[::-1] if var in self.graph.adj[launcher]), None)

    def targeting(self, matcher):
        if self.JUMPING and self.jumpto is not None:
            if matcher != self.jumpto:
                return False
            self.jumpto = None
        return True

    def assign(self, variable, value):
        self.graph.assignments[variable] = value
        self.assign_stack.append(variable)

    def unassign(self, variable):
        self.graph.assignments[variable] = 0
        self.assign_stack.pop()
