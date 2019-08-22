# coding: utf-8

import time


inicio = time.time()

n = 2
found = []

def next():
    global n
    n+=1
    return n

def is_perfect(n):
    global found
    dividers = [1]
    for x in range(2, (n/2)+1):
        if n % x == 0:
            dividers.append(x)
    if n == reduce((lambda x, y: x + y), dividers):
        found.append(n)
        print(n)

while len(found) < 100000:
    is_perfect(next())

fim = time.time()
print('\ntempo decorrido: %f segundos\n' % (fim - inicio))