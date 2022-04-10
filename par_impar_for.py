tamanho=int(input("Digite a quantidade que deseja:"))
i =range(tamanho)
qual= input("Deseja numeros pares ou impares ?")
count=0

if qual=="pares" or qual == "par":
    for n in i:
        if n%2 ==0:
           print(n)
           count +=1
    print("De 0 a %s são %r pares" %(tamanho,count) )
else:
    for n in i:
        if n%2==1:
            print(n)
            count +=1
    print("De 0 a %s são %r impares" %(tamanho,count) )






