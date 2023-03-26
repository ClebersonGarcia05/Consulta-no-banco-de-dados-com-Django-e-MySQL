![image](https://i0.wp.com/niwakatech.info/wp-content/uploads/2021/09/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A%E3%81%AE%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%81%AE%E3%82%B3%E3%83%94%E3%83%BC-1.png?fit=2240%2C1260&ssl=1)

# PROJETO CRUD MySQL COM PYTHON e Django.

Projeto desenvolvido para demonstrar meu conhecimento na área de integração de linguagem backend com banco de dados. O Objetivo deste projeto é:

• Adicionar, alterar, excluir dados no banco de dados através da interface adiministrativa do Django de forma simples e objetiva.

• Listar pedidos por usuário que solicitou.

•É possível ordenar por o tipo de informação, nome, item, email, telefone
# TECNOLOGIAS UTILIZADAS:

• PYTHON

• DJANGO

• MySQL

• Docker

Foi utilizado o framework Django para a realização do projeto devido a sua fácil conexão e manipulado do banco de dados e por se tratar de um framework robusto caso necessário a configuração ou a utilização de outras técnologias juntamente a ele.

# REQUISITOS:

Para conseguir rodar esse código localmente, será necessário ter instalado e configurado o docker em sua maquina. Após execute os seguintes comandos abaixo:

```python
docker-compose build
docker-compose up -d
docker-compose run api python3 manage.py makemigrations #criar migrações
docker-compose run api python3 manage.py migrate #migrar para o banco de dados
docker-compose run api python3 manage.py createsuperuser #criar super usuário
```

O último comando é para a criação de um super usuário para acesso na interface administrativa, deverá colocar ususário, e-mail e senha.

Após isso a aplicação estará rodando em localhost:8000

# DESAFIOS:

## 1º: Configuração do docker para rodar Django + MySQL
As configurações inseridas estavam dando erro devido ao nome da pasta estar diferente da com que estava localmente, foi necessário trocar o nome da pasta na configuração.

## 2º: Valor total do order
A coluna toal_value não estava recebendo a multiplicação entre o item_price e item_quantity, para resolver o problema foi necessário fazer um def save customizado onde o objeto total_value recebe a multiplicação após a criação do pedido. 

## 3º: Testes Unitários
Os testes unitários estavam apresentando erros devido ao def save,pois o max_digts do total_value estava pequeno para a quantidade de digitos armazenados se necessário, para resolver o problema foi necessário aumentar a quantidade de dígitos e realizar a migração novamente.


# Bibliotecas utilizadas

Foi utilizada as bibiliotecas do coverage, model_mommy para realizar os testes unitários, o coverage ajuda a verificar o que precisa ser testado e o model_mommy cria um objeto da respectiva classe que vai ser testada para verificar se está retornando o resultado esperado.

Para realizar o teste unitário é só rodar o comando abaixo:
```python
docker-compose run api coverage run manage.py test
docker-compose run api coverage report
```

A última linha de comando retornará uma tabela indicanto qual a porcentagem que o programa foi testado.

Nesse caso pedi para o coverage analisar somente a parte de banco de dados, tirando o teste da parte de frontend.

Para a conexão do Django com o Banco de dados MySQL foi utilizada a biblioteca mysqlclient.
