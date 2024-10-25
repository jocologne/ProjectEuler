
//largest prime factor of the number 600851475143.

#include <stdio.h>

int isprime(int n);

int main(void)
{
	unsigned int i = 2;
	long long num = 600851475143;
	while (num > 1)
	{
		while ((num % i) == 0)
		{
			num = num / i;
			printf("Factor_%d\n", i);
		}
		i++;
		while (!isprime(i))
			i++;
	}
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
