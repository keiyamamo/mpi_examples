from mpi4py import MPI
comm = MPI.COMM_WORLD
import sys
import numpy as np
import sympy

x = sympy.Symbol("x")
f = eval(sys.argv[-1])
rank = comm.Get_rank()
size = comm.Get_size()
a, b = 0.0, 1.0
N = eval(sys.argv[-2]) # Number of subdivisions for each rank
dx = (b-a)/size
a_hat = rank*dx
b_hat = (rank+1)*dx
xj = np.linspace(a_hat, b_hat, N+1)
fj = [f.subs(x, y) for y in xj]
Ij = (b_hat-a_hat)/float(N)*(0.5*(fj[0]+fj[-1])+sum(fj[1:-1]))
I = comm.reduce(Ij)
if rank == 0:
    print ("Integral of f(x) from ", a, "to", b, "is ≈", I)
    print ("Exact                               = ", f.integrate((x, (a, b))).evalf())


    