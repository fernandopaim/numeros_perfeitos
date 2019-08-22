# coding: utf-8

import threading
import time
import multiprocessing


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

threads = []
number_threads = multiprocessing.cpu_count()
for x in range(number_threads):
    t = threading.Thread(target=is_perfect, args=(next(),))
    threads.append(t)
    t.start()

while len(found) < 100000:
    for t in threads:
        if not t.isAlive():
            threads.remove(t)
            t = threading.Thread(target=is_perfect, args=(next(),))
            threads.append(t)
            t.start()

for t in threads:
    t.join()

fim = time.time()
print('\ntempo decorrido: %f segundos\n' % (fim - inicio))