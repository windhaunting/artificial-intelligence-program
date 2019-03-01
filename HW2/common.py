import itertools

class Sudoku:

    numbers = '012345678'

    def __init__(self, sudoMat):
        self.variables = list(),
        self.domains = dict(),
        self.constraints = list()
        self.neighbors = dict()
        self.pruned = dict()

        strLst = []
        for i in range(0, 9):
            for j in range(0, 9):
                strLst.append(str(sudoMat[i][j]))
                

        self.variables = self.combine(self.numbers, self.numbers)

        #print ("variables: ", self.variables)
        self.domains = {v: list(range(1, 10)) if strLst[i] == '0' else [int(strLst[i])] for i, v in enumerate(self.variables)}
        #print ("domains: ", self.domains)

        self.pruned = {v: list() if strLst[i] == '0' else [int(strLst[i])] for i, v in enumerate(self.variables)}
        #print ("pruned: ", self.pruned)


        blocks = (
            [self.combine(self.numbers, number) for number in self.numbers] +
            [self.combine(num, self.numbers) for num in self.numbers] +
            [self.combine(numTriA, numTriB) for numTriA in ('012', '345', '678') for numTriB in ('012', '345', '678')]
        )

        for block in blocks:
            combinations = self.permutate(block)
            for combination in combinations:
                if [combination[0], combination[1]] not in self.constraints:
                    self.constraints.append([combination[0], combination[1]])

        for x in self.variables:
            self.neighbors[x] = list()
            for c in self.constraints:
                if x == c[0]:
                    self.neighbors[x].append(c[1])

        #print ("neighbors: ", self.neighbors)

    def solved(self):

        for v in self.variables:
            if len(self.domains[v]) > 1:
                return False

        return True

    def consistent(self, assignment, var, value):

        consistent = True

        for key, val in assignment.items():
            if val == value and key in self.neighbors[var]:
                consistent = False

        return consistent

    @staticmethod
    def constraint(xi, xj): return xi != xj

    @staticmethod
    def combine(alpha, beta):
        return [a + b for a in alpha for b in beta]

    @staticmethod
    def permutate(iterable):
        result = list()

        for L in range(0, len(iterable) + 1):
            if L == 2:
                for subset in itertools.permutations(iterable, L):
                    result.append(subset)

        return result
