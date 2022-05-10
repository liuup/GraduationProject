from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
# from typing import Optional

import json
import mysql.connector

app = FastAPI()

origins = {
    "*"
}

# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 本地数据库配置
localdb = {
    "user": "root",
    "password": "123698745leo",
    "host": "127.0.0.1",
    "database": "db1"
}

success_json = json.dumps({"status": "success"})
failure_json = json.dumps({"status": "failure"})

# 权限根路由配置
stu_root_router = "/stu"
teacher_root_router = "/teacher"
admin_root_router = "/admin"


'''
测试接口
'''
@app.get("/")
def root():
    return success_json



'''
学生登录接口
'''
class User(BaseModel):
    identity: str   # 身份
    account: str    # 账号
    pwd: str        # 密码

@app.post("/login")
def login(user: User):
    print(user)
    cnx = mysql.connector.connect(**localdb)
    # 查询游针
    cursor = cnx.cursor()

    # 将接收到的数据转为字典
    post_dict = json.loads(user.json())

    # 用户权限查询数据库表
    table = post_dict["identity"]

    query_sql = "select * from " + table + " where account = '{}' and password = '{}'"\
        .format(post_dict["account"], post_dict["pwd"])

    cursor.execute(query_sql)

    # 全部数据
    data = cursor.fetchall()

    print(data)
    
    # 关闭连接
    cursor.close()
    cnx.close()


    if(len(data) == 1):
        return success_json
    else:
        return failure_json




'''
用户注册接口
'''
class RegUser(BaseModel):
    name: str
    num: str
    pwd: str
    phone: str
    date: str

@app.post("/register")
def register(reguser: RegUser):
    print(reguser)

    # cnx = mysql.connector.connect(**localdb)
    # # 查询游针
    # cursor = cnx.cursor()
    
    # # 获取post请求体的字典类型数据
    # user_dict = json.loads(reguser.json())

    # sql = "insert into user(name, password, last_logintime, phone, num) values ('{}', '{}', '{}', '{}', '{}')"\
    #     .format(user_dict["name"], user_dict["pwd"], user_dict["date"], user_dict["phone"], user_dict["num"])
    
    # cursor.execute(sql)
    # cnx.commit()

    # cursor.close()
    # cnx.close()

    # if cursor.rowcount == 0:
    #     return failure_json
    # else:
    #     return success_json
    
    return failure_json


'''
公告返回接口
'''
@app.get("/notices")
def notices():
    cnx = mysql.connector.connect(**localdb)
    # 查询游针
    cursor = cnx.cursor()

    query_sql = "select * from notices"

    cursor.execute(query_sql)
    
    # 全部数据
    data = cursor.fetchall()
    # 数据描述
    desc = cursor.description

    # print(data)
    # print(desc)

    # 存储全部数据的列表
    res_list = []
    
    for i in range(0, len(data)):
        # 存储单个数据的字典
        res_dist = {}
        for j in range(0, len(data[0])):
            # 将时间序列化
            if desc[j][0] == "msg_date":
                res_dist[desc[j][0]] = str(data[i][j])
                continue
            # pass
            res_dist[desc[j][0]] = data[i][j]
        res_list.append(res_dist)

    # print(res_list)

    # 关闭连接
    cursor.close()
    cnx.close()

    if len(res_list) == 0:
        return failure_json
    else:
        return json.dumps(res_list)


'''
================================================================
#
# 公告[添加，编辑，删除]接口
#
================================================================
'''

'''
公告添加接口
'''
class Notice(BaseModel):
    title: str
    message: str
    msg_date: str

@app.post("/notices/add")
def noticesAdd(notice: Notice):
    print(notice)

    cnx = mysql.connector.connect(**localdb)
    # 查询游针
    cursor = cnx.cursor()

    # 获取post请求体的字典类型数据
    notice_dict = json.loads(notice.json())

    # print(notice_dict)

    sql = "insert into notices(title, message, msg_date) values ('{}', '{}', '{}')"\
        .format(notice_dict["title"], notice_dict["message"], notice_dict["msg_date"])
    
    cursor.execute(sql)
    cnx.commit()

    cursor.close()
    cnx.close()

    if cursor.rowcount == 0:
        return failure_json
    else:
        return success_json


'''
公告编辑接口
'''
# class Notice(BaseModel):
#     title: str
#     message: str
#     msg_date: str

@app.post("/notices/edit")
def noticeEdit():
    return failure_json


'''
公告删除接口
'''
# class Notice(BaseModel):
#     title: str
#     message: str
#     msg_date: str

@app.post("/notices/delete")
def noticeDelete():
    return failure_json