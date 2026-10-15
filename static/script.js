
const chat = document.getElementById("chat");
const form = document.getElementById("composer");
const input = document.getElementById("message");
const sendBtn = document.getElementById("send");

function scrollToBottom() {
  chat.scrollTop = chat.scrollHeight;
}

// Turns plain text into DOM nodes, making http(s) links clickable.
function fillBubble(el, text) {
  const urlPattern = /(https?:\/\/[^\s]+)/g;

  text.split(urlPattern).forEach((part) => {
    if (/^https?:\/\//.test(part)) {
      const a = document.createElement("a");
      a.href = part;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.textContent = part;
      el.appendChild(a);
    } else if (part) {
      el.appendChild(document.createTextNode(part));
    }
  });
}

// Creates a message bubble.
function addMessage(role, text, intent) {
  const wrap = document.createElement("div");
  wrap.className = `msg ${role}`;

  const who = document.createElement("span");
  who.className = "who";
  who.textContent = role === "user" ? "You" : "Q-TIP";

  const bubble = document.createElement("p");
  bubble.className = "bubble";
  fillBubble(bubble, text);

  wrap.append(who, bubble);

  if (intent) {
    const small = document.createElement("small");
    small.className = "intent";
    small.textContent = `Detected intent: ${intent}`;
    wrap.appendChild(small);
  }

  chat.appendChild(wrap);
  scrollToBottom();

  return { wrap, bubble };
}

// Displays the bot's response one word at a time.
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function typeMessage(bubble, text, delay = 65) {
  const words = text.match(/\S+\s*/g) || [];

  for (const word of words) {
    fillBubble(bubble, word);
    scrollToBottom();
    await sleep(delay);
  }
}

function addTyping() {
  const wrap = document.createElement("div");
  wrap.className = "msg bot";

  const who = document.createElement("span");
  who.className = "who";
  who.textContent = "Q-TIP";

  const bubble = document.createElement("div");
  bubble.className = "bubble typing";
  bubble.setAttribute("aria-label", "Q-TIP is typing");

  for (let i = 0; i < 3; i++) {
    bubble.appendChild(document.createElement("span"));
  }

  wrap.append(who, bubble);
  chat.appendChild(wrap);
  scrollToBottom();

  return wrap;
}

function setBusy(busy) {
  sendBtn.disabled = busy;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const text = input.value.trim();
  if (!text || sendBtn.disabled) return;

  addMessage("user", text);
  input.value = "";

  // Exit command.
  if (text.toLowerCase() === "exit") {
    const { wrap, bubble } = addMessage(
      "bot",
      "",
      null
    );

    await typeMessage(
      bubble,
      "Goodbye! Good luck with your studies!",
      65
    );

    input.disabled = true;
    sendBtn.disabled = true;
    return;
  }

  setBusy(true);
  input.disabled = true;

  const typing = addTyping();

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });

    if (!res.ok) {
      throw new Error(`Server returned ${res.status}`);
    }

    const data = await res.json();

    // Replace the animated typing indicator with an empty response bubble.
    typing.remove();

    const { bubble } = addMessage(
      "bot",
      "",
      data.intent
    );

    // Reveal the reply one word at a time.
    await typeMessage(bubble, data.reply, 40);

  } catch (err) {
    typing.remove();

    const { wrap } = addMessage(
      "bot",
      "I couldn't reach the server. Check that it's running, then try again."
    );

    wrap.classList.add("error");

  } finally {
    setBusy(false);
    input.disabled = false;
    input.focus();
  }
});
