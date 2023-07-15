import re
import PyPDF2
#This file is for extracting requirements for another pdf with sometimes inconsistent formatting 
pdf_file = PyPDF2.PdfReader(open("Nasav3.pdf", "rb"))
text = ""
for page in range(len(pdf_file.pages)):
    text += pdf_file.pages[page].extract_text()
#print(text,len(pdf_file.pages),len(text))    
# Find sentences containing "shall" and extract them
print(text)
text = text.replace("\n", " ")
sentences = re.findall('[^.]* shall [^.]*\.', text)

text2=""
#sentences = re.findall(r'[^.?!]*(?<=[.?\s!])flung(?=[\s.?!])[^.?!]*[.?!]', pdf_text)
for sentence in sentences:
   text2 += sentence + "\n"
with open("statementlarsscv3.txt", "w",encoding="utf-8") as f:
    for sentence in sentences:
        #text2 += sentence + "\n"
        f.write(sentence+"\n")
print(text2)