from pdf2image import convert_from_path

for i in range(1,101):
    # convert(f"/root/autodl-tmp/resume_parse/data/{i}.docx", f"/root/autodl-tmp/resume_parse/data_pdf/{i}.pdf")
    
    pages = convert_from_path(f"/root/autodl-tmp/resume_parse/data_pdf/{i}.pdf")
    for index , page in enumerate(pages):
        page.save(f"/root/autodl-tmp/resume_parse/data_png/{i}_{index}.png", 'PNG')