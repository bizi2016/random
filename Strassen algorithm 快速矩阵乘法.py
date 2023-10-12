import numpy as np



# strassen矩阵乘法快速算法
# 时间复杂度：O(n^log2(7))
def strassen(matrix_a, matrix_b):
    
    if len(matrix_a) == 1:
        return matrix_a * matrix_b
    
    size = len(matrix_a) // 2
    
    # 将输入矩阵分割成四个子矩阵
    a11 = matrix_a[:size, :size]
    a12 = matrix_a[:size, size:]
    a21 = matrix_a[size:, :size]
    a22 = matrix_a[size:, size:]
    
    b11 = matrix_b[:size, :size]
    b12 = matrix_b[:size, size:]
    b21 = matrix_b[size:, :size]
    b22 = matrix_b[size:, size:]
    
    # 计算七个矩阵乘法的递归调用
    m1 = strassen(a11 + a22, b11 + b22)
    m2 = strassen(a21 + a22, b11)
    m3 = strassen(a11, b12 - b22)
    m4 = strassen(a22, b21 - b11)
    m5 = strassen(a11 + a12, b22)
    m6 = strassen(a21 - a11, b11 + b12)
    m7 = strassen(a12 - a22, b21 + b22)
    
    # 计算四个子矩阵的结果
    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4
    c22 = m1 - m2 + m3 + m6
    
    # 将四个子矩阵合并成一个矩阵
    result_matrix = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    
    return result_matrix



if __name__ == '__main__':
    
    matrix_a = np.array([ [1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, 12],
                          [13, 14, 15, 16],
                          ])

    matrix_b = np.array([ [17, 18, 19, 20],
                          [21, 22, 23, 24],
                          [25, 26, 27, 28],
                          [29, 30, 31, 32],
                          ])

    ans = strassen(matrix_a, matrix_b)
    print(ans)
    print()

    ans = np.dot(matrix_a, matrix_b)
    print(ans)


























    
