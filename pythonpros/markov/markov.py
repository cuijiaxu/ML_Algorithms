import numpy as np

def markov():
    paramarray=np.array([0.1,0.3,0.6])
    transfer_martrix = np.array([[0.9,0.075,0.025],
                                 [0.15,0.8,0.05],
                                 [0.25,0.25,0.5]])
    restmp = paramarray
    for i in range(25):
        res = np.dot(restmp,transfer_martrix)
        print(i,"\t",res)
        restmp = res

markov()