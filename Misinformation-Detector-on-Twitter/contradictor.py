from utils import compareList, similar
from pattern.text.en import singularize

#====== Constants
similarityDegreeValue = 2
negations = ["not", "no", "never", "lie", "lying", "not true", "false", "hardly", "rarely", "scarcely", "none", "fake" ]

parent = "Petrol prices reaches 80 in delhi"

tweets = [
    "Petrol prices hiked in delhi",
    "petrol prices in delhi increased",
    "Delhi suffering from highly increased petrol prices",
    "Fake news spread about hike in petrol prices",
    "Petrol prices are not hiked in delhi",
    "India got its first gold medal",
    "Delhi suffered from pollution"
]

def checkNegative(text):
    text = text.split(' ')
    negCount = compareList(text, negations)
    if(negCount % 2):
        return 0
    else:
        return 1


def fakeNewsDetector(parent, tweets):
    for tweet in tweets:
        similarityValue = similar(tweet, parent)
        if similarityValue >= similarityDegreeValue:
            if(checkNegative(tweet) ^ checkNegative(parent)):
                print(" ===> " + tweet)


fakeNewsDetector(parent, tweets)

