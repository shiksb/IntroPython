def matrix_transpose(matrix_A):
    #Your codes here


    return transposed_matrix


def matrix_det(matrix_A):
    #Your codes here


    return determinant

def matrix_add(matrix_A, matrix_B):
    #Your codes here


    return matrix_sum

def matrix_mult(matrix_A, matrix_B):
    #Your codes here


    return matrix_product

if __name__ == '__main__':

    test_1 = [[1,9,-13],[20,5,-6]]
    test_2 = [[1,9],[20,5]]
    test_3 = [[4,8],[9,16]]

    print("Transpose Input:", test_1)
    print("Your transpose:", matrix_transpose(test_1))
    print("Expected transpose:", [[1,20],[9,5],[-13,-6]])

    print("Determinant Input:", test_2)
    print("Your determinant:", matrix_det(test_2))
    print("Expected determinant:", -175)

    print("Sum Input:", test_2, test_3)
    print("Your sum:", matrix_add(test_2, tesst_3))
    print("Expected sum:", [[5,17],[29,21]])

    print("Multiply Input:", test_2, test_3)
    print("Your product:", matrix_mult(test_2, test_3))
    print("Expected transpose:", [[85,152],[125,240]])
