

# def fib_gen():
#     a, b = 0, 1
#     for i in xrange(0, 10):
#         yield a
#         (a, b) = (b, a + b)
#
# ry = fib_gen()
# print ry.next()
# print ry.next()
# print ry.next()
# print ry.next()
# print ry.next()
# print ry.next()

sentence = "The words of a sentence!"
def words_of_sentence(sentence):
    punc = sentence[-1]
    sentence = sentence.rstrip(punc)
    words = sentence.split(' ')
    return words, punc

def put_back_together(words):
    sentence = [' '.join(word) for word in words]
    return sentence

def attempt2(words, punctuation):
    sent = ' '.join(words)
    sentence = sent + punctuation
    return sentence

print words_of_sentence(sentence)
print put_back_together(words_of_sentence(sentence))
print "Attempt2"
values = words_of_sentence(sentence)
print attempt2(*values)
print values



rally_tasks
LICENSE
README.rst
disruptor.py
requirements.txt	
test_disruptor.py