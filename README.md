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

Ela estará acessível no endereço localhost:5000.
É uma aplicação escrita em Python utilizando Flask e MongoEngine (ODM para Mongo DB).
Todos os comandos possíveis são acessados pelo endereço raiz (localhost:5000).
Uma requisição POST com os parâmetros *name*, *x* e *y* cria um POI com estas informações.
Uma requisição GET sem parâmetros lista todos os POIs disponíveis.
Uma requisição GET com os parâmetros *x*, *y* e *dmax* lista todos os POIs presentes a uma distância máxima *dmax* do ponto descrito pelo ponto (*x*, *y*).

O servidor da aplicação pode ser finalizado pressionando Ctrl+C no terminal da aplicação e posteriormente com o comando:

*sudo docker-compose down --volumes*
