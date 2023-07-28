import numpy as np

# Create array
mat1 = np.random.randint(low=1, high=10, size=(3,3))
mat2 = np.random.randint(low=1, high=20, size=(3,3))
print("mat1 : \n", mat1)
print("mat2 : \n", mat2)

# Addition de Array
print("Addition de mat1 et mat2 : \n", mat1 + mat2)
print("Addition de mat1 et mat2 : \n", np.add(mat1, mat2))
# Soustraction de Array
print("Soustraction de mat1 par mat2 : \n", mat1 - mat2)
print("Soustraction de mat1 par mat2 : \n", np.subtract(mat1, mat2))

# multiplication de matrice
mat3 = np.random.randint(low=1, high=10, size=(3,2))
mat4 = np.random.randint(low=1, high=20, size=(2,3))
print("mat3 : \n", mat3)
print("mat4 : \n", mat4)

# print("Multiplication de mat3 par mat4 : \n", mat3 * mat4)
print("Multiplication de mat3 par mat4 : \n", np.matmul(mat3, mat4))