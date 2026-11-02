import React, { useState, useRef } from 'react';

function RefLoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const usernameInputRef = useRef(null);

  const handleLogin = (e) => {
    e.preventDefault();

    if (!username.trim() || !password.trim()) {
      setMessage('⚠️ Please provide both username and password.');
      if (!username.trim() && usernameInputRef.current) {
        usernameInputRef.current.focus();
      }
      return;
    }

    // Local demo feedback without page reload
    setMessage(`✅ Login simulated for user: "${username}". Field cleared & re-focused.`);

    // Clear username field
    setUsername('');

    // Re-focus username input using useRef
    if (usernameInputRef.current) {
      usernameInputRef.current.focus();
    }
  };

  return (
    <div className="component-card">
      <h3>2. Controlled Login with Focus Management</h3>
      <form onSubmit={handleLogin} className="form-stack">
        <div className="form-group">
          <label htmlFor="ref-username">Username:</label>
          <input
            ref={usernameInputRef}
            id="ref-username"
            type="text"
            className="form-control"
            placeholder="Enter username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            autoComplete="username"
          />
        </div>

        <div className="form-group">
          <label htmlFor="ref-password">Password:</label>
          <input
            id="ref-password"
            type="password"
            className="form-control"
            placeholder="Enter password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoComplete="current-password"
          />
        </div>

        <button type="submit" className="btn btn-primary">
          Log In
        </button>
      </form>

      {message && <div className="feedback-banner">{message}</div>}
    </div>
  );
}

export default RefLoginForm;

