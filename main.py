from stats import count_words
from stats import dictionary
from stats import sorted
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
    with open(sys.argv[1], encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text()
    word_count = count_words(text)
    char_count = dictionary(text)
    #print(f'{word_count} words found in the document')
    #print(f'Character count: {char_count}')
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    a = sorted(char_count)
    for i in a:
        if i["char"].isalpha() != True:
            pass
        else:
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


main()
