from sympy import *


# determinant
def det(matrix_first, n):
    if n == 1:
        return matrix_first[0][0]
    elif n == 2:
        return matrix_first[0][0] * matrix_first[1][1] - matrix_first[1][0] * matrix_first[0][1]
    else:
        matrix_l = 0
        for i in range(n):
            matrix_s = []
            for k in range(n):
                r = []
                for j in range(n):
                    if k != 0 and j != i:
                        r += [matrix_first[k][j]]
                if r:
                    matrix_s += [r]
            matrix_l += matrix_first[0][i] * ((-1) ** i) * det(matrix_s, n - 1)
        return matrix_l


def determinant_of_the_matrix(matrix):
    n = len(matrix)
    return det(matrix, n)


# eigenvalues
x = Symbol('x')


def eigenvalues(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = (matrix[i][j] - x)
    n = len(matrix)

    def equation(matrix_first, n):
        if n == 1:
            return matrix_first[0][0]
        elif n == 2:
            return matrix_first[0][0] * matrix_first[1][1] - matrix_first[1][0] * matrix_first[0][1]
        else:
            matrix_l = 0
            for i in range(n):
                matrix_s = []
                for k in range(n):
                    r = []
                    for j in range(n):
                        if k != 0 and j != i:
                            r += [matrix_first[k][j]]
                    if r != []:
                        matrix_s += [r]
                matrix_l += matrix_first[0][i] * ((-1) ** i) * equation(matrix_s, n - 1)
            return matrix_l

    return solve(equation(matrix, n), x)


# inverse
def inverse(m):
    determinant = determinant_of_the_matrix(m)
    try:
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]]
        cofactors = cofactor(m)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return cofactors
    except:
        print("can't continue because the determinant is 0")



# operations
def operations(operator, first_matrix, second_matrix):
    if operator == 'mult':
        return mult(first_matrix, second_matrix)
    elif operator == 'div':
        return div(first_matrix, second_matrix)
    elif operator == 'add':
        return add(first_matrix, second_matrix)
    elif operator == 'red':
        return reduction(first_matrix, second_matrix)
    else:
        return "there is no such function"


def split(first_matrix, n):
    k, m = divmod(len(first_matrix), n)
    return list(first_matrix[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def add(first_matrix, second_matrix):
    if len(second_matrix) != len(first_matrix) or len(second_matrix[0]) != len(first_matrix[0]):
        return 'Dimension mismatch'
    else:
        result = []
        for i in range(len(first_matrix)):
            for j in range(len(first_matrix[0])):
                result.append(first_matrix[i][j] + second_matrix[i][j])
            k, m = divmod(len(first_matrix), len(first_matrix))

        return split(result, len(first_matrix))


def reduction(first_matrix, second_matrix):
    if len(second_matrix) != len(first_matrix) or len(second_matrix[0]) != len(first_matrix[0]):
        return 'Dimension mismatch'
    else:
        result = []
        for i in range(len(first_matrix)):
            for j in range(len(first_matrix[0])):
                result.append(first_matrix[i][j] - second_matrix[i][j])
            k, m = divmod(len(first_matrix), len(first_matrix))

        return split(result, len(first_matrix))


def mult(first_matrix, second_matrix):
    if len(second_matrix) != len(first_matrix[0]):
        return "Dimension mismatch"
    else:
        result = [[sum(f * g for f, g in zip(E_row, R_col)) for R_col in zip(*second_matrix)] for E_row in first_matrix]
        return result


def div(first_matrix, second_matrix):
    b_ins = inverse(second_matrix)

    return mult(first_matrix, b_ins)


# cofactor
def cofactor(m):
    cof2 = []
    try:
        for j in range(len(m)):
            cof = []
            for i in range(len(m)):
                temp = [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]
                cof.append((-1) ** (i + j) * determinant_of_the_matrix(temp))
            cof2.append(cof)
        return cof2
    except IndexError:
        print("INDICES START WITH 0")


def cofactor_of_element(m, i, j):
    temp = []
    try:
        for row in (m[:i] + m[i + 1:]):
            temp.append(row[:j] + row[j + 1:])
        return (-1) ** (i + j) * determinant_of_the_matrix(temp)

    except IndexError:
        print("INDICES START WITH 0")


def transpose(m):
    temp = []
    row = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            row.append(m[j][i])
        temp.append(row)
        row = []
    return temp


# adjoint
def adjoint(m):
    temp = []
    row = []
    for i in range(len(m)):
        for j in range(len(m)):
            row.append(cofactor_of_element(m, i, j))
        temp.append(row)
        row = []

    return transpose(temp)


# cramer's rule
def cramer(m):
    main = []
    const = []
    ans = []
    for row in m:
        main.append(row[:-1])
        const.append(row[-1])
    print("MAIN", main)
    print("CRAMER LAST ROW", const)

    D = determinant_of_the_matrix(main)
    temp = main.copy()
    temp2 = []
    for i in range(len(main[0])):
        print("main", temp)
        try:
            j = 0
            for row in temp:
                row[i - 1] = temp2[j]
                j += 1
        except IndexError:
            pass
        temp2 = []
        j = 0
        for row in temp:
            temp2.append(row[i])
            row[i] = const[j]
            j += 1
        print(temp)
        print(temp2)
        ans.append(determinant_of_the_matrix(temp) / D)
    return ans
