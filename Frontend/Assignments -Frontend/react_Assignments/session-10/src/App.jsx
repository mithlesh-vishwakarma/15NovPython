import React, { useContext } from 'react';
import Navbar from './components/Navbar';
import NestedComponents from './components/NestedComponents';
import NotificationDemo from './components/NotificationDemo';
import { ThemeContext } from './context/ThemeContext';
import './index.css';

function AppContent() {
  const { theme } = useContext(ThemeContext);

  return (
    <div className={`app-shell theme-${theme}`}>
      <Navbar />

      <main className="main-container">
        <header className="page-header">
          <h1>Session 10: React Context API</h1>
          <p className="subtitle">
            Global state without prop drilling: User auth context, Theme context & WhatsApp notification badge
          </p>
        </header>

        <section className="context-sections">
          <NestedComponents />
          <NotificationDemo />
        </section>
      </main>
    </div>
  );
}

function App() {
  return <AppContent />;
}

export default App;

