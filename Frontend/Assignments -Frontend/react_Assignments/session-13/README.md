# Session 13: Production Build and Deployment Preparation

## Implemented Tasks
1. Configured Vite production build pipeline (`npm run build`).
2. Configured and confirmed build output directory as `dist/`.
3. Added `public/_redirects` containing `/* /index.html 200` to support client-side deep routing on Netlify.
4. Added new features per assignment requirements:
   - Dynamic **Dark Mode / Light Mode** theme toggle.
   - Dedicated **About Us** page (`/about`).
   - Responsive navbar and footer.
5. Prepared comprehensive Netlify deployment instructions and mobile peer-testing feedback template in `answers.md`.
6. Verified fresh production build locally.

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

### Test Production Build
```bash
npm run build
```

### Preview Production Build
```bash
npm run preview
```

