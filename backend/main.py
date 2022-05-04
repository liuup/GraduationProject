# from ast import Num
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


'''
测试接口
'''
@app.get("/")
def root():
    return success_json

'''
用户登录接口
'''
class User(BaseModel):
    num: str
    pwd: str

@app.post("/login")
def login(user: User):
    # print(user)
    cnx = mysql.connector.connect(**localdb)
    # 查询游针
    cursor = cnx.cursor()

    # 将接收到的数据转为字典
    post_dict = json.loads(user.json())

    query_sql = "select * from user where num = '{}' and password = '{}'"\
        .format(post_dict["num"], post_dict["pwd"])

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