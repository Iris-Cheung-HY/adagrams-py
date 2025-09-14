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

SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 4, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 1, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 4, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10

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
    letter_bank_copy = letter_bank.copy()
    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    total_score = 0
    for letter in word.upper():
        total_score += SCORE_CHART[letter]
    if len(word) >= 7 and len(word) <= 10:
        total_score += 8
    return total_score


def get_highest_word_score(word_list):
    highest_word_score = tuple([])
    loop_score = 0
    highest_score = 0

    for word in word_list:
        for letter in word.upper():
            loop_score += SCORE_CHART[letter]
            if loop_score > highest_score:
                highest_score = loop_score
                highest_word_score([0]) = word
                highest_word_score([1]) = highest_score
    return highest_word_score
            





