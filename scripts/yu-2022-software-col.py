import pandas as pd
import datetime as dt

# 根目录
root_path = "C://Users//UP//Desktop//毕设//学情分析-数据//雨课堂课堂表现数据//"
file_name = "软件工程基础-数据 - 副本.xlsx"

# 标准签到时间
std_time_8 = dt.datetime(2022, 4, 18, 8, 20)
std_time_10 = dt.datetime(2022, 4, 18, 10, 20)

stu_list = []

# 读取文件
df = pd.read_excel(root_path + file_name)

# 准时
ontime = 0
# 迟到
aftertime = 0
# 未上课
nocheck = 0

# 第一次签到统计
# print(df.values[0])

# 4 6 8 12 14 18 20 22 26
time = 26

for j in range(df.shape[0]):
    stu = df.values[j]

    if stu[time] == "未上课":
        nocheck += 1
        continue

    check_time = dt.datetime.strptime(stu[time], "%Y-%m-%d %H:%M:%S").replace(month=4, day=18)

    if check_time <= std_time_10:
        ontime += 1
    else:
        aftertime += 1

    # check_time <= std_time_8 ? ontime += 1 : aftertime += 1

print("{}, {}, {}".format(ontime, aftertime, nocheck))
