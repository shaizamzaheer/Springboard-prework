def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = list('aeiouAEIOU')
    out = ''
    vowels_found = {}
    for idx,ltr in enumerate(s):
        if ltr in vowels:
            vowels_found[idx]=ltr
    keys, values = vowels_found.keys(), vowels_found.values()
    keys = reversed(keys)
    new_vowels = dict(zip(keys,values))
    for idx,ltr in enumerate(s):
        if new_vowels.get(idx):
            out+=new_vowels.get(idx)
        else:
            out += ltr
    return out