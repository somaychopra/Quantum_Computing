import numpy as np
#import matplotlib.pyplot as plt

class qubit:
	#initializing single quibit
	def __init__(self, a = np.complex_(), b = np.complex_()):
		self.mat = np.zeros(2, dtype = np.complex_())
		self.mat[0] = a
		self.mat[1] = b
class X:
	def __init__(self):
		self.mat = np.eye(2, dtype  = np.complex_())
		self.mat[0][0] = 0
		self.mat[0][1] = 1
		self.mat[1][0] = 1
		self.mat[1][1] = 0
class Y:
	def __init__(self):
		self.mat = np.eye(2, dtype  = np.complex_())
		self.mat[0][0] = 0
		self.mat[0][1] = -1j
		self.mat[1][0] = 1j
		self.mat[1][1] = 0
class Z:
	def __init__(self):
		self.mat = np.eye(2, dtype  = np.complex_())
		self.mat[0][0] = 1
		self.mat[0][1] = 0
		self.mat[1][0] = 0
		self.mat[1][1] = -1
class H:
	def __init__(self):
		self.mat = np.eye(2, dtype  = np.complex_())
		self.mat[0][0] = 1/np.sqrt(2)
		self.mat[0][1] = 1/np.sqrt(2)
		self.mat[1][0] = 1/np.sqrt(2)
		self.mat[1][1] = -1/np.sqrt(2)
		

if __name__ == "__main__":
	n = input("Enter a valid value for n : ")
	n = int(n)
	f= np.full(2**n,0)
	for i in range(2**n):
		f[i] = input("Enter the value of f[{}] : ".format(i))
	H = H()
	temp = H.mat
	for i in range(n-1):
		H.mat = np.kron(H.mat,temp)
    
	q_0 = qubit(1,0)
	q_1 = qubit(0,1)
	q_0n = qubit(1,0)
	for i in range(n-1):
		q_0n.mat = np.kron(q_0n.mat,q_0.mat)
	H_f = np.kron(H.mat,temp)
	x = q_0n.mat
	y = q_1.mat
	#print(np.size(x))
	x = np.matmul(H.mat,x)
	#print(np.shape(x))
	Uf = np.identity(2**n)
	for i in range(2**n):
		Uf[i][i] = (-1)**int(f[i])
	#print(np.size(Uf))
	#print(x)
	x = np.matmul(Uf,x)
	#print(x)
	I = np.identity(2)
	H_nI = np.kron(H.mat,I)
	#phi_2 = np.kron(x,y)
	phi_3x = np.matmul(H.mat,x)
	#print(H.mat)
	#print(phi_3x)
	if phi_3x[0]==0:
		print("f(x) is a balanced function\n")
	else:
		print("f(x) is a constant function\n")


		



