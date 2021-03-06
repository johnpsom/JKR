import pandas as pd
import numpy as np
from itertools import combinations


'''this function creates all the number combinations in a m from n lottery'''
def create_lot(n,m):
    L=np.arange(1,n+1,1)
    columns=[f'st{mo}' for mo in range(1,m+1)]
    tot_lot_list=[list(comb) for comb in combinations(L, m)]
    df = pd.DataFrame(tot_lot_list, columns = columns)
    return df


'''example of a 5 from 45 lottery'''
m=5
n=45
df_jkr=create_lot(n,m)
df_jkr.to_pickle(f"./lottery_{m}outof{n}.pkl")  


