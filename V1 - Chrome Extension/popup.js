document.addEventListener("DOMContentLoaded", function () {
  const startTypingButton = document.getElementById("startTyping");
  const essayInput = document.getElementById("essayInput");

  startTypingButton.addEventListener("click", function () {
    const essayText = essayInput.value;
    if (essayText) {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        chrome.tabs.executeScript(
          tabs[0].id,
          { code: "var essayText = `" + essayText + "`;" },
          function () {
            chrome.tabs.executeScript(tabs[0].id, { file: "content.js" });
          }
        );
      });
    }
  });
});
