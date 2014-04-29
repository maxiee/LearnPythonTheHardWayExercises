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

