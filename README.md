# Ponderada Caso de Teste

## Descrição

O projeto consiste em uma aplicação web simples que integra um frontend básico em HTML/CSS com um backend em Python utilizando o módulo `http.server`. A aplicação exibe uma página com um botão que, ao ser clicado, faz uma requisição a uma rota de API `/api/dados` que retorna uma mensagem JSON.

## Estrutura do Projeto

```
/projeto
 ├── /backend
 ├──────  server.py
 ├──────  /tests 
 ├───────────  test_server.py  
 ├── /frontend
 ├──────  index.html
 ├──────  style.css  
/README.md 
```

## Desenvolvimento

### Backend:
- Implementado um servidor HTTP com as rotas:
  - `/`: Serve o `index.html`.
  - `/style.css`: Serve o arquivo de estilo CSS.
  - `/api/dados`: Retorna uma resposta JSON simulando uma API simples.

### Frontend:
- Página `index.html` com botão que faz requisição `fetch()` para `/api/dados`.
- Estilização básica com `style.css`, utilizando um `card` com título, botão e espaço para resposta da API.

## Testes Unitários

Foram desenvolvidos dois testes automáticos no arquivo `test_server.py`, localizados em `backend/tests/`.

### O que cada teste faz:

**test_get_html**  
   Verifica se a rota `/` está funcionando corretamente, garantindo que o servidor responde com o status HTTP 200 (OK) ao acessar a página inicial.
- Objetivo: Verificar se a página HTML principal está sendo servida corretamente.

- Pré-condição: O servidor precisa estar rodando em http://localhost:8000.

- Procedimento de teste: Realizar uma requisição GET para /.

- Resultado esperado: O status da resposta deve ser 200 (OK).

- Resultado obtido: O teste retornou o status 200 com sucesso.

- Pós-condição: O HTML da página principal foi carregado corretamente.

**test_get_css**  
   Verifica se o arquivo de estilo `/style.css` está sendo servido corretamente, testando tanto o status HTTP 200 quanto se o cabeçalho `Content-Type` retornado é `text/css`.
   - Objetivo: Verificar se o arquivo CSS está sendo servido corretamente.

- Pré-condição: O servidor precisa estar rodando em http://localhost:8000.

- Procedimento de teste: Realizar uma requisição GET para /style.css.

- Resultado esperado: O status da resposta deve ser 200 (OK) e o cabeçalho Content-Type deve ser text/css.

- Resultado obtido: O teste retornou o status 200 e o Content-Type como text/css.

- Pós-condição: O CSS da aplicação foi carregado corretamente.

## Como rodar o projeto

### Passo 1: Subir o servidor

No terminal, navegue até a pasta do backend:

```bash
cd projeto/backend
```

Depois, reinicie o servidor:
```bash
python server.py
```
O servidor estará disponível em:  
> **[http://localhost:8000/](http://localhost:8000/)**  


### Passo 2: Rodar os testes

Em outro terminal, na mesma pasta backend, execute:

```bash
python -m unittest tests/test_server.py
```

Os testes serão executados e o resultado aparecerá no terminal.
No caso dos meus testes, as duas abordagens testadas foram validadas, ou seja, os testes passaram com sucesso.

## Observação
- Todo o projeto foi desenvolvido apenas com módulos nativos do Python, não sendo necessário instalar dependências externas.
- O objetivo foi construir uma aplicação simples e funcional, com cobertura de testes nas rotas principais.