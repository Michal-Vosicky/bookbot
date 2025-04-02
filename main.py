from stats import count_words 
from stats import count_characters
from stats import sorted
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text
    

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    words = count_words(book_text)
    char_counts = count_characters(book_text)

    sorted_counts = sorted(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in sorted_counts:
        if char["character"].isalpha():
            print(f"{char["character"]}: {char["count"]}")
    
    print("============= END ===============")

   

   

main()





