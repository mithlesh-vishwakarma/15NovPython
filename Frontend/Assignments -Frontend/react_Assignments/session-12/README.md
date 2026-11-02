# Session 12: Fetch, Reload, Status Handling, and Errors

## Implemented Tasks
1. `TrendingSongsFetch`: Fetches first three titles from `https://jsonplaceholder.typicode.com/posts` using native `fetch()`.
2. Exact Error Text Handling: On failure, conditionally renders the exact string `Error loading data` in place of the list.
3. Reload Capability: Provides a Reload button that re-triggers the network query, retaining the error message if retry fails.
4. `IPLScoresFetch`: Fetches `https://jsonplaceholder.typicode.com/users`, verifies `response.ok`, throws on non-success HTTP status codes, and displays the exact message `Error loading scores` on error. Clearly labeled as simulated cricket demo data.
5. Implemented standard safe `useEffect` pattern with `AbortController`, `try/catch/finally`, and status validation.

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

