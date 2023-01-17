import pyodbc


# ─── Conexão Com O Banco De Dados ─────────────────────────────────────────────

dados_conexao = (
    'Driver={SQL Server};' # Driver do SQL Server
    'Server=JOAO\SQLEXPRESS;' # Nome do servidor
    'Database=CadastroPessoas;' # Nome do banco de dados
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("""SELECT * FROM Pessoas ORDER BY ID_Pessoa""")  # Ordena a tabela por ID_Pessoa


# ─── Verificação do Nome ───────────────────────────────────────────────────────


def verificar_nome(str):
    # Retorna True se os caracteres forem alfabéticos ou espaços
    return all(char.isalpha() or char.isspace() for char in str)


# ─── Cadastrar o Nome ─────────────────────────────────────────────────────────


def nome_pessoa(n):
    while True:
        nome_cadastro = input(nome).upper()
        if len(nome_cadastro.split()) == 0: # Verifica se o nome está vazio
            print('ERRO! Nome do cliente não pode estar vazio.')
        elif not verificar_nome(nome_cadastro): # Verifica se há algum caractere numérico ou especial
            print('ERRO! Digite o nome do cliente corretamente.')
        else:
            nome_cadastro = nome_cadastro.strip()   # Caso passe pelas verificações, será validado
            return nome_cadastro


# ─── Cadastrar a Idade ────────────────────────────────────────────────────────


def idade_pessoa(i):
    while True:
        idade_cadastro = input(idade)
        try:
            idade_cadastro = int(idade_cadastro)    # Tenta converter o input em inteiro
            if idade_cadastro > 0:   # Verifica se a idade fornecida é maior que 0
                return idade_cadastro
            else:
                raise ValueError
        except (ValueError, KeyError):   # Caso ocorra algum erro na conversão ou na verificação da idade
            print('ERRO! Digite um número inteiro válido para a pessoa.')
            continue


# ─── Cadastrar O Sexo ─────────────────────────────────────────────────────────


def sexo_pessoa(s):
    while True:
        sexo_cadastro = input(sexo).upper()    # Obtém a entrada do usuário e converte para letra maiúscula
        if sexo_cadastro == 'M' or sexo_cadastro == 'F':    # Verifica se a entrada é 'M' ou 'F'
            return sexo_cadastro
        else:
            print('ERRO! Digite uma opção válida.')
            continue


# ─── Cadastrar O Peso ─────────────────────────────────────────────────────────


def peso_pessoa(p):
    while True:
        peso_cadastro = str(input(peso)).replace(',', '.')    # Converte o input para string e troca a vírgula por ponto
        try:
            peso_cadastro = float(peso_cadastro)    # Tenta converter o input para float
            return peso_cadastro
        except (ValueError, KeyError):  # Caso ocorra algum erro na conversão
            print('ERRO! Digite um número real para o peso.')
            continue


# ─── Cadastrar A Altura ───────────────────────────────────────────────────────


def altura_pessoa(a):
    while True:
        altura_cadastro = str(input(altura)).replace(',', '.')   # Converte o input para string e troca a vírgula por ponto
        altura_cadastro = float(altura_cadastro)
        if altura_cadastro > 2.5:   # Verifica se a altura é maior que 2.5 metros
            print('ERRO! Digite uma altura válida.')
            continue
        try:
            altura_cadastro = float(altura_cadastro) # Tenta converter o input para float
            return altura_cadastro
        except (ValueError, KeyError): # Caso ocorra algum erro na conversão
            print('ERRO! Digite um número real válido para a altura, em metros.')
            continue


# ─── Cadastrar O Cpf ──────────────────────────────────────────────────────────


def validador_cpf(c):
    while True:
        cpf_cadastro = input(cpf).strip().replace(' ', '').replace('.', '').replace('-', '')    # Remove os espaços em branco da direita e da esquerda e realiza as trocas do replace
        if cpf_cadastro.isnumeric() and len(cpf_cadastro) == 11:    # Verifica se o cpf digitado só possui caracteres numéricos e se possui 11 caracteres
            cpf_cadastro = list(cpf_cadastro)   # Transforma em uma lista para a verificação seguinte
            for k, v in enumerate(cpf_cadastro):    # Verifica se todos os caracteres digitados foram numéricos e inteiros
                cpf_cadastro[k] = int(v)
            break
        elif len(cpf_cadastro) != 11:
            print('ERRO! O cpf precisa conter 11 digitos inteiros.')
            continue
        elif cpf_cadastro.isalpha() or cpf_cadastro.isalnum():
            print('ERRO! O cpf não pode conter letras.')
            continue

    # Declaramos duas variáveis que serão utilizadas para verificar se o cpf digitado é um cpf válido        
    digito1 = False
    digito2 = False

    # Realiza a primeira verificação do CPF
    multiplicacao1 = 10
    soma1 = 0
    for numero in cpf_cadastro[0:9]:
        soma1 += multiplicacao1 * numero
        multiplicacao1 -= 1
    soma1 = soma1 * 10 % 11
    if soma1 == 10:
        soma1 = 0
    if soma1 == cpf_cadastro[9]:
        digito1 = True
    else:
        digito1 = False

    # Realiza a segunda verificação do CPF
    multiplicacao2 = 11
    soma2 = 0
    for numero in cpf_cadastro[0:10]:
        soma2 += multiplicacao2 * numero
        multiplicacao2 -= 1
    soma2 = soma2 * 10 % 11
    if soma2 == 10:
        soma2 = 0
    if soma2 == cpf_cadastro[10]:
        digito2 = True
    else:
        digito2 = False

    # Se ambas as verificações passarem, retorna o CPF formatado para o formato xxx.xxx.xxx-xx
    if digito1 and digito2:
        cpf_cadastrado = str(cpf_cadastro).strip().replace(', ', '').removeprefix('[').removesuffix(']') # Remove as vírgulas e colchetes da lista
        return f'{cpf_cadastrado[0:3]}.{cpf_cadastrado[3:6]}.{cpf_cadastrado[6:9]}-{cpf_cadastrado[9:]}' # Retorna o cpf formatado
    else:
        print('O cpf não é válido, por favor digite um cpf válido.')
        return validador_cpf(cpf)  # Caso o cpf não seja válido, chama a função novamente


# ─── Cadastrar O Salário ──────────────────────────────────────────────────────


def salario_pessoa(s):
    while True:
        salario_cadastrar = input(salario)
        try:
            salario_cadastrar = float(salario_cadastrar)  # Tenta converter o salário em float
            return salario_cadastrar
        except (ValueError, KeyError):   # Caso ocorra algum erro na conversão
            print('ERRO! Digite apenas números reais para o salário.')
            continue


# ─── Armazenar Os Dados Na Tabela ─────────────────────────────────────────────


def cadastrar_pessoa():
    # Seleciona todas as linhas da tabela Pessoas ordenadas pelo ID_Pessoa
    cursor.execute("""SELECT * FROM Pessoas ORDER BY ID_Pessoa""")
    # Armazena o tamanho da lista retornada
    tamanho_lista = len(cursor.fetchall())

    if tamanho_lista == 0:  # Se a lista estiver vazia, o próximo ID será 1
        indice = 1
    else:   # Caso contrário, o próximo ID será o tamanho da lista + 1
        indice = tamanho_lista + 1

    cpf_cadastrado = validador_cpf(cpf)  # Obtém o cpf válido

    cursor.execute(f"""SELECT CPF FROM Pessoas WHERE CPF = '{cpf_cadastrado}'""")   # Seleciona o cpf da tabela Pessoas onde o cpf é igual ao cpf fornecido
    verificar_cpf = cursor.fetchall()   # Armazena a lista retornada
    if len(verificar_cpf) > 0:    # Se o tamanho da lista for maior que 0, o cpf já está cadastrado
        print(f'Usuário com o cpf {cpf_cadastrado} já está cadastrado.')
        return cadastrar_pessoa()   # Retorna para a função cadastrar_pessoa()
    else:
        pass

    # Obter as funções validadas
    nome_cadastrado = nome_pessoa(nome)  
    idade_cadastrada = idade_pessoa(idade)    
    sexo_cadastrado = sexo_pessoa(sexo)   
    peso_cadastrado = peso_pessoa(peso)   
    altura_cadastrada = altura_pessoa(altura)  
    imc_cadastrado = float(f'{peso_cadastrado / (altura_cadastrada ** 2):.2f}') # Calcula o IMC
    salario_cadastrado = salario_pessoa(salario)  

    print(f'{nome_cadastrado} cadastrado com sucesso.\n'
          f'Idade: {idade_cadastrada} anos.\n'
          f'Sexo: {sexo_cadastrado}.\n'
          f'Peso: {peso_cadastrado:.1f}Kg.\n'
          f'Altura: {altura_cadastrada}cm.\n'
          f'IMC: {imc_cadastrado}.\n'
          f'CPF: {cpf_cadastrado}.\n'
          f'Salário: R${salario_cadastrado:.2f}')

    dados = [indice, nome_cadastrado, idade_cadastrada, sexo_cadastrado, peso_cadastrado, altura_cadastrada,
             imc_cadastrado,
             cpf_cadastrado, f'{salario_cadastrado:.2f}']

    if len(dados) == 1:    # Se o tamanho da lista de dados for igual a 1, adiciona os dados
        pessoas_cadastradas.append(dados) # Adiciona os dados
    else:
        indice += len(pessoas_cadastradas) # Adiciona o tamanho da lista de pessoas cadastradas ao índice
        dados[0] = indice  # Atribui o índice ao primeiro elemento da lista dados
        pessoas_cadastradas.append(dados)

    while True:
        pergunta = str(input('Continuar cadastro? [S/N] ')).upper() # Pergunta se o usuário deseja continuar o cadastro
        if pergunta == 'S':
            print()
            return cadastrar_pessoa()
        elif pergunta == 'N':
            adicionar_pessoa_cadastro()
            print()
            break


# ─── Adicionar Ao Banco De Dados ──────────────────────────────────────────────


def adicionar_pessoa_cadastro(): 
    for idpessoa, nome, idade, sexo, peso, altura, imc, cpf, salario in pessoas_cadastradas:
        adicionar_pessoas = f"""INSERT INTO Pessoas(ID_Pessoa, Nome, Idade, Sexo, Peso, Altura, IMC, CPF, Salário)
        VALUES
        ({idpessoa}, '{nome}', {idade}, '{sexo}', {peso}, {altura}, {imc}, '{cpf}', {salario})""" # Comando SQL para adicionar os dados na tabela Pessoas
        cursor.execute(adicionar_pessoas)
    cursor.commit()
    pessoas_cadastradas.clear() # Limpa a lista de pessoas cadastradas


# ─── Exibir Todas As Pessoas Cadastradas ──────────────────────────────────────


def mostrar_pessoas_cadastradas():
    # Seleciona todos os dados da tabela Pessoas
    dados_pessoas = """SELECT * FROM Pessoas"""

    # Executa o comando SQL
    cursor.execute(dados_pessoas)

    # Pega todas as linhas da tabela
    linhas = cursor.fetchall()

    # Salva as alterações
    cursor.commit()

    print(f'A tabela tem ao todo {len(linhas)} cadastros.\n')
    tabela_ordenada = """SELECT * FROM Pessoas ORDER BY ID_Pessoa""" # Ordena a tabela pelo ID
    cursor.execute(tabela_ordenada)

    for linha in linhas:   # Imprime os dados
        print('ID: ', linha[0], end='  ')
        print('Nome: ', linha[1], end='  ')
        print('Idade: ', linha[2], end='  ')
        print('Sexo: ', linha[3], end='  ')
        print('Peso: ', linha[4], end='  ')
        print('Altura: ', linha[5], end='  ')
        print('IMC: ', linha[6], end='  ')
        print('CPF: ', linha[7], end='  ')
        print('Salário: ', linha[8], end='  \n')
    print()


# ─── Atualizar Algum Dado ─────────────────────────────────────────────────────


def atualizar_dado():
    cursor.execute("""SELECT ID_Pessoa FROM Pessoas ORDER BY ID_Pessoa""") # Seleciona todos os ID's da tabela Pessoas e ordena-os.
    linha = cursor.fetchall()

    print('1 - Nome\n2 - Idade\n3 - Peso\n4 - Salário\n5 - Aumentar o peso de todos os usuários\n6 - Para sair\n')
    opcao = input('Campo a atualizar: ')

    if opcao == '6':
        print('-' * 50)
        return

    while True:
        try:    # Verifica se a opção é um número inteiro.
            opcao = int(opcao)
            if opcao > 6 or opcao <= 0: # Verifica se a opção está dentro do intervalo de opções existentes.
                print('Digite uma opção válida.')
                continue
            break
        except (ValueError, KeyError):  # Caso não seja, pede para o usuário digitar novamente.
            print('Digite uma opção válida.')
            continue

    # ──────────────────────────────────────────────────────────────────────

    if opcao == 1:
        while True:
            pessoa_a_atualizar = input('ID da pessoa a atualizar: ')
            try:
                pessoa_a_atualizar = int(pessoa_a_atualizar) # Verifica se o ID é um número inteiro.
                if pessoa_a_atualizar > len(linha) or pessoa_a_atualizar <= 0: # Verifica se o ID está dentro do intervalo de ID's existentes.
                    print('Usuário não encontrado.')
                    continue
                else:
                    break
            except (ValueError, KeyError):
                print('Digite o número do ID da Pessoa corretamente.') # caso não seja, pede para o usuário digitar novamente.
                continue
        opcao = 'Nome'

        while True:
            dado_atualizado = input('Novo nome: ')
            if verificar_nome(dado_atualizado): # Verifica se o nome é válido.
                cursor.execute(
                    f"""UPDATE Pessoas SET {opcao} = '{dado_atualizado}' WHERE ID_Pessoa = {pessoa_a_atualizar}""") # Atualiza o nome.
                cursor.commit()
                break
            else:
                print('Nome inválido. Digite apenas letras alfabéticas.') # Caso o nome não seja válido, pede para o usuário digitar novamente.
                continue
    
    # ──────────────────────────────────────────────────────────────────────

    elif opcao == 2:
        while True:
            pessoa_a_atualizar = input('ID da pessoa a atualizar: ')
            try:
                pessoa_a_atualizar = int(pessoa_a_atualizar) # Verifica se o ID é um número inteiro.
                if pessoa_a_atualizar > len(linha) or pessoa_a_atualizar <= 0: # Verifica se o ID está dentro do intervalo de ID's existentes.
                    print('Usuário não encontrado.')
                    continue
                else:
                    break
            except (ValueError, KeyError): # Caso não seja, pede para o usuário digitar novamente.
                print('Digite o número do ID da Pessoa corretamente.')
                continue
        opcao = 'Idade'

        while True:
            dado_atualizado = input('Nova idade: ')
            try:
                dado_atualizado = int(dado_atualizado) # Verifica se a idade é um número inteiro.
                cursor.execute(
                    f"""UPDATE Pessoas SET {opcao} = {dado_atualizado} WHERE ID_Pessoa = {pessoa_a_atualizar}""") # Atualiza a idade.
                cursor.commit()
                break 
            except (ValueError, KeyError): # Caso não seja, pede para o usuário digitar novamente.
                print('Digite apenas números inteiros válidos.')
                continue

    # ──────────────────────────────────────────────────────────────────────

    elif opcao == 3:
        while True:
            pessoa_a_atualizar = input('ID da pessoa a atualizar: ')
            try:
                pessoa_a_atualizar = int(pessoa_a_atualizar)
                if pessoa_a_atualizar > len(linha) or pessoa_a_atualizar <= 0: # Verifica se o ID está dentro do intervalo de ID's existentes.
                    print('Usuário não encontrado.')
                    continue
                else:
                    break
            except (ValueError, KeyError): # Caso não seja, pede para o usuário digitar novamente.
                print('Digite o número do ID da Pessoa corretamente.')
                continue
        opcao = 'Peso'

        while True: 
            dado_atualizado = input('Novo peso: ') 
            try:
                dado_atualizado = int(dado_atualizado) # Verifica se o peso é um número inteiro.
                cursor.execute(
                    f"""UPDATE Pessoas SET {opcao} = {dado_atualizado} WHERE ID_Pessoa = {pessoa_a_atualizar}""") # Atualiza o peso.
                cursor.commit()
                cursor.execute(
                    f"""UPDATE Pessoas SET IMC = ROUND(Peso / POWER(Altura, 2), 2) WHERE ID_Pessoa = {pessoa_a_atualizar}""") # Atualiza o IMC.
                cursor.commit()
                break
            except (ValueError, KeyError): # Caso não seja, pede para o usuário digitar novamente.
                print('Digite apenas números inteiros válidos.')
                continue

    # ──────────────────────────────────────────────────────────────────────

    elif opcao == 4:
        while True:
            pessoa_a_atualizar = input('ID da pessoa a atualizar: ')
            try:
                pessoa_a_atualizar = int(pessoa_a_atualizar)
                if pessoa_a_atualizar > len(linha) or pessoa_a_atualizar <= 0: # Verifica se o ID está dentro do intervalo de ID's existentes.
                    print('Usuário não encontrado.')
                    continue
                else:
                    break
            except (ValueError, KeyError): # Caso não esteja, pede para o usuário digitar novamente.
                print('Digite o número do ID da Pessoa corretamente.')
                continue
        opcao = 'Salário'

        while True: # Verifica se o salário é um número real.
            dado_atualizado = input('Novo salário: ')
            try:
                dado_atualizado = float(dado_atualizado)
                cursor.execute(
                    f"""UPDATE Pessoas SET {opcao} = {dado_atualizado} WHERE ID_Pessoa = {pessoa_a_atualizar}""") # Atualiza o salário.
                cursor.commit()
                break
            except (ValueError, KeyError): # Caso não seja, pede para o usuário digitar novamente.
                print('Digite apenas números reais válidos.')
                continue

    # ──────────────────────────────────────────────────────────────────────

    elif opcao == 5:
        while True:
            aumento_peso = input('Quantos % deseja aumentar no peso de todos os usuários? ')
            try:
                aumento_peso = int(aumento_peso)
                aumento_peso = aumento_peso / 100
                cursor.execute("""SELECT ID_Pessoa, Peso, Altura, IMC FROM Pessoas""")
                pesos_pessoas = cursor.fetchall()
                for k, p in enumerate(pesos_pessoas):
                    peso_aumentado = p[1] * (1 + aumento_peso)
                    cursor.execute(f"""UPDATE Pessoas SET Peso = {peso_aumentado} WHERE ID_Pessoa = {p[0]}""")
                    cursor.commit()
                    cursor.execute(
                        f"""UPDATE Pessoas SET IMC = ROUND(Peso / POWER(Altura, 2), 2) WHERE ID_Pessoa = {p[0]}""")
                    cursor.commit()
                break
            except (ValueError, KeyError):
                print('Digite um valor inteiro válido.')
                continue


# ─── Remover Algum Dado ───────────────────────────────────────────────────────


def remover_cadastro():
    while True:
        while True:
            remover = input('Digite o índice do cadastro que deseja remover (caso queira cancelar, digite "Sair"): ').upper()
            # Verifica se o usuário quer cancelar a remoção
            if remover == 'SAIR':
                print()
                return
            # Verifica se o índice digitado é válido
            try:
                remover = int(remover)
                print(f'Dados de índice {remover} removidos.')
                break
            except (ValueError, KeyError):
                print('ERRO! Digite o número do índice correto.')
                break

        # Seleciona todos os dados da tabela Pessoas
        dados_pessoas = """SELECT * FROM Pessoas ORDER BY ID_Pessoa"""
        cursor.execute(dados_pessoas)
        linhas = cursor.fetchall()

        # Deleta o cadastro do índice digitado
        cursor.execute(f"""DELETE FROM Pessoas WHERE ID_Pessoa = {remover}""")
        cursor.commit()

        # Atualiza os índices dos cadastros restantes
        for linha in linhas[remover:]:
            cursor.execute(f"""UPDATE Pessoas SET ID_Pessoa = {linha[0] - 1} WHERE ID_Pessoa = {linha[0]}""")
            cursor.commit()


# ──────────────────────────────────────────────────────────────────────────────

nome = 'Nome: '
idade = 'Idade: '
sexo = 'Sexo [M/F]: '
peso = 'Peso (em kg): '
altura = 'Altura (em metros): '
cpf = 'CPF: '
salario = 'Salário: R$'
pessoas_cadastradas = []