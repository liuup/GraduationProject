from tkinter.messagebox import YES
import pandas as pd
import datetime as dt

# 根目录
root_path = "C://Users//UP//Desktop//毕设//学情分析-数据//雨课堂课堂表现数据//"
file_name = "软件工程基础-数据 - 副本.xlsx"

stu_list = []

# 读取文件
df = pd.read_excel(root_path + file_name)

# 11 17 25 29
A = 0
B = 0
C = 0
D = 0
E = 0
NULL = 0

# 第几次
time = 29


for j in range(df.shape[0]):
    stu = df.values[j]

    # 单选
    if stu[time] == "未答题":
        NULL += 1
    elif "A" in stu[time]:
        A += 1
    elif "B" in stu[time]:
        B += 1
    elif "C" in stu[time]:
        C += 1
    elif "D" in stu[time]:
        D += 1

    # 多选
    # if stu[time] == "未答题":
    #     NULL += 1
    #     continue

    # if "A" in stu[time]:
    #     A += 1
    # if "B" in stu[time]:
    #     B += 1
    # if "C" in stu[time]:
    #     C += 1
    # if "D" in stu[time]:
    #     D += 1
    # if "E" in stu[time]:
    #     E += 1

print("{} {} {} {} {} {}".format(A, B, C, D, E, NULL))

