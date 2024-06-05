# Define the mapping from English keys to Arabic letters
english_to_arabic = {
    'a': 'ش',
    'b': 'ل',
    'c': 'ا',
    'd': 'ي',
    'e': 'ث',
    'f': 'ب',
    'g': 'ل',
    'h': 'ا',
    'i': 'ه',
    'j': 'ت',
    'k': 'ن',
    'l': 'م',
    'm': 'ة',
    'n': 'ى',
    'o': 'خ',
    'p': 'ح',
    'q': 'ض',
    'r': 'ق',
    's': 'س',
    't': 'ف',
    'u': 'ع',
    'v': 'ر',
    'w': 'ص',
    'x': 'ء',
    'y': 'غ',
    'z': 'ئ',
    ';': 'ك',
    "'": 'ط',
    ',': 'و',
    '.': 'ز',
    '/': 'ظ',
    ']': 'د',
    '[': 'ج',
    '`': 'ذ'  
}

def decode_word(encoded_word):
    """
    This function takes an encoded word (a string of English characters meant to be Arabic letters)
    and decodes it to the correct Arabic word using a predefined mapping.
    
    :param encoded_word: str : the input word encoded using English keyboard mapping for Arabic
    :return: str : the decoded word in Arabic
    """
    decoded_word = ""
    for char in encoded_word:
        if char in english_to_arabic:
            decoded_word += english_to_arabic[char]
        else:
            decoded_word += char  # if the character is not in the mapping, keep it as is (e.g., spaces, punctuation)
    return decoded_word

encoded_input = input("Enter The Encoded String: ")
decoded_output = decode_word(encoded_input)
print("Decoded Output:", decoded_output)
