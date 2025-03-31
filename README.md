# Movie_catalog
Functional Programing project / Projeto de programação funcional 

# Projeto de Programação Funcional

## Nome: Guilherme De Bernardi  
**Matrícula:** 2318122  

## Documento de Requisitos

## 1. Introdução
Este documento descreve os requisitos do **Movie Catalog**, que permite o cadastro, avaliação e recomendação de filmes. O objetivo é fornecer um programa para usuários cadastrarem filmes, avaliarem e receberem recomendações personalizadas.

## 2. Definição de Papéis
**Desenvolvedor:** Guilherme De Bernardi  


---

## 3. Requisitos Funcionais

### 3.1 Cadastro de Filmes
O sistema deve permitir o cadastro de filmes com os seguintes atributos:
- **Título**
- **Diretor**
- **Gênero**
- **Ano de lançamento**
- Cada filme cadastrado recebe um **ID único**.

### 3.2 Cadastro de Usuários
O sistema deve permitir o cadastro de usuários com os seguintes atributos:
- **Nome**
- **ID único** gerado automaticamente

### 3.3 Avaliação de Filmes
- O sistema deve permitir que usuários avaliem filmes cadastrados.
- As avaliações devem ser feitas com notas de **1 a 5 estrelas**.
- Cada avaliação deve ser vinculada a um **usuário e a um filme**.

### 3.4 Listagem de Filmes
O sistema deve permitir a **listagem dos filmes** cadastrados no catálogo.

### 3.5 Filtragem de Filmes
O sistema deve permitir a **filtragem de filmes** com base em diferentes critérios, como:
- **Gênero**
- **Diretor**
- **Ano de lançamento**

### 3.6 Recomendações de Filmes
O sistema deve recomendar filmes a um usuário com base nas avaliações feitas.
Os critérios de recomendação incluem:
- **Gêneros** de filmes bem avaliados pelo usuário
- **Diretores** cujos filmes foram bem avaliados pelo usuário

### 3.7 Exibição de Filmes Populares
O sistema deve listar os **filmes mais bem avaliados**, levando em consideração a média de avaliações.

### 3.8 Sugestão de Filmes Similares
O sistema deve sugerir **filmes similares** com base no **gênero** e no **diretor** do filme consultado.

### 3.9 Exibição de Detalhes de Filmes
O sistema deve permitir a **consulta dos detalhes** de um filme específico, incluindo:
- **Título**
- **Diretor**
- **Gênero**
- **Ano de lançamento**
- **Média de avaliações**
- **Número total de avaliações**

---

## 4. Requisitos Não-Funcionais
- O sistema deve fornecer **mensagens claras** em caso de erro.
- As operações devem ser **fáceis de entender e executar**.
- O sistema deve ser capaz de **processar a adição e consulta de filmes** de forma eficiente.
- A recomendação de filmes deve ser **gerada rapidamente**.
- O código deve seguir **boas práticas de desenvolvimento** para facilitar futuras manutenções.
- O uso de **programação funcional** deve ser destacado no código.

---

## 5. Uso de Programação Funcional
O código faz uso de conceitos de **programação funcional** nos seguintes pontos:
- **Uso de Closure:** Para gerar IDs unicos tanto para os filmes quanto para usuários.
- **Uso de Funções de Ordem Superior:** Métodos como `filter_movies` utilizam funções como argumentos.
- **Uso de Lambda Functions:** Funções lambda são utilizadas para filtragem e ordenação de dados.
- **Uso de List Comprehension:** Para a formatação dos filmes listados.

---
## 6. Sobre os Arquivos
`catalog.py`: O script define um classe MovieCatalog que tem todas as funcionalidades sitadas a cima, servindo de biblioteca para importa a classe e sua funcionalidades.  
`Catalog_test.py`: O script da um caso de uso para o codigo e testa as funcionalidades.

## 7. Link
**Disponível no repositório GitHub:** [GitHub - Movie Catalog](https://github.com/Guilhermedbs/Movie_catalog.git)
