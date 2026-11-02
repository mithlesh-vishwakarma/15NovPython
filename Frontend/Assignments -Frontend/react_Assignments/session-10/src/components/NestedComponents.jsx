import React, { useContext } from 'react';
import { ThemeContext } from '../context/ThemeContext';

// Deepest Child Component: Reads theme directly from context WITHOUT prop drilling
function DeepThemeBadge() {
  const { theme } = useContext(ThemeContext);

  return (
    <div className={`deep-child-badge ${theme}`}>
      <span>Direct Context Consumer: <strong>Theme is {theme.toUpperCase()}</strong></span>
    </div>
  );
}

// Intermediate Component 2: Passes NO theme prop
function LevelTwoContainer() {
  return (
    <div className="intermediate-level level-2">
      <p className="level-label">Level 2 Component (No theme props passed through here)</p>
      <DeepThemeBadge />
    </div>
  );
}

// Intermediate Component 1: Passes NO theme prop
function LevelOneContainer() {
  return (
    <div className="intermediate-level level-1">
      <p className="level-label">Level 1 Component (No theme props passed through here)</p>
      <LevelTwoContainer />
    </div>
  );
}

function NestedComponents() {
  return (
    <div className="component-card">
      <h3>5. Eliminating Prop Drilling with Context</h3>
      <p className="subtext">
        Intermediate components (Level 1 and Level 2) no longer receive or forward <code>theme</code> props.
        The deepest child reads the active theme directly via <code>useContext(ThemeContext)</code>.
      </p>
      <LevelOneContainer />
    </div>
  );
}

export default NestedComponents;

