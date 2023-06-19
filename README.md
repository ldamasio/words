# words3

## Words3 é um programa para backend em Python.

Words3 usa o Flask para facilitar a implementação da API na linguagem Python.

Por razões de segurança, faz uso de uma Interface de Porta de Entrada do Servidor Web (WSGI).

Enfim, o Words3 é uma API com as seguintes rotas:

## Rotas da API

[POST] /vowel_count -- conta vogais em palavras
Requisição: {"words": ["batman", "robin", "coringa"]}
Resposta: {"batman": 2, "robin": 2, "coringa": 3}

[POST] /sort -- ordena palavras em um array, aceitando ordenação reversa
Requisição: {"words": ["batman", "robin", "coringa"], "order": "asc"}
Resposta: ["batman", "coringa", "robin"]

Requisição: {"words": ["batman", "robin", "coringa"], "order": "desc"}
Resposta: ["robin", "coringa", "batman"]

## Validações da API e menssagens de erro

Exemplos de requisições inválidas:

Sem application/json no content-type: 
> Oops, got an error! 415 Unsupported Media Type: Did not attempt to load JSON data because the request Content-Type was not 'application/json'.

Requisição não utiliza método POST: 
> Oops, got an error! 405 Method Not Allowed: The method is not allowed for the requested URL.

Rotas inexistentes:
> Oops, got an error! 404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.

## Deployment e Online Demo

Fizemos uso da UOL Cloud para prover uma infraestrutura para nossa versão de demonstração.

Configramos o seguinte domínio para facilitar o acesso: words3.robson.srv.br

Essas duas rotas podem ser acessadas pelo navegador web:

http://words3.robson.srv.br:5000/health

http://words3.robson.srv.br:5000/docs


