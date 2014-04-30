from nose.tools import *
from ex48 import parser

def test_sentence():
    sentence1 = "bear go east"
    sentence2 = "princess kill bear"
    words1 = parser.scan(sentence1)
    words2 = parser.scan(sentence2)
    s_testing = parser.parse_sentence(words1)
    s = parser.Sentence(('noun','bear'),('verb','go'),('direction','east'))
    assert_equal(s_testing.subject,s.subject)
    assert_equal(s_testing.verb,s.verb)
    assert_equal(s_testing.object,s.object)
