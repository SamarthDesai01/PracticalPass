import random
class sentence:

    sentenceTypes = [
        ['adj','alliterate-pluralnoun','pluralverb','pluralnoun'],
    ]

    @classmethod
    def getSentence(cls):
        return random.choice(sentence.sentenceTypes)


