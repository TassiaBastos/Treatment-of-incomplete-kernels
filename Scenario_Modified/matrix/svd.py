import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds
from functools import partial


def emsvd(data, k= None, tol=1E-3, maxiter=None):
    """
    Approximate SVD on data with missing values via expectation-maximization

    Inputs:
    -----------
    Y:          (nobs, ndim) data matrix, missing values denoted by NaN/Inf
    k:          number of singular values/vectors to find (default: k=ndim)
    tol:        convergence tolerance on change in trace norm
    maxiter:    maximum number of EM steps to perform (default: no limit)

    Returns:
    -----------
    Y_hat:      (nobs, ndim) reconstructed data matrix
    mu_hat:     (ndim,) estimated column means for reconstructed data
    U, s, Vt:   singular values and vectors (see np.linalg.svd and
                scipy.sparse.linalg.svds for details)
    """
    if k is None:
        svdmethod = partial(np.linalg.svd, full_matrices=True)
    else:
        svdmethod = partial(svds, k=k)
    if maxiter is None:
        maxiter = np.Inf

    # initialize the missing values to their respective column means
    mu_hat = np.nanmean(data, axis=0, keepdims=1)
    valid = np.isfinite(data)
    Y_hat = np.where(valid, data, mu_hat)

    halt = False
    ii = 1
    v_prev = 0

    while not halt:

        # SVD on filled-in data
        U, s, Vt = svdmethod(Y_hat - mu_hat)

        # impute missing values
        Y_hat[~valid] = (U.dot(np.diag(s)).dot(Vt) + mu_hat)[~valid]

        # update bias parameter
        mu_hat = Y_hat.mean(axis=0, keepdims=1)

        # test convergence using relative change in trace norm
        v = s.sum()
        if ii >= maxiter or ((v - v_prev) / v_prev) < tol:
            print(ii)
            halt = True
        ii += 1
        v_prev = v

    return Y_hat, mu_hat, U, s, Vt


if __name__ == '__main__':
    df = pd.read_csv('Modified_na_10_Kd_std.txt', sep=" ", header=None, delimiter = "\t")
    np_array = df.to_numpy()
    # np_array = [[1,4,np.NaN], [np.NaN,np.NaN, 4], [1,2,3]]
    print(np_array)
    # print(df)
    Y_hat, mu_hat, u, s, vt = emsvd(np_array, k=6, tol=1E-3, maxiter=100)

    # print('Y_hat:\n', Y_hat) #Y_hat
    # print('\nmu_hat:', mu_hat)
    # print('\nU:', u)
    # print('\ns:', s)
    # print('\nVt:', vt)

    np.savetxt('na_10_Kd_std.txt', Y_hat)









