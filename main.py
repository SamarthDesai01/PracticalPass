import json, os, random
import words

os.chdir(os.getcwd())

nouns = json.load(open("nouns.json"))
adjectives = json.load(open("adjectives.json"))
verbs = json.load(open("verbs.json"))

passwordPatterns = [['adj','alliterate-noun','verb','pluralnoun']]

def getRandomPass():
    return generatePass(random.choice(passwordPatterns), 1, True)

def generatePass(passwordPattern, replaceWithNums = 0, appendNumbersToEnd = False):
    """Method to generate password string based on a password pattern 
    
    passwordPattern - array describing the sequence of words to be included in the password
    replaceWithNums - integer number of times to replace a letter with a number 
    appendNumbersToEnd - add the required numbers to the end of the password rather than through replacement
    """
    attempts = 0
    replacements = 0

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
            appendToPass = words.getNoun(True, previousFirstLetter).capitalize()
        elif(currentWordType == 'verb'):
            appendToPass = words.getVerb().capitalize()
        
        previousFirstLetter = appendToPass[0].lower()
        password.append(appendToPass)
    
    if(not appendNumbersToEnd):
        while(replacements < replaceWithNums and attempts < len(password)*3):
            randIndex = random.randrange(len(password))
            wordBeforeReplacement = password[randIndex]
            newWord = words.replaceLetterWithNum(password[randIndex])
            if(wordBeforeReplacement != newWord):
                password[randIndex] = newWord
                replacements+=1
            attempts+=1

    if(replacements!=replaceWithNums):
        numsToAdd = replaceWithNums - replacements
        numberString = words.getRandomNumber(numsToAdd)
        password.append(numberString)

    return ''.join(password)

for x in range(10):
    print(getRandomPass())