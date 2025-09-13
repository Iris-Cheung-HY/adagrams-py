
while len(letter_strings) != 10:
    random_num = randint(0, 25)
    change_letter = chr(65 + random_num)  
    letter_left = LETTER_POOL[change_letter]
    if letter_left > 0 and change_letter not in letter_strings:
        letter_strings.append(change_letter)
return letter_strings