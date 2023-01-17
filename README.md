Manipulação de banco de dados com Python utilizando o pacote pyodbc para realizar a conexão com o SQL Express, com as seguintes informações: nome, idade, sexo, altura, peso, cpf e salário. Cada dado fornecido é armazenado na tabela, e o usuário pode realizar as seguintes operações: inserir, remover, alterar e consultar. Além de calcular o IMC de cada pessoa automaticamente com base na altura e peso fornecidos pelo usuário.

Foram feitos tratamentos de exceções para evitar que o usuário insira dados inválidos, como letras em campos numéricos, ou números em campos de texto. Também foi feito um tratamento para evitar que o usuário insira um CPF já existente no banco de dados ou que não seja válido.

Pacotes necessários: `pyodbc`