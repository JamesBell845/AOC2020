from itertools import combinations
from functools import reduce

f = 'C:/WS/AOC/Day 1/input.txt'


print(reduce(lambda a,b: int(a)*int(b), list(filter(lambda x: int(x[0]) + int(x[1]) == 2020, list(combinations(list(open(f).readlines()), 2))))[0]))

#print(list(zip(l[::],l[1::])))

#print(list(map(lambda x: int(x), open(f).readlines()))