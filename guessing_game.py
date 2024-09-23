import random
state_bank = ['ohio', 'haiti', 'michigan', 'texas', 'florida', 'virginia']
state = random.choice(state_bank)
guessedState= ['_'] *len(state)
attempts=10

while attempts>0:
    print('\nCurrent word: '+' '.join(guessedState))

guess= input('Guess a letter: ')

if guess in state:
    for i in range(len(state)):
        if  state[i] == guess
        guessedState[i] = guess
        print('Great guess!')
    else:
        attempts -=1
        print('Wrong guess! Attempts left: ' +str(attempts))
    if '_' not in guessedState:
        print('\nCongratulations! You guessed the word '+ state)
        break
    else:
        print('\n You\'ve run out of attempts! The word was: '+ word )




