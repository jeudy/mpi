# -*- coding: UTF-8 -*-
import numpy
import mpi4py.MPI as MPI

N = 100000000  # int(raw_input('Digite el N: '))

if not MPI.Is_initialized():
    MPI.Init()

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
size = comm.Get_size()

chunk = N / size
rest = N % size

start = (myid * chunk) + 1
end = start + chunk + (rest if myid == size - 1 else 0)


my_acum = numpy.array([1.0])

i = start

while i < end:
    # Producto de Wallis
    my_acum[0] *= ((2.*i / (2.*i - 1)) * (2.*i / (2.*i + 1)))
    i += 1

print 'Soy proceso %s y mi acum es: %s' % (myid, my_acum[0])

result = numpy.array([1.], dtype='d')

comm.Reduce([my_acum, MPI.DOUBLE], [result, MPI.DOUBLE], op=MPI.PROD, root=0)

print result[0] * 2.