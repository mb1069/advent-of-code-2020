from q14.shared import read_file
import re
import copy


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

            registers = self.get_memory_addresses(register)
            for register in registers:
                self.update_register(register, val)

    def update_mask(self, mask):
        self.mask = mask

    def get_masked_val(self, val):
        binary_val = "{0:b}".format(val).zfill(36)
        new_vals = []
        for i, (b_i, m_i) in enumerate(zip(binary_val, self.mask)):
            if m_i == '0':
                char = b_i
            elif m_i == '1':
                char = '1'
            else:
                char = 'X'
                _new_vals = []
            new_vals.append(char)
        return new_vals

    def update_register(self, register, val):
        self.registers[register] = val

    def get_memory_addresses(self, register):
        binary_register = "{0:b}".format(register).zfill(36)
        addresses = [[]]
        for b_i, m_i in zip(binary_register, self.mask):
            if m_i == '0':
                char = b_i
                for val in addresses:
                    val.append(char)
            if m_i == '1':
                char = '1'
                for val in addresses:
                    val.append(char)

            if m_i == 'X':
                new_vals = []
                _current_values = copy.deepcopy(addresses)
                for v in addresses:
                    for char in ['0', '1']:
                        new_vals.append(v + [char])
                addresses = new_vals
        addresses = [int(''.join(v), base=2) for v in addresses]
        return addresses

    def get_memory_val(self):
        return sum([v for v in self.registers.values()])


def main():
    instructions = read_file()
    m = Memory()
    m.process_instructions(instructions)
    print(m.get_memory_val())


if __name__ == '__main__':
    main()
