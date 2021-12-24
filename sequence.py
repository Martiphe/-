import itertools

class Fib:
    class _Fib_iter:

        def __init__(self):
            self.data = []
            self.data.append(0)
            self.data.append(1)
            self.count = 0

        def __next__(self):
            if self.count < 2:
                self.count += 1
                return self.data[self.count - 1]
            self.data.append(self.data[self.count - 1] + self.data[self.count - 2])
            self.count += 1
            return self.data[self.count - 1]

    def __iter__(self):
        return Fib._Fib_iter()

Dike = Fib()
print(list(itertools.islice(Fib(), 50)))








