import sys
from itertools import combinations

universe, planet = map(int, input().split())
data = [list(map(int, sys.stdin.readline().split())) for i in range(universe)]
planet_case = combinations(range(planet), 2)
universe_case = combinations(range(universe), 2)
for i in universe_case:
    target1 = data[i[0]]
    target2 = data[i[1]]
    for j in planet_case:
        front, back = j[0], j[1]
        if (target1[front] - target1[back] > 0 and target2[front] - target2[back] > 0) or (target1[front] - target1[back] == 0 and target2[front] - target2[back] == 0):
            print(front)

