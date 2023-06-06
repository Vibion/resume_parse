# from pprint import pprint
# from paddlenlp import Taskflow
import re

with open('../data_txt/1.txt','r',encoding='utf-8') as f:
    data = f.read()
def nlpResume(data):    
    schema = ['姓名', '学历', '籍贯', '政治面貌' , '电话' , '邮箱']
    ie = Taskflow('information_extraction', schema=schema)
    pprint(ie(data))
# print(data)

# 正则匹配邮箱和电话号码
def reResume(data):
    # print(data)
    telephone = re.search(r"1[35678]\d{9}",data)
    print(telephone.group())
    email = re.search(r'[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}',data)
    print(email.group())

    
reResume(data)    