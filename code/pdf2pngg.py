from pdf2image import convert_from_path
pages = convert_from_path("/root/autodl-tmp/resume_parse/code/1.pdf")
for page in pages:
    page.save("/root/autodl-tmp/resume_parse/code/1.png", 'PNG')