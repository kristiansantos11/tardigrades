# Hands on 10

vowels = 'aeiou'


def translate(word):
    word = word.lower()
    # Case: Word starts with vowel
    if word[0] in vowels:
        return word + "ay"
    else:
        # Iterate from the first character in
        # word, up to the first occurance of vowel
        for i in range(len(word)):
            # Case when there is a vowel
            if word[i] in vowels:
                return word[i:] + word[:i] + 'ay'
        # Case when there is no vowel in the word
        return word + "ay"


s = input("Enter a sentence: ")
print(' '.join(translate(word) for word in s.split()))
