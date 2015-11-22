# -*- coding: UTF-8 -*-
import numpy
from pi_serial import calcular_pi
import mpi4py.MPI as MPI

N = 1000000000

if not MPI.Is_initialized():
    MPI.Init()

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
size = comm.Get_size()

my_acum = numpy.array([1.0])
result = numpy.array([1.])

chunk = N / size
rest = N % size

start = (myid * chunk) + 1
end = start + chunk + (rest if myid == size - 1 else 0)

i = start

my_acum[0] = calcular_pi(end, start)

print 'Soy proceso %s y mi acum es: %s, Rango: %s - %s' % (myid, my_acum[0], start, end)

comm.Reduce([my_acum, MPI.DOUBLE], [result, MPI.DOUBLE], op=MPI.PROD, root=0)

if myid == 0:
    print result[0] * 2.

MPI.Finalize()
