import pandas as pd
import numpy as np

def prepare_data(A,B,dataAmatchcol,dataBmatchcol):

    print("Removing rows that are not present in both data sets.")
    A = A.loc[A[('meta', dataAmatchcol)].isin(B[('meta', dataBmatchcol)])]
    B = B.loc[B[('meta', dataBmatchcol)].isin(A[('meta', dataAmatchcol)])]

    A = A.sort_values(('meta', dataAmatchcol))
    B = B.sort_values(('meta', dataBmatchcol))

    print("Verifying that the wavelengths for all data sets are the same")
    assert (len(A['wvl'].columns) == len(B['wvl'].columns)), \
        'Data sets A and B have different numbers of spectral channels!'
    assert (A['wvl'].columns.values[0] == B['wvl'].columns.values[0]), \
        "Data set A and B wavelengths are not identical. Check rounding and/or resample one data set onto the other's wavelengths"

    print("Averaging repeat spectra")
    A_uniques = np.unique(A[('meta', dataAmatchcol)])
    if len(A_uniques)==len(A[('meta', dataAmatchcol)]):
        print("Data set A: No repeat spectra, no need to calculate averages!")
        A_mean = A
    else:
        A_mean = pd.DataFrame(index=A.columns, columns=A_uniques)
        for value in A_uniques:
            print('Averaging data set A spectra: '+value)
            temp = pd.DataFrame(A[A[('meta', dataAmatchcol)] == value].mean(axis=0))
            temp.at[('meta', dataAmatchcol), 0] = value
            A_mean.loc[:, value] = temp
        A_mean = A_mean.T

    B_uniques = np.unique(B[('meta', dataBmatchcol)])
    if len(B_uniques)==len(B[('meta', dataBmatchcol)]):
        print("Data set B: No repeat spectra, no need to calculate averages!")
        B_mean = B
    else:
        B_mean = pd.DataFrame(index=B.columns, columns=B_uniques)
        for value in np.unique(B[('meta', dataBmatchcol)]):
            print('Averaging data set B spectra: ' + value)
            temp = pd.DataFrame(B[B[('meta', dataBmatchcol)] == value].mean(axis=0))
            temp.at[('meta', dataBmatchcol), 0] = value
            B_mean.loc[:, value] = temp
        B_mean = B_mean.T

    return A_mean, B_mean

