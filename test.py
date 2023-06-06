from pprint import pprint
from paddlenlp import Taskflow

schema = {'姓名':['出生日期','毕业学校','学历']}
# ['年龄', '姓名','毕业学校','学历']
ie = Taskflow('information_extraction', schema=schema, precision='fp16')
for i in range(18,101):
    with open(f'/home/jiajun/jiajun_data/transformers/resume_parse/data_txt/{i}.txt','r')as f :
        data = f.read()
    # pprint(ie(data))
    pprint(ie(data)[0]['姓名'][0]['text'])
# schema = {'就读学校':['时间','所学专业','学历']}
# ie.set_schema(schema)
# pprint(ie(data))
# [{'姓名': [{'end': 64,
#           'probability': 0.9909876619361349,
#           'relations': {'出生日期': [{'end': 10,
#                                   'probability': 0.9975840632731305,
#                                   'start': 3,
#                                   'text': '1996.05'}],
#                         '毕业学校': [{'end': 451,
#                                   'probability': 0.9149491045183673,
#                                   'start': 445,
#                                   'text': '华南理工大学'}]},
#           'start': 61,
#           'text': '江奕云'},
#          {'end': 1397,
#           'probability': 0.760637988663639,
#           'relations': {'毕业学校': [{'end': 1171,
#                                   'probability': 0.8419093510203339,
#                                   'start': 1165,
#                                   'text': '华南理工大学'}]},
#           'start': 1394,
#           'text': '罗嘉良'}]}]
