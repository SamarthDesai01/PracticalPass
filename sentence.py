import random
class sentence:

    sentenceTypes = [
        ['adj','alliterate-pluralnoun','pluralverb','pluralnoun'],
        ['adj','alliterate-pluralnoun','pluralverb','adj','pluralnoun'],
        ['adj','alliterate-pluralnoun','alliterate-pluralverb','alliterate-pluralnoun'],
    ]

    @classmethod
    def getSentence(cls):
        return random.choice(sentence.sentenceTypes)


