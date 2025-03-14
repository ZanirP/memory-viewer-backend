from ..instructions import Instruction

class ADD_Instruction(Instruction):
    """
    Add (ADD) Instruction.
    Adds the values of two registers and stores the result in a destination register.
    """
    
    def __init__(self, destination, reg1, reg2):
        """
        Initialize the ADD instruction.

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
        Execute the ADD instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        # TODO fix overflow issues
        self.isReverted = False
        self.previous_value = registers.get(self.destination)
        registers.set(self.destination, registers.get(self.reg1) + registers.get(self.reg2))
        
    def revert(self, registers, memory):
        """
        Revert the ADD instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        if self.previous_value is not None:
            registers.set(self.destination, self.previous_value)
            self.previous_value = None
            self.isReverted = True
        else:
            pass