import os


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        txt = [l.strip() for l in f.readlines()]
    return txt


class HandHeldDevice:
    def __init__(self):
        self.accumulator = 0
        self.terminated = False
        self.line_num = 0
        self.states = []

    def step(self, instruction):
        if 'nop' in instruction:
            self.line_num += 1
            return

        if 'acc' in instruction:
            val = int(instruction.split(' ')[1])
            self.accumulator += val
            self.line_num += 1
            return

        if 'jmp' in instruction:
            val = int(instruction.split(' ')[1])
            self.line_num += val
            return

    def run(self, instructions):
        while not self.terminated:
            state = self.get_state()
            if state not in self.states:
                self.record_state(state)
            else:
                return self.states[-1]
            instruction = instructions[self.line_num]
            self.step(instruction)
            print(instruction, self.accumulator)

    def get_state(self):
        return self.line_num

    def record_state(self, state):
        self.states.append(state)

    def reset(self):
        self.states = []
        self.accumulator = 0
        self.line_num = 0
