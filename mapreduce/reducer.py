#!/usr/bin/env python
import sys

a = {}
b = {}

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    v = value.split(',')
    if key == 'a':
        a[(int(v[1]), int(v[2]))] = float(v[3])
    elif key == 'b':
        b[(int(v[1]), int(v[2]))] = float(v[3])

# print(a)
# print(b)
# print(a[(0, 1)])
result = 0

'''
A[i][k] * B[k][j] => C[i][j]
'''


for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if (i, k) in a and (k, j) in b:
                result = result+a[(i, k)]*b[(k, j)]
        print('({0},{1})\t{2}'.format(i, j, result))
        result = 0
