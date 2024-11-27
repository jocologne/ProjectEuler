function isPrime(num) {
	if (num < 2) return false;
	for (let i = 2; i <= Math.sqrt(num); i++) {
		if (num % i == 0) return false;
	}
	return true;
}

function primeFactors(num) {
	const factors = [];
	for (let i = 2; i <= num; i++) {
		if (isPrime(i) && num % i == 0) {
			factors.push(i);
			num /= i;
		}
	}
	return factors;
}
console.log(primeFactors(600851475143));