let n = 3;
let res = 0; 
while (n < 1000)
{
	if (n % 3 == 0 || n % 5 == 0)
	{
		res = res + n;
	}
	n++;
}
console.log(res);
