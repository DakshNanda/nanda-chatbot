import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [chat, setChat] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    const userMessage = { sender: 'user', text: query };
    setChat([...chat, userMessage]);

    const response = await fetch('/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: query })
    });

    const data = await response.json();
    const botMessage = { sender: 'bot', text: data.answer };
    setChat([...chat, userMessage, botMessage]);
    setQuery('');
  };

  return (
    <div className="chat-container">
      <h1>Nanda and Bros Co. 🤝</h1>
      <div className="chat-box">
        {chat.map((msg, idx) => (
          <div key={idx} className={`chat-message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit} className="chat-form">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask us anything..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
