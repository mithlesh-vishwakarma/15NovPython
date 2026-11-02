# Session 9: React Router

## Implemented Tasks
1. Integrated `react-router-dom` v6 routing.
2. Configured root `BrowserRouter` without duplicate or nested wrappers in `index.jsx`.
3. Created page components:
   - `HomePage.jsx`
   - `DealsPage.jsx`
   - `CartPage.jsx`
   - `NotFound.jsx` (404 Fallback)
4. Configured route matching in `App.jsx`:
   - `/` → `HomePage`
   - `/deals` → `DealsPage`
   - `/cart` → `CartPage`
   - `*` → `NotFound`
5. Created `Navbar` with `NavLink` for Home, Deals, and Cart.
6. Styled active links using the v6 `({ isActive })` className callback pattern.

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

