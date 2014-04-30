lexicon_list = [('direction', 'north'),
                ('direction', 'south'),
                ('direction', 'east'),
                ('direction', 'west'),
                ('verb', 'go'),
                ('verb', 'kill'),
                ('verb', 'eat'),
                ('noun', 'bear'),
                ('noun', 'princess'),
                ('stop', 'the'),
                ('error', 'error')]

def scan(sentence):
    words = sentence.split()
    result = []
    for word in words:
        value = convert_number(word)
        if value:
            result.append(('number', value))
        else:
            for lexicon in lexicon_list:
                if word == lexicon[1]:
                    result.append(lexicon)
                    break
                if lexicon[1] == "error":
                    result.append(('error',word))
    return result

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, object):
        # take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

# word_list: [(kind, word), (kind, word)...]
def match(word_list, expecting):
    if word_list:
        #print "before pop:" ,
        #print word_list
        # return the first item from word_list
        word = word_list.pop(0)
        #print "after pop:" ,
        #print word
        if word[0] == expecting:
            # returns just one word with its kind
            return word
        else:
            return None
    else:
        return None

# scan the sentence and remove some kinds of words at the first
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    #print verb
    #print obj

    return Sentence(subj, verb, obj)

# word_list: sentence first be splited and then be scaned
def parse_sentence(word_list):
    # overview stop words
    skip(word_list, 'stop')
    # get the kind of the first word
    start = peek(word_list)
    #print "start is :" + start
    # if first word is a noun
    if start == 'noun':
        # then we pop the first noun from word_list
        # save it to subj
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, or verb not: %s" % start)

#print "b = 'bear go east'"
#b = "bear go east"
#print "split to c"
#c = scan(b)
#print "parse_sentence to a"
#a = parse_sentence(c)
