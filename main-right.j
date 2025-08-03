const input = document.getElementById('terminal-input-right');
const terminal = document.getElementById('output-right');

function appendOutput(text) {
  terminal.innerHTML += `<div>> ${text}</div>`;
  terminal.scrollTop = terminal.scrollHeight;
}

input.addEventListener('keydown', async (e) => {
  if (e.key === 'Enter') {
    const command = input.value.trim();
    input.value = '';
    appendOutput(command);

    try {
      const response = await fetch('/run-right', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command })
      });
      const result = await response.json();
      appendOutput(result.output);
    } catch (err) {
      appendOutput('[Error] Could not reach OSINT tools backend.');
    }
  }
});