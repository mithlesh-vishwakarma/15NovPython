# JavaScript Complete & Exhaustive Topic-Wise Notes

This document provides a comprehensive, fully-detailed topic-by-topic master guide to JavaScript. It combines the original lecture contents from `js/lect-1` through `js/lect-8` with essential foundational concepts (Execution Context, Scope Chain, Loose vs Strict Equality, Truthy/Falsy, Loop Controls, Object Utilities, DOM Traversal, Event Capturing, etc.) to ensure complete mastery of the language up through DOM and Events.

---

## Table of Contents
1. [Topic 1: JavaScript Fundamentals & Core Concepts](#topic-1-javascript-fundamentals--core-concepts)
2. [Topic 2: Data Types, Conversion & Operators](#topic-2-data-types-conversion--operators)
3. [Topic 3: Control Flow & Loops](#topic-3-control-flow--loops)
4. [Topic 4: Functions & Functional Programming](#topic-4-functions--functional-programming)
5. [Topic 5: Objects & Constructor Functions](#topic-5-objects--constructor-functions)
6. [Topic 6: Document Object Model (DOM) Manipulation](#topic-6-document-object-model-dom-manipulation)
7. [Topic 7: Event Handling & Event Propagation](#topic-7-event-handling--event-propagation)

---

## Topic 1: JavaScript Fundamentals & Core Concepts

### 1.1 Execution Context & Hoisting
JavaScript is a single-threaded, synchronous language. When code executes, JavaScript creates an **Execution Context** with two phases:
1. **Memory Creation Phase (Creation Phase):** Variables are allocated memory (`var` initialized to `undefined`, `let`/`const` placed in Temporal Dead Zone), and function declarations are stored completely in memory.
2. **Code Execution Phase:** Code is executed line-by-line, assigning actual values to variables and executing functions.

**Hoisting** is JavaScript's default behavior of moving declarations to the top of their scope during the Memory Creation Phase.

```javascript
// Function Hoisting (Works because function declarations are fully loaded during memory phase)
sayHello(); // Output: "Hello World!"

function sayHello() {
    console.log("Hello World!");
}

// Variable Hoisting (var vs let/const)
console.log(a); // Output: undefined (var is hoisted and initialized to undefined)
var a = 10;

// console.log(b); // ❌ ReferenceError: Cannot access 'b' before initialization (TDZ)
let b = 20;
```

### 1.2 Strict Mode (`"use strict"`)
Strict mode enforces cleaner code and prevents silent errors by throwing exceptions for undeclared variables or unsafe actions.
- Place `"use strict";` at the top of a script or function.

```javascript
"use strict";
console.log("Hello World");
m = 100; // ❌ ReferenceError: m is not defined (Strict mode prevents automatic global variable creation)
```

### 1.3 Variable Declarations (`var`, `let`, `const`)
JavaScript provides three keywords to declare variables: `var`, `let`, and `const`.

| Feature | `var` | `let` | `const` |
| :--- | :--- | :--- | :--- |
| **Scope** | Function scope | Block scope `{}` | Block scope `{}` |
| **Redeclarable** | Yes | No | No |
| **Redefinable (Reassignable)** | Yes | Yes | No |
| **Hoisting** | Hoisted with `undefined` | Hoisted in Temporal Dead Zone | Hoisted in Temporal Dead Zone |

```javascript
// --- let ---
let cName = "Tops Tech";
cName = "CodeBite"; // ✅ Allowed (reassignable)
// let cName = "ABC"; // ❌ SyntaxError: Identifier 'cName' has already been declared

// --- const ---
const PI = 3.14;
// PI = 2.7; // ❌ TypeError: Assignment to constant variable

// --- var ---
var m = 100;
var m = 400; // ✅ Allowed (redeclarable and reassignable)
console.log(m); // 400
```

### 1.4 Comments & Template Literals
- **Comments:** Single-line `//` or multi-line `/* ... */`.
- **Template Literals (Backticks `` ` ``):** Allow embedded expressions `${expression}` and multi-line strings without string concatenation.

```javascript
let name = "Megha";
let role = "Instructor";

// Template Literal String Interpolation
let greeting = `Hello ${name}, your role is ${role}.
Welcome to the JavaScript Masterclass!`;
console.log(greeting);
```

### 1.5 User Interaction Modals
JavaScript provides three built-in dialog boxes for interacting with users:

```javascript
// 1. Alert Box: Shows a message to the user
alert("Welcome to JS tutorial");

// 2. Prompt Box: Takes input from the user (returns string or null)
let userName = prompt("Enter your name");
console.log(userName);

// 3. Confirm Box: Asks for user confirmation (returns boolean: true/false)
let isConfirmed = confirm("Are you sure you want to delete items?");
if (isConfirmed) {
    alert("Item deleted successfully!");
}
```

---

## Topic 2: Data Types, Conversion & Operators

### 2.1 Primitive vs Non-Primitive Data Types
JavaScript is dynamically typed. Data types are categorized into **Primitive** (immutable, passed by value) and **Non-Primitive** (mutable, passed by reference) types.

```javascript
// 1. Number (Integers and Floating point)
let num1 = 123;
console.log(typeof num1); // "number"

// 2. BigInt (for integers larger than 2^53 - 1, appended with 'n')
let largeNum = 12378797987878978998n;
console.log(typeof largeNum); // "bigint"

// 3. String
let name = "Manthan";
console.log(typeof name); // "string"

// 4. Symbol (ES6 unique identifier)
let id1 = Symbol("id");
let id2 = Symbol("id");
console.log(id1 === id2); // false (Symbols are guaranteed unique)

// 5. Null (intentional absence of any object value)
let res = null;
console.log(typeof res); // "object" (historic JS quirk)

// 6. Undefined (variable declared but not assigned a value)
let m;
console.log(typeof m); // "undefined"

// 7. Boolean
let flag = true;
console.log(typeof flag); // "boolean"

// 8. Object (Non-Primitive: Arrays, Objects, Functions)
let user = { name: "abc", email: "abc@gmail.com" };
console.log(typeof user); // "object"
```

### 2.2 Truthy & Falsy Values
In JavaScript, any value evaluated in a boolean context is treated as either **Truthy** or **Falsy**.

#### The 6 Falsy Values in JavaScript:
1. `false`
2. `0` (and `-0`, `0n`)
3. `""` (empty string)
4. `null`
5. `undefined`
6. `NaN` (Not a Number)

*Every other value in JavaScript is **Truthy*** (including `"0"`, `"false"`, `[]`, `{}`, `function(){}`).

```javascript
if ("") {
    console.log("Will not run because empty string is falsy");
}

if ("Hello") {
    console.log("Will run because non-empty string is truthy");
}
```

### 2.3 Loose Equality (`==`) vs Strict Equality (`===`)
- **Loose Equality (`==`):** Converts operands to a common type before comparison (**Implicit Type Coercion**).
- **Strict Equality (`===`):** Compares both **value** AND **data type** without type conversion.

```javascript
console.log(5 == "5");  // true  (string "5" is coerced to number 5)
console.log(5 === "5"); // false (types differ: number vs string)

console.log(null == undefined);  // true
console.log(null === undefined); // false
```

### 2.4 Type Conversion & Type Coercion

#### Implicit Type Coercion:
- `+` with a string performs **string concatenation**.
- `*`, `/`, `-` convert numeric strings into **numbers**.

```javascript
console.log("12" + 3);     // "123" (string concatenation)
console.log(2 + 2 + "1");  // "41"  (left-to-right evaluation: 2+2=4, 4+"1"="41")
console.log("12" * 3);     // 36   (implicit conversion to number)
console.log("6" / "2");     // 3    (implicit conversion to number)
```

#### Explicit Type Conversion:
Using built-in constructors to explicitly convert types.

```javascript
// Converting to Number
console.log(Number("123")); // 123
console.log(Number("abc")); // NaN (Not a Number)
console.log(Number(true));  // 1

// Unary Plus Operator (+) for quick conversion
let num = +prompt("Enter number"); // Converts prompt string directly to number

// Converting to Boolean
console.log(Boolean(undefined)); // false
console.log(Boolean("false"));   // true (non-empty string is truthy)
```

#### Relational Comparison Gotcha:
```javascript
console.log(3 > 2 > 1); // false
// Explanation: (3 > 2) evaluates to true -> true > 1 -> 1 > 1 -> false
```

### 2.5 Advanced Operators (`??`, `&&`, `||`, Ternary)

#### Ternary Operator (`condition ? exprIfTrue : exprIfFalse`)
A shorthand for `if-else` statements.

```javascript
let age = 20;
let canVote = (age >= 18) ? "Eligible to Vote" : "Not Eligible";
console.log(canVote); // "Eligible to Vote"
```

#### Nullish Coalescing Operator (`??`) vs Logical OR (`||`)
- `??` checks specifically for `null` or `undefined`.
- `||` checks for any **falsy** value (`0`, `""`, `false`, `null`, `undefined`, `NaN`).

```javascript
let count = 0;
console.log(count || 10); // 10 (0 is falsy, so falls back to 10)
console.log(count ?? 10); // 0  (0 is NOT null/undefined, so retains 0)
```

---

## Topic 3: Control Flow & Loops

### 3.1 Conditional Statements (`if`, `else if`, `else`)
Conditional statements control execution based on boolean expressions.

```javascript
function findEvenOdd(num) {
    if (num % 2 === 0) {
        alert("Even number");
    } else {
        alert("Odd number");
    }
}
```

#### Practical DOM Application: Dynamic Image Filter Switcher
```javascript
function filterImg(filterProp) {
    let img = document.getElementById('img1');
    
    if (filterProp === "gray") {
        img.style.filter = "grayscale(60%)";
    } else if (filterProp === "blur") {
        img.style.filter = "blur(4px)";
    } else if (filterProp === "bright") {
        img.style.filter = "brightness(80%)";
    } else if (filterProp === "contrast") {
        img.style.filter = "contrast(70%)";
    } else {
        img.style.filter = "none";
    }
}
```

### 3.2 Switch-Case Statements
Ideal for comparing a single variable against multiple exact values.

```javascript
function calculate(num1, num2, op) {
    let result;
    switch (op) {
        case '+':
            result = `Add = ${num1 + num2}`;
            break;
        case '-':
            result = `Sub = ${num1 - num2}`;
            break;
        case '*':
            result = `Mul = ${num1 * num2}`;
            break;
        case '/':
            result = `Div = ${num1 / num2}`;
            break;
        default:
            alert("Invalid Operator");
            return;
    }
    console.log(result);
}
```

### 3.3 Iterative Loops & Loop Control (`break`, `continue`)

```javascript
// 1. While Loop (Entry-controlled)
let i = 1;
while (i <= 5) {
    console.log("i =", i);
    i++;
}

// 2. For Loop (Entry-controlled)
for (let i = 1; i <= 5; i++) {
    console.log("i =", i);
}

// 3. Do-While Loop (Exit-controlled: executes body at least ONCE)
let j = 19;
do {
    console.log("j =", j);
    j++;
} while (j <= 10);

// 4. Loop Control Statements: break & continue
for (let k = 1; k <= 10; k++) {
    if (k === 3) continue; // Skips current iteration when k === 3
    if (k === 7) break;    // Exits loop completely when k === 7
    console.log("k =", k); // Outputs: 1, 2, 4, 5, 6
}
```

#### Practical Matrix Generation: Chessboard Grid
```javascript
function generateChessboard() {
    let str = "";
    for (let i = 1; i <= 8; i++) {
        str += "<div>";
        for (let j = 1; j <= 8; j++) {
            // Alternate colors based on row + column sum parity
            if ((i + j) % 2 === 0) {
                str += `<span class="black">${i}</span>`;
            } else {
                str += `<span class="white">${i}</span>`;
            }
        }
        str += "</div>";
    }
    document.getElementById('main').innerHTML = str;
}
```

---

## Topic 4: Functions & Functional Programming

### 4.1 Function Declarations, Scope Chain & Rest Parameters
Functions are first-class citizens in JavaScript.

```javascript
// 1. Basic Function Declaration
function displayMessage() {
    console.log("Welcome to JavaScript!");
}
displayMessage();

// 2. Default Parameters
function addition(x, y, z = 0) {
    console.log(`Sum: ${x + y + z}`);
}
addition(1, 2);    // Sum: 3
addition(3, 4, 5); // Sum: 12

// 3. Rest Parameters (...args - collects arbitrary arguments into an array)
function sumAll(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}
console.log(sumAll(10, 20, 30, 40)); // 100

// 4. Scope Chain & Lexical Environment
let globalVar = "Global";

function outer() {
    let outerVar = "Outer";
    function inner() {
        let innerVar = "Inner";
        console.log(innerVar, outerVar, globalVar); // Inner function has access to outer scopes
    }
    inner();
}
outer();
```

### 4.2 Function Expressions, Arrow Functions & IIFE

```javascript
// 1. Function Expression
const addNumbers = function(x, y) {
    return x + y;
};

// 2. Arrow Function (ES6)
const multiply = (a, b) => a * b;
console.log(multiply(4, 5)); // 20

// 3. Immediately Invoked Function Expression (IIFE)
// Runs immediately upon definition without polluting global scope
(function() {
    let privateSecret = "Initialized safely";
    console.log("IIFE Executed:", privateSecret);
})();
```

### 4.3 Callback Functions & Pure vs Impure Functions
- **Callback Function:** A function passed as an argument to another function.
- **Pure Function:** Given the same input, always returns the exact same output and has no side effects.

```javascript
// Pure Function (No side effects)
function pureAdd(a, b) {
    return a + b;
}

// Callback Pattern Example
function even(num) { console.log(`${num} is Even`); }
function odd(num)  { console.log(`${num} is Odd`); }

function findEvenOdd(cb1, cb2) {
    let num = prompt("Enter a number");
    if (num % 2 === 0) {
        cb1(num);
    } else {
        cb2(num);
    }
}
findEvenOdd(even, odd);
```

---

## Topic 5: Objects & Constructor Functions

### 5.1 Object Creation, Dynamic Keys & Property Access

```javascript
// 1. Object Literal Syntax
let user = {
    username: "john",
    email: "john@gmail.com",
    "total exp": "5 years" // Bracket notation required for keys with spaces
};

console.log(user.username);     // Dot notation
console.log(user["total exp"]); // Bracket notation

// 2. Dynamic Property Binding from HTML Input attributes
document.getElementById('txt1').addEventListener('change', (event) => {
    let userObj = {};
    let key = event.target.name;   // e.g., "uname"
    let val = event.target.value;  // e.g., "John Doe"
    userObj[key] = val;            // Dynamic property key assignment
    console.log(userObj);
});
```

### 5.2 Built-in Object Utility Methods & Destructuring

```javascript
let product = { pname: "Laptop", price: 50000, category: "Electronics" };

// 1. Object Utilities
console.log(Object.keys(product));   // ["pname", "price", "category"]
console.log(Object.values(product)); // ["Laptop", 50000, "Electronics"]
console.log(Object.entries(product));// [["pname", "Laptop"], ["price", 50000], ...]

// 2. Freezing & Sealing Objects
Object.freeze(product); // Prevents adding, deleting, or modifying properties
// product.price = 60000; // ❌ Mutation ignored in strict mode

// 3. Object Destructuring (ES6)
const person = { name: "Alice", age: 25 };
const { name, age } = person;
console.log(name, age); // "Alice", 25

// 4. Property Deletion
let tempObj = { a: 1, b: 2 };
delete tempObj.a;
console.log(tempObj); // { b: 2 }
```

### 5.3 Object Methods, `this` Keyword & Shallow vs Deep Copying

```javascript
let user = {
    uname: "abc",
    printName: function() {
        console.log(this.uname); // 'this' binds to current object instance
    }
};
user.printName();

// Pass-By-Reference
let admin = user;
admin.uname = "john";
console.log(user.uname); // "john" (mutates original reference)

// Shallow Copy using Object.assign() or Spread Operator ({ ...obj })
const original = { a: 1, b: 2 };
const copy = Object.assign({}, original);
copy.a = 99;
console.log(original.a); // 1 (Original remains unchanged)
```

### 5.4 Constructor Functions & Optional Chaining (`?.`)

```javascript
// Constructor Function
function User(name, email) {
    this.uname = name;
    this.email = email;
}

let u1 = new User('Kaif', 'kaif@test.com');
let u2 = new User('Sufiyan', 's@test.com');

// Optional Chaining Operator (?.)
let editData = { name: 'john', cat: { exp: 2 } };
console.log(editData?.cat?.exp);     // 2
console.log(editData?.address?.zip); // undefined (Prevents TypeError crash)
```

---

## Topic 6: Document Object Model (DOM) Manipulation

### 6.1 DOM Selection & Traversal Methods

```javascript
// 1. Selection Methods
let elementById = document.getElementById('para-1');
let elementsByClass = document.getElementsByClassName('box'); // Live HTMLCollection
let singleQuery = document.querySelector('.box');           // First matching node
let allQuery = document.querySelectorAll('p');               // Static NodeList

// 2. DOM Traversal Properties
let child = document.getElementById('para-1');
let parentNode = child.parentElement;             // Selects parent node
let nextSibling = child.nextElementSibling;       // Selects next adjacent sibling
let prevSibling = child.previousElementSibling;   // Selects previous adjacent sibling
let firstChild = parentNode.firstElementChild;    // Selects first child element
```

### 6.2 Modifying Content, Attributes & Inline Styles

```javascript
let p1 = document.getElementById('parar1');

// Content Modifications
p1.innerText = "Plain Text";         // Sets visible text only
p1.textContent = "<b>Raw Code</b>";  // Treats HTML tags as raw literal text
p1.innerHTML = "<b>Bold Text</b>";   // Parses and renders HTML elements

// Attribute Modifications
p1.setAttribute("data-role", "heading");
console.log(p1.getAttribute("data-role")); // "heading"
p1.removeAttribute("data-role");

// Dynamic Styling Loop
let boxArray = document.getElementsByClassName('box');
for (let i = 0; i < boxArray.length; i++) {
    boxArray[i].style.backgroundColor = (i % 2 === 0) ? "gray" : "white";
}
```

### 6.3 Class Manipulation & Node Removal

```javascript
let box = document.getElementById('box1');

// Class List Methods
box.classList.add('show');
box.classList.remove('hide');
box.classList.toggle('active'); // Toggles class presence automatically
console.log(box.classList.contains('show')); // true

// Removing Elements from DOM
// element.remove() or parentElement.removeChild(element)
box.remove();
```

### 6.4 Dynamic Element Creation (Interactive Todo App)

```javascript
let counter = 1;

function addTask() {
    let taskName = document.getElementById('txt1').value;
    if (!taskName) return;

    let li = document.createElement('li');
    li.innerText = taskName;
    li.setAttribute('id', 'liid_' + counter);

    let checkBox = document.createElement('input');
    checkBox.type = "checkbox";
    checkBox.setAttribute('id', 'chck_' + counter);

    let containerDiv = document.createElement('div');
    containerDiv.appendChild(li);
    containerDiv.appendChild(checkBox);

    document.getElementById('tasklist').appendChild(containerDiv);
    document.getElementById('txt1').value = "";
    counter++;
}
```

---

## Topic 7: Event Handling & Event Propagation

### 7.1 Common Browser Events & Form Interception

```javascript
let inputField = document.getElementById('txt1');

// 1. Keyboard Events (keyup, keydown)
inputField.addEventListener('keyup', (event) => {
    console.log("Current value:", event.target.value);
});

// 2. Focus & Blur Events
inputField.addEventListener('focus', (event) => {
    event.target.style.backgroundColor = "lightgray";
});
inputField.addEventListener('blur', (event) => {
    event.target.style.backgroundColor = "white";
});

// 3. Form Submit Event (Prevent default HTTP reload)
document.getElementById('frm1').addEventListener('submit', (event) => {
    event.preventDefault(); // Intercepts form submission
    console.log("Form submission handled asynchronously");
});
```

### 7.2 Event Propagation: Capturing vs Bubbling
Event propagation in the DOM occurs in 3 phases:
1. **Capturing Phase:** Event travels down from `window` $\rightarrow$ `document` $\rightarrow$ parent elements to the target element.
2. **Target Phase:** Event reaches the actual target element.
3. **Bubbling Phase:** Event bubbles up from the target element $\rightarrow$ parent elements back to `window`.

```javascript
let child = document.getElementById('child');
let parent = document.getElementById('parent');

// Default Listener (Bubbling Phase - triggers child first, then parent)
child.addEventListener('click', () => console.log("Child Clicked"));
parent.addEventListener('click', (e) => {
    console.log("Target:", e.target);         // Exact element clicked
    console.log("Current Target:", e.currentTarget); // Element carrying listener
    console.log("Parent Clicked (Bubbled)");
});

// Stop Event Propagation (Prevents event from bubbling up to parent)
child.addEventListener('click', (e) => {
    e.stopPropagation(); // Halts bubbling chain!
});
```

### 7.3 Event Delegation
Instead of attaching separate listeners to every dynamic child element, attach a single event listener to a common parent element.

```javascript
// Event Delegation on Todo List Container
document.getElementById('tasklist').addEventListener('click', (e) => {
    // Check if clicked element has an ID matching our pattern
    if (e.target && e.target.id) {
        let idParts = e.target.id.split('_');
        let targetLi = document.getElementById('liid_' + idParts[1]);
        if (targetLi) {
            targetLi.style.textDecoration = "line-through";
        }
    }
});
```

---
*Comprehensive Master Study Notes created for JavaScript Topics 1 through 7.*
