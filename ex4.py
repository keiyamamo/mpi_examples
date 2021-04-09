'''
Given a global matrix A[N, N] and a vector x[N]
Compute the matrix vector product through MPI by distributing the matrix such that its local size on each rank is A[Np, N], where Np = N/(Number of ranks)
Verify the result by comparing to a serial code
'''
from mpi4py import MPI
comm = MPI.COMM_WORLD
import numpy as np
import sys

rank = comm.Get_rank()
size = comm.Get_size()

n = eval(sys.argv[-1])
N = n*size
A = None; x = None

if rank == 0:    
    A = np.random.randint(5, size=(N, N))
    x = np.random.randint(5, size=N)
    b = A.dot(x)    
    
A = comm.bcast(A, root=0) 
x = comm.bcast(x, root=0)

# perfrom multiplication for each rank
Ap = A[rank*n:(rank+1)*n]
bp = Ap.dot(x)
comm.barrier()

if rank == 0:
    recvbuf = np.empty(N, dtype=int)
else: recvbuf = None

# gahter bp into one array(recvbuf) to rank 0 
comm.Gather(sendbuf=bp, recvbuf=recvbuf, root=0)

if rank == 0:
    print("correct result")
    print(b)
    print("MPI result")
    print(recvbuf)
    

    
    

    


