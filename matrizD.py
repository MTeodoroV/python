import math
import numpy as np

def determinant(A):
    n=np.shape(A)[0]
    if(n==2):
        det=A[0,0]*A[1,1]-A[0,1]*A[1,0]
    else:    
        det=0
        for i in range(n):
            # Expansion by first line
            newMatrix=A[1:,:]
            newMatrix=np.delete(newMatrix,i,axis=1)
            det=det+math.pow(-1,1+i+1)*A[0,i]*(determinant(newMatrix))
    return det

if __name__ == '__main__':

    print("Matrix 1")
    A=((1, 2, 3),(4, 5 , 6),(7,8,9))
    print("Numpy: ", np.linalg.det(A))
    A=np.array(A)
    print("Ours: ",determinant(A))

    print("Matrix 2")
    A=((1, 2, 3),(4, 5 , 6),(7,8,13))
    print("Numpy: ",np.linalg.det(A))
    A=np.array(A)
    print("Ours: ",determinant(A))

    print("Matrix 3")
    A=((2, -2, 0, 3),(-5, 2 , 2, 1),(1,-1,0,-3),(2, 0, 0, -1))
    print("Numpy: ",np.linalg.det(A))
    A=np.array(A)
    print("Ours: ",determinant(A))