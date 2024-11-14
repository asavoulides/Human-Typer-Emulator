import pyautogui
import time
import random

# Define a dictionary to map each key to its nearby keys on a QWERTY keyboard
NEARBY_KEYS = {
    'a': 'qwsz',
    'b': 'vghn',
    'c': 'xdfv',
    'd': 'erfcxs',
    'e': 'wsdr',
    'f': 'rtgvcd',
    'g': 'tyhbvf',
    'h': 'ujygnb',
    'i': 'uojk',
    'j': 'uikmnh',
    'k': 'iolmj',
    'l': 'opk',
    'm': 'njk',
    'n': 'bhjm',
    'o': 'ipkl',
    'p': 'ol',
    'q': 'wa',
    'r': 'tedf',
    's': 'awedxz',
    't': 'ryfg',
    'u': 'yihj',
    'v': 'cfgb',
    'w': 'qase',
    'x': 'zsdc',
    'y': 'tuhg',
    'z': 'asx',
    ' ': ' '
}


def type_essay(essay, wpm, error_rate):
    lines = essay.split('\n')
    delay = 60 / wpm
    start_time = time.time()

    for line in lines:
        words = line.split()
        for word in words:
            typo_made = False
            for char in word:
                if random.random() < error_rate / 100:
                    typo = random.choice(NEARBY_KEYS.get(char, char))
                    pyautogui.typewrite(typo)
                    typo_made = True
                else:
                    pyautogui.typewrite(char)

            pyautogui.press('space')

            if typo_made:
                time.sleep(0.2)
                pyautogui.press('backspace', presses=len(word) + 1)
                time.sleep(0.2)
                pyautogui.typewrite(word)
                pyautogui.press('space')

            time.sleep(delay)

            elapsed_time = time.time() - start_time
            remaining_time = (len(essay.split()) * 60 / wpm) - elapsed_time
            print(f"ETA: {remaining_time:.2f} seconds")
            time.sleep(0.1)

        pyautogui.press('enter')

    print("Done!")


def run_typing_emulator(essay, wpm, error_rate):
    if not essay:
        print("Essay is empty. Exiting.")
        return

    print("Starting in 5 seconds...")
    time.sleep(1)

    for i in range(4, 0, -1):
        print(f"Starting in {i} seconds...")
        time.sleep(1)

    print("Typing...")
    type_essay(essay, wpm, error_rate)


# Example usage - (params = essay, wpm, error_rate)
run_typing_emulator("This is a test essay.\nIt has multiple lines.", 80, 10)
