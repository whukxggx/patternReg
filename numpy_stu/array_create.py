import numpy as np

# 一维
array = np.arange(20)

# 二维
array_2 = np.arange(20).reshape(4, 5)

# 三维
array_3 = np.arange(27).reshape(3, 3, 3)

arr_t = np.arange(10, 25, 2)  # 间隔为2
print(arr_t)

np.zeros((2, 4))
np.ones((2, 4))
em = np.empty((2, 3))  # 内容随机
print(em)
y = np.empty_like(array_2)  # Create an empty matrix with the same shape as x
print(y)

# full 指定值
full1 = np.full((2, 2), 3)  # 以3填充
full_like = np.full_like(array_2, 3)
print(full1)
print(full_like)

# eye创建对角线为1其余为0
np.eye(3, 3)

# linspace 指定间隔内的返回间隔均匀的数字
np.linspace(0, 10, 4)

# 列表转换
list = [4, 5, 6]
array_list = np.array(list)
print(type(list))
print(type(array_list))


# 随机函数
r2=np.random.random((2,2))
r3=np.random.random((3,4,5))
print(r2)
print(r3)
