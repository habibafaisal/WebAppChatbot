function sendMessage() {
  var userInput = document.getElementById("user-input").value;
  document.getElementById("user-input").value = "";

  appendMessage("You", userInput);

  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: userInput }),
  })
    .then((response) => response.json())
    .then((data) => {
      appendMessage("Bot", data.response);
    })
    .catch((error) => {
      console.error("Error:", error);
    });

  function appendMessage(sender, message) {
    var chatBox = document.getElementById("chat-box");
    var messageElement = document.createElement("div");
    messageElement.classList.add("message");
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(messageElement);

    // Scroll to bottom of chat box
    chatBox.scrollTop = chatBox.scrollHeight;
  }
}
