class Tape():
    # A node is a single square on the 'tape'
    class Node():
        def __init__(self):
            self.prev = None
            self.next = None
            self.val = 0

    def __init__(self):
        self.current = self.Node()

    def read(self):
        return self.current.val

    def write(self, data: int):
        self.current.val = data

    def increment(self):
        self.current.val += 1
    
    def decrement(self):
        self.current.val -= 1

    def goLeft(self):
        if not self.current.prev:
            self.current.prev = self.Node()
            self.current.prev.next = self.current
        self.current = self.current.prev

    def goRight(self):
        if not self.current.next:
            self.current.next = self.Node()
            self.current.next.prev = self.current
        self.current = self.current.next

    def __str__(self):
        result: str = ''
        temp = self.current
        while temp.prev:
            temp = temp.prev
        while temp:
            result += f'{temp.val} '
            temp = temp.next
        return result