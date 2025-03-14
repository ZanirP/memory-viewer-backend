from ..instructions import Instruction

class No_Instruction(Instruction):
    """
    No Operation (NOP) Instruction.
    Represents an instruction that does nothing.
    """

    def __init__(self):
        """
        Initialize the NOP instruction.
        """
        print("NO INSTRUCTION FOUND")
        self.isReverted = False

    def execute(self, registers, memory):
        """
        Execute the NOP instruction.

        Args:
            registers (Registers): The registers object.
            memory (Memory): The memory object.
        """
        pass

    def revert(self, registers):
        """
        Revert the NOP instruction.

        Args:
            registers (Registers): The registers object.
        """
        pass