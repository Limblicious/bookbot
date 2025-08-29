def count_words(text):
    words = text.split()
    return len(words)

def dictionary(text):
    char_dict = {}
    for ch in text:            # iterate raw characters
        let = ch.lower()
        if let not in char_dict:
            char_dict[let] = 1
        else:
            char_dict[let] += 1
    return char_dict

def sorted(char_dict):
    char_sort = []
    for i in char_dict:
        char_sort.append({"char":i, "num":char_dict[i]})
        
    def sort_on(item):
        return item["num"]
    
    char_sort.sort(reverse=True, key=sort_on)
    return char_sort

    
    