# Trolls are spamming your social media comments with random words.
# You troll back by spamming them with the same words but with vowels
# replaced by '*'.

def troll(s):
    return s.translate(s.maketrans('aeiouAEIOU', '*'*10))

print(troll('Unuseful function'))