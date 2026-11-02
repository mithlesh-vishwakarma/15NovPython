import React, { createContext, useState } from 'react';

export const NotificationContext = createContext({
  unreadCount: 0,
  incrementCount: () => {},
  decrementCount: () => {},
  clearCount: () => {},
});

export function NotificationProvider({ children }) {
  const [unreadCount, setUnreadCount] = useState(3);

  const incrementCount = () => {
    setUnreadCount((prev) => prev + 1);
  };

  const decrementCount = () => {
    setUnreadCount((prev) => (prev > 0 ? prev - 1 : 0));
  };

  const clearCount = () => {
    setUnreadCount(0);
  };

  return (
    <NotificationContext.Provider
      value={{ unreadCount, incrementCount, decrementCount, clearCount }}
    >
      {children}
    </NotificationContext.Provider>
  );
}

