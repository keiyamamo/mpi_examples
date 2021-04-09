from mpi4py import MPI
comm = MPI.COMM_WORLD
assert comm.Get_size() == 2
import numpy as np   # numpy module for doing math with arrays in Python
import sys           # sys module used here for handling input parameter

rank = comm.Get_rank()
N = eval(sys.argv[-1])         # Get the last argument in the call to program
sendarray = np.random.random(N)# Create N random floats
recvarray = np.zeros(N)
comm.Send(sendarray, dest=(rank+1)%2)    # Large S in Send for numpy arrays
comm.Recv(recvarray, source=(rank+1)%2)  # Large R in Recv for numpy arrays

print("Rank", rank, "sent the array    ", sendarray)
print("Rank", rank, "received the array", recvarray)

