# Antigravity Master Prompt: React Assignments (Sessions 1--14)

## Objective

Complete **all React frontend assignments from Session 1 through Session
14** in the existing project folders on this computer.

Act as a careful senior React developer and assignment implementation
assistant. Inspect the folders that already exist, understand their
structure, and make the required changes directly in those folders. The
folders have already been created. **Do not create duplicate project
folders or replace the existing work unnecessarily.**

These assignments are frontend-only React exercises. Do not create a
backend, database, server API, authentication service, or unrelated
infrastructure.

------------------------------------------------------------------------

## 1. First: inspect the workspace before changing anything

1.  Inspect the current workspace and identify all existing assignment
    folders for Sessions 1--14.
2.  Read each folder's `package.json`, source files, and existing
    components before editing.
3.  Determine whether the projects use Create React App or Vite.
    Preserve the existing setup in each folder.
4.  Build a session-to-folder map and keep it in your execution notes.
5.  If a session folder is missing, do not silently create a duplicate
    or guess where it belongs. Report the missing folder and continue
    with the folders that exist.
6.  Preserve existing student work that is unrelated to the tasks. Do
    not delete assets, configuration, or files just to make the
    implementation easier.
7.  Avoid installing a second copy of React or replacing project tooling
    when the required dependencies are already present.

### Important project-structure rule

-   If each session has its own React project, implement that session in
    its own existing folder.
-   If multiple sessions intentionally share one React project, preserve
    that arrangement and organize components clearly.
-   Do not combine all sessions into one giant `App.js`.
-   Keep each assignment independently understandable and runnable in
    its intended folder.

------------------------------------------------------------------------

## 2. Implementation standards

Use these standards across all sessions:

-   Use JavaScript and JSX unless the existing project is already
    configured for TypeScript.
-   Use functional components by default. Use a class component only
    where Session 2 explicitly requires it.
-   Use React hooks correctly and follow the Rules of Hooks.
-   Use semantic, valid HTML. Close every JSX tag and use valid nesting.
-   Give mapped elements stable, unique `key` props.
-   Use controlled inputs for forms unless a task specifically asks for
    `useRef` behavior.
-   Handle loading, empty, success, and error states where the task
    requires them.
-   Keep components small, reusable, and named clearly.
-   Use readable variable names and consistent formatting.
-   Add only the dependencies needed for the assignments.
-   Do not add unnecessary UI libraries or CSS frameworks.
-   Create simple, clean, responsive styling. Keep styling local to each
    session where practical.
-   Ensure buttons have the correct `type` attribute inside forms.
-   Prevent default form submission when handling forms in React.
-   Never expose real API secrets or API keys in frontend source code.
-   Do not claim that a mock API is live production data. Label dummy
    data clearly.
-   Avoid deprecated React patterns unless the assignment explicitly
    asks for them.

### Dependency and compatibility notes

-   For Session 1, use `npx create-react-app` only if the existing
    folder is not already a React project and setup is genuinely needed.
    Do not overwrite an existing project.
-   For React Router, inspect the installed version. Use the syntax
    supported by the installed version. For React Router v6 or newer,
    use `element` and a wildcard route rather than the removed
    `component` and `activeClassName` APIs.
-   Install `prop-types` only if it is not already installed.
-   Install `axios` only if it is not already installed.
-   Do not downgrade or upgrade React just to match an outdated
    tutorial.
-   If Create React App is already present, preserve it. If a project
    uses Vite, keep Vite.

------------------------------------------------------------------------

# 3. Assignment requirements by session

Implement every task below. Treat the descriptions as acceptance
criteria.

## Session 1: React setup and components

1.  Confirm Node.js and npm are available. Do not install system
    software or change machine-level settings without permission. If
    Node.js is unavailable, report that clearly.
2.  In the existing Session 1 project, ensure the React app is named or
    identified as `InstaCloneStarter`. Do not create a duplicate folder
    if the assignment folder already exists.
3.  Update `App.js` to render:
    -   An `<h1>` containing `Welcome to My React Zomato App`.
    -   A `TrendingSong` component below it.
4.  Create `TrendingSong.js` as a functional component returning an
    `<h2>` containing `Trending on Spotify: Calm Down`.
5.  Export and import the component correctly.
6.  Add a short 3--4 line explanation of the Virtual DOM in the
    assignment README or a clearly named `answers.md` file:
    -   React maintains a lightweight representation of the UI.
    -   It compares the new representation with the previous one.
    -   It updates only the necessary parts of the real DOM.
    -   This can reduce unnecessary DOM operations and make UI updates
        more efficient.

## Session 2: JSX, props, functional and class components

1.  Update `App.js` to show an `<h1>` containing
    `Welcome to React JSX!`.
2.  Create a functional `UserGreeting` component that accepts `username`
    and displays `Hello, {username}!`.
3.  Create a class component named `UserGreetingClass` with the same
    `username` prop and output.
4.  Render both greeting components in `App.js`, using `Mithlesh` as the
    username.
5.  Create a `MiniProfile` functional component that displays:
    -   A profile image using a safe public image URL.
    -   The name `Mithlesh`.
    -   A short profile status.
6.  Render the mini profile in the app.
7.  Ensure the JSX is valid, all tags are closed, elements are correctly
    nested, and the component returns one valid parent element.

## Session 3: Props, defaults, and prop validation

1.  Create `ProductCard` accepting `productName` and `price`, and
    display both in a styled card.
2.  Create `UserProfile` accepting `username`, `followers`, and
    `profilePic`.
3.  Display a profile image, username, and follower count in an
    Instagram-style card.
4.  Set `UserProfile.defaultProps` so missing `followers` becomes `0`
    and missing `profilePic` uses a sensible default image URL.
5.  Add `prop-types` validation to `ProductCard`:
    -   `productName`: `PropTypes.string`
    -   `price`: `PropTypes.number`
6.  Include a small demo in `App.js` showing both components, including
    at least one example that uses the default values.

## Session 4: useState interaction exercises

1.  Create `LikeButton`: show a heart button and count starting at `0`;
    each click increments the count by one.
2.  Create `CartItem`: show an item name, quantity, plus button, and
    minus button. Quantity starts at `1`, increments on plus, and cannot
    fall below `0` on minus.
3.  Create `SongVote`: show a song title, vote count, upvote and
    downvote controls. Do not allow the vote count to become negative.
4.  Create a five-star rating selector. Clicking a star highlights that
    star and all preceding stars. Store the selected rating with
    `useState`.
5.  Render all four exercises in the session app.

## Session 5: events, controlled inputs, and forms

1.  Create a `LikeButton` that increments and displays a count when
    clicked.
2.  Create a `SearchBar` with a controlled input. Display the current
    input value below it as the user types.
3.  Create a `LoginForm` with username and password fields. On submit:
    -   Prevent the browser's default page reload.
    -   Display an alert containing the entered username and password,
        as requested by the assignment.
    -   Clear both controlled input fields after submission.
    -   Do not use `window.location` or reload the page.
4.  Create a `PlaylistAdder` with song name and artist fields. On
    submit, add the song to a list displayed below the form.
5.  Use React state for form values and playlist entries. Use stable
    keys for playlist items.
6.  Keep the password demonstration local only. Do not send or store
    credentials.

## Session 6: lists and conditional rendering

1.  Create `Playlist`, receiving an array of `{ title, artist }` song
    objects and rendering them with `map()` in a `<ul>`.
2.  Create `OrderStatus`, receiving boolean `isDelivered` and using a
    ternary expression to show:
    -   `Order Delivered 🎉` when true.
    -   `Order on the way 🚚` when false.
3.  Create `FollowerList`, receiving an array of usernames. Show
    `No followers yet` when empty; otherwise render the list.
4.  Create `CartSummary`, receiving an array of `{ name, price }` items:
    -   Render each item.
    -   Show `Cart is empty` when the array is empty.
    -   Show `Checkout Now` only when there are at least three items.
5.  Add representative demo data in `App.js`, including empty and
    non-empty examples where useful.

## Session 7: useEffect and data fetching

1.  Create `TrendingSongs` using `useEffect` with an empty dependency
    array to log `Component mounted` once per mount. Explain that React
    Strict Mode may run effects an extra time during development.
2.  Create `IPLScoreFetcher`:
    -   Fetch `https://jsonplaceholder.typicode.com/posts` when mounted.
    -   Check `response.ok` before parsing JSON.
    -   Display the first post's `title` as the match headline.
    -   Include loading and error handling.
    -   Clearly label the content as mock data, not live IPL scores.
3.  Create `MovieSuggestions`:
    -   Fetch `https://jsonplaceholder.typicode.com/users` on mount.
    -   Show a loading message while waiting.
    -   Display returned `name` values in a list.
    -   Handle request failures with a readable error message.
4.  Refactor the existing button-triggered fetch exercise so the fetch
    runs automatically in `useEffect` on mount. Preserve its existing UI
    and styling as much as possible; only move the fetch behavior and
    add necessary lifecycle handling.
5.  Use cleanup with `AbortController` where appropriate to prevent
    setting state after an aborted/unmounted request.

## Session 8: useRef and controlled forms

1.  Create `SearchBar` with an input and button. Use `useRef` to focus
    the input automatically after mount.
2.  Create a login form with controlled username and password inputs
    using `useState`. On clicking Login:
    -   Perform the requested local demo behavior without a page reload.
    -   Clear the username field.
    -   Focus the username input using `useRef`.
3.  Create `AddToPlaylist`:
    -   Accept a song name.
    -   Add it to a displayed playlist on Add.
    -   Clear the input if appropriate.
    -   Focus the input again after adding.
4.  Refactor a feedback form with controlled name and message inputs.
    Add a button that focuses the message input using `useRef`.
5.  Do not access `ref.current` before the element is mounted. Handle
    empty input sensibly.

## Session 9: React Router

1.  Install `react-router-dom` only if missing.
2.  Configure `BrowserRouter` in the correct root location, avoiding
    nested routers.
3.  Create:
    -   `HomePage.js`
    -   `DealsPage.js`
    -   `CartPage.js`
    -   `NotFound.js`
4.  Configure routes:
    -   `/` → Home
    -   `/deals` → Deals
    -   `/cart` → Cart
    -   `*` → Not Found
5.  Create a navigation bar using `NavLink` for Home, Deals, and Cart.
6.  Highlight the active link using the `style` callback or `className`
    callback supported by the installed React Router version.
7.  Verify that direct navigation to each route works in development. Do
    not add a `homepage` field to package.json unless the deployment
    target actually requires it.

## Session 10: Context API

1.  Create `UserContext.js` with a context default value containing a
    username and `loggedIn` status.
2.  Create a `Navbar` component that uses `useContext` to display the
    current username.
3.  Create a theme context/provider with `light` and `dark` theme state
    and a toggle function.
4.  Add a toggle button. Update the main app area's background, text
    color, and other necessary styles according to the selected theme.
5.  Refactor a nested component example so the deepest child reads the
    theme directly from context. Remove unnecessary theme props from
    intermediate components.
6.  Create a notification-count context/provider:
    -   Store unread notification count.
    -   Expose a way to increase or decrease the count.
    -   Do not allow the count below zero.
    -   Show the count in a small WhatsApp-style notification demo.
7.  Keep contexts and providers in clearly named files. Avoid
    unnecessary duplicate providers.

## Session 11: Axios GET, POST, search, and request states

1.  Install Axios only if it is missing.
2.  Create a popular-movies component using Axios:
    -   Use TMDB's popular movies endpoint if a valid API key is already
        configured securely for local development.
    -   Never invent or expose an API key.
    -   If no key is available, use
        `https://jsonplaceholder.typicode.com/posts` as the assignment's
        allowed mock alternative.
    -   Display the first five titles.
3.  Create `AddPlaylist` with playlist name and description. POST the
    data to `https://jsonplaceholder.typicode.com/posts` using Axios and
    show a success message when the request succeeds. Explain that
    JSONPlaceholder simulates creation and does not persist real data.
4.  Create a restaurant search component:
    -   Fetch a public mock restaurant list using Axios.
    -   If the supplied Mocki endpoint is unavailable, use a reliable
        mock/fallback dataset stored locally in the frontend and explain
        that it is demo data.
    -   Filter restaurant names as the user types, case-insensitively.
    -   Show a useful empty state when there are no matches.
5.  Update the movie list to show `Loading...` during the request and a
    readable error message if it fails.
6.  Create a comment form with `username` and `comment` fields. POST to
    `https://jsonplaceholder.typicode.com/comments` using Axios and
    display the returned response below the form.
7.  Use `try/catch`, check response status where useful, and avoid
    duplicate requests caused by incorrect effect dependencies.

## Session 12: fetch, reload, status handling, and errors

1.  Create `TrendingSongs` using `fetch()` to get posts from
    `https://jsonplaceholder.typicode.com/posts` and display the first
    three titles.
2.  If the request fails, show exactly `Error loading data` instead of
    the list.
3.  Add a Reload button that retries the request. Keep the error message
    visible if the retry fails.
4.  Create `IPLScores` using
    `https://jsonplaceholder.typicode.com/users` as dummy data:
    -   Check `response.ok` before parsing.
    -   Throw an error for non-success HTTP responses.
    -   Show `Error loading scores` if the request fails.
    -   Label the output as mock cricket data, not live scores.
5.  Fix the provided buggy effect pattern by checking HTTP status and
    catching both network and HTTP errors. Use this safe pattern as a
    guide:

``` jsx
useEffect(() => {
  const controller = new AbortController();

  async function loadData() {
    try {
      setLoading(true);
      setError(false);

      const response = await fetch(
        "https://jsonplaceholder.typicode.com/posts",
        { signal: controller.signal }
      );

      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }

      const result = await response.json();
      setData(result);
    } catch (error) {
      if (error.name !== "AbortError") {
        setError(true);
      }
    } finally {
      if (!controller.signal.aborted) {
        setLoading(false);
      }
    }
  }

  loadData();
  return () => controller.abort();
}, []);
```

6.  Keep the exact requested error messages for the relevant exercises.

## Session 13: production build and deployment preparation

1.  Run the existing project's production build command, normally
    `npm run build`, in the correct project folder.
2.  Confirm the build completes successfully and identify the generated
    output directory:
    -   Create React App normally outputs `build/`.
    -   Vite normally outputs `dist/`.
3.  Do not commit generated build output unless the repository's
    deployment setup specifically requires it.
4.  Prepare deployment instructions for Netlify:
    -   Connect the intended GitHub repository through Netlify.
    -   For Create React App, build command is `npm run build` and
        publish directory is `build`.
    -   For Vite, build command is `npm run build` and publish directory
        is `dist`.
5.  For a React Router single-page app, add the correct Netlify redirect
    configuration so deep links resolve to `index.html`. For example,
    create `public/_redirects` for Create React App or
    `public/_redirects` for Vite, containing:

``` text
/*    /index.html   200
```

Ensure the file is copied to the build output. 6. Do not set a fake
`homepage` URL. Do not invent a Netlify site URL or claim deployment has
happened. Deployment requires the user's GitHub and Netlify accounts and
authorization. 7. Add a new feature to the deployed-app exercise, such
as a dark-mode toggle or About page, and verify it locally with a fresh
production build. 8. Add a short feedback template asking a friend to
test the app on a phone. Include two example UX improvements to
consider, such as improving mobile spacing and optimizing image sizes.
Do not claim that real feedback was collected.

## Session 14: reusable profile and portfolio components

1.  Create a new React app named `InstaBio` only if the existing Session
    14 folder is not already a React app. Do not create a duplicate
    project.
2.  Create a reusable `ProfileCard` component accepting name, profile
    picture URL, and bio.
3.  Create a reusable `SocialLinks` component accepting an array of
    social links for Instagram, LinkedIn, and GitHub.
4.  Render the links as clickable icons or accessible text links. Use
    valid URLs and accessible labels. Do not use dead `href="#"` links.
5.  Assemble a clean homepage using `ProfileCard` and `SocialLinks`.
6.  Add an optional `theme` prop to `SocialLinks`, supporting `light`
    and `dark`, with sensible defaults and distinct styles.
7.  At the top of `ProjectCard.js`, add a clearly marked comment
    describing a reasonable reusable `ProjectCard` structure, as
    requested by the Copilot exercise. Do not claim the comment was
    generated by GitHub Copilot unless Copilot was actually used.
8.  Implement `ProjectCard` with reusable props such as project title,
    description, image, technology list, and project URL. Handle
    optional values gracefully.

------------------------------------------------------------------------

# 4. Suggested folder organization

Adapt this to the existing project rather than forcing a restructure. A
typical structure is:

``` text
Session-XX/
├── public/
├── src/
│   ├── components/
│   │   ├── LikeButton.jsx
│   │   ├── SearchBar.jsx
│   │   └── ...
│   ├── context/
│   │   ├── UserContext.js
│   │   ├── ThemeContext.js
│   │   └── NotificationContext.js
│   ├── pages/
│   │   ├── HomePage.jsx
│   │   ├── DealsPage.jsx
│   │   ├── CartPage.jsx
│   │   └── NotFound.jsx
│   ├── App.js
│   ├── App.css
│   └── index.js
├── package.json
└── README.md
```

Do not create every suggested folder if the session does not need it.
Match the existing naming convention where practical.

------------------------------------------------------------------------

# 5. Assignment documentation

For each session folder:

1.  Create or update a `README.md` that lists the session's tasks and
    the files implementing them.
2.  Include brief instructions to run the app, such as:

``` bash
npm install
npm start
```

For Vite projects, use the existing script, commonly:

``` bash
npm install
npm run dev
```

3.  Add `answers.md` only where written explanations are needed,
    including the Virtual DOM explanation in Session 1 and any necessary
    notes about mock APIs or deployment.
4.  Keep documentation concise and accurate. Do not mark a task complete
    unless its implementation exists and has been checked.

------------------------------------------------------------------------

# 6. Verification checklist

After implementation, verify every existing session project
independently.

For each project:

-   [ ] Dependencies are installed or already available.
-   [ ] The correct start script exists.
-   [ ] The app compiles without syntax or import errors.
-   [ ] All requested components are imported and rendered.
-   [ ] All JSX is valid and semantic.
-   [ ] State updates work as expected.
-   [ ] Forms do not reload the page.
-   [ ] Empty, loading, and error states work where required.
-   [ ] API requests check HTTP errors as well as network errors.
-   [ ] React Router routes and the not-found route work.
-   [ ] Context values are available to the intended descendants.
-   [ ] No API keys or credentials are hardcoded.
-   [ ] Responsive styling is usable on mobile and desktop.

Run the available build command in each project. If a build fails,
diagnose and fix errors caused by your changes. Do not hide or ignore
build errors. If an external API is unavailable, distinguish that from a
code/build failure and provide a local demo fallback where the
assignment permits it.

------------------------------------------------------------------------

# 7. Execution order and final report

Work through Sessions 1--14 in order. You may make safe, independent
changes efficiently, but do not skip a session.

At the end, provide a concise completion report containing:

1.  The folder mapped to each session.
2.  The main files created or modified in each session.
3.  Dependencies installed, if any.
4.  Build/test result for each session (`Passed`, `Failed`, or
    `Blocked`).
5.  Any tasks blocked by missing folders, unavailable API services,
    missing credentials, or account-based deployment steps.
6.  Exact commands the student should run to start each project.
7.  Any manual steps still required from the student.

**Do not claim that Node.js was installed, a site was deployed, a friend
tested the site, or an external API worked unless you actually verified
it.**

## Final instruction

Make the changes directly in the existing assignment folders. Prioritize
correctness, clarity, and completing the stated requirements over
unnecessary redesign. Keep every project frontend-only, preserve
existing work, verify the result, and report honestly what was
completed.
