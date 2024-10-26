#Problema 05

cd=1
n=232000000

while cd==1:
    if n%1==0 and n%2==0  and n%3==0 and n%4==0  and n%5==0  and n%6==0  and n%7==0  and n%8==0  and n%9==0  and n%10==0  and n%11==0  and n%12==0  and n%13==0  and n%14==0  and n%15==0  and n%16==0  and n%17==0  and n%18==0  and n%19==0  and n%20==0:
        cd=0
    print(n)
    n+=1
    if n >1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20:
        cd=0
        print("Erro...limite atingido")

#Funciona mas demora a dar uma resposta, precisa ser otimizado.