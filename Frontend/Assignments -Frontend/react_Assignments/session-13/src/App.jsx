import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import About from './pages/About';
import Products from './pages/Products';
import NotFound from './pages/NotFound';
import './index.css';

function App() {
  const [darkMode, setDarkMode] = useState(false);

  return (
    <div className={`app-wrapper ${darkMode ? 'dark-theme' : 'light-theme'}`}>
      <Navbar darkMode={darkMode} setDarkMode={setDarkMode} />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/products" element={<Products />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
      <footer className="site-footer">
        <p>© 2026 DeployPro. Production Build Verified with Netlify Redirects Support.</p>
      </footer>
    </div>
  );
}

export default App;

