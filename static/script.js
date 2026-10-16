const chat = document.getElementById("chat");
const form = document.getElementById("composer");
const input = document.getElementById("message");
const sendBtn = document.getElementById("send");

const launcher = document.getElementById("qtip-launcher");
const qtipWindow = document.getElementById("qtip-window");
const closeBtn = document.getElementById("close-qtip");

function scrollToBottom() {
  chat.scrollTop = chat.scrollHeight;
}

// Open the Q-TIP window.
function openQtip() {
  qtipWindow.hidden = false;
  launcher.setAttribute("aria-expanded", "true");

  input.disabled = false;
  sendBtn.disabled = false;
  input.focus();

  scrollToBottom();
}

// Close the Q-TIP window without clearing the conversation.
function closeQtip() {
  qtipWindow.hidden = true;
  launcher.setAttribute("aria-expanded", "false");
  launcher.focus();
}

launcher.addEventListener("click", () => {
  if (qtipWindow.hidden) {
    openQtip();
  } else {
    closeQtip();
  }
});

closeBtn.addEventListener("click", closeQtip);

// Allow the user to close the window with Escape.
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !qtipWindow.hidden) {
    closeQtip();
  }
});

// Turns plain text into DOM nodes, making URLs clickable.
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

// Create a chat message.
function addMessage(role, text) {
  const wrap = document.createElement("div");
  wrap.className = `msg ${role}`;

  const who = document.createElement("span");
  who.className = "who";
  who.textContent = role === "user" ? "You" : "Q-TIP";

  const bubble = document.createElement("p");
  bubble.className = "bubble";
  fillBubble(bubble, text);

  wrap.append(who, bubble);

  chat.appendChild(wrap);
  scrollToBottom();

  return { wrap, bubble };
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Reveal the response one word at a time.
async function typeMessage(bubble, text, delay = 40) {
  const words = text.match(/\S+\s*/g) || [];

  for (const word of words) {
    fillBubble(bubble, word);
    scrollToBottom();
    await sleep(delay);
  }
}

// Show the animated typing indicator.
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
  input.disabled = busy;
}

// Send the message to the existing Flask backend.
form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const text = input.value.trim();

  if (!text || sendBtn.disabled) return;

  addMessage("user", text);
  input.value = "";

  // Local exit command.
  if (text.toLowerCase() === "exit") {
    const { bubble } = addMessage("bot", "");

    setBusy(true);
    await typeMessage(
      bubble,
      "Goodbye! Good luck with your studies!",
      40
    );

    input.disabled = true;
    sendBtn.disabled = true;
    return;
  }

  setBusy(true);
  const typing = addTyping();

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: text })
    });

    if (!res.ok) {
      throw new Error(`Server returned ${res.status}`);
    }

    const data = await res.json();

    typing.remove();

    const { bubble } = addMessage("bot", "");

    await typeMessage(
      bubble,
      data.reply || "Sorry, I couldn't generate a response.",
      40
    );

  } catch (error) {
    typing.remove();

    const { wrap } = addMessage(
      "bot",
      "I couldn't reach the server. Check that it's running, then try again."
    );

    wrap.classList.add("error");

    console.error("Q-TIP request failed:", error);

  } finally {
    // Keep the input disabled if the user issued exit.
    if (text.toLowerCase() !== "exit") {
      setBusy(false);
      input.focus();
    }
  }
});