from nltk.stem import PorterStemmer, LancasterStemmer
stemmer = PorterStemmer()


def stem(sentence):
    '''
        Given a stemmer and a sentence, stem each word in the sentence and return the sentence.
    '''
    words = sentence.split()
    words = [stemmer.stem(w) for w in words]
    return ' '.join(words)


def clean(text):
    '''
        Remove all special characters from the text. Only keep the characters from a-z and whitespaces.
    '''
    return re.sub(r'[^a-z\s]', '', text)
