import numpy as np

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

    def Pivoting_1(self,A,b):
        self.A=A
        self.b=b
        for i in range(self.A.shape[0]):
            a_ii=self.A[i,i]
            for j in range(i+1,self.A.shape[0]):
                a_ji=self.A[j,i]
                self.A[j,:]=self.A[j,:]-a_ji*self.A[i,:]/a_ii
                self.b[j]=self.b[j]-a_ji*self.b[i]/a_ii
        return self.A,self.b
