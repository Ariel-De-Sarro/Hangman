import os
import random
import time

print('Let`s play The Hangman...\n\n')

while True:
    option = input('Select: 1. Player 1 vs CPU\n2. Player 1 vs Player 2\n')
    if option == '1':
        file = open('words.txt', 'r')
        list_words = file.readlines()
        global Player_1
        Player_1 = random.choice(list(list_words))
        Player_1 = Player_1.replace('\n', '')
        break
    elif option == '2':
        Player_1 = input('Write a word to be guessed: ')
        os.system('cls')
        break
    else:
        print('Your option is invalid')

Player_1_list = [letter for letter in Player_1]

gallows = ['    _____', '    |   |', '    |', '    |', '    |', '____|____']

secret_word = ['_' for letter in Player_1]
print(secret_word)

turns_remaining = 6

while True:
    os.system('cls')
    for line in gallows:
        if line != gallows[-1]:
            print(line)
        else:
            print(line, end='')
    print('  ', secret_word, '\n')
    Player_2 = input('Guess a letter: ')
    if Player_2 in Player_1_list:
        idxs = [idx for idx, x in enumerate(Player_1_list) if x == Player_2]
        for inx in idxs:
            secret_word[inx] = Player_2
        if secret_word == Player_1_list:
            time.sleep(1)
            os.system('cls')
            print('----YOU WIN !!!' * 50)
            break
    else:
        if turns_remaining == 6:
            turns_remaining -= 1
            gallows[2] = '    |   0'
        elif turns_remaining == 5:
            turns_remaining -= 1
            gallows[2] = '    |   0'
            gallows[3] = '    |   |'
        elif turns_remaining == 4:
            turns_remaining -= 1
            gallows[2] = '    |   0'
            gallows[3] = '    |  /|'
        elif turns_remaining == 3:
            turns_remaining -= 1
            gallows[2] = '    |   0'
            gallows[3] = '    |  /|\\'
        elif turns_remaining == 2:
            turns_remaining -= 1
            gallows[2] = '    |   0'
            gallows[3] = '    |  /|\\'
            gallows[4] = '    |  /'
        elif turns_remaining == 1:
            turns_remaining -= 1
            gallows[2] = '    |   0'
            gallows[3] = '    |  /|\\'
            gallows[4] = '    |  / \\'
            os.system('cls')
            for i in gallows:
                print(i)
            print('GAME OVER')
            break





