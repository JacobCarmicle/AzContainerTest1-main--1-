import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [msg, setMsg] = useState("Loading...");
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const API = "https://apps-env-placeholder.victoriousdune-7778cfb6.eastus2.azurecontainerapps.io/api/message";
    fetch(API)
      .then(r => {
        if (!r.ok) throw new Error("Network response was not ok");
        return r.json();
      })
      .then(d => {
        setMsg(d.message);
        setIsLoading(false);
      })
      .catch(e => {
        setMsg(`Error connecting to backend: ${e.message}`);
        setIsLoading(false);
      });
  }, []);

  return (
    <div className="app-container">
      <div className="fun-header">
        <h1 className="title">🚀 Hello World! 🚀</h1>
        <div className="subtitle">Your Awesome Container App</div>
      </div>
      
      <div className="message-container">
        <div className="message-label">Backend says:</div>
        <div className={`message ${isLoading ? 'loading' : 'loaded'}`}>
          {isLoading ? (
            <div className="loading-spinner">
              <div className="spinner"></div>
              <span>Connecting to backend...</span>
            </div>
          ) : (
            <span className="message-text">{msg}</span>
          )}
        </div>
      </div>
      
      <div className="fun-footer">
        <div className="floating-emoji">🎉</div>
        <div className="floating-emoji">✨</div>
        <div className="floating-emoji">🌟</div>
      </div>
    </div>
  );
}

export default App;