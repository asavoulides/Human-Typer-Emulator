import pyautogui
import time
import random
import tkinter as tk

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
            eta_label.config(text=f"ETA: {remaining_time:.2f} seconds")
            root.update_idletasks()
            time.sleep(0.1)

        pyautogui.press('enter')

    eta_label.config(text="Done!")
    root.update_idletasks()


def start_typing():
    essay = essay_text.get("1.0", tk.END).strip()
    wpm = int(wpm_entry.get())
    error_rate = float(error_rate_entry.get())

    if not essay:
        return

    countdown_label.config(text="Starting in 5 seconds...")
    root.update_idletasks()
    time.sleep(1)

    for i in range(4, 0, -1):
        countdown_label.config(text=f"Starting in {i} seconds...")
        root.update_idletasks()
        time.sleep(1)
    countdown_label.config(text="")
    root.update_idletasks()
    countdown_label.config(text="Typing...")
    root.update_idletasks()
    type_essay(essay, wpm, error_rate)


# Create the Tkinter window
root = tk.Tk()
root.title("Essay Typing Emulator")

# Create a Text widget to input the essay
essay_text = tk.Text(root, wrap=tk.WORD, width=50, height=10)
essay_text.pack()

# Create Entry widgets to configure WPM and error rate
wpm_label = tk.Label(root, text="WPM:")
wpm_label.pack()
wpm_entry = tk.Entry(root)
wpm_entry.insert(0, "80")
wpm_entry.pack()

error_rate_label = tk.Label(root, text="Error Rate (%):")
error_rate_label.pack()
error_rate_entry = tk.Entry(root)
error_rate_entry.insert(0, "10")
error_rate_entry.pack()

# Create a button to start typing
start_button = tk.Button(root, text="Start Typing", command=start_typing)
start_button.pack()

# Create a label to display the countdown timer
countdown_label = tk.Label(root, text="")
countdown_label.pack()

# Create a label to display the ETA
eta_label = tk.Label(root, text="")
eta_label.pack()

# Run the Tkinter event loop
root.mainloop()
