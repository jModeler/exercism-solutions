class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cbuffer = [[]] * self.capacity
        self.item_age = [0] * self.capacity

    def read(self):
        # check if empty, raise BufferEmptyException
        empty_check = list(map(len, self.cbuffer))
        if sum(empty_check) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        else:
            # get the index for the item that is oldest
            ind = self.item_age.index(max(self.item_age))
            val = self.cbuffer[ind][0]
            # replace the value with an empty list
            self.cbuffer[ind] = []
            # update the item age
            self.item_age[ind] = 0
            return val

    def write(self, data):
        # check if full, raise BufferFullException
        if 0 not in self.item_age:
            raise BufferFullException("Circular buffer is full")
        else:
            # write into an empty slot, whichever one has age == 0
            ind = self.item_age.index(0) # will give us the first empty buffer slot
            self.cbuffer[ind] = [data]
            # update the item ages of all other items
            self.item_age = [age + 1 if age != 0 else age for age in self.item_age]
            # update the item age for the item just written
            self.item_age[ind] = 1

    def overwrite(self, data):
        if 0 in self.item_age:
            self.write(data)
        else:
            # get the index of the item with the max age
            ind = self.item_age.index(max(self.item_age))
            # replace this element
            self.cbuffer[ind] = [data]
            # update the item ages of all other items
            self.item_age = [age + 1 if age != 0 else age for age in self.item_age]
            # update the item age for the item just over-written
            self.item_age[ind] = 1

    def clear(self):
        # work only on non-empty buffers
        empty_check = list(map(len, self.cbuffer))
        if sum(empty_check) != 0:
            self.item_age = [0] * self.capacity
            self.cbuffer = [[]] * self.capacity
