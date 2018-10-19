# python3

import sys
sys.setrecursionlimit(100000)
# f = open('tests/116', 'r')
# n, m = map(int, f.readline().split())
# lines = list(map(int, f.readline().split()))
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # while parent[table] != table:
    #     table = parent[table]
    # return table

    if parent[table] == table:
        return table
    else:
        table = parent[table]
        table = getParent(table)
    return table

def merge(destination, source, ans):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return ans
    else:
        if lines[realDestination] >= lines[realSource]:
            lines[realDestination] = lines[realDestination] + lines[realSource]
            parent[realSource] = parent[realDestination]
            if lines[realDestination] > ans:
                ans = lines[realDestination]
        else:
            lines[realSource] = lines[realDestination] + lines[realSource]
            parent[realDestination] = parent[realSource]
            if lines[realSource] > ans:
                ans = lines[realSource]
    return ans


for i in range(m):
    # destination, source = map(int, f.readline().split())
    destination, source = map(int, sys.stdin.readline().split())
    ans = merge(destination - 1, source - 1, ans)
    print(ans)
# f.close()