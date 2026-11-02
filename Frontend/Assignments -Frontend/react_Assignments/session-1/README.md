# Session 1: React Setup and Components

Project Name: `InstaCloneStarter`

## Implemented Tasks
1. Confirmed Node.js and npm availability (`node v24.18.0`, `npm 11.16.0`).
2. Configured React project named `instaclonestarter`.
3. Created `App.js` rendering `<h1>Welcome to My React Zomato App</h1>` and the `TrendingSong` component.
4. Created `TrendingSong.js` functional component rendering `<h2>Trending on Spotify: Calm Down</h2>`.
5. Exported and imported `TrendingSong` into `App.js`.
6. Documented Virtual DOM explanation in `answers.md` and below.

## Virtual DOM Summary
- React maintains a lightweight representation of the UI in memory.
- It compares the new representation with the previous one (diffing).
- It updates only the necessary parts of the real DOM (reconciliation).
- This minimizes costly direct DOM manipulations and maximizes UI performance.

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

