from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

src  = rank-1
if rank == 0:
    src = size-1

recvmessage = 0
sum_value = 0

for i in range(size):
    if i == 0:
        recvmessage = comm.sendrecv(dest=(rank+1)%size, source=src, sendobj=rank)
        sum_value += recvmessage
    else:
        recvmessage = comm.sendrecv(dest=(rank+1)%size, source=src, sendobj=recvmessage)
        sum_value += recvmessage

print("rank = ", rank, "sum = ", sum_value) 

