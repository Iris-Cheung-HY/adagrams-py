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
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
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
        while qty > 0: #when qty left > 0
            all_letter_strings.append(letter) # then append the letter to all_letter_strings, until qty left == 0
            qty -= 1 #qty left - 1

    while len(letter_strings_ten) < 10: #when letter_strings_ten < 10:
        random_num = randint(0, len(all_letter_strings) - 1) #get a random number in all_letter_strings as index
        new_letter = all_letter_strings[random_num] #assisgn the letter related to the index to a new variable
        letter_strings_ten.append(new_letter) #append the letter to the letter_strings_ten
        all_letter_strings.remove(new_letter) #remove the letter from all_letter_strings
        
    return letter_strings_ten

def uses_available_letters(word, letter_bank):
    #make a copy of the letter_bank
    letter_bank_copy = letter_bank.copy()
    # loop over the letter in word and changed all word to upper case
    for letter in word.upper():
        if letter in letter_bank_copy: #if letter is in letter_bank_copy
            letter_bank_copy.remove(letter) #the remove the letter in letter_bank_copy
        else:
            return False
    return True

def score_word(word):
    # set a total score to 0
    total_score = 0
    # loop over the letter in word and changed all word to upper case
    for letter in word.upper():
        total_score += SCORE_CHART[letter] #sum up the score for word
    if len(word) >= 7 and len(word) <= 10: #if the length of the word is >= 7 and <= 10
        total_score += 8 #then add 8 points more to the total score
    return total_score


def get_highest_word_score(word_list):
    #set a highest score = 0
    highest_score = 0
    #set an empty string to store the highest score word
    highest_score_word = ""

    #loop over the word in the word list
    for word in word_list:
        #set a total_score = 0 for each word
        total_score = 0
        #loop over the letter in word and set them upper case
        for letter in word.upper():
            #sum up the score for word
            total_score += SCORE_CHART[letter]
        #if the length of the word is >= 7 and <= 10
        if len(word) >= 7 and len(word) <= 10:
            #then add 8 points more to the total score
            total_score += 8
        #if total_score more than highest_score
        if total_score > highest_score:
            #replacing the highest_score and highest_score_word with the current word and score
            highest_score = total_score
            highest_score_word = word
        #if they are tie
        if total_score == highest_score:
            #check if either word or highest_score_word has length over 10, if so the one with length > 10 will be the highest_score_word
            if len(word) == 10 and len(highest_score_word) < 10:
                highest_score_word = word
            #check when both length < 10, will assign the one with less length to the highest_score_word
            elif len(word) < 10 and len(highest_score_word) < 10 \
                and len(word) < len(highest_score_word) : 
                highest_score_word = word
            #if they both have the same length, keep the one in highest_score_word since it is the first order in the list
            elif len(word) == len(highest_score_word):
                continue


    return tuple([highest_score_word, highest_score])





            





