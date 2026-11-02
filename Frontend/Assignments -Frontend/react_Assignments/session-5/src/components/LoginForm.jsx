import React, { useState } from 'react';

function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!username.trim() || !password.trim()) {
      alert('Please fill in both username and password fields.');
      return;
    }

    // Local demo alert per assignment requirements
    alert(`Login Submitted:\nUsername: ${username}\nPassword: ${password}`);

    // Clear both controlled inputs without reloading the page
    setUsername('');
    setPassword('');
  };

  return (
    <div className="card">
      <h3>3. Controlled Login Form</h3>
      <form onSubmit={handleSubmit} className="form-stack">
        <div className="input-group">
          <label htmlFor="login-username" className="form-label">Username:</label>
          <input
            id="login-username"
            type="text"
            className="form-control"
            placeholder="Enter username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            autoComplete="username"
            required
          />
        </div>

        <div className="input-group">
          <label htmlFor="login-password" className="form-label">Password:</label>
          <input
            id="login-password"
            type="password"
            className="form-control"
            placeholder="Enter password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoComplete="current-password"
            required
          />
        </div>

        <button type="submit" className="btn btn-primary">
          Log In
        </button>
      </form>
    </div>
  );
}

export default LoginForm;

