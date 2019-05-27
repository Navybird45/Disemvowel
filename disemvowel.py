def disemvowel(word):
    result = ""
    for letter in word:
        if letter.lower() not in 'aeiou':
            result += letter
    print(result)

disemvowel(input("Type a word\n> "))
