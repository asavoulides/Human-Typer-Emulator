let index = 0;
let mistakes = 0;
let textarea = document.querySelector("textarea"); // Target the textarea

function typeCharacter() {
  if (index < essayText.length) {
    // Simulate a mistake with a 5% chance
    if (Math.random() < 0.05) {
      textarea.value += "x";
      mistakes++;
    } else {
      textarea.value += essayText[index];
    }
    index++;
  }

  // Simulate backspace to correct a mistake
  if (mistakes > 0 && Math.random() < 0.1) {
    textarea.value = textarea.value.slice(0, -1);
    mistakes--;
  }

  if (index < essayText.length) {
    setTimeout(typeCharacter, 750); // 80 words per minute
  }
}

typeCharacter();
