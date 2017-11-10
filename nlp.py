import nltk
#nltk.download()
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

nltk.data.path.append("/build/nlp/nltk_data/")

sentence = "The Quick brown fox, Jumps over the lazy little dog. Hello World."
sentence.split(" ")
word_tokenize(sentence)
w = word_tokenize(sentence)
nltk.pos_tag(w)
nltk.help.upenn_tagset()
syn = wordnet.synsets("computer")
print(syn)
print(syn[0].name())
print(syn[0].definition())
print(syn[1].name())
print(syn[1].definition())
yn = wordnet.synsets("talk")
syn[0].examples()
syn = wordnet.synsets("speak")[0]
print(syn.hypernyms())
print(syn.hyponyms())
syn = wordnet.synsets("good")
for s in syn:
    for l in s.lemmas():
        if (l.antonyms()):
            print(l.antonyms())
syn = wordnet.synsets("book")
for s in syn:
    print(s.lemmas())
stopwords.words('english')[:16]
para = "The program was open to all women between the ages of 17 and 35, in good health, who had graduated from an accredited high school. "
words = word_tokenize(para)
print(words)
useful_words = [word for word in words if word not in stopwords.words('english')]
print(useful_words)
from nltk.corpus import movie_reviews
movie_reviews.words()
movie_reviews.categories()
movie_reviews.fileids()[:4]
all_words = movie_reviews.words()
freq_dist = nltk.FreqDist(all_words)
freq_dist.most_common(20)


