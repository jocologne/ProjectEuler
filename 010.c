
//Find the sum of all the primes below two million

#include <stdio.h>

int isprime(int n);

int main(void)
{
	long long sum = 0;
	int lim = 2000000;
	int n = 2;
	while (n < lim)
	{
		if (isprime(n))
		{
			sum += n;
			printf("%lld\n", sum);
		}
		n++;
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