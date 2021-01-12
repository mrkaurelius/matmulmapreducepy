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

result = 0

'''
A[i][k] * B[k][j] => C[i][j]
i m1 in satir sayisi
j m2 nin sutun sayisi
k m1 sutun sayisi
6 15 15 6
'''
iv = 6
jv = 6
kv = 15

for i in range(0, iv):
    for j in range(0, jv):
        for k in range(0, kv):
            if (i, k) in a and (k, j) in b:
                result = result+a[(i, k)]*b[(k, j)]
        print('({0},{1})\t{2}'.format(i, j, result))
        result = 0
