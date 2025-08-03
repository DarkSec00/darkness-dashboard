document.addEventListener("DOMContentLoaded", () => {
  const terminal = document.getElementById("terminal");

  const writeLine = (text, delay = 0) => {
    setTimeout(() => {
      const line = document.createElement("div");
      line.textContent = text;
      terminal.appendChild(line);
      terminal.scrollTop = terminal.scrollHeight;
    }, delay);
  };

  writeLine("Initializing Darkness Security Terminal...", 500);
  writeLine("Loading container engine: kali-suite-darksec", 1200);
  writeLine("Container ready. Type 'help' for commands.", 2000);

  const handleCommand = (command) => {
    const output = document.createElement("div");
    output.textContent = `You entered: ${command}`;
    terminal.appendChild(output);
    terminal.scrollTop = terminal.scrollHeight;
  };

  const input = document.getElementById("terminal-input");
  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      const command = input.value.trim();
      if (command) handleCommand(command);
      input.value = "";
    }
  });
});