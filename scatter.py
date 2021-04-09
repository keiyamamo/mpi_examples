from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
data = None
if rank == 0:
    data = [0, 1, 4, 9]

data = comm.scatter(data, root=0)

print("`Rank", rank, "data=", data)