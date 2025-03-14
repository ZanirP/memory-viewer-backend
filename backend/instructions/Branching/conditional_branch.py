from ..instructions import Instruction

class Conditional_Branch_Instruction(Instruction):
    """
    Conditional Branch (CB) Instruction.
    Changes the program counter to the address of a specified label if a condition is met.
    """
    
    def __init__(self, condition, label):
        """
        Initialize the Conditional Branch instruction.

        Args:
            condition (function): The condition function to evaluate.
            label (str): The label to branch to if the condition is met.
        """
        self.condition = condition
        self.label = label
        
    def execute(self, registers, memory, labels, flags, pc):
        """
        Execute the Conditional Branch instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
            labels (dict): A dictionary of labels and their addresses.
            flags (dict): A dictionary of condition flags.
            pc (list): The program counter.
        """
        if self.condition(registers, flags):
            return labels[self.label]
        return pc[0] + 1
        
    def revert(self, pc, previous_pc):
        """
        Revert the Conditional Branch instruction.

        Args:
            pc (list): The program counter.
            previous_pc (int): The previous program counter value.
        """
        pc[0] = previous_pc