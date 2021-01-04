from q14.shared import read_file
import re


class Memory:
    bit_width = 36
    mask = None

    def __init__(self):
        self.registers = dict()

    def process_instructions(self, insts):
        for inst in insts:
            self.process_instruction(inst)

    def process_instruction(self, inst):
        if 'mask' in inst:
            self.update_mask(inst.split(' ')[-1])
        else:
            res = re.findall(r'mem\[(\d+)\] = (\d+)', inst)
            register, val = list(map(int, res[0]))
            self.update_register(register, val)

    def update_mask(self, mask):
        self.mask = mask

    def get_masked_val(self, val):
        binary_val = "{0:b}".format(val).zfill(36)
        new_val = []
        for b_i, m_i in zip(binary_val, self.mask):
            if m_i != 'X':
                new_val.append(m_i)
            else:
                new_val.append(b_i)

        return ''.join(new_val)

    def update_register(self, register, val):
        new_val = self.get_masked_val(val)
        self.registers[register] = new_val

    def get_memory_val(self):
        return sum([int(v, base=2) for v in self.registers.values()])


def main():
    instructions = read_file()
    print(instructions)
    m = Memory()
    m.process_instructions(instructions)
    print(m.get_memory_val())
    print(m.registers)


if __name__ == '__main__':
    main()
