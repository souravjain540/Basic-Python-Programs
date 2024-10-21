import numpy as np

# 1. Receive the N nodes, connectivities

n = input('Enter the number of nodes: ')
connectivities = []
nodes = []
loads = []

for i in range(int(n)):
    x = input(f'Enter the x coordinate of node {i}: ')
    y = input(f'Enter the y coordinate of node {i}: ')
    node = [x, y]
    nodes.append(node)
    connectivity = input('Enter a list of connectivities for this node separated by commas: ').split(', ')
    for i in range(len(connectivity)):
        if connectivity[i].isdigit():
            connectivity[i] = int(connectivity[i])
        else:
            print(f"Error: '{connectivity[i]}' is not a valid integer.")
            break
    else:
        connectivities.append(connectivity)    
    loadX = int(input(f'Enter the load applied to node {i} in X: '))
    loadY = int(input(f'Enter the load applied to node {i} in Y: '))
    load = [loadX, loadY]
    loads.append(load)
    print('\n')

area = input('Enter the cross-sectional area: ')
elasticity = input('Enter the modulus of elasticity: ')
tension = input('Enter the tensile stress: ')
rupture = input('Enter the rupture stress: ')

print('\n\n\n')

element_list = []
element_matrices = {}
for i in range(len(connectivities)):
    for j in range(len(connectivities[i])):
        nodes_pair = sorted([i, int(connectivities[i][j])])
        if tuple(nodes_pair) not in element_list:
            print(f'Element {i} connected to node {int(connectivities[i][j])} with incidence in {i} and {int(connectivities[i][j])}')
            element_list.append(tuple(nodes_pair))
            node1 = nodes[i]
            node2 = nodes[int(connectivities[i][j])]
            x1, y1 = float(node1[0]), float(node1[1])
            x2, y2 = float(node2[0]), float(node2[1])
            L = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            c = (x2 - x1) / L
            s = (y2 - y1) / L
            print(f'\nFor element {i} we have: c = {c} and s = {s}')
            k = float(area) * float(elasticity) / L
            element_matrix = (float(elasticity) * float(area))/ L * np.array([[c**2, c*s, -c**2, -c*s], [c*s, s**2, -c*s, -s**2], [-c**2, -c*s, c**2, c*s], [-c*s, -s**2, c*s, s**2]])
            element_matrices[tuple(nodes_pair)] = element_matrix

# Calculating the degree of freedom numbering
dof = []
for i in range(int(n)):
    dof.append([2*i, 2*i+1])
    print('Node', i, '->', dof[i])

# Calculating degrees of freedom with restriction
# Restriction at node 0 (element 0 and 1), and at the last node (element last node * 2i + 1)
restricted_dof = []
restricted_dof.append(dof[0][0])
restricted_dof.append(dof[0][1])
restricted_dof.append(dof[-1][1])
print(restricted_dof)

# Degree of freedom of nodes with load
loads_dict = {}
for i in range(int(n)):
    if (loads[i][0] != 0 or loads[i][1] != 0):
        loads_dict[dof[i][0]] = loads[i][0]
        loads_dict[dof[i][1]] = loads[i][1]
        print("For degree of freedom", dof[i][0], "the load is", loads[i][0], 'in the positive x direction')
        print("For degree of freedom", dof[i][1], "the load is", loads[i][1], 'in the positive y direction')

# 2. Pre-Processing
# a. Assembly of element matrices

# b. Superposition of matrices - Global stiffness of the structure
K = np.zeros((2 * len(nodes), 2 * len(nodes)))
for (i, j), matrix in element_matrices.items():
    # Get the global degree of freedom indices for the nodes of the element
    dof_indices = dof[i] + dof[j]
    for m in range(4):
        for n in range(4):
            K[dof_indices[m]][dof_indices[n]] += matrix[m][n]

print('\nGlobal stiffness matrix:')
print(K)

# c. Assembly of the global load vector of the structure
F = np.zeros(2 * len(nodes))
for dof, load in loads_dict.items():
    F[dof] = load

# d. Application of boundary conditions
for dof in restricted_dof:
    K[dof] = np.zeros(2 * len(nodes))
    K[:,dof] = np.zeros(2 * len(nodes))
    K[dof][dof] = 1
    F[dof] = 0

# Ensure that the main diagonal of K is not zero
for i in range(len(K)):
    if round(K[i][i], 3) == 0:
        K[i][i] = 1

K_copy = K.copy()

print(f'\nInverse Matrix:')

# Print the K matrix
for i in range(len(K)):
    for j in range(len(K[i])):
        print(f'{K[i][j]:.2f}', end=' ')
    print()

# e. Solving the system of equations
# Ensuring that F has the same size as the solution vector
F = F.reshape((2 * len(nodes), 1))

# Now solving the system
displacements = np.linalg.solve(K, F)

print('\nNodal force matrix (in N):')
print(F)

print('\nDisplacements at nodes (in meters):')
for i in range(len(nodes)):
    print(f'Node {i}: ({displacements[2*i][0]}, {displacements[2*i+1][0]})')

# f. Calculating the stress in each element
stress_list = []
print('\nStress in each element (in Pa):')
for i in range(len(element_list)):
    node1 = nodes[element_list[i][0]]
    node2 = nodes[element_list[i][1]]

    x1, y1 = float(node1[0]), float(node1[1])
    x2, y2 = float(node2[0]), float(node2[1])
    L = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    c = (x2 - x1) / L
    s = (y2 - y1) / L

    displacement1 = displacements[2*element_list[i][0]:2*element_list[i][0]+2]
    displacement2 = displacements[2*element_list[i][1]:2*element_list[i][1]+2]

    stress = (float(elasticity) / L) * np.array([-c, -s, c, s]).dot(np.concatenate((displacement1, displacement2)))
    stress_list.append(stress)
    print(f'Element {i}: {stress[0]}')

# g. Calculating the reactions at the support nodes
# Calculating reaction forces through stress and area
reactions = {}

print('\nReaction forces in each element (in N):')
for i in range(len(element_list)):
    node1 = nodes[element_list[i][0]]
    node2 = nodes[element_list[i][1]]
    x1, y1 = float(node1[0]), float(node1[1])
    x2, y2 = float(node2[0]), float(node2[1])
    L = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    c = (x2 - x1) / L
    s = (y2 - y1) / L
    displacement1 = displacements[2*element_list[i][0]:2*element_list[i][0]+2]
    displacement2 = displacements[2*element_list[i][1]:2*element_list[i][1]+2]
    stress = (float(elasticity) / L) * np.array([-c, -s, c, s]).dot(np.concatenate((displacement1, displacement2)))
    reactions[i] = stress * float(area)
    print(f'Element {i}: {reactions[i]}')
    

# 4
def gauss_seidel(A, b, max_iter=90, tol=1e-20):
    x = np.zeros_like(b)
    for it_count in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=tol):
            break
        x = x_new
    return x

A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
B = [7.85, -19.3, 71.4]

print('\nSolution of the linear equations system with the Gauss-Seidel method:')
print(gauss_seidel(np.array(A), np.array(B)))

# Comparing the displacement from linalg (already calculated) and gauss_seidel
print('\nComparison between numpy.linalg.solve and Gauss-Seidel:')
print('Displacements (in meters):')
print('Numpy:', displacements)
print('Gauss-Seidel:', gauss_seidel(K_copy, F))

# 5. Analysis of stress conditions in each element
print('\nAnalysis of stress conditions in each element:')

rupture = float(rupture)

for i in range(len(element_list)):
    # a. Failure by stress
    if abs(stress_list[i]) > rupture:
        print(f'Element {i}: Failure by stress. Stress of {stress_list[i]} is greater than the rupture stress {rupture}.')

    # b. Failure by buckling
    # The critical buckling load (Pcr) for a column with fixed ends is given by Pcr = pi^2*EI/(KL)^2
    # where E is the modulus of elasticity, I is the moment of inertia, K is the column coefficient (1 for fixed ends), and L is the length of the column.
    # For a bar with a circular cross-section, I = pi*r^4/4, where r is the radius of the cross-section.
    # Assuming the cross-sectional area is a circle, we can calculate the radius as r = sqrt(area/pi).
    # Assuming the bar is a column with fixed ends, K = 1.
    # Therefore, the critical buckling load is Pcr = pi^2*E*(pi*r^4/4)/(L^2) = pi^3*E*r^4/(4*L^2).
    # The buckling stress is then Pcr/area = pi^3*E*r^4/(4*L^2*area) = pi^3*E*r^2/(4*L^2) = pi^3*E/(4*L^2*(area/pi)) = pi^2*E/(4*L^2/r^2) = pi^2*E*r^2/(4*L^2).
    # The buckling load is the buckling stress times the area, or Pcr = pi^2*E*r^2/(4*L^2)*area = pi^2*E*area/(4*L^2/r^2) = pi^2*E*area*r^2/(4*L^2).
    # Therefore, if the stress in the element is negative (compression) and the magnitude of the stress is greater than the buckling stress, the element fails by buckling.
    r = np.sqrt(float(area) / np.pi)
    Pcr = np.pi**2 * float(elasticity) * float(area) * r**2 / (4 * L**2)
    if stress_list[i] < 0 and abs(stress_list[i]) > Pcr:
        print(f'Element {i}: Failure by buckling. Magnitude of compressive stress {abs(stress_list[i])} is greater than the critical buckling load {Pcr}.')
