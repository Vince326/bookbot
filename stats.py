def wordCount (book_text):
    words =  book_text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")
    return num_words


def charFrequency(book_text):
    lowerChar = book_text.lower()

    char_dict = {}
    
    for ch in lowerChar:
        if ch in char_dict:
            char_dict[ch]= char_dict[ch] + 1
        else:
            char_dict[ch] = 1
            
    return char_dict

def sortChars(char_dict):
    characters = []
    for char, num in char_dict.items():
        characters.append({"char": char, "num": num})
    characters.sort(reverse=True, key=sort_on)
    return characters

def sort_on(item):
    return item["num"]