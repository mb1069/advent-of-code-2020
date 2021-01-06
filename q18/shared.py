import os


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        problems = f.readlines()
    return [p.strip() for p in problems]


class Problem:
    def __init__(self, txt_description):
        self.blobs = txt_description

        self.stack_val = None
        self.operator = None

    def solve(self):
        while len(self.blobs):
            if '(' in self.blobs[0]:
                self.sub_problem()
                continue

            blob = self.blobs.pop(0)

            if not any([c in blob for c in ['*', '+', '(', ')']]):
                blob = int(blob)
                if self.stack_val is None:
                    self.stack_val = blob
                else:
                    if self.operator == '+':
                        self.stack_val += blob
                    elif self.operator == '*':
                        self.stack_val *= blob
            else:
                self.operator = blob

        return self.stack_val

    def sub_problem(self):
        depth = self.blobs[0].count('(')
        end = 1
        while depth > 0:
            depth = (depth - (self.blobs[end].count(')')) + (self.blobs[end].count('(')))
            end += 1

        subproblem_blobs = self.blobs[0:end]
        subproblem_blobs[0] = subproblem_blobs[0][1:]

        subproblem_blobs[-1] = subproblem_blobs[-1][:-1]
        subproblem = Problem(subproblem_blobs)

        self.blobs = [str(subproblem.solve())] + self.blobs[end:]