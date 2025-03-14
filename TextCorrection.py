from textblob import TextBlob


def correct_spelling(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()  
    return str(corrected_text)


if __name__ == "__main__":
    print("Welcome to the Spelling Correction Tool!")
    user_input = input("Enter the text with spelling errors: ")
    
    corrected_text = correct_spelling(user_input)
    
    print("\nOriginal Text: ", user_input)
    print("Corrected Text: ", corrected_text)
from textblob import TextBlob
from transformers import pipeline


corrector = pipeline("text2text-generation", model="facebook/bart-large-cnn")


def basic_spelling_correction(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()  
    return str(corrected_text)

def advanced_spelling_correction(text):
    result = corrector(text)
    return result[0]['generated_text']


def combined_correction(text):
    
    basic_corrected_text = basic_spelling_correction(text)
    

    advanced_corrected_text = advanced_spelling_correction(basic_corrected_text)
    
    return advanced_corrected_text


if __name__ == "__main__":
    print("Welcome to the Combined Spelling Correction Tool!")
    user_input = input("Enter the text with spelling errors: ")
    
    corrected_text = combined_correction(user_input)
    
    print("\nOriginal Text: ", user_input)
    print("Corrected Text: ", corrected_text)
