def menu():
    opçao =input(''' 
    ===================================
               AGENDA     
    MENU: 
    
    [1] ADICIONAR CONTATO
    [2] LISTAR CONTATO
    [3] DELETAR CONTATO
    [4] BUSCAR CONTATO PELO ID
    
    ==================================
    ESCOLHA UMA OPÇÃO ACIMA:
    ''')

    if opçao == '1':
        cadastrar_contato()
    elif opçao == '2':
        listar_contato()
    elif opçao == '3':
        deletar_contato()
    else:
        buscar_contato()



def cadastrar_contato():

    idContato = input('Escolha o ID do contato: ')
    nome = input('Escreva o nome do contato: ')
    telefone= input('Escreva o telefone do contato: ')
    email = input('Escreva o e-mail do contato: ')

    try: #tratamento de erro 
        agenda = open('agenda.txt','a') #vai criar e abrir um arquivo 'agenda.txt' e vai adicionar 'a' dados nessa agenda
        dados = f'{idContato};{nome};{telefone};{email} \n' #vai escrever os dados #fechou uma string pq adicionou virgula entre {} 
        #usou o \n para pular de linha 
        agenda.write(dados)
        agenda.close() #vai fechar o documento agenda
        print(f'Contato gravado com sucesso !!!')
    except: 
        print('ERRO na gravação do contato')




def listar_contato():
    agenda = open('agenda.txt', 'r') #abrir agenda e 'r' serve apenas para leitura
    for contato in agenda:
        print(contato)
    agenda.close()



def deletar_contato():
    nome_deletado = input('Digite o nome a ser deletado: ')
    agenda = open('agenda.txt', 'r')
    aux = [] #variavel auxiliar que recebe uma lista vazia
    aux2 = [] #variavel auxiliar 2 
    for i in agenda:
        aux.append(i) #jogou as informaçoes da agenda na variavel auxiliar1
    for i in range(0, len(aux)):
        if nome_deletado not in aux[i]:
            aux2.append(aux[i])
    agenda = open('agenda.txt', 'w') #abriu agenda na condiçao de escrita 'w'
    for i in aux2:
        agenda.write(i) #gravou linha por linha na agenda
    print(f'Contato deletado com sucesso!')
    listar_contato()






def buscar_contato():
    nome = input(f'Digite o nome a ser procurado: ') #criou uma variavel para digitar o nome a ser procurado na agenda
    agenda = open('agenda.txt', 'r') #abriu a agenda somente para leitura 
    for contato in agenda:
        if nome in contato.split(';')[1]: #split(';') = vai cortar sempre na virgula para fazer uma coluna , #[1]= 1 é a coluna do nome, vai procurar o nome
            print(contato)
    agenda.close()
    


def main(): 

    menu()


main()
