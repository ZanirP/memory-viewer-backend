from ..instructions import Instruction

class STR_Instruction(Instruction):
    """
    Store Register (STR) Instruction.
    Stores a double word from a register into memory.
    """

    def __init__(self, reg, base, offset=0):
        """
        Initialize the STR instruction.

        Args:
            reg (str): The source register.
            base (str): The base register.
            offset (int, optional): The offset value. Defaults to 0.
        """
        self.reg = reg
        self.base = base
        self.offset = offset
        self.previous_value = None
        self.isReverted = False

    def execute(self, registers, memory):
        """
        Execute the STR instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.

        Raises:
            ValueError: If the base register is invalid.
        """
        value = registers.get(self.base)

        if self.base is None or not isinstance(self.base, int):
            raise ValueError("Invalid base register")

        address = value + self.offset

        self.previous_value = memory.load_double_word(address)

        value_store = registers.get(self.reg)
        memory.store_double_word(address, value_store)
        self.isReverted = False

    def revert(self, registers, memory):
        """
        Revert the STR instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        if self.previous_value is not None:
            address = registers.get(self.base) + self.offset
            memory.store_double_word(address, self.previous_value)
            self.previous_value = None
            self.isReverted = True
