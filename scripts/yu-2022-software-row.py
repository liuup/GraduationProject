import pandas as pd
import datetime as dt

# 根目录
root_path = "C://Users//UP//Desktop//毕设//学情分析-数据//雨课堂课堂表现数据//"
file_name = "软件工程基础-数据.xlsx"

# 标准签到时间
std_time_8 = dt.datetime(2022, 4, 18, 8, 20)
std_time_10 = dt.datetime(2022, 4, 18, 10, 20)

stu_list = []

# 读取文件
df = pd.read_excel(root_path + file_name)

for j in range(df.shape[0]):
    # 学生的计算总分，计算完一次清零
    count = 0

    # 获得学生
    stu = df.values[j]

    '''
    八点签到分数计算
    '''
    # for i in (4, 8, 12, 20, 22):
    #     if stu[i] == "未上课":
    #         continue
    #     check_time = dt.datetime.strptime(stu[i], "%Y-%m-%d %H:%M:%S").replace(month=4, day=18)
    #     interval = check_time - std_time_8
    #     # print(int(interval.total_seconds() / 60))
    #     if int(interval.total_seconds() / 60) <= 0:
    #         count += 45
    #     elif 0 < int(interval.total_seconds() / 60) <= 45:
    #         count += (45 - int(interval.total_seconds() / 60))

    '''
    十点签到分数计算
    '''
    # for i in (6, 14, 18, 26):
    #     if stu[i] == "未上课":
    #         continue
    #     check_time = dt.datetime.strptime(stu[i], "%Y-%m-%d %H:%M:%S").replace(month=4, day=18)
    #     interval = check_time - std_time_10
    #     # print(int(interval.total_seconds() / 60))
    #     if int(interval.total_seconds() / 60) <= 0:
    #         count += 45
    #     elif 0 < int(interval.total_seconds() / 60) <= 45:
    #         count += (45 - int(interval.total_seconds() / 60))

    '''
    弹幕分数计算
    '''
    # for i in (5, 7, 9, 13, 15, 19, 21, 23, 27):
    #     danmu_count = stu[i]
    #     if danmu_count > 10:
    #         count += 10
    #     else:
    #         count += danmu_count

    '''
    答题计算
    '''
    for i in (10, 16, 24, 28):
        if stu[i] == 1:
            count += 30
        elif stu[i] == 0 and stu[i + 1] == "未答题":
            count += 0
        else:
            count +=15

    stu_list.append(count)

stu_list.sort(reverse=True)

file = open(root_path + "stu.txt", "w")
for i in range(len(stu_list)):
    file.write("[" + str(i + 1) + "," + str(stu_list[i]) + "],\n")
    # file.write(str(stu_list[i]) + "\n")
file.close()

# print(stu_list)
