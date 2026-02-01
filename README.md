# Resumo
A gripe (influenza) é uma doença respiratória infecciosa caracterizada por transmissão rápida e recorrência sazonal. Modelos epidemiológicos são frequentemente utilizados para compreender sua dinâmica de propagação. Neste trabalho, apresentamos uma implementação computacional discreta do modelo SIR (Suscetíveis–Infectados–Recuperados), com o objetivo de explorar como regras locais simples, quando iteradas em um sistema computacional finito, produzem padrões epidêmicos globais. O foco do estudo não é a previsão quantitativa da gripe, mas a análise conceitual da modelagem epidemiológica sob restrições computacionais explícitas. Os resultados evidenciam a emergência de comportamentos típicos de surtos epidêmicos e destacam os limites inerentes à abstração computacional.


## Introdução

A gripe é uma doença viral amplamente disseminada, responsável por surtos anuais que impactam sistemas de saúde em todo o mundo. Sua transmissão ocorre principalmente por contato direto e aerossóis, tornando-a um exemplo clássico para o estudo de fenômenos epidemiológicos em populações humanas.
A modelagem matemática da gripe tradicionalmente utiliza equações diferenciais contínuas para descrever a evolução temporal dos indivíduos suscetíveis, infectados e recuperados. Entretanto, a implementação computacional desses modelos exige discretizações que alteram a forma como o fenômeno é representado. Dessa forma, a epidemiologia computacional não deve ser vista apenas como uma ferramenta de previsão, mas também como um campo de investigação sobre os limites e possibilidades da computação aplicada a sistemas complexos.
Neste trabalho, a gripe é adotada como fenômeno epidemiológico de referência para a implementação de um modelo SIR discreto. O objetivo é refletir sobre o comportamento emergente do sistema e sobre as simplificações necessárias para tornar o fenômeno computável.


## Modelo e Metodologia Computacional
O modelo SIR divide a população em três compartimentos: suscetíveis (S), infectados (I) e recuperados (R). No contexto da gripe, indivíduos suscetíveis podem contrair o vírus ao entrar em contato com indivíduos infectados, enquanto indivíduos infectados eventualmente se recuperam e deixam de participar da transmissão.
A população total é considerada constante, homogênea e bem misturada. O tempo é tratado de forma discreta, em passos que representam unidades temporais finitas. Em cada iteração do algoritmo, duas regras governam a dinâmica do sistema: (i) uma fração dos suscetíveis torna-se infectada em função do número de indivíduos infectados; (ii) uma fração dos infectados se recupera.
Essa abordagem evita o uso explícito de equações diferenciais contínuas e torna o processo computacional transparente, permitindo observar diretamente como o estado do sistema é atualizado a cada passo temporal. O código-fonte completo da simulação está disponível em repositório público no GitHub, cujo link é fornecido ao final deste artigo.


## Resultados
A simulação computacional do modelo SIR aplicado à gripe apresenta um crescimento inicial do número de infectados, seguido por um pico epidêmico e posterior declínio, conforme ilustrado na Figura 1. Esse comportamento é característico de surtos de gripe em populações fechadas e emerge naturalmente da aplicação iterativa das regras locais do modelo, sem que o pico seja explicitamente programado no código.
O pico de infectados não é imposto explicitamente no código, mas surge como consequência da interação entre a redução progressiva de indivíduos suscetíveis e o aumento do número de recuperados. Observa-se ainda que pequenas variações nos parâmetros de infecção e recuperação resultam em diferenças significativas na altura e no momento do pico epidêmico.
Esses resultados ilustram como sistemas computacionais simples podem reproduzir padrões qualitativos observados em fenômenos epidemiológicos reais, mesmo quando baseados em abstrações extremas.

![123](https://github.com/user-attachments/assets/3272ba70-2ee0-4fbd-9df9-a6cb1c84efc8)


## Discussão
Apesar de sua utilidade exploratória, o modelo apresenta limitações importantes. A ausência de estrutura espacial, a suposição de população homogênea e a inexistência de mudanças comportamentais reduzem a capacidade do modelo de representar com fidelidade a dinâmica real da gripe.
Entretanto, tais limitações não devem ser interpretadas apenas como deficiências epidemiológicas. Elas decorrem diretamente da necessidade de manter o sistema computável em uma máquina finita, operando em tempo discreto e sob regras claramente definidas. A simplificação do fenômeno é, portanto, uma condição necessária para a simulação computacional.
Nesse sentido, o modelo SIR discreto funciona como um laboratório conceitual, no qual é possível investigar como escolhas computacionais moldam a representação de processos biológicos complexos.


## Conclusão
O modelo computacional discreto apresentado neste trabalho demonstra como a propagação da gripe pode ser explorada a partir de regras simples e iterativas. Embora não tenha como objetivo realizar previsões epidemiológicas precisas, a simulação evidencia a emergência de padrões globais típicos de surtos infecciosos.
A análise reforça a ideia de que a epidemiologia computacional deve ser compreendida não apenas como uma ferramenta aplicada, mas como uma linguagem para pensar sistemas complexos sob restrições computacionais. Assim, o modelo SIR discreto contribui para a compreensão conceitual dos limites e possibilidades da modelagem computacional de doenças infecciosas.
Disponibilidade do Código
O código-fonte completo da simulação está disponível em:

