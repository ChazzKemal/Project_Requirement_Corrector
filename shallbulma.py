import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
# For easier files this could help for extracting requirement sentences
# Open the PDF file and extract the text
pdf_file = PyPDF2.PdfReader(open("D18.pdf", "rb"))
text = ""
for page in range(len(pdf_file.pages)):
    text += pdf_file.pages[page].extract_text()

# Split the text into sentences
sentences = sent_tokenize(text)

# Loop through the sentences and extract those containing the word "shall"
shall_sentences = []
for sentence in sentences:
    if "shall" in sentence:
        shall_sentences.append(sentence)

# Print the extracted sentences
for sentence in shall_sentences:
    print(sentence)