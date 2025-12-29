from stats import wordCount, charFrequency
from stats import sortChars
import sys

def get_book_text (filePath):
    
    with open(filePath) as f:
        file_contents = f.read()

    return file_contents





def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    
    book_word_count = wordCount(book_text)
    print(f"Found {book_word_count} total words")

    print("--------- Character Count -------")
    char_dict = charFrequency(book_text)
    sorted_list = sortChars(char_dict)

    for char in sorted_list:
        ch = char["char"]
        count = char["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")

    print("============= END ===============")
    
    


if __name__ == "__main__":
    main()

