import inflect, json, os, random

plural = inflect.engine()

nouns = json.load(open("nouns.json"))
adjectives = json.load(open("adjectives.json"))
verbs = json.load(open("verbs.json"))

leetDefinitions = {'a':'4','A':'4','e':'3','E':'3','g':'6','G':'6','l':'1','L':'1','o':'0','O':'0','s':'5','S':'5','t':'7','T':'7'}
specialCharacters = {'separators': [',', '.','-','-'], 'appender':['@','$','?','!']}

def getNoun(isPlural = False, alliterateChar = ''):
    """Get a random noun, can either specify what the noun should begin with or if it is plural
    isPlural - boolean specifying if the noun returned should be in plural form
    alliterateChar - the letter the noun should begin with
    """
    randomNoun = getRandomWord(nouns, alliterateChar)
    if(isPlural):
        return plural.plural_noun(randomNoun)
    else:
        return randomNoun

def getAdjective(alliterateChar = ''):
    """Get a random adjective, can specify what letter the adjective should begin with
    alliterateChar - the letter the adjective should begin with
    """
    return getRandomWord(adjectives, alliterateChar)

def getVerb(isPlural= False, alliterateChar = ''):
    """Get a random verb, can either specify what the verb should begin with or if it is plural
    isPlural - boolean specifying if the verb returned should be in plural form
    alliterateChar - the letter the verb should begin with
    """
    randomVerb = getRandomWord(verbs, alliterateChar)
    if(isPlural):
        return plural.plural_verb(randomVerb)
    else:
        return randomVerb


def getRandomWord(wordList, alliterateChar = ''):
    """Pull a random work from a wordList object, can supply a char that the word should begin with
    wordList - Dictionary of words to pull a random word from
    alliterateChar - defaults to an empty char, if one is provided function will find a random word beginning with that char
    """
    
    if(alliterateChar == ''):
        randomKey = random.choice(list(wordList.keys()))
        currentWords = wordList[randomKey]
        randomWord = random.choice(currentWords)
    else:
        currentWords = wordList[alliterateChar]
        randomWord = random.choice(currentWords)
    return randomWord

def replaceLetterWithNum(word):
    """Replace a random letter within a word with its 1337 equivalent.
    word - word to replace one letter with 
    """
    wordAsList = list(word)
    replacedLetter = False
    attemptsToReplace = 0
    while(not replacedLetter and attemptsToReplace < 30):
        letter = random.choice(wordAsList)
        if(letter in leetDefinitions):
            word = word.replace(letter,leetDefinitions[letter],1)
        replacedLetter = True
    attemptsToReplace+=1
    return word
    
def getRandomNumber(length):
    """Get a string of numbers of a specified length
    length - length of returned string
    """
    numberString = ''
    for i in range(length):
        randNumber = random.randint(0,9)
        numberString+=str(randNumber)
    return numberString

def processSpecialCharacters(password,specialCharactersToAdd,numbersAppendedToEnd = False):
    """Add a specified number of special characters to the current password
    password - list containing the current password
    specialCharactersToAdd - number of special characters to insert into the password
    numbersAppendedToEnd - boolean stating whether numbers could have been added to the end of the password, 
                           used for creating more natural setences when inserting appenders
    """
    separatorIndex = 1
    if(specialCharactersToAdd == 1):
        randomKey = random.choice(list(specialCharacters.keys()))
        if(randomKey == 'separators'):
            password.insert(separatorIndex, random.choice(specialCharacters[randomKey]))
        elif(numbersAppendedToEnd):
            if(password[-1].isdigit()):
                password.insert(len(password) - 1, random.choice(specialCharacters[randomKey]))
        else:
            password.append(random.choice(specialCharacters[randomKey]))
    else:
        pass
        #TODO: Implement extended special character behavior
    return password