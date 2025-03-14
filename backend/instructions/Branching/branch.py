# This file contains the implementation of the branch instruction
from ..instructions import Instruction

class Branch_Instruction(Instruction):
    """
    Branch (B) Instruction.
    Changes the program counter to the address of a specified label.
    """
    
    def __init__(self, label):
        """
        Initialize the Branch instruction.

        Args:
            label (str): The label to branch to.
        """
        self.label = label
        
    def execute(self, registers, memory, labels, pc):
        """
        Execute the Branch instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
            labels (dict): A dictionary of labels and their addresses.
            pc (list): The program counter.
        """
        if self.label in labels:
            pc[0] = labels[self.label]
        else:
            raise ValueError(f"Undefined label: {self.label}")
        
    def revert(self, pc, previous_pc):
        """
        Revert the Branch instruction.

        Args:
            pc (list): The program counter.
            previous_pc (int): The previous program counter value.
        """
        pc[0] = previous_pc

