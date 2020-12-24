import copy

from q8.shared import read_file, HandHeldDevice


class HandHeldDeviceFixer(HandHeldDevice):
    def run(self, instructions):
        while not self.terminated:
            if self.line_num > len(instructions) - 1:
                self.terminated = True
                break

            state = self.get_state()
            if state not in self.states:
                self.record_state(state)
            else:
                return self.states[-1]
            instruction = instructions[self.line_num]
            self.step(instruction)
            print(instruction, self.accumulator, self.states)

    def get_state(self):
        return self.line_num

    def record_state(self, state):
        self.states.append(state)


def main():
    _instructions = read_file()
    dev = HandHeldDeviceFixer()
    for i, inst in enumerate(_instructions):
        instructions = copy.deepcopy(_instructions)
        if 'nop' in inst:
            instructions[i] = 'jmp' + inst[3:]
        elif 'jmp' in inst:
            instructions[i] = 'nop' + inst[3:]
        else:
            continue
        print(f'Swapped {inst} for {instructions[i]}')

        dev.run(instructions)
        if dev.terminated:
            print(f'Terminated: {dev.accumulator}')
            break
        else:
            dev.reset()
            print(' ')


if __name__ == '__main__':
    main()
