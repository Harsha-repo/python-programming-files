#we try make the files read in the audio form 
#we intall two libraries that are usefull for the audio genartion using python
#pip install pyttsx3 and pip install pyPDF 
#after installing both the libraries we start the program
import pyttsx3
import PyPDF3

file = open ("pdfs.pdf",mode="rb")
pdf_reader = PyPDF3.PdfFileReader(file)
pages = pdf_reader.getNumPages()
print(pages)

melo = pyttsx3.init()
page = pdf_reader.getPage(6)
text = page.extractText()


melo.say(text)

melo.runAndWait()

