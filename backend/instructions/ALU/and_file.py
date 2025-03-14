from ..instructions import Instruction

class AND_Instruction(Instruction):
    """
    Logical AND (AND) Instruction.
    Performs a bitwise AND operation between two registers or a register and an immediate value.
    """

    def __init__(self, destination, reg1, reg2_or_immediate):
        """
        Initialize the AND instruction.

        Args:
            destination (str): The destination register.
            reg1 (str): The first source register.
            reg2_or_immediate (str): The second source register or an immediate value.
        """
        self.destination = destination
        self.reg1 = reg1
        self.reg2_or_immediate = reg2_or_immediate
        self.is_immiedate = reg2_or_immediate.startswith("X") == False
        self.previous_value = None
        self.isReverted = False

    def execute(self, registers, memory):
        """
        Execute the AND instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        self.previous_value = registers.get(self.destination)
        self.isReverted = False

        if self.is_immiedate:
            result = registers.get(self.reg1) & int(self.reg2_or_immediate)
        else:
            result = registers.get(self.reg1) & registers.get(self.reg2_or_immediate)

        registers.set(self.destination, result & 0xFFFFFFFFFFFFFFFF)

    def revert(self, registers, memory):
        """
        Revert the AND instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        if self.previous_value is not None:
            registers.set(self.destination, self.previous_value)
            self.previous_value = None
            self.isReverted = True