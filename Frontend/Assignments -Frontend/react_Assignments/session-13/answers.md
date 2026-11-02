# Session 13: Deployment Guide, Build Analysis & Mobile Feedback Template

## 1. Production Build & Output Directory Analysis
- **Build Command:** `npm run build` (executing `vite build`).
- **Output Directory:** `dist/`.
- In Create React App, the default output directory is `build/`. In Vite, it is `dist/`.
- In our project, Vite builds all minified HTML, bundled JS, CSS chunks, and copies the `public/_redirects` file directly into `dist/_redirects`.

## 2. Netlify Deployment Instructions
> **Notice:** Actual deployment to Netlify requires connecting your authenticated GitHub account and Netlify workspace. Never invent URLs or assume automatic deployment without authorization.

### Step-by-Step Guide:
1. Push this project repository to your personal GitHub account:
   ```bash
   git add .
   git commit -m "feat: complete Session 13 production build configuration"
   git push origin main
   ```
2. Log in to [Netlify](https://app.netlify.com/).
3. Click **"Add new site"** > **"Import an existing project"**.
4. Select **GitHub** and grant permissions for your assignment repository.
5. In the Build & Deployment Settings:
   - **Base directory:** `session-13` (if deploying from a monorepo) or leave empty if the root repository is this project.
   - **Build command:** `npm run build`
   - **Publish directory:** `dist`
6. Click **"Deploy site"**. Netlify will run the build and publish the live site with an SSL certificate.

## 3. Why `_redirects` is Essential for Single Page Apps (SPA)
In a client-side routed SPA (like React Router), routes such as `/about` or `/products` do not exist as static files on the server.
If a visitor navigates directly to `yoursite.netlify.app/about` or refreshes the page, the Netlify web server looks for a physical file at `/about/index.html` and returns a **404 Not Found** error.

By adding `public/_redirects`:
```text
/*    /index.html   200
```
Netlify is instructed to rewrite all requested paths (`/*`) to `/index.html` with an HTTP status `200` OK. React Router then reads `window.location.pathname` and mounts the correct route component on the client.

## 4. Mobile Testing & UX Feedback Template
Below is the review template to share with a peer/friend for mobile UX verification:

---
### Mobile App Testing Feedback Form (Template)
**Tester Name:** _____________________
**Device & Browser Tested:** (e.g. iPhone 14 Safari / Samsung S23 Chrome)

1. **First Impressions:**
   - Did the page load quickly without visible layout shift? [ ] Yes  [ ] No
   - Is text easy to read in both Light and Dark modes? [ ] Yes  [ ] No

2. **Navigation & Routes:**
   - Does tapping "Home", "Products", and "About" navigate smoothly? [ ] Yes  [ ] No
   - Does browser refresh on `/about` or `/products` reload properly without a 404? [ ] Yes  [ ] No

3. **Key UX Improvements to Evaluate:**
   - **Touch Target & Mobile Spacing:** Are navigation links and the theme toggle button spaced adequately for thumb tapping without accidental mis-clicks?
   - **Image & Asset Optimization:** Are assets and cards appropriately sized for mobile viewports without causing horizontal overflow or excessive bandwidth consumption?

**Additional Comments / Suggestions:**
____________________________________________________________________
---
*(Note: This is an evaluation template. Real peer testing feedback should be collected directly from peers following live deployment.)*

