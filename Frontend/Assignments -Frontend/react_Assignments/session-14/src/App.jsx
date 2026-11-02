import React, { useState } from 'react';
import ProfileCard from './components/ProfileCard';
import SocialLinks from './components/SocialLinks';
import ProjectCard from './components/ProjectCard';
import './index.css';

function App() {
  const [socialTheme, setSocialTheme] = useState('light');

  const mySocialLinks = [
    { platform: 'GitHub', url: 'https://github.com/mithlesh-dev' },
    { platform: 'LinkedIn', url: 'https://linkedin.com/in/mithlesh-developer' },
    { platform: 'Instagram', url: 'https://instagram.com/mithlesh.tech' },
  ];

  const myProjects = [
    {
      id: 1,
      title: 'Zomato Food Delivery Clone',
      description: 'Interactive restaurant discovery and order tracking application with React Router and state hooks.',
      image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80',
      technologies: ['React 18', 'Vite', 'CSS3 Modules'],
      projectUrl: 'https://github.com/mithlesh-dev/zomato-react-clone',
    },
    {
      id: 2,
      title: 'Spotify Playlist Explorer',
      description: 'Music catalog with instant search, track upvoting, and controlled playlist builder components.',
      image: 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=600&q=80',
      technologies: ['React', 'Axios', 'REST API'],
      projectUrl: 'https://github.com/mithlesh-dev/spotify-playlist-explorer',
    },
    {
      id: 3,
      title: 'Realtime Cricket Scoreboard',
      description: 'Robust asynchronous match tracker featuring AbortController and resilient network fallback states.',
      // Optional image omitted intentionally to test graceful fallback
      technologies: ['React Hooks', 'AbortController', 'Fetch API'],
      // Optional projectUrl omitted to test fallback badge
    },
  ];

  return (
    <div className="portfolio-app">
      <main className="content-container">
        <header className="hero-header">
          <ProfileCard
            name="Mithlesh"
            bio="Frontend Engineer specializing in clean React architecture, accessible UI design, and responsive web applications."
            profilePictureUrl="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=320&q=80"
          />

          <div className="theme-toggle-row">
            <span className="theme-label">Social Links Theme:</span>
            <button
              type="button"
              className={`pill-btn ${socialTheme === 'light' ? 'active' : ''}`}
              onClick={() => setSocialTheme('light')}
            >
              Light
            </button>
            <button
              type="button"
              className={`pill-btn ${socialTheme === 'dark' ? 'active' : ''}`}
              onClick={() => setSocialTheme('dark')}
            >
              Dark
            </button>
          </div>

          <SocialLinks links={mySocialLinks} theme={socialTheme} />
        </header>

        <section className="portfolio-section" aria-label="Featured Projects">
          <h2 className="section-title">Featured Portfolio Projects</h2>
          <div className="projects-grid">
            {myProjects.map((project) => (
              <ProjectCard
                key={project.id}
                title={project.title}
                description={project.description}
                image={project.image}
                technologies={project.technologies}
                projectUrl={project.projectUrl}
              />
            ))}
          </div>
        </section>
      </main>

      <footer className="footer-bar">
        <p>Built with React & Vite • InstaBio Session 14</p>
      </footer>
    </div>
  );
}

export default App;

