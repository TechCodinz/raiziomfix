import React, { useState } from 'react';
import { askAI } from '../api/raiziom';

export default function RaiziomAssistant() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const askRaiziom = async () => {
    const token = localStorage.getItem('raiziomToken');
    if (!token) {
      alert('Login required');
      return;
    }
    const data = await askAI(message, token);
    if (data.reply) setResponse(data.reply);
  };

  return (
    <div style={{ position: 'fixed', bottom: 20, right: 20, background: '#fff', padding: 20 }}>
      <h3>Raiziom</h3>
      <input value={message} onChange={(e) => setMessage(e.target.value)} placeholder="Ask" />
      <button onClick={askRaiziom}>Send</button>
      <div>{response}</div>
    </div>
  );
}
