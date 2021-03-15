import Matrix_Operator
from Gauss_Elimination import Gauss_Elimination
import numpy as np
import time

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #M1=np.array([[2,1,0],[0,-1,-2]])
    #M2=np.array([[0,1],[1,0],[2,2]])

    A=np.array([[999,998],[1000,999]],dtype=float)
    b=np.array([1997,1999],dtype=float)

    ge=Gauss_Elimination(A,b)
    print(ge.Eliminate_1(A,b))
    print(ge.Eliminate_2(A,b))

    # M1=np.random.randint(0,10,(1000,1000))
    # M2=np.random.randint(0,10,(1000,1000))
    # MO= Matrix_Operator.Matrix_Operator(M1,M2)
    #
    # #1 multiply ijk
    # start_time=time.time()
    # M=MO.multiply_matrix_1(M1,M2)
    # elapsed_time=time.time()-start_time
    # print("M1 x M2 ijk ",elapsed_time)
    #
    # #2 multiply jik
    # start_time=time.time()
    # M=MO.multiply_matrix_2(M1,M2)
    # elapsed_time=time.time()-start_time
    # print("M1 x M2 jik ",elapsed_time)
    #
    # #3 multiply kij
    # start_time=time.time()
    # M=MO.multiply_matrix_3(M1,M2)
    # elapsed_time=time.time()-start_time
    # print("M1 x M2 kij ",elapsed_time)
    #
    # #4 multiply kji
    # start_time=time.time()
    # M=MO.multiply_matrix_4(M1,M2)
    # elapsed_time=time.time()-start_time
    # print("M1 x M2 kji ",elapsed_time)
    #
    # #5 multiply ikj
    # start_time=time.time()
    # M=MO.multiply_matrix_5(M1,M2)
    # elapsed_time=time.time()-start_time
    # print("M1 x M2 ikj ",elapsed_time)
    #
    # #6 multiply jki
    # start_time=time.time()
    # M=MO.multiply_matrix_5(M1,M2)
    # elapsed_time=time.time()-start_time
    # print("M1 x M2 jki ",elapsed_time)
    #
    # #3 multiply kij
    # start_time=time.time()
    # M=MO.multiply_matrix_3(M1,M2)
    # elapsed_time=time.time()-start_time
    # print("M1 x M2 kij ",elapsed_time)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
