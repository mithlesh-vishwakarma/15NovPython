# Session 14: Reusable Profile and Portfolio Components

Project Name: `InstaBio`

## Implemented Tasks
1. Configured React application named `InstaBio` in `session-14/`.
2. Created reusable `ProfileCard` component accepting `name`, `profilePictureUrl`, and `bio`.
3. Created reusable `SocialLinks` component accepting an array of link objects for Instagram, LinkedIn, and GitHub.
4. Rendered links as accessible links with valid URLs, platform icons, labels, and zero dead `href="#"` links.
5. Assembled clean homepage in `App.jsx` showcasing profile, social links, and project cards.
6. Implemented optional `theme` prop (`light` and `dark`) for `SocialLinks` with custom styles and an interactive toggle.
7. Added specification comment at the top of `ProjectCard.jsx` describing expected props, structure, and fallback handling.
8. Implemented `ProjectCard` with reusable props (`title`, `description`, `image`, `technologies`, `projectUrl`) with graceful fallbacks for missing images, URLs, and technologies.

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

