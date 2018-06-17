import random
class sentence:

    sentenceTypes = [
        ['adj','alliterate-noun','verb','pluralnoun'],
    ]

    @classmethod
    def getSentence(cls):
        return random.choice(sentence.sentenceTypes)


