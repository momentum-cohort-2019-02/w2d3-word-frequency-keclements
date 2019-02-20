STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# 

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass

def normalize_text(text):
    """
    take imported text, lower case, remove punctuation--> remove whitespace-- 
    """
    text = text.lower()
    valid_chars = string.ascii_letters + string.whitespace + string.digits


#imported text from ClintonÍ
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)


 # remove punctuation
    new_text = ""
    for char in text:
        if char in valid_chars:
            new_text += char

    text = new_text
    text = text.replace("\n", " ")
    return text

# Print Word frequence from given file
 print(
# # get dictionary frequency    

#print 




