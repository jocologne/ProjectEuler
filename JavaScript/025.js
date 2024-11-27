function fibIndex(n) {
	let a = BigInt(1);
	let b = BigInt(1);
	let index = 2;

	while (b.toString().length < n) {
		let temp = b;
		b = a + b;
		a = temp;
		index++;
	}
	return index;
}

const index = fibIndex(1000);
console.log(index);