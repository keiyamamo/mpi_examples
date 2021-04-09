'''
Modify trapz.py to use the composite Simpson's rule instead of the trapezoidal rule.
Modify the code to work with any interval size of the decomposed mesh, not just uniform.
'''
from mpi4py import MPI
comm = MPI.COMM_WORLD
import sys
import numpy as np
import sympy

x = sympy.Symbol("x")
f = eval(sys.argv[-1])
rank = comm.Get_rank()
size = comm.Get_size()
a = eval(sys.argv[-2]); a = float(a)
b = eval(sys.argv[-3]); b = float(b)
N = eval(sys.argv[-4]) # Number of subdivisions for each rank
dx = (b-a)/size
a_hat = rank*dx
b_hat = (rank+1)*dx
xj = np.linspace(a_hat, b_hat, N+1)
fj = [f.subs(x, y) for y in xj]

integrand = 0
for i in range(1, N):
    integrand = integrand + 2*fj[i] if i%2 == 0 else integrand + 4*fj[i]

Ij = (b_hat-a_hat)/3./float(N)*(fj[0]+ fj[-1] + integrand)
I = comm.reduce(Ij)
if rank == 0:
    print ("Integral of f(x) from ", a, "to", b, "is ≈", I)
    print ("Exact                               = ", f.integrate((x, (a, b))).evalf())

