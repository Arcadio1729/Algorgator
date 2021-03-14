import numpy as np

class Matrix_Operator:
    def __init__(self,A,B):
        self.A=A #left side matrix
        self.B=B #right side matrix

        self.m=len(A[:,0]) #rows in matrix A
        self.n=len(B[0]) #columns in matrix B
        self.l=len(A[0]) # columns rows in A B

        self.C=np.zeros([self.m,self.n]) #output matrix C m x n

    def __get_scalar_product(self,a, b):
        scalar_product = 0
        for i in range(len(a)):
            scalar_product += a[i] * b[i]
        return scalar_product

    def __get_rank_one_1(self,A, B, common_row_column):
        temp_matrix=np.zeros([self.m,self.n])
        for i in range(self.m):
            for j in range(self.n):
                temp_matrix[i,j]=np.zeros([self.m,self.n])[i, j] = A[i, common_row_column] * B[common_row_column, j]
        return temp_matrix

    def __get_rank_one_2(self,A, B, common_row_column):
        temp_matrix=np.zeros([self.m,self.n])
        for j in range(self.n):
            for i in range(self.m):
                temp_matrix[i,j] = A[i, common_row_column] * B[common_row_column, j]
        return temp_matrix

    def multiply_matrix_1(self,A, B):
        self.C = np.zeros([self.m, self.n])
        for i in range(self.m):
            for j in range(self.n):
                self.C[i, j] = self.__get_scalar_product(A[i], B[:, j])
                # for k in range(l):
                # C[i,j]+=A[i,k]*B[k,j]

    def multiply_matrix_2(self,A, B):
        self.C = np.zeros([self.m, self.n])
        for j in range(self.n):
            for i in range(self.m):
                self.C[i, j] = self.__get_scalar_product(A[i], B[:, j])

    def multiply_matrix_3(self,A, B):
        self.C = np.zeros([self.m, self.n])
        for k in range(self.l):
            self.C += self.__get_rank_one_1(A, B, k)

    def multiply_matrix_4(self,A, B):
        self.C = np.zeros([self.m, self.n])
        for k in range(self.l):
            self.C += self.__get_rank_one_2(A, B, k)


    def multiply_matrix_5(self,A,B):
        self.C = np.zeros([self.m, self.n])
        for i in range(self.m):
            for k in range(self.l):
                for j in range(self.n):
                    self.C[i,j]+=A[i,k]*B[k,j]

    def multiply_matrix_6(self,A,B):
        self.C = np.zeros([self.m, self.n])
        for j in range(self.n):
            for k in range(self.l):
                for i in range(self.m):
                    self.C[i,j]+=A[i,k]*B[k,j]
