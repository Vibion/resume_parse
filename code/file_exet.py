# from docx import Document
# import aspose.words as aw

# doc = aw.Document("D:\\ruanjianbeiA8\\resume_parse\\code\\1.docx")
# doc.save("D:\\ruanjianbeiA8\\resume_parse\\code\\1.pdf")
# from docx2pdf import convert
from pdf2image import convert_from_path

for i in range(1,101):
    # convert(f"/root/autodl-tmp/resume_parse/data/{i}.docx", f"/root/autodl-tmp/resume_parse/data_pdf/{i}.pdf")
    
    pages = convert_from_path(f"/root/autodl-tmp/resume_parse/data_pdf/{i}.pdf")
    for page in pages:
        page.save(f"/root/autodl-tmp/resume_parse/data_png/{i}.png", 'PNG')