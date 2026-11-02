# Session 11: Axios GET, POST, Search, and Request States

## Implemented Tasks
1. Integrated Axios (`axios@^1.7.9`).
2. `PopularMoviesAxios`: Fetches first five titles via Axios using the approved JSONPlaceholder fallback endpoint without hardcoding or inventing private API credentials, supporting loading and error states.
3. `AddPlaylistAxios`: Performs Axios `POST` to `https://jsonplaceholder.typicode.com/posts` with playlist name and description, displaying a success message with returned simulated ID.
4. `RestaurantSearchAxios`: Fetches restaurant data with reliable local fallback, performs live case-insensitive substring search, and provides a clear empty state.
5. `CommentFormAxios`: Submits username and comments via Axios `POST` to `https://jsonplaceholder.typicode.com/comments` and renders the server response directly in the UI.
6. All asynchronous Axios calls are protected with `CancelToken` / cancellation cleanups and `try/catch` error boundaries.

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

