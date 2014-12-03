import numpy
import mpi4py.MPI as MPI

if not MPI.Is_initialized():
    MPI.Init()

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
size = comm.Get_size()
token = numpy.empty(1, dtype='i')

if myid == size - 1:
    token[0] = myid
    comm.Send([token, MPI.INT], dest=0, tag=100)
else:
    token[0] = myid
    comm.Send([token, MPI.INT], dest=myid+1, tag=100)

if myid == 0:
    comm.Recv([token, MPI.INT], source=size-1, tag=100)
else:
    comm.Recv([token, MPI.INT], source=myid-1, tag=100)

print 'I am process %s an received message from %s' % (myid, token)

MPI.Finalize()
