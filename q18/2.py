from q18.shared import read_file


def find_closing_bracket(subproblem):
    stack = 1
    i = 1
    while stack > 0:
        if subproblem[i] == ')':
            stack -= 1
        if subproblem[i] == '(':
            stack += 1
        i += 1
    return i


def solve(problem):
    # Solution: recursive evaluation of problem following order of operations
    problem = list(problem)
    problem = list(filter(lambda c: c != ' ', problem))
    while len(problem) > 1:
        if '(' in problem:
            b_start = problem.index('(')
            b_end = find_closing_bracket(problem[b_start:]) + b_start - 1
            subproblem = solve(problem[b_start + 1:b_end])
            return solve(problem[0:b_start] + [subproblem] + problem[b_end + 1:])

        if '+' in problem:
            i = problem.index('+')
            b_start = i - 1
            b_end = i + 1
            op1 = problem[b_start]
            op2 = problem[b_end]
            val = int(op1) + int(op2)
            print(problem[0:b_start] + [str(val)] + problem[b_end + 1:])
            return solve(problem[0:b_start] + [str(val)] + problem[b_end + 1:])

        if '*' in problem:
            i = problem.index('*')
            b_start = i - 1
            b_end = i + 1
            op1 = problem[b_start]
            op2 = problem[b_end]
            val = int(op1) * int(op2)
            print(problem[0:b_start] + [str(val)] + problem[b_end + 1:])
            return solve(problem[0:b_start] + [str(val)] + problem[b_end + 1:])

    return int(problem[0])


def main():
    problems = read_file()
    total = 0
    for p_txt in problems:
        solution = solve(p_txt)
        print(solution)
        print('\n')

        total += solution
    print(total)


if __name__ == '__main__':
    main()
