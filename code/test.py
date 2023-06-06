from pprint import pprint
from paddlenlp import Taskflow
import re

# with open('/root/autodl-tmp/resume_parse/data_txt/1.txt','r',encoding='utf-8') as f:
#     data = f.read()
def nlpResume():    
    schema = ['姓名', '学历','出生时间', '籍贯', '政治面貌' , '电话' , '邮箱','毕业院校','教育背景','求职意向']
    # ie = Taskflow('information_extraction', schema=schema,model="uie-x-base")
    ie = Taskflow("information_extraction", schema=schema, model="uie-x-base")
    # pprint(ie(data))
    pprint(ie({"doc": "/root/autodl-tmp/resume_parse/data_png/1_0.png"}))
# print(data)

# 正则匹配邮箱和电话号码
def reResume(data):
    # print(data)
    telephone = re.search(r"1[35678]\d{9}",data)
    print(telephone.group())
    email = re.search(r'[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}',data)
    print(email.group())
# reResume(data)   
nlpResume() 