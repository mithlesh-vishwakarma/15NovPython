
// --- Task 1 ---
// Create an array called favApps with the names of 5 apps you use daily and use a for loop to print each app name in the console.
console.log("--- Task 1 ---");
const favApps = ["Instagram", "Zomato", "Paytm", "WhatsApp", "YouTube"];
for (let i = 0; i < favApps.length; i++) {
  console.log(favApps[i]);
}

// --- Task 2 ---
// Create an array called playlist containing 5 of your favorite song names and use a for loop to print each song name in the console.
console.log("\n--- Task 2 ---");
const playlist1 = ["Kesariya", "Tum Hi Ho", "Chaleya", "Apna Bana Le", "Deva Deva"];
for (let i = 0; i < playlist1.length; i++) {
  console.log(playlist1[i]);
}

// --- Task 3 ---
// Given an array of cricket team names for IPL, use a while loop to print each team name in uppercase.
console.log("\n--- Task 3 ---");
const iplTeams = ["Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bengaluru", "Gujarat Titans"];
let task3Index = 0;
while (task3Index < iplTeams.length) {
  console.log(iplTeams[task3Index].toUpperCase());
  task3Index++;
}

// --- Task 4 ---
// Given an array of Instagram usernames, use a while loop to print each username in uppercase.
console.log("\n--- Task 4 ---");
const instaUsernames = ["john_doe", "code_ninja", "tech_guru", "dev_master"];
let task4Index = 0;
while (task4Index < instaUsernames.length) {
  console.log(instaUsernames[task4Index].toUpperCase());
  task4Index++;
}

// --- Task 5 ---
// Create an array called playlist with 4 song names (strings). Use a do-while loop to print each song name along with its index in the console.
console.log("\n--- Task 5 ---");
const playlist2 = ["Kesariya", "Passori", "Maan Meri Jaan", "Raataan Lambiyan"];
let task5Index = 0;
if (playlist2.length > 0) {
  do {
    console.log(`${task5Index}: ${playlist2[task5Index]}`);
    task5Index++;
  } while (task5Index < playlist2.length);
}

// --- Task 6 ---
// Use a do-while loop to simulate a Zomato order tracker that prints order statuses in sequence.
console.log("\n--- Task 6 ---");
const orderStatuses = ["Preparing", "Out for delivery", "Delivered"];
let statusIndex = 0;
do {
  console.log(`Order status: ${orderStatuses[statusIndex]}`);
  statusIndex++;
} while (statusIndex < orderStatuses.length);

// --- Task 7 ---
// Given an array of objects representing Flipkart products, use a for-of loop to print only the product names.
console.log("\n--- Task 7 ---");
const flipkartProducts = [
  { name: "Wireless Headphones", price: 1999 },
  { name: "Smart Watch", price: 2999 },
  { name: "Power Bank", price: 999 },
  { name: "Gaming Mouse", price: 1499 }
];
for (const product of flipkartProducts) {
  console.log(product.name);
}

// --- Task 8 ---
// Given an array of Flipkart product prices, use a for-of loop to calculate and print the total price of all products.
console.log("\n--- Task 8 ---");
const productPrices = [1999, 2999, 999, 1499];
let totalPrice = 0;
for (const price of productPrices) {
  totalPrice += price;
}
console.log(`Total price of all products: ₹${totalPrice}`);

// --- Task 9 ---
// Create an array of 5 WhatsApp contacts. Use forEach with an arrow function to print a message for each.
console.log("\n--- Task 9 ---");
const whatsappContacts = ["Alex", "Priya", "Rahul", "Neha", "Vikram"];
whatsappContacts.forEach(name => {
  console.log(`Sending hi to ${name} on WhatsApp!`);
});

// --- Task 10 ---
// Use the forEach method to loop through an array of cricket team names and print 'Go [team]!' for each.
console.log("\n--- Task 10 ---");
const teams = ["MI", "CSK", "RCB", "GT"];
teams.forEach(function (team) {
  console.log(`Go ${team}!`);
});
