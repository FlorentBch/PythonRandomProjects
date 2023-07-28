import numpy as np

# Create an Array

Array1 = np.array([])
print("Array1 : ", Array1)

# Avec des valeur en : 1D
Array2 = np.array([1,2,3,4,5,6])
print("Array2 : ", Array2)

# Avec des valeur en : 2D
Array3 = np.array([[1,2],[3,4],[5,6]])
print("Array3 : ", Array3)

# Avec des valeur en : 3D
Array4 = np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
print("Array4 : ", Array4)

# numpy avec valeurs random
random_array = np.random.randint(low=10, high=99, size=(4,2,3,6))
print("Random_array : ", random_array)

# Tableau de zero
zero_array = np.zeros((2,4,6))
print("Zero Array : ", zero_array)

# Création avec des données spécifique
spe_array = np.arange(start=0, stop=100, step=10)
print("Spe Array : ",spe_array)

# Matrice identité
identity_array = np.identity(4)
print("Idendity Array : \n", identity_array)

##############
# Manipulation des Array
##############

# Ajout de valeurs en Array 1D
appended_array = np.append(Array2, [10,20,30])
print("Appended Array",appended_array)

# Ajout de valeurs en Array 2D
appended_Array2D = np.append(Array3, [[10,20],[30,40]], axis=0)
print("Array 2D : ", appended_Array2D)

# Suppression de valeurs 

random_arr = np.random.randint(low=10, high=99, size=(10))
Deleted_array = np.delete(random_arr, obj=[1,2,3,4])
print("Deleted array : ", Deleted_array)
