"""
Hola mundo en python
"""

import mpi4py.MPI as MPI

if not MPI.Is_initialized():
    MPI.Init()

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
size = comm.Get_size()

print "I am process %s. Total size: %s" % (myid, size)

MPI.Finalize()