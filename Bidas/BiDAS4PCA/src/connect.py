'''
    Connects to an R server specified by user.
    The function accepts parameters for configuration.
'''

import pyRserve as R

def connect():
    return R.connect()

def get_metrics(c, X, y):
    c.r.X = X
    c.r.y = y
    c.r('df_X <- as.data.frame(X)')
    c.r('df_y <- as.data.frame(y)')
    c.r('library("ECoL")')
    metrics = []
    balance = c.r('balance(df_X, df_y)')
    for i in range(len(balance)):
        metrics.append(balance[i])
    print('# Balance (C1, C2):\t', balance)
    correlation = c.r('correlation(df_X, df_y)')
    for i in range(len(correlation)):
        metrics.append(correlation[i])
    print('# Correlation (C1, C2, C3, C4):\t', correlation)
    dimensionality = c.r('dimensionality(df_X, df_y)')
    for i in range(len(dimensionality)):
        metrics.append(dimensionality[i])
    print('# Dimensionality (T2, T3, T4):', dimensionality)
    linearity = c.r('linearity(df_X, df_y)')
    for i in range(len(linearity)):
        metrics.append(linearity[i])
    print('# Linearity (L1, L2, L3):\t', linearity)
    neighborhood = c.r('neighborhood(df_X, df_y)')
    for i in range(len(neighborhood)):
        metrics.append(neighborhood[i])
    print('# Neighborhood (N1, N2, N3, N4, T1, LSC):\t', neighborhood)
    network = c.r('network(df_X, df_y)')
    for i in range(len(network)):
        metrics.append(network[i])
    print('# Network (Density, ClsCoef, Hubs):\t', network)
    overlap = c.r('overlapping(df_X, df_y)')
    for i in range(len(overlap)):
        metrics.append(overlap[i])
    print('# Overlap (F1, F1v, F2, F3, F4):\t', overlap)
    smoothness = c.r('smoothness(df_X, df_y)')
    for i in range(len(smoothness)):
        metrics.append(smoothness[i])
    print('# Smoothness (S1, S2, S3, S4):\t', smoothness)
    return metrics
    
