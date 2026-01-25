class EmptyListException(Exception):
    def __init__(self, message = "The list is empty."):
        super().__init__(message)


class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=None):
        if values:
            current = Node(values[0])
            for value in values[1:]:
                new_node = Node(value)
                new_node._next = current
                current = new_node
            self._head = current
        else:
            self._head = None

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.value()
            current = current.next()

    def __len__(self):
        ll = 0
        current = self._head
        while current is not None:
            ll += 1
            current = current.next()
        return ll

    def head(self):
        if self._head is None:
            raise EmptyListException()
        else:
            return self._head

    def push(self, value):
        if self._head is None:
            self._head = Node(value)
        else:
            current = self._head
            self._head = Node(value)
            self._head._next = current

    def pop(self):
        if self._head is None:
            raise EmptyListException()

        current = self._head
        popped_value = current.value()
        self._head = current._next

        return popped_value

    def reversed(self):
        past = None
        current = self._head

        while current is not None:
            next_node = current._next
            current._next = past
            past = current
            current = next_node

        self._head = past
        return self
