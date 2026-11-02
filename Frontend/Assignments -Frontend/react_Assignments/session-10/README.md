# Session 10: Context API

## Implemented Tasks
1. `UserContext.jsx`: Context initialized with default username (`Mithlesh`) and `loggedIn: true` state.
2. `Navbar.jsx`: Uses `useContext(UserContext)` to display the authenticated username and provide login toggling.
3. `ThemeContext.jsx`: Provides `light` and `dark` themes with a toggle function.
4. Dynamic Theme Switching: Theme toggle updates whole application background, card panels, text color, and borders.
5. Nested Component Refactoring: `DeepThemeBadge` consumes `ThemeContext` directly, eliminating intermediate prop drilling through `LevelOneContainer` and `LevelTwoContainer`.
6. `NotificationContext.jsx`: Manages unread count with WhatsApp-style badge, increment/decrement controls, and lower bound preventing counts below zero.
7. Clean context architecture with individual context files in `src/context/`.

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

