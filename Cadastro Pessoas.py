import cadastro_pessoa.funcao_cadastro as fc
import pyodbc

# Dados de conexão com o banco de dados
dados_conexao = (
    'Driver={SQL Server};' # Driver do SQL Server
    'Server=host\SQLEXPRESS;' # Nome do servidor
    'Database=CadastroPessoas;' # Nome do banco de dados
)

# Cria a conexão
conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida'), print()

# Cria o cursor
cursor = conexao.cursor()

# Verifica se a tabela existe
tabela = 'Pessoas'
verificar_tabela = f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{tabela}'"
cursor.execute(verificar_tabela)
if cursor.fetchone()[0]: # fetchone()[0] retorna o primeiro valor da primeira linha da tabela
    print(f"A tabela {tabela} existe no banco de dados."), print()
else:
    print(f"A tabela {tabela} não existe no banco de dados, mas será criada agora."), print()
    # Caso não exista, cria a tabela
    cursor.execute("CREATE TABLE dbo.Pessoas(ID_Pessoa int, Nome char(26), Idade int, Sexo char(2), Peso float, Altura float, IMC float, CPF char(16), Salário float) GO")
    cursor.commit()

while True:
    print('1 - Novo cadastro')
    print('2 - Visualizar pessoas cadastradas')
    print('3 - Atualizar algum dado')
    print('4 - Remover cadastro')
    print('5 - Encerrar')
    print('6 - Apagar tabela completa\n')
    opcao = input('Escolha uma opção: ')
    print('-' * 50, '\n')

    try:
        opcao = int(opcao) # Verifica se a opção é um número inteiro

        match opcao:  # Python v3.10
            case 1:
                fc.cadastrar_pessoa()

            case 2:
                fc.mostrar_pessoas_cadastradas()

            case 3:
                fc.atualizar_dado()

            case 4:
                fc.remover_cadastro()

            case 5:
                print('Programa finalizado.')
                break

            case 6:
                confirmacao = input('Tem certeza que deseja apagar todos os dados da tabela? (S/N) ').upper()
                print()
                if confirmacao != 'S':
                    print('Operação cancelada.')
                    continue

                apagar_tabela = """DELETE FROM Pessoas""" # Apaga todos os dados da tabela
                cursor.execute(apagar_tabela)
                cursor.commit()
                print('Tabela apagada com sucesso.')
                print('-' * 50, '\n')

    except KeyboardInterrupt: # Caso o usuário aperte Ctrl + C
        continue 

    except (ValueError, KeyError): # Caso o usuário digite uma opção inválida
        print('Digite uma opção válida.')
        continue