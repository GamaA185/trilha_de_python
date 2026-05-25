# 🐍 Trilha de Python

Repositório desenvolvido para estudos e prática de programação em Python, abordando conceitos fundamentais da linguagem, versionamento com Git e organização de projetos.

## Conteúdos abordados

- Variáveis e tipos de dados
- Entrada e saída de dados
- Operações matemáticas
- Estruturas condicionais
- Estruturas de repetição
- Funções
- Manipulação de arquivos
- Git e GitHub

### Semana 1:
Foi-se criada uma calculadora com uso voltado p/ nômades digitais (ou outras pessoas) que precisam de auxílio para organizar algumas de suas despesas.

## Perguntas teóricas da Semana 1

### Qual a diferença entre o comando git add . e git commit -m "mensagem"?

O git add . adiciona todas as alterações, novos arquivos e exclusões da pasta atual para a Staging Area. Tipo uma seleção prévia do que será salvo no próximo commit, enquanto o git commit -m "mensagem" salva permanentemente no histórico local do repositório todas as alterações que estavam na Staging Area (área de preparação), criando um ponto de restauração acompanhado de uma mensagem descritiva.

### Por que é necessário realizar o casting (conversão de tipo) ao usar a função input() em Python para cálculos matemáticos?

A função input() retorna os dados digitados pelo usuário no formato str (texto), mesmo quando números são informados.

### O que acontece se tentarmos somar uma variável do tipo str com uma do tipo float?

O Python gera um erro do tipo TypeError. Ele não permite operações entre tipos incompatíveis sem fazer a devida conversão antes.

## Semana 1 concluída 😉

#### --------------------------------------------------------------------------------------------------------------------------------------------------------

### Semana 2
Foi-se criado um protótipo p/ um tipo de Jogo de Carta Colecionável (Trading Card Game) que simula um duelo entre dois montros.

## Perguntas teóricas da semana 2

## Qual é a principal diferença prática entre usar um laço for e um laço while em Python? Por que o while foi a melhor escolha para este duelo?
O laço for é utilizado quando sabemos quantas vezes uma repetição acontecerá. Já o while é utilizado quando a repetição depende de uma condição.
No duelo, o while foi a melhor escolha porque não há o conhecimento acerca de quantos turnos serão necessários até que um dos monstros tenha o HP zerado. É bem mais fácil, neste caso, usar while do que usar for.

## Para que serve a palavra-chave return dentro de uma função? O que acontece se uma função fizer um cálculo matemático mas não possuir o return?
Serve p/ devolver um valor produzido pela função. Sem o return, a função pode até realizar cálculos internamente, mas o resultado não poderá ser reutilizado em outras partes do programa, e isso resulta em que o Python responde automaticamente None.

## O que é um "Loop Infinito" e como podemos evitá-lo ao construir uma estrutura while?
Um loop infinito acontece quando a condição de parada de um while nunca é satisfeita, e pode-se evitar isso garantindo que alguma variável seja alterada dentro do laço, permitindo que a condição eventualmente se torne falsa.

## Semana 2 concluída 😉
