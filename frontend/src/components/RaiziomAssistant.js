import React, { useState } from 'react';

export default function RaiziomAssistant() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const askRaiziom = async () => {
    const res = await fetch("https://raiziomfix.onrender.com/ai/respond", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input: message }),
    });

    const data = await res.json();
    setResponse(data.reply);
  };

  return (
    <div style={{ position: "fixed", bottom: 20, right: 20, background: "#fff", padding: 20 }}>
      <h3>Raiziom</h3>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask"
      />
      <button onClick={askRaiziom}>Send</button>
      <div>{response}</div>
    </div>
  );
}
