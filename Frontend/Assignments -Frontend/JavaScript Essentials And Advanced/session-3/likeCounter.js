// task:2 Create a JavaScript file called likeCounter.js that declares a variable likes with value 0, increments it by 1 using the += operator, and logs the updated likes count to the console.
let likes = 0;
likes += 1;

console.log(likes);

// task:3 Write a function showDiscountTag(price) that checks if a product's price is less than 500 using a comparison operator. If true, print 'Special Discount!', otherwise, print 'Regular Price'.


function showDiscountTag() {
    let price = 400;
    if (price < 500) {
        console.log("Special Discount!");
    }
    else {
        console.log("Regular Price");
    }
}
showDiscountTag();

// task:4 Write a function isEligibleForDiscount(totalAmount) that returns true if the totalAmount is greater than or equal to 500, otherwise false. Test it with values 300 and 700.

function isEligibleForDiscount(totalAmount) {
    if (totalAmount >= 500) {
        console.log("Eligible for discount");
    }
    else {
        console.log("Not eligible for discount");
    }
}

isEligibleForDiscount(300);
isEligibleForDiscount(700);

// task:5 Build a mini Instagram-style verification badge logic: declare a variable followers and use a ternary operator to set a variable badge to 'Verified Creator' if followers is more than 1000, or 'Regular User' otherwise. Print the badge value.

let followers = 10000;
let badge = followers > 1000 ? "Verified Creator" : "Regular User";
console.log(badge);


function getBadge(followers) {
    let badge = followers >= 1000 ? "Verified Creator ⭐" : "Regular User";
    console.log(badge);
}
getBadge(500);

// task:6  Given a variable isPremiumUser and hasActiveSubscription, use logical operators to check if both are true. If so, print 'Access Granted'; otherwise, print 'Upgrade Needed'.<em><strong>Hint:</strong> Use the && operator for this check.</em>

let hasActiveSubscription = true;
let isPremiumUser = true;

if (isPremiumUser && hasActiveSubscription) {
    console.log("Access Granted");
}
else {
    console.log("Upgrade Needed");
}


// task:7  Given a variable username, write a condition that checks if username is truthy, and if so, logs 'Welcome, [username]!', otherwise logs 'Guest Login'.<em><strong>Hint:</strong> Try with username = '', username = null, and username = 'Priya'.</em>

let username = 'Mithlesh';

if (username) {
    console.log(`Welcome, ${username}`);
}
else {
    console.log('Guest Login');
}

// task:8 Write a function isTruthy(input) that takes any value and returns 'Truthy' or 'Falsy' based on JavaScript's truthy/falsy evaluation. Test it with '', 0, null, 'hello', and 42.<em><strong>Constraint:</strong> Do not use if-else; use the ternary operator.</em>

function isTruthy(input) {
    if (input)
        console.log("Truthy");
    else
        console.log("Falsy");
}

isTruthy('');
isTruthy(0);
isTruthy(null);
isTruthy('hello');
isTruthy(42);

// task:9 Create a function canOrderFood(isLoggedIn, hasPaymentMethod) that returns true only if both isLoggedIn and hasPaymentMethod are true, using logical operators. Test your function with all possible combinations of true/false.
function canOrderFood(isLoggedIn, hasPaymentMethod) {
    if (isLoggedIn && hasPaymentMethod)
        console.log("You can order food");
    else
        console.log("You cannot order food");
}

canOrderFood(true, true);
canOrderFood(true, false);
canOrderFood(false, true);
canOrderFood(false, false);