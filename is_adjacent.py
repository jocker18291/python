#For two nodes in a graph to be considered adjacent to one another
#there must be an edge between them. In the example given
#nodes 0 and 1 are adjacent, but nodes 0 and 2 are not.

import numpy as np

def is_adjacent(matrix, node1, node2):
    if matrix[node1][node2] == 1:
        return True
    else:
        return False

matrix = np.array([
  [ 0, 1, 0, 1, 1 ],
  [ 1, 0, 1, 0, 0 ],
  [ 0, 1, 0, 1, 0 ],
  [ 1, 0, 1, 0, 1 ],
  [ 1, 0, 0, 1, 0 ]
])
node1 = int(input("Enter the first node: "))
node2 = int(input("Enter the second node: "))
print(is_adjacent(matrix, node1, node2))