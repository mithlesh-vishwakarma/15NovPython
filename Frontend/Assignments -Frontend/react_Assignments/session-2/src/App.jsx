import React from 'react';
import UserGreeting from './components/UserGreeting';
import UserGreetingClass from './components/UserGreetingClass';
import MiniProfile from './components/MiniProfile';
import './index.css';

function App() {
  const currentUsername = 'Mithlesh';

  return (
    <main className="app-container">
      <header>
        <h1>Welcome to React JSX!</h1>
      </header>

      <section className="greetings-section" aria-label="Greeting components">
        <h2>Greeting Demonstrations</h2>
        <UserGreeting username={currentUsername} />
        <UserGreetingClass username={currentUsername} />
      </section>

      <section className="profile-section" aria-label="User Profile">
        <h2>User Profile</h2>
        <MiniProfile
          name={currentUsername}
          status="Frontend developer exploring React JSX, props, and components!"
        />
      </section>
    </main>
  );
}

export default App;

