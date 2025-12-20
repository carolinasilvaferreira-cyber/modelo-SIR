## Introdução

A modelagem matemática e computacional desempenha um papel central na compreensão da
dinâmica de doenças infecciosas. No entanto, todo modelo é uma abstração da realidade,
limitada tanto por escolhas conceituais quanto pelas capacidades da computação.

Neste trabalho, utilizamos um modelo SIR discreto para explorar a propagação de uma doença
em uma população fechada. A escolha por um modelo discreto reflete a natureza finita e
iterativa dos sistemas computacionais, aproximando a simulação da forma como algoritmos
operam em máquinas reais.

## Descrição do Modelo

A população é dividida em três compartimentos:

- **S (Suscetíveis)**: indivíduos que podem contrair a doença
- **I (Infectados)**: indivíduos que transmitem a doença
- **R (Recuperados)**: indivíduos que não participam mais da transmissão

O tempo é tratado em passos discretos (dias). A cada iteração, regras locais determinam a
transição entre os compartimentos, baseadas em taxas de infecção e recuperação.

Diferentemente de abordagens contínuas baseadas em equações diferenciais, aqui o modelo é
implementado diretamente como um algoritmo iterativo, explicitando o processo computacional.

## Metodologia Computacional

A simulação inicia com um único indivíduo infectado em uma população de 100.000 pessoas.
Em cada passo temporal:

- Uma fração dos suscetíveis torna-se infectada, proporcional ao número de contatos com
infectados.
- Uma fração dos infectados se recupera.

Essas regras são aplicadas de forma determinística, permitindo observar como padrões
globais emergem a partir de regras simples.

## Resultados

A simulação apresenta um crescimento inicial rápido do número de infectados, seguido por
um pico epidêmico e posterior declínio. Esse comportamento não foi explicitamente
programado, mas emerge da interação entre as regras de infecção e recuperação.

Observa-se também a redução contínua do número de suscetíveis e o aumento monotônico dos
recuperados, refletindo a dinâmica típica de epidemias em populações fechadas.

## Discussão e Limitações

Apesar de capturar padrões gerais, o modelo apresenta limitações importantes:

- Assume população homogênea e bem misturada
- Não considera estrutura espacial ou redes de contato
- Ignora mudanças comportamentais e intervenções externas
- Utiliza parâmetros constantes no tempo

Essas limitações não são apenas epidemiológicas, mas também computacionais. A necessidade
de manter o sistema finito, discreto e computável impõe simplificações que afastam o modelo
da complexidade do mundo real.

Assim, o modelo deve ser interpretado como uma ferramenta exploratória, e não preditiva.

## Conclusão

O modelo SIR discreto implementado demonstra como sistemas computacionais simples podem
produzir comportamentos complexos e informativos. A abordagem adotada reforça a importância
de compreender não apenas os resultados da simulação, mas também os limites conceituais e
computacionais que moldam esses resultados.

Este trabalho evidencia que a modelagem epidemiológica computacional é tanto um exercício
de abstração quanto de reflexão crítica sobre o que pode — e o que não pode — ser 
representado por algoritmos.

![modeloSIR](https://github.com/user-attachments/assets/fa76bdc1-e30f-4e7e-94dc-22f7b56a53d0)

