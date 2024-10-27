//Find the largest palindrome made from the product of two 3-digit numbers.

#include <stdio.h>

//Falta implementar a função is_palindrome.
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
	while (i < 1000)
	{
		j = i;
		while (j < 1000)
		{
			if (is_palindrome(i * j) && (i * j) > result)
				result = i * j;
			j++;
		}
		i++;
	}
	printf("%d\n", result);
}