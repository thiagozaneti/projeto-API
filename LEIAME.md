Esta API, composta por três arquivos (app.py, funcoes.py e random_data.py), oferece funcionalidades para consulta e análise de dados de pessoas fictícias.

Arquitetura:

app.py:
Define as rotas da API e as chamadas das funções de negócio.
Recebe requisições HTTP, processa-as e retorna respostas no formato JSON.
funcoes.py:
Implementa as funções de negócio da API.
Acessa e manipula os dados de pessoas fictícias.
Retorna os resultados das operações para o app.py.
random_data.py:
Armazena um conjunto de 1.000 dados de pessoas fictícias.
Fornece os dados para as funções de negócio do arquivo funcoes.py.

Esta API fornece acesso a dados de pessoas fictícias, permitindo consultas sobre suas idades, salários e outras características.

Funcionalidades:

Obter lista de todas as pessoas (/)
Obter contagem de pessoas com mais de 50 anos (/idades)
Obter contagem e porcentagem de pessoas com salário acima de R$ 2.000,00 (/salarios)
Obter os três maiores salários (/maiores_salarios)
Obter média de salário de todas as pessoas (/media_salarios)
Obter média de salário e informações sobre o sexo mais e menos frequente (/medias)
Obter média de idade e informações sobre o sexo mais e menos frequente por sexo (/intervalo_de_idade/<string:sexo>)
Métodos HTTP suportados:

GET
Requisições:

Todas as requisições retornam um objeto JSON com a chave Status indicando o código de status HTTP (200 para sucesso) e outras chaves contendo os dados específicos da requisição.
A requisição /intervalo_de_idade/<string:sexo> espera um parâmetro de rota sexo com valor f ou m para feminino ou masculino, respectivamente.
Exemplos de uso:

Obter lista de todas as pessoas:
curl http://localhost:5000/
Obter contagem de pessoas com mais de 50 anos:
curl http://localhost:5000/idades
Obter média de salário e informações sobre o sexo mais e menos frequente:
curl http://localhost:5000/medias
Obter média de idade e informações sobre o sexo mais e menos frequente para mulheres:
curl http://localhost:5000/intervalo_de_idade/f