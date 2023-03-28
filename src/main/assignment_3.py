import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)


def eulerMethod(initPoint, low, high, numIter, func):
    h = (high - low) / numIter
    t = low
    w = initPoint

    for i in range(1, numIter+1):
        w = w + (h * eval(func))
        t = low + (i * h)

    return w


def evalFunc(t, w):
    return t - w**2


def rungeKutta(initPoint, low, high, numIter, func):
    h = (high - low) / numIter
    t = low
    w = initPoint

    for i in range(1, numIter+1):
        k1 = h * evalFunc(t, w)

        k2 = h * evalFunc(t + (h/2), w + (k1/2))

        k3 = h * evalFunc(t + (h/2), w + (k2/2))

        k4 = h * evalFunc(t + h, w + k3)

        w = w + (k1 + (2 * k2) + (2 * k3) + k4)/6
        t = low + (i * h)

    return w

def gaussianElimination(n, matrix):
    p = -1

    for i in range(0, n-1):
        for j in range(i, n):
            if matrix[j, i] != 0:
                p = j
                break
        if p == -1:
            print("No solution")
            return

        if p != i:
            matrix[[p, i]] = matrix[[i, p]]

        for j in range(i+1, n):
            m = matrix[j, i] / matrix[i, i]
            Ei = matrix[i] * m
            matrix[j] -= Ei

    if matrix[n-1, n-1] == 0:
        print("No solution")
        return

    x = np.zeros(n)
    x[n-1] = matrix[n-1, n] / matrix[n-1, n-1]

    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += (matrix[i, j] * x[j])
        x[i] = (matrix[i, n] - sum) / matrix[i, i]

    return x

def LUFactorization(n, matrix):
    l = np.zeros(matrix.shape)
    u = np.zeros(matrix.shape)

    for i in range(0, n):
        l[i, i] = 1

    u[0,0] = matrix[0, 0]
    if(l[0,0] * u[0,0] == 0):
        print("Impossible")
        return

    for j in range(1, n):
        u[0,j] = matrix[0,j]/l[0,0]
        l[j,0] = matrix[j,0]/u[0,0]

    for i in range(1, n-1):
        sum = 0
        for k in range(0, i):
            sum += l[i,k]*u[k,i]
        u[i,i] = matrix[i,i] - sum

        if(l[i,i]*u[i,i] == 0):
            print("Impossible")
            return

        for j in range(i+1, n):
            sum = 0
            for k in range(0, i):
                sum += l[i,k] * u[k,j]
            u[i,j] = (1/l[i,i]) * (matrix[i,j] - sum)

            sum = 0
            for k in range(0, i):
                sum += l[j,k] * u[k,i]
            l[j,i] = (1/u[i,i]) * (matrix[j,i] - sum)

    sum = 0
    for k in range(0, n):
        sum += l[n-1,k] * u[k,n-1]
    u[n-1,n-1] = matrix[n-1, n-1] - sum

    return (l, u)

def diagonallyDominant(n, matrix):
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            if j != i:
                sum += matrix[i, j]
        if abs(matrix[i, i] < sum):
            return False
    return True

def positiveDefinite(matrix):
    if np.array_equal(matrix, np.transpose(matrix)) == False:
        return False
    eigen = np.linalg.eig(matrix)[0]
    if np.all(eigen > 0):
        return True
    return False



if __name__ == "__main__":
    # Problem 1
    initPoint = 1
    low = 0
    high = 2
    numIter = 10
    func = 't-w**2'
    print(eulerMethod(initPoint, low, high, numIter, func))
    print()

    # Problem 2
    print(rungeKutta(initPoint, low, high, numIter, func))
    print()

    # Problem 3
    n = 3
    matrix = np.array([[ 2.0, -1.0, 1.0,  6.0],
                       [ 1.0,  3.0, 1.0,  0.0],
                       [-1.0,  5.0, 4.0, -3.0]])
    print(gaussianElimination(n, matrix))
    print()

    # Problem 4
    n = 4
    matrix = np.array([[ 1.0,  1.0,  0.0,  3.0],
                       [ 2.0,  1.0, -1.0,  1.0],
                       [ 3.0, -1.0, -1.0,  2.0],
                       [-1.0,  2.0,  3.0, -1.0]])

    print(np.linalg.det(matrix))
    print()
    ans = LUFactorization(n, matrix)
    print(ans[0])
    print()
    print(ans[1])
    print()

    # Problem 5
    n = 5
    matrix = np.array([[9, 0, 5,  2, 1],
                       [3, 9, 1,  2, 1],
                       [0, 1, 7,  2, 3],
                       [4, 2, 3, 12, 2],
                       [3, 2, 4,  0, 8]])
    print(diagonallyDominant(n, matrix))
    print()

    # Problem 6
    n = 3
    matrix = np.array([[2, 2, 1],
                       [2, 3, 0],
                       [1, 0, 2]])
    print(positiveDefinite(matrix))