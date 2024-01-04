# Converts PDF to MP3 using the detected language and voice.

import pyttsx3
import PyPDF2
from langdetect import detect

# Function to extract text from the PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_number in range(len(reader.pages)):
            text += reader.pages[page_number].extract_text()
    return text

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Path to the PDF file
pdf_path = 'book.pdf'  # Replace with the path to your PDF file

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Detect the language of the extracted text
detected_language = detect(pdf_text)

# Set the language for text-to-speech based on the detected language
if detected_language == 'en':
    engine.setProperty('voice', 'english')
    print("English text detected. Using an English voice.")
elif detected_language == 'el':
    engine.setProperty('voice', 'greek')
    print("Greek text detected. Using a Greek voice.")
else:
    print("Language not detected or language not supported. Using default voice.")

# Save the text as an MP3 file
output_file = 'book.mp3'
engine.save_to_file(pdf_text, output_file)
engine.runAndWait()

print(f"PDF converted to MP3 using the detected language and voice as: {output_file}")