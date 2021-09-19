def generate_hashtag(s):
    if s == '': return False

    line = [n.lower().capitalize() for n in s.split()]

    hashtag = '#'
    hashtag += ''.join(line)
    
    return hashtag if len(hashtag) <= 140 else False


# print(generate_hashtag(" Hello there thanks for trying my Kata"))
#   =>  "#HelloThereThanksForTryingMyKata"
# print(generate_hashtag("    Hello     World   ")) #                  =>  "#HelloWorld"
print(generate_hashtag("")) #                        =>  false