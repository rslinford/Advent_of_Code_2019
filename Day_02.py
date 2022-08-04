import unittest


def run_program(program):
    pc = 0
    while program[pc] != 99:
        op_index_1 = program[pc + 1]
        op_index_2 = program[pc + 2]
        target_index = program[pc + 3]
        op_1 = program[op_index_1]
        op_2 = program[op_index_2]

        match program[pc]:
            case 1:
                program[target_index] = op_1 + op_2
            case 2:
                program[target_index] = op_1 * op_2
        pc += 4
    return program[0]


filename = 'Day_02_data.txt'
with open(filename, 'r') as f:
    program = [int(x) for x in f.read().strip().split(',')]
print(program)
# todo mod program prior
result = run_program(program)


class TestProgram(unittest.TestCase):
    def test_run_program(self):
        result = run_program([1, 0, 0, 0, 99])
        self.assertEqual(2, result)

        program = [2, 3, 0, 3, 99]
        run_program(program)
        self.assertEqual([2, 3, 0, 6, 99], program)

        program = [2, 4, 4, 5, 99, 0]
        run_program(program)
        self.assertEqual([2, 4, 4, 5, 99, 9801], program)

        program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        result = run_program(program)
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], program)


if __name__ == '__main__':
    unittest.main()
