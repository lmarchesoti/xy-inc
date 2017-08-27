# xy-inc
Teste de programação

É necessário ter instalado *docker* e *docker-compose*.
Para executar os testes é necessário o pacote *nose*.

# Test
Execute os testes da aplicação com o comando:

*sudo docker-compose -p tests run -p 3000 web nosetests*

Ao finalizar a execução dos testes execute:

*sudo docker-compose -p tests down*

Para finalizar os containers de teste.

# Run
Execute a aplicação com o comando:

*sudo docker-compose up*

