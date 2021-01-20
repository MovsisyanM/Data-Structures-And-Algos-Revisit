class StackUnderflow(Exception):
    pass


class StackOverflow(Exception):
    pass


class Stack:
    def __init__(self, *items):
        *self.__s, = items[:]
        self.__top = len(items)

    def Push(self, *items):
        """Pushes the item to the top of the stack."""
        try:
            self._Stack__s += items
            self._Stack__top += 1
        except:
            raise StackOverflow("Failed to add an item to the stack")

    def Pop(self):
        """Pops an element from the top of the stack."""
        try:
            item = self._Stack__s.pop(self._Stack__top)
            self._Stack__top -= 1
            return item
        except:
            raise StackUnderflow("Failed to remove an item from the stack")

    def Top(self):
        """Returns the pointer value that points to the top of the stack."""
        # Shallow copy return of int
        return self._Stack__top

    def __len__(self):
        return self.Top()

    def IsEmpty(self):
        """Returns True if the stack contains 0 tiems, otherwise returns False."""
        return True if self._Stack__top == 0 else False

    def __repr__(self):
        print(self._Stack__s)

    def __str__(self):
        return str(self._Stack__s)

    def Contains(self, item):
        return item in self._Stack__s

# Code block by Movsisyan


# print("Creating stack containing 1, 2, 3 and printing it.")
# t = Stack(1, 2, 3)
# print(t)

# print("Pushing 999 to the stack and printing it.")
# t.Push(999)
# print(t)

# print("Pushing 7, 8 to the stack and printing it.")
# t.Push(7, 8)
# print(t)

# print("Popping 8 from the stack and printing the stack.")
# t.Pop()
# print(t)

# print(f"Is stack empty? {t.IsEmpty()}")
# print(f"Length of stack is: {len(t)}")

# Code block by Movsisyan
