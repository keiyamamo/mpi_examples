from mpi4py import MPI
comm = MPI.COMM_WORLD
print("Hello world! from", comm.Get_rank(), "of", comm.Get_size(), "processors")