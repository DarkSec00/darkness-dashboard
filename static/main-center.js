const host = window.location.hostname;
setupTerm('term-center', `wss://${host}:7681`);
function setupTerm(containerId, socketUrl) {
  const term = new Terminal({cols:80, rows:24, cursorBlink:true});
  term.open(document.getElementById(containerId));
  term.write('\x1b[32mConnecting...\x1b[0m\r\n');
  const socket = new WebSocket(socketUrl);
  socket.onopen = () => term.write('\x1b[32mConnected!\x1b[0m\r\n');
  socket.onmessage = evt => term.write(evt.data);
  term.onData(data => socket.send(data));
}