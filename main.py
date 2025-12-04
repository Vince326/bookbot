from stats import wordCount, charFrequency

def get_book_text (filePath):
    
    with open(filePath) as f:
        file_contents = f.read()

    return file_contents





def main():
    book_text = get_book_text("books/frankenstein.txt")
    book_word_count = wordCount(book_text)
    book_dict = charFrequency(book_text)
    print(book_dict)
    


if __name__ == "__main__":
    main()

