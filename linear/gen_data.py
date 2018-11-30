#! -*- coding: utf-8 -*-

import random
import sys

import numpy as np
import pandas as pd

# bias
bias = -23.5

# dimensions 5
weights = [4, 2.34, -1.4, 2.689, 6.6]




def gen_data(length, filename):
    

    ft = []

    for x in range(0, length):
        vec = [random.uniform(-20, 20) for x in range(0, 5)]
        val = np.dot(vec, weights)
        vec = [val] + vec

        ft.append(vec)

    df = pd.DataFrame(ft)

    print(df)
    df.to_csv(filename, float_format='%.6f', header=0, index=0)
        



def main():
    gen_data(500, 'linear_train.txt')
    gen_data(50, 'linear_test.txt')


if __name__ == '__main__':
    main()



