# 1

def text_analysis(text):
    en_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    dictionary = {}
    for letter in text:
        letter = letter.lower()
        if letter in en_alphabet:
            if letter not in dictionary:
                dictionary[letter] = 0
            dictionary[letter] += 1
    result1 = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    result1 = dict(result1)
    for k, v in result1.items():
        print(k.upper(), v)

    print()

    dictionary2 = {}
    words = text.lower().split()
    for word in words:
        if word[-1] not in en_alphabet:
            word = word[0:-1]
        if word not in dictionary2:
            dictionary2[word] = 0
        dictionary2[word] += 1

    for k, v in dictionary2.items():
        print(k.lower(), v)


text_analysis('Hello world! hello')


# 2

def cipher(text):
    en_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    dictionary = {}
    for i in range(26):
        a = input().strip().lower().split()
        dictionary[a[0]] = a[1]
        dictionary[a[0].upper()] = a[1].upper()
    print(dictionary)

    result = ''
    for symbols in text:
        if symbols.lower() not in en_alphabet:
            result += symbols
        else:
            result += dictionary[symbols]
    return result


print(cipher('Aba Cz.'))
