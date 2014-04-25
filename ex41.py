import random
from urllib import urlopen
import sys

#What content words.txt contains?
#There're a bunch of words, to randomly substitude the wildcards
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
#when 'english' is not used
#the keys of PHRASES are the questions
#values are the answers
PHRASES = {
        "Class %%%(%%%):":
          "Make a class named %%% that is-a %%%.",
        "Class %%%(object):\n\tdef __init__(self,***)":
          "class %%% has-a __init__ that takes self and *** parameters.",
        "class %%%(object):\n\tdef ***(self,@@@)":
          "class %%% has-a function named *** that takes self and @@@ parameters.",
        "*** = %%%()":
          "From *** get the *** function, and call it with parameters self, @@@.",
        "***.*** = '***'":
          "From *** get the *** attribute and set it to '***'."
          }

PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

#readlines returns a list
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

#snippet is a piece of question
def convert(snippet, phrase):
    #sample(population, k): Return a k length list of unique elements chosen from the population sequence.
    #count("%%%"): find how many "%%%" in the snippet(question) 
    #find how many "%%%"(class) there are, and then randomly select some words to
    #substitude them, finally capitalize the first character of words
    #this single line contains so much stuff!
    class_names = [w.capitalize() for w in
            random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    #to randomly generate the parameters.
    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    #following line means 1. sentence=snippet, 2.sentence=phrase
    for sentence in snippet, phrase:
        #python way of coping a list
        result = sentence[:]
        #substitude names from result looply, one at a time.
        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results

try:
    while True:
        #keys(): Return a copy of the dictionary's list of keys
        snippets = PHRASES.keys()
        #shuffle(x): Shuffle the sequence x in place.
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            #if we use 'english' option, answer becomes question, vice versa.
            if PHRASE_FIRST:
                question, answer = answer, question

            print question
            #input your answer first
            raw_input(">")
            #then view the answer, comparing to yours
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"
