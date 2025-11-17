const wordCountMessage = document.getElementById("wordCountMessage");

function limitWords(input, maxWords) {
  const value = input.value.trim();

  if (!value) {
    wordCountMessage.textContent = `0 / ${maxWords} words`;
    return;
  }

  const words = value.split(/\s+/);

  if (words.length > maxWords) {
    input.value = words.slice(0, maxWords).join(" ");
    wordCountMessage.textContent = `Limit reached: ${maxWords} words max.`;
  } else {
    wordCountMessage.textContent = `${words.length} / ${maxWords} words`;
  }
}
