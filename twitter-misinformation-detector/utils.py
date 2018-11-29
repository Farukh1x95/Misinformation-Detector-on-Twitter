from nltk.corpus import wordnet
from pattern.text.en import singularize
from nltk.stem.wordnet import WordNetLemmatizer

def compareList(list1, list2):
    count = 0
    for item in list1:
        if item.lower() in list2:
            count += 1 
    return count

def similar(text1, text2):
    found = False
    count = 0

    text1 = text1.split(' ')
    text2 = text2.split(' ')

    # ----------------------------------------------
    # Singularizing the words
    text1 = [singularize(word) for word in text1]

    # Singularizing the words
    text2 = [singularize(word) for word in text2]

    # ----------------------------------------------
    #Conerting in lower case
    text1 = [word.lower() for word in text1]

    #Conerting in lower case
    text2 = [word.lower() for word in text2]

    # ----------------------------------------------
    # Converting into present form
    text1 = [WordNetLemmatizer().lemmatize(word, 'v') for word in text1]

    # Converting into present form
    text2 = [WordNetLemmatizer().lemmatize(word, 'v') for word in text2]


    for word in text1:
        if len(word) > 3:
            if singularize(word) in text2:
                count += 1
            else:
                for syn in wordnet.synsets(word):
                    for name in set(syn.lemma_names()):
                        if name in text2:
                            count += 1
                            found = True
                            break
                    if found:
                        found = False
                        break
    return count


