from collections import Counter
import re


def top_3_words(text):
    text = re.sub("[^a-z' ]+", '', text.lower())
    text = re.sub("[^a-z]+'[^a-z]+", '', text.lower())
    cnt = Counter(text.split())
    return [top[0] for top in cnt.most_common(3)]


print(top_3_words("  '  "))
print(top_3_words("  '''  "))

print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))  # ["e", "ddd", "aa"]
print(top_3_words(" //wont won't won't"))  # ["won't", "wont"]
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))
