"""
Hola mundo en python
"""

import numpy
import mpi4py.MPI as MPI

if not MPI.Is_initialized():
    MPI.Init()

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
size = comm.Get_size()
N = 10
chunk = N / size
rest = N % size

data = numpy.empty(N, dtype='d')

if myid == 0:
    data = numpy.random.sample(N)
    print 'Data in root is: ', data

comm.Bcast([data, MPI.DOUBLE], root=0)

start = myid * chunk
end = start + chunk + (rest if myid == size - 1 else 0)

result = numpy.array([0.], dtype='d')

mysum = numpy.array(data[start:end].sum())

print 'I am process %s and my range goes from %s to %s' % (myid, start, end), data[start:end], mysum

comm.Reduce([mysum, MPI.DOUBLE], [result, MPI.DOUBLE], op=MPI.SUM, root=0)

if myid == 0:
    print 'Reduced sum is: %s. From original data: %s' % (result[0], data.sum())

MPI.Finalize()