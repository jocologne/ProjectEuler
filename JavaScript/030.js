function sumOfFifthPowers() {
	const power = 5;
	const limit = 6 * Math.pow(9, power); // 6 * 9^5 is a safe upper limit
	let sum = 0;

	for (let i = 2; i <= limit; i++) {
		let digits = i.toString().split('');
		let sumOfPowers = digits.reduce((acc, digit) => acc + Math.pow(parseInt(digit), power), 0);

		if (sumOfPowers === i) {
			sum += i;
		}
	}

	return sum;
}

console.log(sumOfFifthPowers());