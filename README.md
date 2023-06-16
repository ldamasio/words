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

