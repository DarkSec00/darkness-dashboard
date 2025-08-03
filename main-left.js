document.addEventListener("DOMContentLoaded", () => {
  const output = document.getElementById("output-left");
  const input = document.getElementById("terminal-input-left");

  const write = (text) => {
    const line = document.createElement("div");
    line.textContent = text;
    output.appendChild(line);
    output.scrollTop = output.scrollHeight;
  };

  write("WiFi Tools Terminal Ready.");

  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      const cmd = input.value.trim();
      write("> " + cmd);
      input.value = "";
      // You can connect to server or just mock for now
      write(`[mock] Command '${cmd}' executed`);
    }
  });
});