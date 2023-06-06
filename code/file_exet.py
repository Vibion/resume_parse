from docx import Document
import aspose.words as aw

# doc = aw.Document("D:\\ruanjianbeiA8\\resume_parse\\code\\1.docx")
# doc.save("D:\\ruanjianbeiA8\\resume_parse\\code\\1.pdf")
from docx2pdf import convert

convert("D:\\ruanjianbeiA8\\resume_parse\\code\\1.docx", "D:\\ruanjianbeiA8\\resume_parse\\code\\1.pdf")