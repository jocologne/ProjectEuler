//Find the largest palindrome made from the product of two 3-digit numbers.

#include <stdio.h>

int is_palindrome(int n)
{
	return (1);
}

int main(void)
{ 
	int result = 0;
	int i = 100;
	int j;
	int limite = 1000;
	while (i < limite)
	{
		j = i;
		while (j < limite)
		{
			if (is_palindrome(i * j) && (i * j) > result)
				result = i * j;
			j++;
		}
		i++;
	}
	printf("%d\n", result);
}