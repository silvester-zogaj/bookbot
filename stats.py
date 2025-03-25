def get_words(text):
    splitText = text.split()
    num_words = 0
    for i in splitText:
        num_words += 1
    return num_words

def get_characters(text):
    character_count = {}
    lowerText = text.lower()
    for letter in lowerText:
        if letter in character_count:
            character_count[letter] += 1
        else:
             character_count[letter] = 1
        
    return character_count
        

def sort_on(item):
    return item["count"]

def sort_characters (char_dict):
    character_list = []
    
    for char in char_dict:
        if char.isalpha():
            character_list.append({"letter": char, "count": char_dict[char]})

    character_list.sort(reverse=True, key=sort_on)
    return character_list 
    
        

