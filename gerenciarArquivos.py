vetorCorretas = []
vetorMatricula = []
vetorRespostas = []
vetorResultado = []

arqResultado = open('resultado.txt','w')


arqGabarito = open('gabarito.txt','r')
respostaGabarito = arqGabarito.readline()
for resp in respostaGabarito:
    vetorCorretas.append(resp)


arqMatricula = open('respostas.txt','r')
cont = 0
for line in arqMatricula:
    if cont>0:
        vetorMatricula.append(line[:4])
        vetorRespostas.append(line[5:])
    cont+=1


respAlunos = []
for r in vetorRespostas:
    respAlunos.append(r.split())
cont2=0


for r in respAlunos:
    for rA in r:
        if rA == vetorCorretas[cont2]:
            vetorResultado.append(vetorCorretas[cont2] + rA +'S')
        else:
            vetorResultado.append(vetorCorretas[cont2] + rA +'N')       

        cont2+=1
    vetorResultado.append('|')
    cont2=0

respCertas = 0
respErradas = 0
posicaoAluno = 0
numAprovados = 0
numReprovados = 0
numExame = 0
vetorAcertadas = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
vetorErradas =   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i = 0

for r in vetorResultado:
    if r[2:]=='S':
        respCertas+=1
        vetorAcertadas[i] += 1
        i+=1
    elif r[2:]=='N':
        respErradas+=1
        vetorErradas[i] += 1
        i+=1 

    num = respCertas + respErradas
    while posicaoAluno < 25 and num == 1:
        arqResultado.write(vetorMatricula[posicaoAluno]+' : ')
        break
    else:
        arqResultado.write(r+' ')

    if r =='|':
        i=0
        if respCertas > 9:
            arqResultado.write(str(respCertas))
        if respCertas <10:
            arqResultado.write('0'+str(respCertas))
        if respCertas > 13:
            arqResultado.write(' APROVADO ')
            numAprovados+=1
        if respCertas < 14 and respCertas > 8:
            arqResultado.write(' EXAME')
            numExame+=1
        if respCertas < 9:
            arqResultado.write(' REPROVADO')
            numReprovados+=1
        arqResultado.write('\n')
        posicaoAluno+=1          
        
        respCertas = 0
        respErradas = 0
        
arqResultado.write(str(numAprovados)+' APROVADO(S)\n')
arqResultado.write(str(numExame)+' EXAME(S)\n')
arqResultado.write(str(numReprovados)+' REPROVADO(S)\n')


for j in range(25):
    if j == 0:
        arqResultado.write('      ')
    if vetorAcertadas[j] < 10:
        arqResultado.write('0' + str(vetorAcertadas[j]) + str(vetorErradas[j])+' ')
    elif vetorErradas[j] < 10:
        arqResultado.write(str(vetorAcertadas[j]) + '0' + str(vetorErradas[j])+' ')
    else:
        arqResultado.write(str(vetorAcertadas[j]) + str(vetorErradas[j])+' ')
    
    
arqResultado.close()