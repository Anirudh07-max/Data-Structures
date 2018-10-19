# python3

class Heap:
    def __init__(self):
        self.data = []
        self.jobs = []
        self.n = 0
        self.m = 0
        self.result = []


    def shiftdown(self, i):
        l = int((2 * i) + 1)
        r = l + 1
        if r < self.n:
            if self.data[i][1] > self.data[l][1] and self.data[i][1] > self.data[r][1]:
                if self.data[l][1] > self.data[r][1]:
                    self.data[i], self.data[r] = self.data[r], self.data[i]
                    self.shiftdown(r)
                elif self.data[l][1] < self.data[r][1]:
                    self.data[i], self.data[l] = self.data[l], self.data[i]
                    self.shiftdown(l)
                else:
                    if self.data[l][0] < self.data[r][0]:
                        self.data[i], self.data[l] = self.data[l], self.data[i]
                        self.shiftdown(l)
                    else:
                        self.data[i], self.data[r] = self.data[r], self.data[i]
                        self.shiftdown(r)

            elif self.data[i][1] > self.data[l][1]:
                self.data[i], self.data[l] = self.data[l], self.data[i]
                self.shiftdown(l)

            elif self.data[i][1] > self.data[r][1]:
                self.data[i], self.data[r] = self.data[r], self.data[i]
                self.shiftdown(r)

            elif self.data[i][1] == self.data[l][1] and self.data[i][1] == self.data[r][1]:
                if self.data[i][0] > self.data[l][0] and self.data[i][0] > self.data[r][0]:
                    if self.data[l][0] < self.data[r][0]:
                        self.data[i], self.data[l] = self.data[l], self.data[i]
                        self.shiftdown(l)
                    else:
                        self.data[i], self.data[r] = self.data[r], self.data[i]
                        self.shiftdown(r)
                elif self.data[i][0] > self.data[l][0]:
                    self.data[i], self.data[l] = self.data[l], self.data[i]
                    self.shiftdown(l)
                elif self.data[i][0] > self.data[r][0]:
                    self.data[i], self.data[r] = self.data[r], self.data[i]
                    self.shiftdown(r)

            elif self.data[i][1] == self.data[l][1]:
                if self.data[l][0] < self.data[i][0]:
                    self.data[i], self.data[l] = self.data[l], self.data[i]
                    self.shiftdown(l)

            elif self.data[i][1] == self.data[r][1]:
                if self.data[r][0] < self.data[i][0]:
                    self.data[i], self.data[r] = self.data[r], self.data[i]
                    self.shiftdown(r)

        elif l == self.n - 1:
            if self.data[i][1] > self.data[l][1]:
                self.data[i], self.data[l] = self.data[l], self.data[i]
                self.shiftdown(l)
            elif self.data[i][1] == self.data[l][1]:
                if self.data[i][0] > self.data[l][0]:
                    self.data[i], self.data[l] = self.data[l], self.data[i]
                    self.shiftdown(l)

    def read(self):
        # f = open('tests/02', 'r')
        # self.n, self.m = map(int, f.readline().split())
        # dat = f.readline().split()
        self.n, self.m = map(int, input().split())
        for i in range(0, self.n):
            self.data.append((i, 0))
        # self.jobs = list(map(int, f.readline().split()))
        self.jobs = list(map(int, input().split()))
        # f.close()

    def assign(self):
        for k in range(0, self.m):
            self.result.append(self.data[0])
            self.data[0] = (self.data[0][0], self.data[0][1] + self.jobs[k])
            self.shiftdown(0)

    def write(self):
        for i in range(0, self.m):
            print(self.result[i][0], self.result[i][1])

if __name__ == '__main__':
    job_queue = Heap()
    job_queue.read()
    job_queue.assign()
    job_queue.write()