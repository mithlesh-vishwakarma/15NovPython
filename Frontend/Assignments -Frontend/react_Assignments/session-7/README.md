# Session 7: useEffect and Data Fetching

## Implemented Tasks
1. `TrendingSongs`: Uses `useEffect` with an empty dependency array `[]` to log `Component mounted` on mount, with full documentation of React Strict Mode double-invocations in development.
2. `IPLScoreFetcher`: Fetches posts from `https://jsonplaceholder.typicode.com/posts`, verifies `response.ok`, extracts the first post's title as a match headline, includes loading/error handling, and clearly labels content as simulated mock cricket data.
3. `MovieSuggestions`: Fetches users from `https://jsonplaceholder.typicode.com/users`, displays loading state, handles errors, and renders user names.
4. `AutoFetchData`: Refactored previous button-triggered fetch to load data automatically upon mounting via `useEffect`, preserving clean UI.
5. `AbortController` used in all asynchronous effects to abort in-flight requests and prevent memory leaks.

## How to Run

### Install Dependencies
```bash
npm install
```

### Start Development Server
```bash
npm run dev
# or
npm start
```

### Production Build
```bash
npm run build
```

