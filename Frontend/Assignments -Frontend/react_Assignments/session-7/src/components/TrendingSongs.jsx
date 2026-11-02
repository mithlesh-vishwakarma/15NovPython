import React, { useEffect, useState } from 'react';

function TrendingSongs() {
  const [mountLogs, setMountLogs] = useState([]);

  useEffect(() => {
    console.log('Component mounted');
    setMountLogs((prev) => [...prev, `[${new Date().toLocaleTimeString()}] Component mounted`]);

    return () => {
      console.log('Component unmounted');
    };
  }, []);

  return (
    <div className="component-card">
      <h3>1. Trending Songs (Mount Lifecycle)</h3>
      <p>
        Check the browser DevTools console to see the logged message:{' '}
        <code>Component mounted</code>.
      </p>
      <div className="callout-box">
        <strong>Strict Mode Note:</strong> In development, <code>&lt;React.StrictMode&gt;</code>{' '}
        deliberately mounts, unmounts, and re-mounts components to help detect side effects and
        missing cleanups. This explains why mount effects run twice in dev mode.
      </div>
      <div className="log-list">
        <strong>Mount events detected:</strong>
        <ul>
          {mountLogs.map((log, index) => (
            <li key={index}>{log}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default TrendingSongs;

