# Session 1 Answers: The Virtual DOM

### Explanation of the Virtual DOM in React:
- React maintains a lightweight in-memory representation of the UI (the Virtual DOM).
- When component state or props change, it compares the new Virtual DOM tree with the previous one using a diffing algorithm.
- It calculates the minimal set of changes and updates only the necessary parts of the real DOM.
- This diffing and batching reduces expensive direct DOM manipulations, resulting in faster and more efficient UI rendering.

