from docx import Document
from docx.shared import Inches

doc = Document()
doc.add_heading("파이썬이다")
doc.add_paragraph("저장")


doc.save('pdoc.docx')
