from ast import Num
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
# from typing import Optional

import json


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
    print(user)
   
    # 测试账号密码
    test_num = "123456"
    test_pwd = "654321"

    # if()
    # 将接收到的数据转为字典
    user_dict = json.loads(user.json())
    # print(user_dict["num"])


    if(user_dict["num"] == test_num and user_dict["pwd"] == test_pwd):
        return success_json
    else:
        return failure_json