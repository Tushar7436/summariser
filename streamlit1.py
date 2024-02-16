import re
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import PyPDF2

nltk.download('punkt')
nltk.download('stopwords')

# Function to extract important sentences from a PDF based on keywords
def extract_important_sentences_from_pdf(pdf_path, keywords):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize a list to store important sentences
        important_sentences = []
        
        # Iterate through each page in the PDF
        for page in pdf_reader.pages:
            # Extract text from the page
            page_text = page.extract_text()
            
            # Tokenize the page text into sentences
            sentences = sent_tokenize(page_text)
            
            # Tokenize the page text into words
            words = word_tokenize(page_text)
            
            # Remove stopwords from the words
            stop_words = set(stopwords.words('english'))
            words = [word for word in words if word.lower() not in stop_words]
            
            # Calculate the frequency distribution of words
            fdist = FreqDist(words)
            
            # Iterate through each sentence in the page
            for sentence in sentences:
                # Check if any of the keywords are present in the sentence
                if any(keyword.lower() in sentence.lower() for keyword in keywords):
                    # Append the sentence to the list of important sentences
                    important_sentences.append(sentence)
        
        # Join the important sentences together
        important_sentences_text = '\n'.join(important_sentences)
        
        # Return the important sentences
        return important_sentences_text

# Sample PDF file path
pdf_path = 'trail.pdf'


# Keywords to search for in the PDF
keywords = ['technology', 'security']

important_sentences = extract_important_sentences_from_pdf(pdf_path, keywords)

# Printing the important sentences
print("The summarization of document:")
print(important_sentences)