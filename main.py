# Project: Text to Morse Code
# Author: Brody Moore

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', ' ': ' ',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-',
}


def translate_to_morse(english):
    letters = list(english)
    result = [MORSE_CODE_DICT[letter.upper()] for letter in letters]
    print(*result)


def translate_to_english(morse):
    inv_dict = {val: key for key, val in MORSE_CODE_DICT.items()}
    letters = []
    i = 0
    for letter in morse:
        if letter != ' ':
            i = 0
            letters.append(inv_dict[letter])
        else:
            i += 1
            if i == 3:
                letters.append(' ')
    print(*letters)


print('Welcome to Morse-ify')
while True:
    direction = input('English -> Morse or Morse -> English: ')
    if direction == 'English -> Morse':
        text = input('Enter your english text: ')
        translate_to_morse(text)
        break
    elif direction == 'Morse -> English':
        code = input('Enter your morse code: ')
        translate_to_english(code)
        break
    else:
        print('Please enter a valid response(English -> Morse or Morse -> English): ')

