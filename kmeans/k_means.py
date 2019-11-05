import random
import operator

# 取k=3，初始点随机取
# 共150个样本


# 获取随机的三个初始点
# n为数据总量
def get_random_init(datas, n):
    z = random.sample(range(0, n), 3)
    return datas[z[0]], datas[z[1]], datas[z[2]]


# 返回的是一个双列表形式和类别名的列表
def read_file(file_name):
    data = []
    data_name = []
    with open(file_name) as file_object:
        lines = file_object.readlines()
        for line in lines:
            line = line.rstrip()
            numbers = line.split(',')
            read_data = [float(x) for x in numbers[0:4]]
            read_data_name = numbers[-1]  # 类别名
            data.append(read_data)
            data_name.append(read_data_name)
        return data, data_name


# 计算两个数组间距离的平方
def compute_distance(arr1, arr2):
    ret = 0.0
    for a, b in zip(arr1, arr2):
        dis1 = abs(a - b) ** 2
        ret += dis1
    return ret


# 计算中心点,arr为多维数组
def compute_mid(arr):
    arr_ret = [0] * len(arr[0])  # 初始化长度为arr的每个子数组的长度,初始值为0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr_ret[j] += arr[i][j]
    for i in range(len(arr_ret)):
        arr_ret[i] /= len(arr)
    return arr_ret


def get_index_of_min(dis):
    mint = min(dis)
    for i in range(len(dis)):
        if dis[i] == mint:
            return i


# 比较中心点是否改变
def compare_mid(z_old, z_new):
    for z_o,z_n in zip(z_old,z_new):
        if operator.eq(z_o,z_n)==False:
            return 0
    return 1


# 通过中心点进行分组
# 返回一个z的子数组(中心点)有多少个的多维数组,data是个多维数组
def dicide_group(z, data):
    group1 = []
    group2 = []
    group3 = []
    # 对数据进行分组，目前是三个
    for d in data:
        dist = []
        for z_sub in z:
            dist.append(compute_distance(z_sub, d))
        # 通过dist数组中最小的那个值确定d应该的分组
        index = get_index_of_min(dist)
        if index == 0:
            group1.append(d)
        elif index == 1:
            group2.append(d)
        else:
            group3.append(d)
    return group1, group2, group3


def k_means(file_name):
    data, dataname = read_file(file_name)
    lend = len(data)
    # 随机选取三个中心点
    z1, z2, z3 = get_random_init(data, lend)
    z = []
    z.append(z1)
    z.append(z2)
    z.append(z3)
    while True:
        g1, g2, g3 = dicide_group(z, data)
        z1 = compute_mid(g1)
        z2 = compute_mid(g2)
        z3 = compute_mid(g3)
        z_new = []
        z_new.append(z1)
        z_new.append(z2)
        z_new.append(z3)
        if compare_mid(z, z_new) == 1:
            break
        z = z_new  # z_new 变为z_old
    return g1, g2, g3  # 返回三个已分好的组

def get_index_of_g_sub(data,g_sub):
    i=0
    for d in data:
        i+=1
        if operator.eq(d,g_sub):
            return i

# 根据数据集已经知道每类50个
def get_accuracy_rate(g,file_name):
    data,dataname=read_file(file_name)
    num1=0
    num2=0
    num3=0
    for g_sub in g:
        if get_index_of_g_sub(data,g_sub)>=1 and\
            get_index_of_g_sub(data,g_sub)<=50:
            num1+=1
    for g_sub in g:
        if get_index_of_g_sub(data,g_sub)>=51 and \
                get_index_of_g_sub(data,g_sub)<=100:
            num2+=1
    for g_sub in g:
        if get_index_of_g_sub(data,g_sub)>=101 and \
                get_index_of_g_sub(data,g_sub)<=150:
            num3+=1
    num=max(num1,num2,num3)  # 在三种类型中最多的就是
    if(num==num1):
        print("Iris-setosa类型，50个样本中共有"+str(num1)+"个命中"+",共聚集了"+str(len(g))+"个数据集"+",命中率"+str(num1/len(g)))
    elif(num==num2):
        print("Iris-versicolor类型，50个样本中共有"+str(num2)+"个命中"+",共聚集了"+str(len(g))+"个数据集"+",命中率"+str(num2/len(g)))
    else:
        print("Iris-virginica类型，50个样本中共有"+str(num3)+"个命中"+",共聚集了"+str(len(g))+"个数据集"+",命中率"+str(num3/len(g)))

if __name__ == '__main__':
    file_name = 'iris.data'
    g1, g2, g3 = k_means(file_name)
    print("group1:")
    print("共"+str(len(g1))+"个")
    print(g1)
    print("group2:")
    print("共"+str(len(g2))+"个")
    print(g2)
    print("group3:")
    print("共"+str(len(g3))+"个")
    print(g3)
    get_accuracy_rate(g1,file_name)
    get_accuracy_rate(g2,file_name)
    get_accuracy_rate(g3,file_name)

