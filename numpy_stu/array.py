import numpy as np

a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
sum = a + b
difference = a - b
product = a * b
quotient = a / b
print("Sum = \n", sum)
print("Difference = \n", difference)
print("Product = \n", product)  # 只是逐元素相乘 a.dot(b)会进行矩阵乘法
print("Quotient = \n", quotient)

# 数组创建

# 一维
a = np.array([0, 1, 2, 3, 4, 5])
b = np.array((0, 1, 2, 3, 4, 5))
c = np.arange(5)
d = np.linspace(0, 2 * np.pi, 5)

print(a)
print(b)
print(c)
print(d)

# 二维
# 为了创建一个二维数组，需要传递一个列表的列表，或一个序列的序列，三维则是列表的列表的列表

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
print(a[2, 4])

# 多维数组切片
# 切片语法 [start_index:end_index:step] step默认为1
# MD slicing
print(a[0, 1:4])  # >>>[12 13 14]
print(a[1:4, 0])  # >>>[16 21 26]
print(a[::2, ::2])  # >>>[[11 13 15]
#     [21 23 25]
#     [31 33 35]]

print(a[:, 1])  # >>>[12 17 22 27 32]

print(type(a))
print(a.dtype)
print(a.size)
print(a.shape)
print(a.itemsize)  # 每个项占用的字节数
print(a.ndim)  # 维数
print(a.nbytes)  # 所有数据占用的字节数，并不计算数组的开销

# Basic Operators
a = np.arange(25)
a = a.reshape((5, 5))
print(a)
c = [0, 2, 4]
print(a[:, c])

b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
b = b.reshape((5, 5))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a < b)
print(a > b)

print(a.dot(b))  # 计算点积

print(a.sum())
print(a.min())
print(a.max())
print(a.cumsum())  # 先将前两个数相加存储在一个列表添加到第三个元素中，然后再存储在一个列表中，重复

# 花式索引 获取特定元素的有效方法
# Fancy indexing
a = np.arange(0, 100, 10)
indices = [1, 5, -1]
b = a[indices]
print(a)  # >>>[ 0 10 20 30 40 50 60 70 80 90]
print(b)  # >>>[10 50 90]

# Boolean masking 布尔屏蔽
import matplotlib.pyplot as plt

a = np.linspace(0, 2 * np.pi, 50)
b = np.sin(a)
plt.plot(a, b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()

# 缺省索引


# where function
a = np.arange(0, 100, 10)
b = np.where(a < 50)
c = np.where(a >= 50)[0]
print(a)
print(b)
print(c)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
row_r1 = a[1, :]  # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)
# Prints "[[ 2]
#          [ 6]
#          [10]] (3, 1)"


# 整数数组索引

a = np.array([[1, 2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"

# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]])  # Prints "[2 2]"

# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"

# 整数数组索引的有效作用为从矩阵的每一行选取或改变一个元素
# Create a new array from which we will select elements
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(a)  # prints "array([[ 1,  2,  3],
#                [ 4,  5,  6],
#                [ 7,  8,  9],
#                [10, 11, 12]])"

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10

print(a)  # prints "array([[11,  2,  3],
#                [ 4,  5, 16],
#                [17,  8,  9],
#                [10, 21, 12]])


# 布尔索引
a = np.array([[1, 2], [3, 4], [5, 6]])

bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
# this returns a numpy array of Booleans of the same
# shape as a, where each slot of bool_idx tells
# whether that element of a is > 2.

print(bool_idx)  # Prints "[[False False]
#          [ True  True]
#          [ True  True]]"

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print(a[a > 2])  # Prints "[3 4 5 6]"

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print(x.T)
print(x.dot(y))  # dot才是矩阵的乘法
print(np.dot(x, y))

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

# broadcasting
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)  # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)

# 或者
vv = np.tile(v, (4, 1))  # stack 4 copies of  v on top of each other
print(vv)
y = x + vv
print(y)

# 然而若使用广播broadcasting，可有
y = x + v  # add v to each row of x using broadcasting

# 将两个数组一起广播遵循以下规则：

# 如果数组不具有相同的rank，则将较低等级数组的形状添加1，直到两个形状具有相同的长度。
# 如果两个数组在维度上具有相同的大小，或者如果其中一个数组在该维度中的大小为1，则称这两个数组在维度上是兼容的。
# 如果数组在所有维度上兼容，则可以一起广播。
# 广播之后，每个数组的行为就好像它的形状等于两个输入数组的形状的元素最大值。
# 在一个数组的大小为1且另一个数组的大小大于1的任何维度中，第一个数组的行为就像沿着该维度复制一样

x = np.array([[1,2,3], [4,5,6]])
print(x.T)
v=np.array([1,2,3])
w=np.array([4,5])
print((x.T+w).T)
print(x+np.reshape(w,(2,1)))
