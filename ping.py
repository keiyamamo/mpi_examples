from mpi4py import MPI
comm = MPI.COMM_WORLD
assert comm.Get_size() == 2        # Check that only 2 cpus are used

rank = comm.Get_rank()
sendmessage = "from " + str(rank)  # Create a unique message

# Send and receive messages
comm.send(sendmessage, dest=(rank+1)%2)   # % is the modulo operator
rcvmessage = comm.recv(source=(rank+1)%2)

print ("Rank", rank, "received the message '", rcvmessage, "'")