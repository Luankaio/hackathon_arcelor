# Pitch do protótipo v3 — VoltMap

Apresentação para a ArcelorMittal Pecém, no contexto do hackathon de eficiência energética. Duração sugerida: 5 minutos. Nome adotado: **VoltMap**.

Cada “tela” abaixo é um slide. A v3 reorganiza a v2 em quatro blocos: **oportunidade** (720 h sem revisão, 1% e R$ 2 milhões, cada um em uma tela), **produto** (uma tela por funcionalidade), **ganhos** (cada número em uma tela só, gigante) e **custo e validação** (precificação e piloto). Uma ideia por slide; contas e ressalvas ficam no rodapé e nas notas.

## Direção visual

Formato 16:9. Identidade visual do VoltMap (`apresentações/v1/identidade/identidade-visual-voltmap.png`): laranja #E85D04 nos destaques, grafite #17212B em textos e slides escuros, branco #FFFFFF de fundo, cinza claro #F3F5F7 em cartões e cinza #52606D em legendas; estados verde #15803D, amarelo #FACC15, vermelho #B91C1C e cinza #64748B. Tipografia Inter (semibold nos títulos, bold nos números). Logo do VoltMap na abertura e no fechamento e o símbolo pequeno no canto superior esquerdo dos demais slides. As logos da ArcelorMittal e do IFCE seguem no rodapé. Telas de ganho: número ocupando cerca de dois terços do slide. Telas de produto: mockup grande (cerca de dois terços), título curto à esquerda ou acima e uma frase de benefício. Evitar tabelas densas.

Em todas as telas, no rodapé: à esquerda a logo da ArcelorMittal com a logo do VoltMap ao lado; à direita a logo do Sebrae junto à do IFCE (IFCE no canto). Todas pequenas, na mesma altura, com proporção preservada e margem de segurança; as logos de parceiros ficam brancas nos slides escuros. Rodapés de premissas entre os dois grupos, legíveis. Usar ativos oficiais; se indisponíveis, reservar espaço identificado para inserção posterior.

## Mapa dos blocos

| Bloco | Telas | Papel |
|---|---|---|
| Abertura e problema | 01–05 | Nome, o Chico, a rotina de rondas e o defeito invisível na ronda semanal e na mensal |
| Oportunidade | 06–08 | 720 h sem revisão, depois 1% e, logo em seguida, R$ 2 milhões/ano |
| Produto | 09–14 | O que é o app + uma tela por funcionalidade |
| Ganhos | 15–18 | até 720 h → 1 min → até 43.200× → até 719 h 59 min |
| Custo, piloto e fecho | 19–21 | Precificação, piloto de 90 dias e fechamento |

## Tela 01 — Abertura · 15 s

**Na tela:**
> VoltMap
>
> Menos tempo até o alerta. Mais energia aproveitada.

**Visual:** silhueta industrial discreta com um ponto de máquina destacado.

**Fala:** “O VoltMap conecta o consumo das máquinas à ação da manutenção. Nossa proposta para o Pecém é perceber desperdícios antes, ajudar a equipe a agir e medir o resultado.”

## Tela 02 — Quem vive o problema · 15 s

**Na tela:**
> Este é o Chico.
>
> Muitas máquinas. Uma equipe. Cada minuto conta.

**Visual:** técnico com EPI, máquina e calendário de inspeção. Rodapé: “Persona e rotina ilustrativas”.

**Fala:** “Chico representa o técnico que acompanha dezenas de máquinas. Entre uma inspeção e outra, um equipamento pode continuar produzindo enquanto consome mais energia do que deveria.”

## Tela 03 — Rotina atual do Chico · 20 s

**Na tela:**
> Rotina atual do Chico
>
> Três ritmos de inspeção. Entre uma ronda e outra, ninguém acompanha o consumo da máquina.

**Visual (lúdico, em calendário, fundo escuro):** uma faixa SEG–DOM com três linhas: **Diária** (um bloco “checklist de turno” em todos os dias), **Semanal** (um bloco laranja “ronda preventiva” só na segunda) e **Mensal** (um mini calendário do mês com um único dia destacado, “inspeção programada”). Abaixo, só a frase “1 vez por semana, 6 dias sem monitoramento”, sem lista de ferramentas.

**Rodapé:** “Persona e rotina ilustrativas; frequências a validar com a equipe de manutenção.”

**Fala:** “Hoje o Chico trabalha em três ritmos. Todo dia, um checklist de turno: olhar e ouvir a máquina. Uma vez por semana, a ronda preventiva, com alicate amperímetro, termografia e escuta. E uma vez por mês, a preventiva programada. Entre uma ronda e outra, ninguém mede o consumo da máquina o tempo todo.”

## Tela 04 — O problema na segunda · 25 s

**Na tela:**
> O problema na segunda.
>
> A ronda é na segunda de manhã. O defeito surge no fim do dia, depois da revisão, e fica invisível por 6 dias.
>
> +15% de potência elevada por 159 h

**Visual:** linha do tempo SEG 09h → SEG 18h (defeito) → TER … DOM → PRÓX. SEG 09h, com um gráfico de potência (%): linha cinza em 100% até segunda 18h, salto para cerca de 115% e platô até a próxima segunda. Balão “Seg 18h · início do defeito e aumento de consumo”. Estilo da referência “O problema na quinta-feira”, fundo escuro.

**Rodapé:** “Cenário ilustrativo: +15% de potência (exemplo do protótipo) e ronda semanal na segunda são hipóteses; não são medições na ArcelorMittal.”

**Fala:** “A ronda semanal é na segunda de manhã e o Chico confere tudo. Na segunda, no fim do dia, depois da revisão, o defeito surge e a potência sobe 15%. Ninguém vê. O consumo fica elevado até a próxima segunda, quando a ronda encontra: cerca de 159 horas, mais de seis dias, pagando energia a mais.”

## Tela 05 — E na ronda mensal? · 20 s

**Na tela:**
> E na ronda mensal?
>
> A revisão é no dia 1 de manhã. O defeito surge no fim do dia, depois da revisão, e fica invisível por quase 30 dias.
>
> +15% de potência elevada por 711 h

**Visual:** mesmo gráfico da tela 04, agora para 1 mês: linha do tempo DIA 1 09h (revisão) → DIA 1 18h (defeito) → DIA 8, DIA 15, DIA 22 → PRÓX. REVISÃO DIA 31 09h; potência em 100% até o defeito, salto para cerca de 115% e platô até a próxima revisão mensal. Balão “Dia 1 · 18h · início do defeito e aumento de consumo”. Fundo escuro.

**Rodapé:** “Cenário ilustrativo: +15% de potência (exemplo do protótipo) e revisão mensal no dia 1 são hipóteses; não são medições na ArcelorMittal.”

**Fala:** “Agora pense na ronda mensal. A revisão acontece no dia 1 de manhã e tudo está certo. No fim do mesmo dia, depois da revisão, o defeito surge e a potência sobe 15%. Ninguém vê. O consumo fica elevado até a próxima revisão mensal, quase 30 dias depois: cerca de 711 horas pagando energia a mais.”

## Tela 06 — Quanto tempo uma máquina pode ficar sem revisão · 15 s

**Na tela, gigante e sozinho:**
> 720 h

**Apoio:** “Tempo que uma máquina pode ficar sem revisão: cerca de 30 dias.”

**Rodapé obrigatório:** “Cenário ilustrativo para comparação; não é intervalo medido na ArcelorMittal.”

**Visual:** número central e uma linha do tempo discreta marcando “revisão” nas duas pontas, sem telas do app. É o primeiro número do pitch, antes do 1%.

**Fala:** “Pense em uma máquina que pode passar até 720 horas, cerca de 30 dias, sem uma revisão. Se ela começar a consumir mais energia no meio desse intervalo, o desperdício corre em silêncio. Esse intervalo é um cenário de demonstração; o piloto vai medir o real.”

## Tela 07 — O tamanho da oportunidade · 15 s

**Na tela, gigante e sozinho:**
> 1%

**Apoio:** “De redução no consumo elétrico da unidade.”

**Rodapé:** “Cenário de eficiência; não é resultado já entregue pelo VoltMap.”

**Visual:** somente o número, o apoio e o rodapé. Nada mais.

**Fala:** “Agora olhemos para a escala da unidade. Quanto vale reduzir em apenas um por cento o consumo elétrico?”

## Tela 08 — O valor desse 1% · 20 s

**Na tela, gigante e sozinho:**
> ≈ R$ 2 milhões/ano

**Apoio:** “Potencial econômico de 1% de eficiência elétrica.”

**Rodapé:** “Estimativa de ordem de grandeza: 12.000 MWh/ano × R$ 178/MWh ≈ R$ 2,14 milhões/ano.”

**Visual:** somente o valor, o apoio e o rodapé. Esta tela vem imediatamente depois do 1%.

**Fala:** “Na base estimada nos materiais do projeto, esse um por cento representa cerca de dois milhões de reais por ano. É a dimensão da oportunidade na unidade. A contribuição do VoltMap será medida no piloto.”

## Tela 09 — O que é o VoltMap · 15 s

**Na tela:**
> Da máquina à ação.
>
> Monitorar → Alertar → Localizar → Medir ganhos

**Visual:** quatro ícones grandes conectados, sem moldura de celular. Cada ícone com uma palavra: Monitoramento, Chamados, Mapa, Analytics. Serve de índice das quatro telas seguintes.

**Fala:** “O VoltMap é um aplicativo para técnicos e gestores. Um sensor em cada máquina envia os sinais elétricos. O app identifica desvios, abre chamado para a equipe do turno, mostra onde a máquina está e acompanha o resultado da correção. Vamos ver cada parte.”

## Tela 10 — O mesmo mês, com o VoltMap · 20 s

**Na tela:**
> O mesmo mês, com o VoltMap.
>
> Na ronda semanal o defeito dura até a ronda seguinte. Com o VoltMap, o alerta sai em ~1 min.
>
> ≈ +3,3% de energia a mais no mês, nessa máquina

**Visual:** gráfico de 30 dias (720 h) com quatro rondas semanais marcadas (SEG em cada semana). Duas linhas: **com ronda semanal**, 100% até o defeito, faixa laranja de 159 h com +15% e volta a 100% na ronda seguinte; **com VoltMap**, linha verde em 100% com um pico mínimo e “alerta em ~1 min”. Contas em texto pequeno: 159 h de 720 h × 15% ≈ 3,3%; com alerta em 1 min ≈ 0%.

**Rodapé:** “Cenário ilustrativo de uma máquina: 15% × 159 h ÷ 720 h ≈ 3,3%; rotina e defeito são hipóteses, não medições na ArcelorMittal.”

**Fala:** “Voltando ao mês, agora lado a lado. Vendo o mês: quatro rondas, sempre na segunda. O defeito surgiu logo depois da primeira e só foi encontrado na segunda: 159 horas das 720 do mês com a potência 15% acima, cerca de 3,3% a mais de energia dessa máquina. Com o VoltMap, o alerta sai em cerca de um minuto e esse excesso praticamente desaparece. É um exemplo ilustrativo de uma única máquina.”

## Tela 11 — Monitoramento · 20 s

**Na tela:**
> Veja o desvio enquanto ele acontece.

**Mockup (tela de app, celular ou painel):** lista de máquinas com potência esperada e medida; ventilador AC-02 em destaque com “+15% de consumo”, gráfico curto e status em texto e cor. Selo “Dados simulados”.

**Benefício:** “Visibilidade contínua para priorizar a inspeção.”

**Fala:** “O painel mostra potência, corrente e tensão por máquina. Quando o consumo sai da faixa esperada, a equipe vê o equipamento e a regra que gerou o alerta. A inspeção confirma a causa.”

## Tela 12 — Chamados · 20 s

**Na tela:**
> O alerta chega a quem pode agir.

**Mockup (tela de app):** chamado AC-02, área Aciaria, prioridade, equipe de turno e botão “Assumir chamado”. Selo “Protótipo”.

**Benefício:** “Responsável definido e atendimento rastreável.”

**Fala:** “O desvio gera um chamado para o time responsável no turno. O técnico assume, registra o atendimento e acompanha o histórico. Isso organiza a resposta e torna visível o que ainda precisa de ação.”

## Tela 13 — Mapa · 20 s

**Na tela:**
> Encontre a máquina. Vá direto ao ponto.

**Mockup (tela de app):** mapa da unidade com AC-02 destacado, TAG, área e caminho a partir da oficina. Selo “Trajeto ilustrativo”.

**Benefício:** “Menos tempo procurando o equipamento.”

**Fala:** “O mapa liga o chamado à localização da máquina e mostra um caminho a partir de um ponto de referência. A proposta é reduzir o tempo gasto procurando o ativo. Esse ganho será cronometrado no piloto.”

## Tela 14 — Analytics · 25 s

**Na tela:**
> Transforme a correção em resultado mensurável.

**Mockup (tela de app ou painel de gestor):** indicadores de energia evitada em MWh, valor estimado em reais, tempo de resposta e ranking de desperdício. Valores com selo “Simulação”, ou traços quando não houver dado.

**Benefício:** “Priorize onde há maior oportunidade de economia.”

**Fala:** “O gestor acompanha os desvios, o tempo de resposta e a energia evitada após cada intervenção. A comparação considera condições equivalentes de operação para distinguir melhoria de uma simples queda de produção.”

## Tela 15 — O tempo até perceber, hoje · 15 s

**Na tela, gigante e sozinho:**
> até 720 h

**Apoio:** “Tempo máximo para identificar um desvio, sem monitoramento contínuo. Faixa estimada: de 24 h até 720 h.”

**Rodapé obrigatório:** “Cenário ilustrativo para comparação; faixa de 24 h a 720 h, não é média medida na ArcelorMittal.”

**Visual:** acima do número, em tamanho pequeno, “de 24 h”; o “até 720 h” é o destaque. Linha do tempo discreta com “início do desvio” e “identificação”, sem telas do app. A palavra **até** deve aparecer visível, no mesmo slide, junto ao número.

**Fala:** “Sem monitoramento contínuo, um desvio pode levar de 24 horas até 720 horas, cerca de 30 dias, para ser identificado. Esse intervalo é uma hipótese de demonstração; o piloto precisa medir o real.”

## Tela 16 — O tempo até perceber, com VoltMap · 15 s

**Na tela, gigante e sozinho:**
> 1 min

**Apoio:** “Meta de tempo para gerar o alerta, com o VoltMap.”

**Rodapé obrigatório:** “Meta de piloto, para desvios elegíveis; depende da regra e da aquisição de dados. Não é tempo de reparo.”

**Visual:** somente o número, o apoio e o rodapé.

**Fala:** “Nossa meta a validar é gerar o alerta em um minuto para os desvios que permitam essa janela. Isso mede a detecção, não o diagnóstico da causa nem a conclusão do reparo.”

## Tela 17 — O ganho de velocidade · 15 s

**Na tela, gigante e sozinho:**
> até 43.200×

**Apoio:** “Mais rápido para detectar, no pior caso do cenário.”

**Rodapé obrigatório:** “Comparação ilustrativa: 720 h ÷ 1 min = 43.200×. Para 24 h seria 1.440×.”

**Visual:** apenas o número (com “até” visível), o apoio e o rodapé; sem gráficos ou telas do aplicativo.

**Fala:** “Comparar até 720 horas com um minuto dá até 43.200 vezes. Se o desvio levasse só 24 horas, ainda seriam 1.440 vezes. É o potencial desse cenário; o piloto vai mostrar a redução real.”

## Tela 18 — O tempo recuperado · 10 s

**Na tela, gigante e sozinho:**
> até 719 h 59 min

**Apoio:** “De antecipação do alerta, no pior caso do cenário.”

**Rodapé:** “Cenário ilustrativo: 720 h menos 1 min; não equivale a horas de parada evitadas.”

**Fala:** “Nesse cenário, a equipe pode ganhar até quase 720 horas de antecedência para começar a agir. O benefício energético depende também de quando a correção acontece.”

## Tela 19 — Custo e precificação · 20 s

**Na tela:**
> R$ 499 por pátio industrial

**Apoio:** “Assinatura do VoltMap. Sensores à parte: de R$ 900 a R$ 1.500 por máquina em baixa tensão no piloto.”

**Rodapé obrigatório:** “Preço de assinatura proposto pela equipe (periodicidade a confirmar); custo de sensores é estimativa de mercado, não orçamento.”

**Visual:** dois cartões lado a lado. À esquerda, o preço grande (“R$ 499”, “por pátio industrial”). À direita, o custo de implantar: “Sensor por máquina: R$ 900–1.500 (piloto)”. Sem gráfico de retorno e sem ROI.

**Fala:** “Para a ArcelorMittal o modelo é simples: R$ 499 por pátio industrial. Além disso, há o custo dos sensores, que no piloto fica entre R$ 900 e R$ 1.500 por máquina em baixa tensão. São valores iniciais de proposta, que ajustamos com a equipe da unidade.”

## Tela 20 — Validar na operação · 25 s

**Na tela:**
> 90 dias. 20 máquinas.
>
> Medir o antes. Acompanhar a resposta. Comprovar o ganho.

**Visual:** três etapas: linha de base → operação assistida → avaliação. Abaixo, três métricas que o piloto mede: tempo até o alerta, tempo para encontrar a máquina, energia evitada.

**Fala:** “Propomos um piloto de 90 dias em 20 máquinas. Vamos medir o tempo até o alerta, o tempo para encontrar a máquina e o tempo até a correção. Também vamos comparar o consumo em condições equivalentes e converter a energia evitada usando o valor interno da unidade. Assim, validamos o ganho antes de ampliar.”

## Tela 21 — Fechamento · 20 s

**Na tela:**
> A máquina avisa.
> A equipe age.
> A economia aparece.
>
> VoltMap

**Fala:** “O Chico continua sendo essencial. Com o VoltMap, ele recebe informação para agir mais cedo, encontra a máquina e registra o resultado. Queremos transformar desperdício invisível em uma oportunidade mensurável de eficiência para o Pecém.”

## Mudanças em relação à v2

- Os blocos agora seguem a ordem **oportunidade → produto → ganhos**. Na v2 o 52 h aparecia antes do 1%; na v3 ele abre o bloco de ganhos.
- Nova tela 06 com **720 h** (tempo que uma máquina pode ficar sem revisão), antes do 1%. O 1% (tela 07) e R$ 2 milhões/ano (tela 08) continuam em telas separadas, em sequência.
- As telas 09 a 14 explicam o app (09), comparam o mês com ronda semanal e com VoltMap (10) e dão uma tela a cada funcionalidade (monitoramento, chamados, mapa, Analytics).
- O bloco de ganhos (telas 15 a 18) mostra um número por tela, com “até” para marcar o máximo: até 720 h hoje (faixa de 24 h a 720 h), 1 min com o VoltMap, até 43.200× mais rápido e até 719 h 59 min de antecipação. Os ganhos agora são calculados sobre 720 h, não mais sobre 52 h.
- Nova tela 19 de custo e precificação: R$ 499 por pátio industrial.
- Novas telas 03 a 05 (rotina do Chico, problema na segunda e problema na ronda mensal) mostram o custo do defeito invisível antes de qualquer número de oportunidade; a comparação de um mês com e sem VoltMap (tela 10) vem depois de “Da máquina à ação”. Na ronda mensal, o defeito dura 711 h (dia 1 às 18h até o dia 31 às 09h).
- Duração total: 15+15+20+25+20 (telas 01 a 05) + 15+15+20 (06 a 08) + 15+20 (09, 10) + 20+20+20+25 (11 a 14) + 15+15+15+10 (15 a 18) + 20+25+20 (19 a 21) = 385 s (≈ 6,4 min). Para voltar a 5 min, cortar as telas 03 e 10 ou fundir 06 com 07.

## Notas de sustentação — fora dos slides

- **Base econômica:** [dados do Pecém](../../dados/pecem.md), seção sobre valor de 1% de eficiência. O documento estima consumo interno de 1.200–1.360 GWh/ano. A ponta inferior, 1.200 GWh × 1% = 12 GWh = 12.000 MWh, a R$ 178/MWh, resulta em R$ 2.136.000/ano. A tela arredonda para aproximadamente R$ 2 milhões. É potencial bruto condicionado ao aproveitamento da energia liberada, não receita garantida ou ganho líquido do app. Valores herdados da pesquisa do projeto; não representam cotação atual.
- **720 horas:** hipótese pedida para o roteiro (720 h = 30 dias), sem evidência de intervalo real de revisão. Serve para dar a dimensão do tempo em que um desvio pode passar despercebido; o piloto mede o intervalo real. Não confundir com os 52 h, que são o tempo até identificar um desvio.
- **24 h a 720 h:** faixa hipotética pedida para o roteiro, sem evidência de média operacional. O valor máximo (720 h) é o teto usado nos ganhos; por isso aparecem com “até”. Medir o intervalo entre início do desvio e identificação; não confundir com procura física da máquina.
- **1 minuto:** meta nova, ainda sem validação. A v1 usa persistência de 5 minutos para o exemplo de sobreuso; essa regra não pode ser anunciada como detecção em 1 minuto. Validar aquisição, persistência, latência e falsos alertas antes de alterar a regra. Se a demonstração mantiver 5 min, usar 5 min na tela 16, até 8.640× na tela 17 (720 h ÷ 5 min) e até 719 h 55 min na tela 18.
- **Cálculos:** 720 × 60 = 43.200 min; 43.200 ÷ 1 = 43.200×; 43.200 − 1 = 43.199 min = 719 h 59 min. Para 24 h: 24 × 60 = 1.440×. São projeções matemáticas, não resultados experimentais.
- **Precificação:** R$ 499 por pátio industrial é valor proposto pela equipe; a periodicidade (mensal/anual) ainda precisa ser confirmada. Sensores: R$ 900–1.500 por máquina, estimativa de busca de 29/10 em [equipamentos.md](../equipamentos.md), não conferida. Não calcular ROI sem custo de instalação e linha de base medida.
- **Rotina e defeito (telas 03 a 05 e 10):** frequências diária/semanal/mensal e a ronda na segunda são hipóteses ilustrativas, a validar com a manutenção. 159 h = de segunda 18h até a próxima segunda 09h (6 dias e 15 h). 15% × 159 ÷ 720 = 3,31% do consumo mensal da máquina. Os +15% são o exemplo do protótipo (AC-02), não um valor típico: ver [estimativas.md](../estimativas.md), onde a maioria dos percentuais base é menor.
- **Mapa:** redução de procura é benefício esperado sem percentual comprovado. Medir separadamente da detecção. Por isso não há número de ganho na tela 13.
- **Economia:** energia evitada exige linha de base ajustada à produção, carga e horas de operação. Descontar custos para calcular ganho líquido. Não somar a oportunidade de 1% a economias de máquinas que já estejam incluídas nela.
- **Produto:** funcionalidades baseadas em [app.md](../app.md). Mockups não comprovam implantação. Persona adaptada de [pitch_prototipov1.md](pitch_prototipov1.md).
