let a = 1
let b = 2
let n = 2
let temp = 0
resp = b
while (b < 4000000)
{
	temp = a
	a = b
	b = a + temp
	if (b % 2 ==0)
	{
		resp += b
	}
	n++
}
console.log(resp)