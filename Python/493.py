
import random

# A urna contem 70 bolas, 10 de cada cor, numeradas de 1 a 7.
urna = [1,1,1,1,1,1,1,1,1,1,
		  2,2,2,2,2,2,2,2,2,2,
		  3,3,3,3,3,3,3,3,3,3,
		  4,4,4,4,4,4,4,4,4,4,
		  5,5,5,5,5,5,5,5,5,5,
		  6,6,6,6,6,6,6,6,6,6,
		  7,7,7,7,7,7,7,7,7,7]

# Função que simula um sorteio de 20 bolas da urna e retorna o numero de cores
def sorteio():
	urna2 = list(urna)
	sorteadas = []
	while len(sorteadas) < 20:
		escolha = random.randint(0, len(urna2) - 1)
		sorteadas.append(urna2[escolha])
		urna2.pop(escolha)
	#print(sorteadas)
	return len(set(sorteadas))

sum = 0
n = 0
while (n < 100000):
	sum += sorteio()
	n += 1

print(sum / n)

#O programa simula um numero grande de sorteios e retorna a media de cores
#distintas encontradas, a resposta se aproxima da solução mas não é exata.

