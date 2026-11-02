import React from 'react';

const ICON_MAP = {
  instagram: '📸',
  linkedin: '💼',
  github: '🐙',
  twitter: '🐦',
  website: '🌐',
};

function SocialLinks({ links = [], theme = 'light' }) {
  if (!links || links.length === 0) {
    return null;
  }

  return (
    <nav className={`social-links-nav theme-${theme}`} aria-label="Social media profiles">
      {links.map((item) => {
        const platformKey = item.platform.toLowerCase();
        const icon = ICON_MAP[platformKey] || '🔗';

        return (
          <a
            key={item.platform}
            href={item.url}
            target="_blank"
            rel="noopener noreferrer"
            className="social-pill"
            aria-label={`Visit my ${item.platform} profile`}
          >
            <span className="social-icon" aria-hidden="true">{icon}</span>
            <span className="social-label">{item.platform}</span>
          </a>
        );
      })}
    </nav>
  );
}

export default SocialLinks;

