# -*- coding: utf-8 -*-
import random

if __name__ == '__main__':
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
========
    ''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========
    ''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========
    ''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========
    ''',
    
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========
    ''',
    
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========
    ''']
    
    words = 'red orange yellow black'.split()
    
    def getRandomWord(wordList):
        # 이 함수는 문자열 리스트에서 임의의 문자열을 선택해서 반환한다.
        wordIndex = random.randint(0,len(wordList)-1)
        return wordList[wordIndex]
    
    def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
        print(HANGMANPICS[len(missedLetters)])
        print()
        
        print('Missed letters:', end=' ')
        for letter in missedLetters:
            print(letter,end=' ')
        print()
        
        blanks = '_'*len(secretWord)
        
        for i in range(len(secretWord)):
            # 맞게 추측한 단어로 빈칸을 채우기
            if secretWord[i] in correctLetters:
                blanks = blanks[:i] + secretWord[i]+blanks[i+1:]
        
        for letter in blanks:
            # 문자와 빈칸으로 비밀 단어 보여주기
            print(letter, end=' ')
        print()
    
    def getGuess(alreadyGuessed):
        # 플레이어가 입력한 글자를 입력한다.
        # 여기에서는 플레이어가 글자를 하나만 입력했는지 확인한다.         
        while True:
            print('Guess a letter.')
            guess = input("> ")
            guess = guess.lower()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in alreadyGuessed:
                print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
            else:
                return guess
    
    def playAgain():
        # 플레이어가 또 게임을 한다고 하면 True를 아니면 False를 반환한다.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')
    
    print("H A N G M A N")
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameIsDone = False
    
    while True:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
        
        #플레이어가 문자를 입력하도록 한다.
        guess = getGuess(missedLetters + correctLetters)
        
        if guess in secretWord:
            correctLetters = correctLetters + guess
            
            # 플레이어가 이겼는지 검사한다.
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! the Secret word is "' + secretWord+'"! You have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess
            
            if len(missedLetters) == len(HANGMANPICS)-1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter '+
                      str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters))+
                      ' correct guess, the word was "' + secretWord +'"')
                gameIsDone = True
        
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break