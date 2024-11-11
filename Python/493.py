
import random

urna = [1,1,1,1,1,1,1,1,1,1,
		  2,2,2,2,2,2,2,2,2,2,
		  3,3,3,3,3,3,3,3,3,3,
		  4,4,4,4,4,4,4,4,4,4,
		  5,5,5,5,5,5,5,5,5,5,
		  6,6,6,6,6,6,6,6,6,6,
		  7,7,7,7,7,7,7,7,7,7]

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
while (n < 80000):
	sum += sorteio()
	n += 1

print(sum / n)

#O programa simula um numero grande de sorteios e retorna a media de cores
#distintas encontradas, a resposta se aproxima da solução mas não é exata.
