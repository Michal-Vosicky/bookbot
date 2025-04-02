def count_words(text):
    words = text.split()
    return len(words)


def count_characters(book_text):

    char_counts = {}
    for character in book_text:
        character = character.lower() #convert to lowercase
        if character in char_counts:
            char_counts[character] += 1
        else:
            char_counts[character] = 1
    return char_counts

#test_result = count_characters("banana")
#print (test_result)

def sorted(char_counts):
   
    result = []

    for key, value in char_counts.items():
        char_dict = {"character": key, "count": value}
        result.append(char_dict)
 

    result.sort(reverse=True, key=lambda x: x["count"])

    return result

#test_char_counts = {
#    "e": 5,
#   "a": 3,
#  "b": 7,
# "c": 2
#}

#sorted_result = sorted(test_char_counts)

#print (sorted_result)



    


