from ..instructions import Instruction

class MUL_Instruction(Instruction):
    """
    Multiply (MUL) Instruction.
    Multiplies the values of two registers and stores the result in a destination register.
    """

    def __init__(self, destination, reg1, reg2):
        """
        Initialize the MUL instruction.

        Args:
            destination (str): The destination register.
            reg1 (str): The first source register.
            reg2 (str): The second source register.
        """
        self.destination = destination
        self.reg1 = reg1
        self.reg2 = reg2
        self.previous_value = None
        self.isReverted = False

    def execute(self, registers, memory):
        """
        Execute the MUL instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        # for now we are going to assume 64-bit multiplcation
        # edge cases to consider: overflow, signed mult vs unsigned (we gonna assume signed)
        # MUL does not handle immediate values

        self.previous_value = registers.get(self.destination)
        registers.set(self.destination, (registers.get(self.reg1) * registers.get(self.reg2)) & 0xFFFFFFFFFFFFFFFF)
        self.isReverted = False

    def revert(self, registers, memory):
        """
        Revert the MUL instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        if self.previous_value is not None:
            registers.set(self.destination, self.previous_value)
            self.previous_value = None
            self.isReverted = True