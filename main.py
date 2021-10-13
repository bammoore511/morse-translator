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
    result = ''
    inv_dict = {val: key for key, val in MORSE_CODE_DICT.items()}
    words = morse.split('   ')
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            result += inv_dict[letter]
        result += ' '

    print(result)


print('Welcome to Morse-ify')
while True:
    direction = input('English -> Morse or Morse -> English: ')
    if direction == 'English -> Morse':
        text = input('Enter your english text: ')
        translate_to_morse(text)
        break
    elif direction == 'Morse -> English':  # TODO change back
        code = input('Enter your morse code: ')
        translate_to_english(code)
        break
    else:
        print('Please enter a valid response(English -> Morse or Morse -> English): ')

