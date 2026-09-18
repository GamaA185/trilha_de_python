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


### Semana 3
Foi-se criado um programa que visa processar informações como nome de reagente, pureza de cada frasco e código do lote, identificar os tipos únicos de reagentes disponíveis e automatizar a seleção de frascos adequados para experimentos que exigem elevada pureza.

## Perguntas teóricas da semana 3

## Levando em consideração a estrutura do nosso inventário, por que seria incorreto usar a função dict() para transformar o resultado do nosso zip() em um dicionário, utilizando o nome do reagente como "Chave" e o lote como "Valor"?
Seria incorreto utilizar dict() porque existem reagentes repetidos associados a diferentes lotes. Como as chaves do dicionário devem ser únicas, dados seriam perdidos.

## O que a função zip() gera na memória do Python antes de usarmos a função list() para forçar a visualização dos dados?
A função zip() gera um objeto iterador do tipo zip object. Os dados só são materializados quando utilizamos list().

## Observando o seu código final, de que forma o List Comprehension substitui a necessidade de criar uma lista vazia e usar a estrutura de repetição for tradicional acompanhada do método .append()?
O List Comprehension substitui a criação de umalista vazia e o uso de append(), realizando afiltragem e construção da lista em uma única expressão.

## Semana 3 concluída 😉


### Semana 4
Programa capaz de automatizar o versionamento de diretórios vazios em um repositório Git. O algoritmo percorre os diretórios do projeto, cria automaticamente arquivos .gitkeep em diretórios vazios, remove esses arquivos quando o diretório deixa de ser vazio e registra todas as alterações em um arquivo log.json, ignorando completamente o diretório logs. (deve ter erros)

## Perguntas teóricas da Semana 4

## Qual a diferença entre json.dump() e json.dumps()?
A função json.dump() grava um objeto Python diretamente em um arquivo no formato JSON. Já a função json.dumps() converte um objeto Python em uma string no formato JSON, permitindo que ela seja armazenada ou manipulada antes de ser salva.

## Qual a diferença entre json.load() e json.loads()?
A função json.load() lê um arquivo JSON e converte seu conteúdo para um objeto Python. Já a função json.loads() recebe uma string contendo um JSON e a transforma em um objeto Python correspondente.

### Outras semanas

## Projeto — Reator Flexível: CSTR / Batch com Cinética de Segunda Ordem

Como projeto próprio, foi-se desenvolvido um simulador de reator líquido ideal com possibilidade de operação em Batch ou CSTR, aplicado à rede de reações:

**A + B ⇌ C → I → P**

O modelo considera uma primeira etapa elementar e reversível, de segunda ordem na direção direta, seguida por etapas elementares irreversíveis de primeira ordem. O programa também incorpora a dependência das constantes cinéticas com a temperatura por meio da equação de Arrhenius e um balanço de energia considerando o calor das reações e a troca térmica com uma camisa.

O código foi estruturado utilizando `dataclass` para organização dos parâmetros do reator e bibliotecas científicas do Python, incluindo NumPy, Pandas, Matplotlib e SciPy. A integração numérica do sistema de equações diferenciais ordinárias é realizada com `solve_ivp`, utilizando o método BDF, adequado para sistemas que podem apresentar comportamento rígido (stiff).
O projeto permite analisar a evolução temporal das concentrações de A, B, C, I e P, além da temperatura do sistema. Ao final da simulação, são calculados parâmetros como conversão aparente de A, temperatura máxima, maior acúmulo do intermediário I e as constantes cinéticas na temperatura final.

## Teste simples - Reator Batelada Ideal (Isotérmico)

Este projeto apresenta um teste básico de simulação cinética utilizando a biblioteca Overreact em Python. O objetivo é verificar a implementação de uma reação simples e visualizar a evolução temporal das concentrações das espécies.

O sistema considerado é:

**Ciclopropano → Propeno**

A reação é modelada como uma etapa irreversível de primeira ordem. O mecanismo é definido diretamente no Overreact por meio de parse_reactions.

**Parâmetros**

A constante cinética utilizada no teste é:

k = 1,5 × 10⁻⁴ s⁻¹

correspondente a T = 763 K no exemplo. A condição inicial considera concentração unitária de ciclopropano e concentração inicial nula de propeno:

Ciclopropano: 1 mol L⁻¹
Propeno: 0 mol L⁻¹

A simulação é realizada entre 0 e 5 × 10⁴ s.

**Método numérico**

A integração das equações diferenciais é realizada utilizando o método Radau, com:

atol = 1 × 10⁻¹⁰
rtol = 1 × 10⁻⁸

O uso de um solver adequado para sistemas de equações diferenciais permite acompanhar a variação das concentrações ao longo do tempo.

**Visualização**

Ao final da simulação, o código gera um gráfico das concentrações de ciclopropano e propeno em função do tempo.

O resultado esperado é a diminuição progressiva da concentração de ciclopropano acompanhada pelo aumento da concentração de propeno.

**Objetivo do projeto**

Este código funciona como um teste introdutório do Overreact, servindo para verificar o fluxo básico:

definição da reação → constante cinética → geração das equações diferenciais → integração numérica → visualização dos resultados.

Ele também serve como uma ponte entre os conceitos de cinética química e a utilização de ferramentas computacionais para Engenharia Química.
