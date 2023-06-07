from paddlenlp.utils.doc_parser import DocParser
from pprint import pprint
from paddlenlp import Taskflow


# 图片解析
doc_parser = DocParser(ocr_lang="ch")
doc_path = "/root/autodl-tmp/resume_parse/data_png/1_0.png"
parsed_doc = doc_parser.parse({"doc": doc_path})
# 处理返回结果,拼接字符串
result = []
for i in range(len(parsed_doc['layout'])):
    result.append(parsed_doc['layout'][i][1])
result = ' '.join(result)
# 提取文本
schema = ['姓名', '学历','出生时间', '籍贯', '政治面貌' , '电话' , '邮箱','毕业院校','教育背景','求职意向','公司']
ie = Taskflow("information_extraction", schema=schema)
# pre = result.replace('[]','')
# print(pre)
pprint(ie(result))

doc_parser.write_image_with_results(
        doc_path,
        layout=parsed_doc['layout'],
        save_path="/root/autodl-tmp/resume_parse/data_ocr/1.png")
print("finish!!!")