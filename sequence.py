import itertools

class Fib:

    class _Fib_iter:

        def __init__(self):
            self.previous_second = 0
            self.previous_first = 1
            self.next = 1

        def __next__(self):
            f = self.next
            self.next = self.previous_second + self.previous_first
            self.previous_second = self.previous_first
            self.previous_first = self.next
            return f

    def __iter__(self):
        return Fib._Fib_iter()

Dike = Fib()
print(list(itertools.islice(Fib(), 50)))











