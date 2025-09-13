from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}



def draw_letters():
    #empty list to store all the letter
    all_letter_strings = []
    #empty list to store ten strings
    letter_strings_ten = []

    # loop over the dictionary LETTER_POOL
    for letter, qty in LETTER_POOL.items():
        while qty > 0:
            all_letter_strings.append(letter)
            qty -= 1

    while len(letter_strings_ten) < 10:
        random_num = randint(0, len(all_letter_strings) - 1)
        new_letter = all_letter_strings[random_num]
        letter_strings_ten.append(new_letter)
        all_letter_strings.remove(new_letter)
        
    return letter_strings_ten





def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass