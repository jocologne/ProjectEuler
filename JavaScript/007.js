function isPrime(num) {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
	 if (num % i == 0) return false;
  }
  return true;
}

let i = 0;
let count = 0;
while (count < 10001) {
  if (isPrime(i)) {
	 count++;
  }
  i++;
}
console.log(i - 1); 