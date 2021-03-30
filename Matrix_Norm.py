import numpy as np

class Matrix_Norm_P:
    def __init__(self,p_value,steps):
        self.__p_value=p_value
        self.__digits_lst=[]
        self.__steps=steps
        self.__vectors_set=[]

    def __get_component(self,n, digit_from, m):
        digit_to = n - m + 1
        if digit_from > digit_to:
            return 0
        if m == 1:
            self.__digits_lst.append(float(n))
            self.__vectors_set.append(np.array(self.__digits_lst) / self.__steps)
            self.__digits_lst.pop(-1)
            return 1
        current_sum = 0
        for first_digit in range(digit_from, digit_to):
            self.__digits_lst.append(first_digit)
            current_sum += self.__get_component(n - first_digit, first_digit, m - 1)
            self.__digits_lst.pop(-1)
        return current_sum

    def __p(self,n, m):
        return self.__get_component(n, 1, m)

    def get_p_norm(self,in_vector, p):
        current_sum = 0
        for v in in_vector:
            current_sum += v ** p
        return current_sum ** (1 / p)

    def calculate_p_norm(self,A):
        self.__p(self.__steps,len(A[0,:]))
        norm_values=[]
        norm_vectors=[]
        W = np.matrix(np.array(self.__vectors_set) ** (1 / self.__p_value))
        U = A * W.T
        for u in U.T:
            norm_values.append(self.get_p_norm(np.array(u)[0], self.__p_value))
            norm_vectors.append(np.array(u)[0])

        maximum_value=max(norm_values)
        return maximum_value,norm_vectors[norm_values.index(maximum_value)]
