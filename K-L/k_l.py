import numpy as np


# 每个样本数据作为一行，每一列作为一个特征


# 平移坐标系
def newData(mat_old):
    meanVal = np.mean(mat_old, axis=0)  # axis为压缩行，求每列的平均值，返回1*n矩阵
    mat_new = mat_old - meanVal  # 减去平均值，即以平均值为新坐标轴，
    # 由于此处减去了平均向量，故求自相关矩阵时可用协方差矩阵
    return mat_new


def pca(mat_data, n):
    mat_new = newData(mat_data)
    mat_cov = np.cov(mat_new, rowvar=0)  # 若rowvar为0，一行代表一个样本

    # 特征值和特征向量
    eigValues, eigVectors = np.linalg.eig(np.mat(mat_cov))  # 特征向量按列放，即一列代表一个特征向量
    eigValuesSort = np.argsort(eigValues)  # 特征值排序
    n_eigValuesIndice = eigValuesSort[-1:-(n + 1):-1]  # 最大的n个特征值的下标  最后的-1为切取方向
    n_eigVect = eigVectors[:, n_eigValuesIndice]  # 最大的n个特征值对应的特征向量
    low_dimension_mat = mat_new * n_eigVect
    return low_dimension_mat


if __name__ == '__main__':
    mat_old = np.array([[0, 0, 0], [1, 0, 0], [1, 0, 1], [1, 1, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 1, 1]])
    mat_low2 = pca(mat_old, 2)
    mat_low1 = pca(mat_old, 1)
    print("降为二维的样本数据为:")
    print(mat_low2)
    print("降为一维的样本数据为:")
    print(mat_low1)
