import docx2txt


for i in range(3,101):
    text = docx2txt.process(f"D:/ruanjianbeiA8/resume_parse/data/{i}.docx")
    text1 = text.replace('\t','')
    text1 = text1.replace(' ','')
    text1 = text1.split('\n')
    # print(text)
    text_post = list(set(text1))
    text_post.sort(key=text1.index)
    text1 = ' '.join(text_post)
    # with open(f'/home/jiajun/jiajun_data/transformers/resume_parse/data_txt/{i}.txt','w') as f :
    #     f.write(text1)
    # print(i)
# print(text)