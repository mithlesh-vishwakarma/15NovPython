# Session 6: Lists and Conditional Rendering

## Implemented Tasks
1. `Playlist`: Renders an array of `{ title, artist }` objects with `map()` inside an unordered list (`<ul>`) with unique keys.
2. `OrderStatus`: Receives `isDelivered` boolean prop and uses a ternary expression to display `Order Delivered 🎉` or `Order on the way 🚚`.
3. `FollowerList`: Receives usernames array and displays `No followers yet` when empty, otherwise renders the list.
4. `CartSummary`: Receives `{ name, price }` array, renders each item, displays `Cart is empty` when empty, and only renders `Checkout Now` when there are at least 3 items.
5. `App.jsx`: Demonstrates both populated and empty cases with interactive toggles.

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

