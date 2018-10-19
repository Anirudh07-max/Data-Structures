# python3

class Heap:
    def __init__(self):
        self.swaps = []
        self.data = []
        self.n = 0

    def read(self):
        # f = open('tests/04', 'r')
        # self.n = int(f.readline())
        # dat = f.readline().split()
        self.n = int(input())
        dat = map(int, input().split())
        self.data = list(dat)
        # f.close()

    def shiftup(self, i):
        l = int(2*i + 1)
        r = l + 1
        if r < self.n:
            if self.data[i] > self.data[r] and self.data[i] > self.data[l]:
                if self.data[l] >= self.data[r]:
                    self.data[i], self.data[r] = self.data[r], self.data[i]
                    self.swaps.append((i, r))
                    self.shiftup(r)
                else:
                    self.data[i], self.data[l] = self.data[l], self.data[i]
                    self.swaps.append((i, l))
                    self.shiftup(l)
            elif self.data[i] > self.data[r]:
                self.data[i], self.data[r] = self.data[r], self.data[i]
                self.swaps.append((i, r))
                self.shiftup(r)
            elif self.data[i] > self.data[l]:
                self.data[i], self.data[l] = self.data[l], self.data[i]
                self.swaps.append((i, l))
                self.shiftup(l)
        elif l == self.n - 1:
            if self.data[i] > self.data[l]:
                self.data[i], self.data[l] = self.data[l], self.data[i]
                self.swaps.append((i, l))
                self.shiftup(l)

    def swap(self):
        for i in range(self.n - 1, -1, -1):
            self.shiftup(i)

    def write(self):
        n_swaps = len(self.swaps)
        print(n_swaps)
        for i in range(n_swaps):
            print(self.swaps[i][0], self.swaps[i][1])
        # for i in range(self.n):
        #     l = int(2 * i + 1)
        #     r = l + 1
        #     if r < self.n:
        #         if self.data[i] > self.data[r] or self.data[i] > self.data[l]:
        #             print(i, l, r)
        #             break
        #     elif l == self.n - 1:
        #         if self.data[i] > self.data[l]:
        #             print("error")
        #             print(i, l)
        #             break
        # print("All good")


if __name__ == '__main__':
    min_heap = Heap()
    min_heap.read()
    min_heap.swap()
    min_heap.write()