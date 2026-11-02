import React, { createContext, useState } from 'react';

export const UserContext = createContext({
  username: 'Mithlesh',
  loggedIn: true,
  setUsername: () => {},
  toggleLogin: () => {},
});

export function UserProvider({ children }) {
  const [username, setUsername] = useState('Mithlesh');
  const [loggedIn, setLoggedIn] = useState(true);

  const toggleLogin = () => {
    setLoggedIn((prev) => !prev);
  };

  return (
    <UserContext.Provider value={{ username, loggedIn, setUsername, toggleLogin }}>
      {children}
    </UserContext.Provider>
  );
}

