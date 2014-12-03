__author__ = 'jeudy'

import mpi4py.MPI as MPI
import numpy as np
import time

N = 10000

def foo(n):
    res = 0
    i = 0
    j = 0
    while i < n:
        while j < n:
            res = i * j
            j += 1
        i += 1
    return res

if not MPI.Is_initialized():
    MPI.Init()

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
size = comm.Get_size()

start = time.time()

for k in range(0, N/size):
    foo(N)

end = time.time()

print "Node %s done in %s" % (myid, end - start)