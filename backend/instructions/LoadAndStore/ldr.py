from ..instructions import Instruction

class LDR_Instruction(Instruction):
    """
    Load Register (LDR) Instruction.
    Loads a double word from memory into a register.
    """

    def __init__(self, destination, base, offset=0):
        """
        Initialize the LDR instruction.

        Args:
            destination (str): The destination register.
            base (str): The base register.
            offset (int, optional): The offset value. Defaults to 0.
        """
        self.destination = destination
        self.base = base
        self.offset = offset
        self.previous_value = None
        self.isReverted = False

    def execute(self, registers, memory):
        """
        Execute the LDR instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.

        Raises:
            ValueError: If the memory address is not aligned.
        """
        address = registers.get(self.base) + self.offset

        if address % 8 != 0:
            raise ValueError("Unaligned memory access")

        self.previous_value = registers.get(self.destination)
        loaded_value = memory.load_double_word(address)
        registers.set(self.destination, loaded_value)
        self.isReverted = False

    def revert(self, registers):
        """
        Revert the LDR instruction.

        Args:
            registers (Registers): The registers object.
        """
        if self.previous_value is not None:
            registers.set(self.destination, self.previous_value)
            self.previous_value = None
            self.isReverted = True
