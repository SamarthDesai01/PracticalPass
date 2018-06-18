import json, os, random
import words
from sentence import sentence

os.chdir(os.getcwd())

def getRandomPass():
    return generatePass(sentence.getSentence(), numsToInclude = 2, appendAllNumbersToEnd = True, specialCharactersToAdd=6)

def generatePass(passwordPattern, numsToInclude = 0, appendAllNumbersToEnd = False, specialCharactersToAdd = 0):
    """Method to generate password string based on a password pattern 
    
    passwordPattern - array describing the sequence of words to be included in the password
    numsToInclude - integer number of times to replace a letter with a number 
    appendNumbersToEnd - add the required numbers to the end of the password rather than through replacement
    """
    attempts = 0
    replacements = 0
    appendedNumbersToEnd = False

    password = []
    previousFirstLetter = ""
    for i in range(len(passwordPattern)):
        currentWordType = passwordPattern[i]
        if(currentWordType == 'adj'):
            appendToPass = words.getAdjective().capitalize()
        elif(currentWordType == 'noun'):
            appendToPass = words.getNoun(isPlural = False).capitalize()
        elif(currentWordType == 'pluralnoun'):
            appendToPass = words.getNoun(isPlural = True).capitalize()
        elif(currentWordType == 'alliterate-noun'):
            appendToPass = words.getNoun(False, previousFirstLetter).capitalize()
        elif(currentWordType == 'alliterate-pluralnoun'):
            appendToPass = words.getNoun(True, previousFirstLetter).capitalize()
        elif(currentWordType == 'verb'):
            appendToPass = words.getVerb().capitalize()
        elif(currentWordType == 'pluralverb'):
            appendToPass = words.getVerb(True).capitalize()
        elif(currentWordType == 'alliterate-verb'):
            appendToPass = words.getVerb(False, previousFirstLetter).capitalize()
        elif(currentWordType == 'alliterate-pluralverb'):
            appendToPass = words.getVerb(True, previousFirstLetter)
        
        previousFirstLetter = appendToPass[0].lower()
        password.append(appendToPass)
    
    if(not appendAllNumbersToEnd):
        while(replacements < numsToInclude and attempts < len(password)*3):
            randIndex = random.randrange(len(password))
            wordBeforeReplacement = password[randIndex]
            newWord = words.replaceLetterWithNum(password[randIndex])
            if(wordBeforeReplacement != newWord):
                password[randIndex] = newWord
                replacements+=1
            attempts+=1

    if(replacements!=numsToInclude):
        numsToAdd = numsToInclude - replacements
        numberString = words.getRandomNumber(numsToAdd)
        password.append(numberString)
        appendedNumbersToEnd = True
    
    password = words.processSpecialCharacters(password,specialCharactersToAdd, appendedNumbersToEnd)

    return ''.join(password)

for x in range(10):
    print(getRandomPass())