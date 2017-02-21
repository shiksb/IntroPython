# convenience function
def getMN(matrix):
    m = len(matrix)
    n = len(matrix[0])
    return m, n

def matrix_transpose(matrix_A):
    old_m, old_n = getMN(matrix_A)
    transposed_matrix = []

    for i in range(old_n):
        new_row = []
        for j in range(old_m):
            new_row.append(matrix_A[j][i])
        transposed_matrix.append(new_row)
    return transposed_matrix


def matrix_det(matrix_A):
    m, n = getMN(matrix_A)
    if m != n:
        print("Cannot calculate determinant of non-square matrix")
        return None
    if m == 1:
        return matrix_A[0][0]
    elif m == 2:
        a = matrix_A[0][0]
        b = matrix_A[0][1]
        c = matrix_A[1][0]
        d = matrix_A[1][1]
        return a * d - b * c
    else:
        print("Cannot calculate dterminant of %d-by-%d matrix" % (m, n))
        return None

def matrix_add(matrix_A, matrix_B):
    a_m, a_n = getMN(matrix_A)
    b_m, b_n = getMN(matrix_B)
    if a_m != b_m or a_n != b_n:
        print("Cannot perform matrix addition between %d-by-%d matrix and %d-by-%d matrix" % (a_m, a_n, b_m, b_n))
        return None

    # initializes a matrix of the proper dimensions
    matrix_sum = [[0 for x in range(a_n)] for y in range(a_m)]
    for i in range(a_m):
        for j in range(a_n):
            matrix_sum[i][j] = matrix_A[i][j] + matrix_B[i][j]

    return matrix_sum

def matrix_mult(matrix_A, matrix_B):
    a_m, a_n = getMN(matrix_A)
    b_m, b_n = getMN(matrix_B)
    matrix_product = [[0 for x in range(b_n)] for y in range(a_m)]
    if a_n != b_m:
        print("Cannot perform matrix multiplication between %d-by-%d matrix and %d-by-%d matrix" % (a_m, a_n, b_m, b_n))
        return None
    for i in range(b_n):
        for j in range(a_m):
            curr_product_sum = 0
            for k in range(a_n):
                curr_product_sum += matrix_A[j][k] * matrix_B[k][i]
            matrix_product[j][i] = curr_product_sum

    return matrix_product

if __name__ == '__main__':

    test_1 = [[1,9,-13],[20,5,-6]]
    test_2 = [[1,9],[20,5]]
    test_3 = [[4,8],[9,16]]

    print("Transpose Input:", test_1)
    print("Your transpose:", matrix_transpose(test_1))
    print("Expected transpose:", [[1,20],[9,5],[-13,-6]])
    print("#" * 50)
    print("Determinant Input:", test_2)
    print("Your determinant:", matrix_det(test_2))
    print("Expected determinant:", -175)
    print("#" * 50)
    print("Sum Input:", test_2, test_3)
    print("Your sum:", matrix_add(test_2, test_3))
    print("Expected sum:", [[5,17],[29,21]])
    print("#" * 50)
    print("Multiply Input:", test_2, test_3)
    print("Your product:", matrix_mult(test_2, test_3))
    print("Expected transpose:", [[85,152],[125,240]])
