# Session 7: Notes on useEffect & React Strict Mode

### Why does useEffect run twice in React development?
In React 18+ development mode with `<React.StrictMode>`, React deliberately runs lifecycle effects twice upon mounting:
1. React mounts the component (`setup`).
2. React unmounts the component (`cleanup`).
3. React mounts the component again (`setup`).

This intentional behavior simulates an unmount/remount cycle to help developers catch:
- Missing cleanup functions (e.g. event listeners, subscriptions, intervals, timers).
- Network race conditions and memory leaks where state is updated on an unmounted component.

In production builds, `useEffect` runs only once per mount. Using `AbortController` in the cleanup function ensures pending network requests are safely cancelled if the component unmounts.

