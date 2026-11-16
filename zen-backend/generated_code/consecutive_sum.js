function consecutiveSum(n) { 
let sum = 0; 
for (let i = 1; i <= n; i++) {
 sum += i; } 
return sum; }
console.log(consecutiveSum(10));