import numpy as np
no_p=5
no_r = 4
allocated = np.array([[4, 0, 0, 1], [1, 1, 0, 0], [1, 2, 5, 4], [0, 6, 3, 3], [0, 2, 1, 2]])
maximum = np.array([[6, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6], [1, 6, 5, 3], [1, 6, 5, 6]])
needed = maximum - allocated
available = np.array([3, 2, 1, 1])
def check(i):
    return all(needed[i] <= available)
Sequence = []
for i in range(no_p):
    for j in range(no_p):
        if j not in Sequence and check(j):
            Sequence.append(j)
            available += allocated[j]
if len(Sequence) == no_p:
    print("Needed Resource:\n", needed)
    print("The system is Safe")
    print("Safe Sequence:", Sequence)
    print("Available Resource:", available)
else:
    print("The system is Unsafe")