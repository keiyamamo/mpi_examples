'''
approximate pi with monte carlo integration
'''

from mpi4py import MPI
comm = MPI.COMM_WORLD
import sys
import numpy as np
from math import pi

rank = comm.Get_rank()
size = comm.Get_size()


N = eval(sys.argv[-1])
num_points = size*N # number of points should be divisible by size

points = None

# points should be made only once
if rank == 0:
    points = np.random.rand(2, num_points) # coordinates of points
    points = points*2-1                    # shift coordianates so that they reside between -1 and 1

# cast points to all the ranks
points = comm.bcast(points, root=0) 

points = points[:,rank*N:(rank+1)*N]                # distribute points to each rank
pointsDistances = np.linalg.norm(points,axis=0)     # compute the distacne from the origin
numInCircle = np.count_nonzero(pointsDistances < 1) # count the number of points inside the circle

numInCircle = comm.reduce(numInCircle) # sum up all the points 

if rank == 0:
    Area = 4.*(numInCircle/num_points)
    print("approximated pi = ", Area)
    print("error  = ", pi-Area)
    





