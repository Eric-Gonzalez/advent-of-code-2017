class CPUMaze(object):
    @staticmethod
    def run(instructions):
        steps = 0
        current_instruction_index = 0
        while current_instruction_index < len(instructions):
            next_instruction = instructions[current_instruction_index]
            instructions[current_instruction_index] = instructions[current_instruction_index] + 1
            current_instruction_index = current_instruction_index + next_instruction
            steps += 1
        return steps
