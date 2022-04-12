import os
import pandas as pd

count = 0

g = os.walk("C://Users//UP//Desktop//毕设//学情分析-数据//雨课堂-软件工程基础-作业情况-2018级学生数据//")

for path, dir_list, file_list in g:  
    for file_name in file_list:  
        df = pd.read_excel(path + file_name, sheet_name=None)
        for pagename in df.keys():
            count += df[pagename].shape[0]


print(count)

