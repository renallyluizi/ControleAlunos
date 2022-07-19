import json

print('\n .:. Bem-vindo(a)! .:.\n')
opcoes = 'MENU:\n1. Adicionar Aluno\n2. Adicionar Nota\n3. Remover Aluno\n4. Remover nota\n5. Alterar Nome do Aluno\n6. Alterar Nota\n7. Buscar Aluno\n8. Média da Turma\n9. Aluno Destaque\n10. Alunos Matriculados\n11. Alunos Ordenados Por Nota\n12. Alunos Aprovados por Média\n13. Alunos Na Final\n14. Alunos Reprovados\n15. Encerrar o Programa\n\nDigite a Opção Desejada:' 
alunos = {}

def cadast():
    nome = str(input('\nDigite o nome do aluno que deseja cadastrar: '))
    nome = nome.upper() 
    if nome in alunos:
         print('\nAluno já cadastrado.')
    else:
         alunos[nome] = []      
         print('\nAluno cadastrado com sucesso!')

def add(): 
    nome = str(input('Digite o nome do aluno que deseja adicionar nota: \n')) 
    nome = nome.upper()
    if nome in alunos:
         if len(alunos[nome]) < 3:         
            nota = float(input('\nDigite a nota do aluno: '))
            if 0 <= nota <= 10 :
                alunos[nome].append(nota)   
                print('\nNota registrada com sucesso.')
            else :
                print('\nErro. Nota inválida.')
         else :
            print('\nO aluno já possui todas as notas.')
    else :
        print('\nErro. O aluno não existe no sistema.')  

def delaluno() :
    nome = str(input('\nDigite o nome do aluno que deseja descadastrar: '))  
    nome = nome.upper()
    if nome in alunos:
        del alunos[nome]
        print('\nAluno removido com sucesso!')
    else:
        print('\nAluno não encontrado.')      

def delnota():
    busca = input('Digite o nome do aluno que deseja alterar a nota: ') 
    busca = busca.upper() 
    for nome in alunos: 
        if busca in nome:
            print(nome , ' Notas: ' , alunos[nome])
            editar = int(input('Qual nota deseja excluir [1/2/3]? ')) 
            if editar == 1:  
                if len(alunos[nome]) < 1:
                    print('\nNota inexistente.')
                else:    
                    alunos[nome].pop(editar-1)
                    print('\nNota excluida com sucesso!') 
            elif editar == 2:  
                if len(alunos[nome]) < 2:
                    print('\nNota inexistente.')
                else:    
                    alunos[nome].pop(editar-1)
                    print('\nNota excluida com sucesso!') 
            elif editar == 3:  
                if len(alunos[nome]) < 3:
                    print('\nNota inexistente.')
                else:
                    alunos[nome].pop(editar-1)
                    print('\nNota excluida com sucesso!') 
        else:
            print('\nAluno não encontrado. ') 
                     
def altaluno():
    nome = str(input('\nDigite o nome do aluno que deseja alterar: '))
    nome = nome.upper()
    if nome in alunos :
        novo = str(input('\nNovo nome: '))
        novo = novo.upper()
        pos = alunos.index(nome)                                
        alunos[pos] = novo
    else:
        print('\nAluno não encontrado.')

def altnota():
    busca = input('\nDigite o nome do aluno que deseja alterar a nota: ') 
    busca = busca.upper() 
    for nome in alunos: 
        if busca in nome:
            print(nome , ' Notas: ' , alunos[nome])
            editar = int(input('\nQual nota deseja editar [1/2/3]? ')) 
            if editar == 1:  
                if len(alunos[nome]) < 1:
                    print('\nNota inexistente.')
                else:    
                    nota = float(input('\nDigite a nova nota: '))
                    alunos[nome].pop(editar-1)
                    alunos[nome].insert(editar-1, nota) 
                    print('\nNota editada com sucesso!') 
            elif editar == 2:  
                if len(alunos[nome]) < 2:
                    print('\nNota inexistente.')
                else:    
                    nota = float(input('\nDigite a nova nota: '))
                    alunos[nome].pop(editar-1)
                    alunos[nome].insert(editar-1, nota) 
                    print('\nNota editada com sucesso!') 
            elif editar == 3:  
                if len(alunos[nome]) < 3:
                    print('\nNota inexistente.')
                else:    
                    nota = float(input('\nDigite a nova nota: '))
                    alunos[nome].pop(editar-1)
                    alunos[nome].insert(editar-1, nota) 
                    print('\nNota editada com sucesso!') 
        else:
            print('\nAluno não encontrado. ') 

def exibir() :
    busca = str(input('Digite o nome do aluno: \n'))
    busca = busca.upper()
    for nome in alunos:
        if busca in nome:
            med = sum(alunos[nome])/3
            print(nome , ' Notas: ' , alunos[nome] , ' Média: ' , med , '\n')
        else:
            print('Aluno não encontrado. \n')    

def media():
    soma = 0
    for nome in alunos:
        notas = alunos[nome]
        soma += exibir(notas)
        medgeral = soma / len(alunos)
        print('A média da turma é: ' , medgeral)

def destq() :
    melhor = 0
    aluno = ''
    for nome in alunos:
        media = sum(alunos[nome])/3
        if media > melhor:
            melhor = media
            aluno = nome   
    print('O aluno destaque é: ' , aluno , 'com média: ', melhor)
        
def todos():
    pos = 0
    for nome in sorted(alunos.keys()):
        med = sum(alunos[nome])/3
        pos += 1
        print(pos , '. ' , nome , " : " , alunos[nome] , ' Média: %.2f'%med)

#def tdsnota():


def apv():
    for nome in alunos:
         med = sum(alunos[nome])/3
         if med >=7:
            print(nome,': aprovado(a), com média: %.2f !\n'% med)

def final():
    for nome in alunos:
         med = sum(alunos[nome])/3
         if 5 <= med < 7:
            print(nome,': na final, com média: %.2f. \n'% med)
def reprov():
    for nome in alunos:
         med = sum(alunos[nome])/3
         if med < 5:
            print(nome,': reprovado(a), com média: %.2f. \n'% med)  

def salvar():
    with open('./alunos.json', 'w') as file:
         data = json.dumps(alunos)
         file.write(data)

def carregar():
    with open('./alunos.json', 'r') as file:
        return json.load(file)
        

escolha = int(input(opcoes))
alunos = carregar()
while escolha != 15:            
     if escolha == 1 : 
         cadast()    
     elif escolha == 2:
         add()       
     elif escolha == 3:
         delaluno()   
     elif escolha == 4:
         delnota()     
     elif escolha == 5:
         altaluno()   
     elif escolha == 6:
         altnota()    
     elif escolha == 7:
         exibir()     
     elif escolha == 8: 
         media()      
     elif escolha == 9:
         destq()    
     elif escolha == 10:
         todos()      
     #elif escolha == 11:
         #tdsnota()   ----- não consegui 
     elif escolha == 12:
         apv()
     elif escolha == 13:
         final()
     elif escolha == 14:
         reprov()

     salvar()
     escolha = int(input(opcoes))
