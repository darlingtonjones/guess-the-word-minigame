import random

lives = 5 #this is a starting live
words = ['antelope', 'planet', 'science', 'measurement',
         'africa', 'space', 'systems', 'continental']
secret_word = random.choice(words)

clue = list('?????')

heart_symbol = u'\u2764'
print(heart_symbol * 5)

guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
    index = 0

    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

    while lives > 0:
        print(clue)
        print('Lives left: ' + heart_symbol * lives)
        guess = input('Guess a letter or the whole word: ')

        if guess == secret_word:
            guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1

    if guessed_word_correctly:
        print('You won! The secret word was ' + secret_word)
    else:
        print('You lost! The secret word was ' + secret_word)


