import numpy as np
import math

class Gauss_Elimination:
    def __init__(self,A,b):
        self.A=A
        self.b=b


    def Eliminate_1(self,A,b):
        self.A=A
        self.b=b
        for i in range(self.A.shape[0]):
            a_ii=self.A[i,i]
            self.A[i,:]=self.A[i,:]/a_ii
            self.b[i]=self.b[i]/a_ii
            for j in range(i+1,self.A.shape[0]):
                a_ji=self.A[j,i]
                self.A[j,:]=self.A[j,:]-a_ji*self.A[i,:]
                self.b[j]=self.b[j]-a_ji*self.b[i]
        return self.A,self.b

    def Eliminate_2(self,A,b):
        self.A=A
        self.b=b
        for i in range(self.A.shape[0]):
            a_ii=self.A[i,i]
            # self.A[i,:]=self.A[i,:]/a_ii
            # self.b[i]=self.b[i]/a_ii
            for j in range(i+1,self.A.shape[0]):
                a_ji=self.A[j,i]
                self.A[j,:]=self.A[j,:]-a_ji*self.A[i,:]/a_ii
                self.b[j]=self.b[j]-a_ji*self.b[i]/a_ii
        return self.A,self.b

    def Pivoting_1(self, A, b):
        self.A = A
        self.b = b
        for i in range(self.A.shape[0]):
            a_ii = self.A[i, i]
            max_row = i
            for k in range(i + 1, self.A.shape[0]):
                if math.fabs(a_ii) < math.fabs(self.A[k, i]):
                    a_ii = self.A[k, i]
                    max_row = k
            if max_row != i:
                self.A[[i, k]] = self.A[[k, i]]
                self.b[[i, k]] = self.b[[k, i]]
            for j in range(i + 1, self.A.shape[0]):
                a_ji = self.A[j, i]
                tmp = a_ji / a_ii
                self.A[j, :] = self.A[j, :] - self.A[i, :] * tmp
                self.b[j] = self.b[j] - self.b[i] * tmp
        return self.A, self.b

    def LU(self, A, b):
        self.A = A
        self.b = b
        identity = np.identity(self.A.shape[0], dtype=float)
        for i in range(self.A.shape[0]):
            a_ii = self.A[i, i]
            for j in range(i + 1, self.A.shape[0]):
                a_ji = self.A[j, i]
                self.A[j, :] = self.A[j, :] - self.A[i, :] * a_ji / a_ii
                self.b[j] = self.b[j] - self.b[i] * a_ji / a_ii
                identity[j, i] = a_ji / a_ii

        return identity, self.A, self.b