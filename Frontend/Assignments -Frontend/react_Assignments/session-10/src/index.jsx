import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { UserProvider } from './context/UserContext';
import { ThemeProvider } from './context/ThemeContext';
import { NotificationProvider } from './context/NotificationContext';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <UserProvider>
      <ThemeProvider>
        <NotificationProvider>
          <App />
        </NotificationProvider>
      </ThemeProvider>
    </UserProvider>
  </React.StrictMode>
);

