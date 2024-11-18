
//Find the 10001 prime number.

#include <stdio.h>

int isprime(int n);

int main(void)
{
	int lim = 10001;
	int count = 0;
	int num = 1;
	while (count < lim)
	{
		num++;
		if (isprime(num))
			count++;
	}
	printf("%d\n", num);
}

int isprime(int n)
{
	if (n <= 1)
		return (0);
	if (n == 2)
		return (1);
	if (n % 2 == 0)
		return (0);
	unsigned int i = 3;
	while (i * i <= n)
	{
		if ((n % i) == 0 )
			return (0);
		i++;
	}
	return (1);
}
