import util


class Memory:

    """Class representing main memory as an array of bytes."""

    def __init__(self, size, block_size):
        """Initialize main memory with a set number of bytes and block size."""
        self._size = size  # Memory size
        self._block_size = block_size  # Block size
        self._data = [util.rand_byte() for i in range(size)]

    def print_section(self, start, amount):
        """Print a section of main memory.

        :param int start: start address to print from
        :param int amount: amount of blocks to print
        """
        address_len = len(str(self._size - 1))
        start = start - (start % self._block_size)
        amount *= self._block_size

        if start < 0 or (start + amount) > self._size:
            raise IndexError

        print()
        for i in range(start, start + amount, self._block_size):
            print(util.dec_str(i, address_len) + ": " +
                  " ".join([util.hex_str(i, 2) for i in self.get_block(i)]))
        print()

    def get_block(self, address):
        """Get the block of main memory (of size self._block_size) that contains
        the byte at address.

        :param int address: address of byte within block of memory
        :return: block from main memory
        """
        start = address - (address % self._block_size)  # Start address
        end = start + self._block_size  # End address

        if start < 0 or end > self._size:
            raise IndexError

        return self._data[start:end]

    def set_block(self, address, data):
        """Set the block of main memory (of size self._block_size) that contains
        the byte at address.

        :param int address: address of byte within block of memory
        :param list data: bytes to set as block of memory
        """
        start = address - (address % self._block_size)  # Start address
        end = start + self._block_size  # End address

        if start < 0 or end > self._size:
            raise IndexError

        self._data[start:end] = data
