import numpy as np

mat = np.array([[1,2,3], [0,1,5], [5,6,0]])
print("Calculating Determinant of:")
print(mat)
try:
    det = np.linalg.det(mat)
    print(f"Determinant is: {round(det)}")
except:
    print("Cannot calculate determinant to the matrix...")