document.addEventListener("DOMContentLoaded", () => {
  const output = document.getElementById("output-right");
  const input = document.getElementById("terminal-input-right");

  const write = (text) => {
    const line = document.createElement("div");
    line.textContent = text;
    output.appendChild(line);
    output.scrollTop = output.scrollHeight;
  };

  write("OSINT Tools Terminal Ready.");

  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      const cmd = input.value.trim();
      write("> " + cmd);
      input.value = "";
      write(`[mock] Executing OSINT command: '${cmd}'`);
    }
  });
});