# Session 8: useRef and Controlled Forms

## Implemented Tasks
1. `AutoFocusSearchBar`: Direct element ref using `useRef`, focusing the search bar automatically on mount inside `useEffect`.
2. `RefLoginForm`: Controlled username and password inputs; on submit, executes demo without reload, clears the username field, and imperatively focuses the username input using `useRef`.
3. `AddToPlaylistRef`: Adds new songs to a displayed list, clears the input, and immediately returns keyboard focus to the input for fast continuous entry.
4. `FeedbackFormRef`: Controlled feedback form with a dedicated "Focus Message Field" button that triggers `.focus()` on the textarea ref.
5. All refs are checked with `ref.current` checks to ensure safety before element mounting.

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

