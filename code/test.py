from pprint import pprint
from paddlenlp import Taskflow
import re
import csv

# 提取基本信息
def nlpResume(data):    
    schema = ['姓名', '学历','出生时间', '籍贯', '政治面貌' ,'毕业院校','求职意向','住址']
    # ie = Taskflow('information_extraction', schema=schema,model="uie-x-base")
    ie = Taskflow("information_extraction", schema=schema)
    # pprint(ie(data))
    result = ie(data)
    pprint(result)
    return result

# 正则匹配邮箱和电话号码
def reResume(data):
    # print(data)
    telephone = re.search(r"1[35678]\d{9}",data)
    # print(telephone.group())
    if telephone == None:
        telnum = ''
    else:
        telnum = telephone.group()
    email = re.search(r'[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}',data)
    # print(email.group())
    if email == None:
        emailNum = ''
    else:
        emailNum = email.group()
    return telnum,emailNum


def writeIntocsv(base_info,telNum,emailNum):
    with open('resume.csv','a',encoding='utf-8',newline='') as f:
        csv_writer = csv.writer(f)
        name = ["姓名","学历","出生时间","籍贯","政治面貌","毕业院校","求职意向",'住址',"电话","邮箱","年龄"]
        # csv_writer.writerow(name)
        result = ["" for i in range(len(name))]
        result[name.index('电话')] = telNum
        result[name.index('邮箱')] = emailNum
        for i in name[:8]:
            if i in base_info[0]:
                if i == '出生时间':
                    for j in base_info[0][i]:
                        result[name.index(i)] =  result[name.index(i)] + j['text'] 
                else:
                    result[name.index(i)] = base_info[0][i][0]['text']
        if result[name.index('住址')] != '':
            result[name.index('籍贯')] = result[name.index('住址')]
        # result.remove(result[name.index('住址')])
        # 计算年龄
        result[name.index('年龄')] = 2023 - int(result[name.index('出生时间')][:4]) + 1
        # 判断中专
        if result[name.index('学历')] == '':
            if '中' in result[name.index('毕业院校')] and '专' in result[name.index('毕业院校')]:
                result[name.index('学历')] = '中专'
        csv_writer.writerow(result)
        print("写入数据成功")
        f.close()
        return result

for i in range(13,16):
    # 打开文件
    print(f'正在提取第{i}份文件')
    with open(f'/root/autodl-tmp/resume_parse/data_txt/{i}.txt','r',encoding='utf-8') as f:
        data = f.read()
    # 提取基本信息
    base_info = nlpResume(data)
    # 正则提取电话和邮箱
    telNum,emailNum = reResume(data) 
    # 写入csv文件
    result = writeIntocsv(base_info,telNum,emailNum)
    print(f"第{i}份简历提取成功")

