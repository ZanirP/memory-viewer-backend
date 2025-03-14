from ..instructions import Instruction

class LSL_Instruction(Instruction):
    """
    Logical Shift Left (LSL) Instruction.
    Shifts the value of a register to the left by a specified amount.
    """
    
    def __init__(self, destination, reg, shift_amount):
        """
        Initialize the LSL instruction.

        Args:
            destination (str): The destination register.
            reg (str): The source register.
            shift_amount (int): The amount to shift.
        """
        self.destination = destination
        self.reg = reg
        self.shift_amount = int(shift_amount)
        self.previous_value = None
        self.isReverted = False
        
    def execute(self, registers, memory):
        """
        Execute the LSL instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        self.previous_value = registers.get(self.destination)
        result = registers.get(self.reg) << self.shift_amount
        registers.set(self.destination, result & 0xFFFFFFFFFFFFFFFF)
        self.isReverted = False
        
    def revert(self, registers, memory):
        """
        Revert the LSL instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        if self.previous_value is not None:
            registers.set(self.destination, self.previous_value)
            self.previous_value = None
            self.isReverted = True

