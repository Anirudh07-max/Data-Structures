# python3

class Heap:
    def __init__(self):
        self.swaps = []
        self.data = []
        self.n = 0

    def read(self):
        f = open('tests/04', 'r')
        self.n = int(f.readline())
        dat = f.readline().split()
        # self.n = int(input())
        # dat = map(int, input().split())
        self.data = list(dat)

    def shiftdown(self, i):
        j = int((i-1)/2)
        if self.data[i] < self.data[j] and i>=1:
            self.data[i], self.data[j] = self.data[j], self.data[i]
            self.swaps.append((j, i))
            self.shiftdown(j)

    def swap(self):
        for i in range(1, self.n):
            self.shiftdown(i)

    def write(self):
        n_swaps = len(self.swaps)
        print(n_swaps)
        for i in range(100):
            print(self.swaps[i][0], self.swaps[i][1])

if __name__ == '__main__':
    min_heap = Heap()
    min_heap.read()
    min_heap.swap()
    min_heap.write()