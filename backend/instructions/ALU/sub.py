from ..instructions import Instruction

class SUB_Instruction(Instruction):
    """
    Subtract (SUB) Instruction.
    Subtracts the value of one register from another and stores the result in a destination register.
    """
    
    def __init__(self, destination, reg1, reg2):
        """
        Initialize the SUB instruction.

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
        Execute the SUB instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        self.previous_value = registers.get(self.destination)
        registers.set(self.destination, registers.get(self.reg1) - registers.get(self.reg2))
        self.isReverted = False
        
    def revert(self, registers, memory):
        """
        Revert the SUB instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        if self.previous_value is not None:
            registers.set(self.destination, self.previous_value)
            self.previous_value = None
            self.isReverted = True