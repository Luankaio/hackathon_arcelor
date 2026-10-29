# Pitch do protótipo v3 — VoltMap

Apresentação para a ArcelorMittal Pecém, no contexto do hackathon de eficiência energética. Duração sugerida: 5 minutos. Nome adotado: **VoltMap**.

Cada “tela” abaixo é um slide. A v3 reorganiza a v2 em quatro blocos: **oportunidade** (720 h sem revisão, forno elétrico a arco, escala e 3 fornos de 27 com +15% por 1 mês), **produto** (uma tela por funcionalidade), **ganhos** (cada número em uma tela só, gigante) e **custo e validação** (precificação e piloto). Uma ideia por slide; contas e ressalvas ficam no rodapé e nas notas.

## Direção visual

Formato 16:9. Identidade visual do VoltMap (`apresentações/v1/identidade/identidade-visual-voltmap.png`): laranja #E85D04 nos destaques, grafite #17212B em textos e slides escuros, branco #FFFFFF de fundo, cinza claro #F3F5F7 em cartões e cinza #52606D em legendas; estados verde #15803D, amarelo #FACC15, vermelho #B91C1C e cinza #64748B. Tipografia Inter (semibold nos títulos, bold nos números). Logo do VoltMap na abertura e no fechamento e o símbolo pequeno no canto superior esquerdo dos demais slides. As logos da ArcelorMittal e do IFCE seguem no rodapé. Telas de ganho: número ocupando cerca de dois terços do slide. Telas de produto: mockup grande (cerca de dois terços), título curto à esquerda ou acima e uma frase de benefício. Evitar tabelas densas.

Em todas as telas, no rodapé: à esquerda a logo da ArcelorMittal com a logo do VoltMap ao lado; à direita a logo do Sebrae junto à do IFCE (IFCE no canto). Todas pequenas, na mesma altura, com proporção preservada e margem de segurança; as logos de parceiros ficam brancas nos slides escuros. Rodapés de premissas entre os dois grupos, legíveis. Usar ativos oficiais; se indisponíveis, reservar espaço identificado para inserção posterior.

## Mapa dos blocos

| Bloco | Telas | Papel |
|---|---|---|
| Abertura e problema | 01–05 | Nome, o Cris, a rotina de inspeções e o defeito invisível na inspeção semanal e na mensal |
| Oportunidade | 06–10 | 720 h sem revisão, um forno elétrico a arco por mês e +15%, a escala com várias máquinas e, por fim, o efeito de 3 fornos de 27 com +15% por 1 mês (≈ R$ 4 mi) |
| Produto | 11–18 | O que é o app + uma tela por funcionalidade |
| Ganhos | 19–22 | até 720 h → 1 min → até 43.200× → até 719 h 59 min |
| Custo, ROI, piloto, fecho e consulta | 23–28 | Precificação, piloto de 90 dias e fechamento |

## Tela 01 — Abertura · 15 s

**Na tela:**
> VoltMap
>
> Menos tempo até o alerta. Mais energia aproveitada.

**Visual:** silhueta industrial discreta com um ponto de máquina destacado.

**Fala:** “O VoltMap conecta o consumo das máquinas à ação da manutenção. Nossa proposta para o Pecém é perceber desperdícios antes, ajudar a equipe a agir e medir o resultado.”

## Tela 02 — Quem vive o problema · 15 s

**Na tela:**
> Este é o Cris.
>
> **Técnico eletromecânico industrial** · Responsável pela manutenção das máquinas
>
> 5.710.000 m² de usina.
>
> Dezenas de máquinas. Checagem manual.
>
> E se o Cris soubesse na hora, e não na próxima inspeção?

**Visual:** a foto do Cris (técnico de manutenção com capacete e EPI dentro da usina, arquivo `imagens/cris.jpg`) em destaque, com cantos arredondados e sombra suave, ao lado do texto. Rodapé: “Persona e rotina ilustrativas. Área da usina: 571 ha (fontes públicas).”

**Fala:** “Cris é técnico eletromecânico industrial, responsável pela manutenção das máquinas, e trabalha numa usina de 5,71 milhões de metros quadrados, com dezenas de máquinas para checar manualmente. Entre uma inspeção e outra, um equipamento pode continuar produzindo enquanto consome mais energia do que deveria. E se o Cris soubesse na hora, e não na próxima inspeção?”

## Tela 03 — Rotina atual do Cris · 20 s

**Na tela:**
> Rotina atual do Cris
>
> Três ritmos de inspeção. Entre uma inspeção e outra, ninguém acompanha o consumo da máquina.

**Visual (lúdico, em calendário, fundo escuro):** uma faixa SEG–DOM com três linhas: **Diária** (um bloco “checklist de turno” em todos os dias), **Semanal** (um bloco laranja “inspeção preventiva” só na segunda) e **Mensal** (um mini calendário do mês com um único dia destacado, “inspeção programada”). Abaixo, só a frase “1 vez por semana, 6 dias sem monitoramento”, sem lista de ferramentas.

**Rodapé:** “Persona e rotina ilustrativas; frequências a validar com a equipe de manutenção.”

**Fala:** “Hoje o Cris trabalha em três ritmos. Todo dia, um checklist de turno: olhar e ouvir a máquina. Uma vez por semana, a inspeção preventiva, com alicate amperímetro, termografia e escuta. E uma vez por mês, a preventiva programada. Entre uma inspeção e outra, ninguém mede o consumo da máquina o tempo todo.”

## Tela 04 — O problema na segunda · 25 s

**Na tela:**
> O problema na segunda.
>
> A inspeção é na segunda de manhã. O defeito surge no fim do dia, depois da revisão, e fica invisível por 6 dias.
>
> +15% de potência elevada por 159 h

**Visual:** linha do tempo SEG 09h → SEG 18h (defeito) → TER … DOM → PRÓX. SEG 09h, com um gráfico de potência (%): linha cinza em 100% até segunda 18h, salto para cerca de 115% e platô até a próxima segunda. Balão “Seg 18h · início do defeito e aumento de consumo”. Estilo da referência “O problema na quinta-feira”, fundo escuro.

**Rodapé:** “Cenário ilustrativo: +15% de potência (exemplo do protótipo) e inspeção semanal na segunda são hipóteses; não são medições na ArcelorMittal.”

**Fala:** “A inspeção semanal é na segunda de manhã e o Cris confere tudo. Na segunda, no fim do dia, depois da revisão, o defeito surge e a potência sobe 15%. Ninguém vê. O consumo fica elevado até a próxima segunda, quando a inspeção encontra: cerca de 159 horas, mais de seis dias, pagando energia a mais.”

## Tela 05 — E na inspeção mensal? · 20 s

**Na tela:**
> E na inspeção mensal?
>
> A revisão é no dia 1 de manhã. O defeito surge no fim do dia, depois da revisão, e fica invisível por quase 30 dias.
>
> +15% de potência elevada por 711 h

**Visual:** mesmo gráfico da tela 04, agora para 1 mês: linha do tempo DIA 1 09h (revisão) → DIA 1 18h (defeito) → DIA 8, DIA 15, DIA 22 → PRÓX. REVISÃO DIA 31 09h; potência em 100% até o defeito, salto para cerca de 115% e platô até a próxima revisão mensal. Balão “Dia 1 · 18h · início do defeito e aumento de consumo”. Fundo escuro.

**Rodapé:** “Cenário ilustrativo: +15% de potência (exemplo do protótipo) e revisão mensal no dia 1 são hipóteses; não são medições na ArcelorMittal.”

**Fala:** “Agora pense na inspeção mensal. A revisão acontece no dia 1 de manhã e tudo está certo. No fim do mesmo dia, depois da revisão, o defeito surge e a potência sobe 15%. Ninguém vê. O consumo fica elevado até a próxima revisão mensal, quase 30 dias depois: cerca de 711 horas pagando energia a mais.”

## Tela 06 — Quanto tempo uma máquina pode ficar sem revisão · 15 s

**Na tela, gigante e sozinho:**
> 720 h

**Apoio:** “Tempo que uma máquina pode ficar sem revisão: cerca de 30 dias.”

**Rodapé obrigatório:** “Cenário ilustrativo para comparação; não é intervalo medido na ArcelorMittal.”

**Visual:** número central e uma linha do tempo discreta marcando “revisão” nas duas pontas, sem telas do app. É o primeiro número do pitch.

**Fala:** “Pense em uma máquina que pode passar até 720 horas, cerca de 30 dias, sem uma revisão. Se ela começar a consumir mais energia no meio desse intervalo, o desperdício corre em silêncio. Esse intervalo é um cenário de demonstração; o piloto vai medir o real.”

## Tela 07 — Um forno elétrico a arco, por mês · 15 s

**Na tela, gigante e sozinho:**
> ≈ R$ 9 mi

**Apoio:** “Por mês em eletricidade, em média, num forno elétrico a arco.” Título pequeno: “Um forno elétrico a arco”. Sem kWh nem MWh na tela.

**Rodapé obrigatório:** “Estimativa para um forno elétrico a arco do grupo ArcelorMittal (27 fornos): ≈ 45 mil t de aço/mês × 400 kWh/t × R$ 0,50/kWh. Tarifa hipotética; não é dado de uma unidade nem do Pecém.”

**Visual:** somente o número, o apoio e o rodapé. Estilo dos números gigantes, fundo claro.

**Fala:** “Pense em um forno elétrico a arco, uma das máquinas que mais consomem eletricidade em uma siderúrgica. O grupo ArcelorMittal opera 27 desses fornos. Pela produção de aço de 2025 e pelo consumo típico de 400 quilowatts-hora por tonelada, um forno médio gasta cerca de 9 milhões de reais por mês só em eletricidade. É uma estimativa com tarifa hipotética, não um dado de uma unidade específica.”

## Tela 08 — Se o forno gastar 15% a mais · 15 s

**Na tela, gigante e sozinho:**
> + R$ 1,35 mi

**Apoio:** “A mais por mês, em um único forno elétrico a arco, se o consumo subir 15%.”

**Rodapé obrigatório:** o mesmo da tela 07.

**Visual:** somente o valor, o apoio e o rodapé. Fundo escuro com o número inteiro (“+ R$ 1,35 mi”) em vermelho claro (#F87171), para dar peso. Logo depois da tela 07.

**Fala:** “Agora, se esse forno passar a consumir 15% a mais de eletricidade, por desgaste, eletrodos, refratário ou operação fora do ponto, são cerca de 1,35 milhão de reais a mais por mês, em um único forno. É um exemplo ilustrativo com tarifa hipotética.”

## Tela 09 — Em larga escala · 15 s

**Na tela:**
> Agora imagine isso em larga escala.

**Visual (ilustração minimalista, fundo claro):** uma grade de pequenos ícones de motores/máquinas, todos em cinza claro, com algumas poucas (cerca de 7 em 70) em laranja com um anel pulsando suave. Legenda: “máquina normal” e “gastando a mais, sem ninguém perceber”. Sem números.

**Rodapé:** “Ilustração: quantidade de máquinas e proporção com desvio são ilustrativas; não são dados da ArcelorMittal.”

**Fala:** “Agora imagine isso em larga escala. Uma usina tem dezenas, centenas de máquinas como esse forno. Em qualquer momento, algumas podem estar gastando a mais, sem que ninguém perceba. Cada ponto laranja aqui é uma máquina nessa situação.”

## Tela 10 — E se 11% dos fornos desregulassem · 25 s

**Na tela (fundo claro):**
> E se 11% dos fornos desregulassem?
>
> ≈ R$ 4 mi a mais no mês, só em eletricidade (+15% por forno)

**Visual:** título em uma linha só, em fonte menor (≈ 56 px), com “11% dos fornos” em laranja e o valor gigante “≈ R$ 4 mi”. Abaixo, uma faixa de cálculo em três caixas ligadas por × e =: **3 de 27 fornos** (3 ÷ 27 ≈ 11%) × **R$ 1,35 mi por forno** (15% de ≈ R$ 9 mi ao mês) = **≈ R$ 4 mi no mês** (≈ 1,7% da eletricidade dos 27 fornos), esta última em laranja.

**Rodapé (explica a referência):** “Referência: relatório anual 2025 do grupo (27 fornos a arco; 14,6 Mt ⇒ ≈ 45 mil t por forno/mês) × 400 kWh/t × R$ 0,50/kWh ≈ R$ 9 mi por forno. Tarifa hipotética; não é dado do Pecém.”

**Fala:** “Agora vamos para a escala. O grupo opera 27 fornos elétricos a arco. Se três deles, cerca de 11%, desregularem e passarem a gastar 15% a mais durante um mês, são três vezes 1,35 milhão, cerca de 4 milhões de reais a mais naquele mês, só em eletricidade. Isso equivale a cerca de 1,7% da eletricidade dos 27 fornos. É um exemplo ilustrativo com tarifa hipotética.”

## Tela 11 — O que é o VoltMap e nossa proposta de valor · 20 s

**Na tela (fundo grafite, usando a identidade do VoltMap):**
> Nossa proposta de valor: Transformamos o **desperdício invisível** de energia em **ação** da manutenção.
>
> Monitorar → Alertar → Localizar → Medir ganhos

**Visual:** no topo, a logo horizontal do VoltMap (versão escura) ao lado da proposta de valor, com destaques em laranja e o símbolo como marca d’água ao fundo. O elemento principal da tela é a **pipeline de quatro cartões grandes** ligados por setas laranja, cada um com um ícone de linha em laranja, um título e uma frase curta: **Monitorar** (sinais elétricos de cada máquina), **Alertar** (chamado para a equipe do turno), **Localizar** (mapa e caminho até a máquina), **Medir ganhos** (energia evitada e economia). Sem cartões de benefício extras e sem cartela de cores.

**Rodapé:** “Funcionalidades do protótipo; não comprovam implantação.”

**Fala:** “O VoltMap é um aplicativo para técnicos e gestores. Um sensor em cada máquina envia os sinais elétricos. Nossa proposta de valor é transformar o desperdício invisível de energia em ação da manutenção, em quatro passos: monitorar, alertar, localizar e medir os ganhos. Vamos ver cada parte.”

## Tela 12 — Do sensor ao celular do Cris · 20 s

**Na tela (fundo claro, ilustração):**
> Monitorar → Alertar: Do sensor ao celular do Cris.

**Visual:** da esquerda para a direita, uma máquina (motor) com um sensor laranja e uma linha de potência no alto; ondas laranja que pulsam, rotuladas “dados em tempo real”; e um celular com o painel do app e, por cima, uma notificação “VOLTMAP · agora — Sobreuso · AC-02, Ventilador de despoeiramento, Aciaria” com a foto do Cris (recorte do rosto) ao lado. Três passos numerados: 1) o sensor mede a máquina o tempo todo, 2) o VoltMap vê o consumo sair da faixa esperada, 3) o Cris recebe o alerta no celular, na hora.

**Rodapé:** “Protótipo do aplicativo; dados simulados. A notificação é ilustrativa; a meta de 1 min para gerar o alerta será validada no piloto.”

**Fala:** “Primeiro passo: monitorar e alertar. Um sensor na máquina mede tensão, corrente e potência o tempo todo e envia os dados em tempo real. Quando o consumo sai da faixa esperada por tempo suficiente, o VoltMap gera o alerta e o Cris recebe uma notificação no celular, com a máquina e o tipo de desvio. Ele não precisa esperar a próxima inspeção para descobrir.”

## Tela 13 — Do alerta ao conserto · 20 s

**Na tela (fundo claro):**
> Localizar → Reparar: Do alerta ao conserto.

**Visual:** à direita, dois celulares lado a lado ligados por uma seta: o **mapa** com a máquina, a TAG e o caminho (“1 · Localizar”) e a lista de **chamados** com “Pegar chamado” (“2 · Assumir e reparar”). À esquerda, quatro cartões de valor: **Vá direto ao ponto** (mapa com a TAG e o caminho até a máquina), **Responsável definido** (o Cris assume o chamado), **Conserto registrado** (histórico de cada intervenção) e **Ganho visível** (o consumo volta ao normal e vira economia no Analytics).

**Rodapé:** “Protótipo do aplicativo; dados simulados. Redução do tempo de procura é benefício esperado, a medir no piloto.”

**Fala:** “Segundo passo: localizar e reparar. Com o alerta, o Cris abre o mapa, vê a máquina, a TAG e o caminho a partir do ponto onde ele está, e vai direto ao ponto, sem perder tempo procurando. Chegando, assume o chamado, corrige o problema e registra o conserto. O consumo volta ao normal e o ganho aparece no Analytics. O valor do mapa e do chamado é reduzir a procura e deixar o conserto rastreável; o ganho de tempo será cronometrado no piloto.”

## Tela 14 — O mesmo mês, com o VoltMap · 20 s

**Na tela (fundo claro):**
> O mesmo mês, com o VoltMap.
>
> Com inspeção mensal, o defeito dura até a revisão seguinte. Com o VoltMap, o alerta sai em ~1 min.
>
> ≈ +14,8% de energia a mais no mês, nessa máquina

**Visual:** gráfico de 30 dias (720 h) do mesmo exemplo da tela 05 (revisão mensal no dia 1, defeito às 18h, próxima revisão no dia 31). Duas linhas: **com inspeção mensal**, 100% até o defeito, faixa laranja de 711 h com +15% até a revisão seguinte; **com VoltMap**, linha verde em 100% com um pico mínimo e “alerta em ~1 min”. Contas em texto pequeno: 711 h de 720 h × 15% ≈ 14,8%; com alerta em 1 min ≈ 0%.

**Rodapé:** “Cenário ilustrativo de uma máquina: 15% × 711 h ÷ 720 h ≈ 14,8%; rotina e defeito são hipóteses, não medições na ArcelorMittal.”

**Fala:** “Voltando ao exemplo da inspeção mensal, agora lado a lado. Com a revisão só uma vez por mês, o defeito que surgiu no dia 1, depois da revisão, fica 711 horas das 720 do mês com a potência 15% acima, quase o mês inteiro. Para essa máquina, são cerca de 14,8% a mais de energia no mês. Com o VoltMap, o alerta sai em cerca de um minuto e esse excesso praticamente desaparece. É um exemplo ilustrativo de uma única máquina.”

## Tela 15 — Monitoramento · 20 s

**Na tela:**
> Veja o desvio enquanto ele acontece.

**Mockup (tela de app, celular ou painel):** lista de máquinas com potência esperada e medida; ventilador AC-02 em destaque com “+15% de consumo”, gráfico curto e status em texto e cor. Selo “Dados simulados”.

**Benefício:** “Visibilidade contínua para priorizar a inspeção.”

**Fala:** “O painel mostra potência, corrente e tensão por máquina. Quando o consumo sai da faixa esperada, a equipe vê o equipamento e a regra que gerou o alerta. A inspeção confirma a causa.”

## Tela 16 — Chamados · 20 s

**Na tela:**
> O alerta chega a quem pode agir.

**Mockup (tela de app):** chamado AC-02, área Aciaria, prioridade, equipe de turno e botão “Assumir chamado”. Selo “Protótipo”.

**Benefício:** “Responsável definido e atendimento rastreável.”

**Fala:** “O desvio gera um chamado para o time responsável no turno. O técnico assume, registra o atendimento e acompanha o histórico. Isso organiza a resposta e torna visível o que ainda precisa de ação.”

## Tela 17 — Mapa · 20 s

**Na tela:**
> Encontre a máquina. Vá direto ao ponto.

**Mockup (tela de app):** mapa da unidade com AC-02 destacado, TAG, área e caminho a partir da oficina. Selo “Trajeto ilustrativo”.

**Benefício:** “Menos tempo procurando o equipamento.”

**Fala:** “O mapa liga o chamado à localização da máquina e mostra um caminho a partir de um ponto de referência. A proposta é reduzir o tempo gasto procurando o ativo. Esse ganho será cronometrado no piloto.”

## Tela 18 — Analytics · 25 s

**Na tela:**
> Transforme a correção em resultado mensurável.

**Mockup (tela de app ou painel de gestor):** indicadores de energia evitada em MWh, valor estimado em reais, tempo de resposta e ranking de desperdício. Valores com selo “Simulação”, ou traços quando não houver dado.

**Benefício:** “Priorize onde há maior oportunidade de economia.”

**Fala:** “O gestor acompanha os desvios, o tempo de resposta e a energia evitada após cada intervenção. A comparação considera condições equivalentes de operação para distinguir melhoria de uma simples queda de produção.”

## Tela 19 — O tempo até perceber, hoje · 15 s

**Na tela, gigante e sozinho:**
> até 720 h

**Apoio:** “Tempo máximo para identificar um desvio, sem monitoramento contínuo. Faixa estimada: de 24 h até 720 h.”

**Rodapé obrigatório:** “Cenário ilustrativo para comparação; faixa de 24 h a 720 h, não é média medida na ArcelorMittal.”

**Visual:** acima do número, em tamanho pequeno, “de 24 h”; o “até 720 h” é o destaque. Linha do tempo discreta com “início do desvio” e “identificação”, sem telas do app. A palavra **até** deve aparecer visível, no mesmo slide, junto ao número.

**Fala:** “Sem monitoramento contínuo, um desvio pode levar de 24 horas até 720 horas, cerca de 30 dias, para ser identificado. Esse intervalo é uma hipótese de demonstração; o piloto precisa medir o real.”

## Tela 20 — O tempo até perceber, com VoltMap · 15 s

**Na tela, gigante e sozinho:**
> 1 min

**Apoio:** “Meta de tempo para gerar o alerta, com o VoltMap.”

**Rodapé obrigatório:** “Meta de piloto, para desvios elegíveis; depende da regra e da aquisição de dados. Não é tempo de reparo.”

**Visual:** somente o número, o apoio e o rodapé.

**Fala:** “Nossa meta a validar é gerar o alerta em um minuto para os desvios que permitam essa janela. Isso mede a detecção, não o diagnóstico da causa nem a conclusão do reparo.”

## Tela 21 — O ganho de velocidade · 15 s

**Na tela, gigante e sozinho:**
> até 43.200×

**Apoio:** “Mais rápido para detectar, no pior caso do cenário.”

**Rodapé obrigatório:** “Comparação ilustrativa: 720 h ÷ 1 min = 43.200×. Para 24 h seria 1.440×.”

**Visual:** apenas o número (com “até” visível), o apoio e o rodapé; sem gráficos ou telas do aplicativo.

**Fala:** “Comparar até 720 horas com um minuto dá até 43.200 vezes. Se o desvio levasse só 24 horas, ainda seriam 1.440 vezes. É o potencial desse cenário; o piloto vai mostrar a redução real.”

## Tela 22 — O tempo recuperado · 10 s

**Na tela, gigante e sozinho:**
> até 719 h 59 min

**Apoio:** “De antecipação do alerta, no pior caso do cenário.”

**Rodapé:** “Cenário ilustrativo: 720 h menos 1 min; não equivale a horas de parada evitadas.”

**Fala:** “Nesse cenário, a equipe pode ganhar até quase 720 horas de antecedência para começar a agir. O benefício energético depende também de quando a correção acontece.”

## Tela 23 — Custo e precificação · 20 s

**Na tela:**
> R$ 499 por pátio industrial

**Apoio:** “Assinatura do VoltMap. Sensores à parte: de R$ 900 a R$ 1.500 por máquina em baixa tensão no piloto.”

**Rodapé obrigatório:** “Preço de assinatura proposto pela equipe (periodicidade a confirmar); custo de sensores é estimativa de mercado, não orçamento.”

**Visual:** dois cartões lado a lado. À esquerda, o preço grande (“R$ 499”, “por pátio industrial”). À direita, o custo de implantar: “Sensor por máquina: R$ 900–1.500 (piloto)”. Sem gráfico de retorno e sem ROI.

**Fala:** “Para a ArcelorMittal o modelo é simples: R$ 499 por pátio industrial. Além disso, há o custo dos sensores, que no piloto fica entre R$ 900 e R$ 1.500 por máquina em baixa tensão. São valores iniciais de proposta, que ajustamos com a equipe da unidade.”

## Tela 24 — ROI estimado: um pátio com 27 fornos elétricos a arco · 25 s

**Na tela (fundo claro):**
> ROI estimado · um pátio com 27 fornos elétricos a arco
>
> **≈ 10.000%** de ROI no 1º ano, com apenas 0,5% de economia

**Visual:** só o ROI em número gigante, em porcentagem (≈ 10.000%). Abaixo, quatro cartões pequenos com a explicação: **Ele gasta** ≈ R$ 243 mi/mês (27 fornos × ≈ R$ 9 mi) · **Economia de 0,5%** ≈ R$ 1,2 mi/mês (com 1%: ≈ R$ 2,4 mi/mês) · **Investimento 1º ano** ≈ R$ 141 mil (27 medidores + R$ 499 × 12) · **Se paga em** < 1 semana, mesmo com 0,5%. O cenário de 3 fornos desregulados (≈ R$ 4 mi) fica só na fala.

**Rodapé:** “Cenário hipotético de um pátio com 27 fornos a arco, cada um ≈ R$ 9 mi/mês (R$ 0,50/kWh). Investimento: 27 multimedidores de até R$ 5 mil + assinatura R$ 499 × 12 ≈ R$ 141 mil. ROI = (economia − custo) ÷ custo × 100. Ganho bruto: não inclui instalação, integração nem reparos.”

**Fala:** “Um exemplo de retorno. Imagine um pátio industrial só com 27 fornos elétricos a arco. Cada um gasta cerca de 9 milhões por mês, são 243 milhões de reais por mês em eletricidade. Se o VoltMap ajudar a reduzir só meio por cento, são cerca de 1,2 milhão por mês; com 1%, 2,4 milhões. E no cenário de três fornos desregulados por um mês, evitar o excesso vale cerca de 4 milhões. Do lado do custo, são cerca de 141 mil reais no primeiro ano. Mesmo com meio por cento, o investimento se paga em menos de uma semana. É um cenário teórico, de ganho bruto, que precisa ser validado no piloto.”

## Tela 25 — Próximos passos · 25 s

**Na tela:**
> Próximos passos
>
> 90 dias. 20 máquinas.
>
> Medir o antes. Acompanhar a resposta. Comprovar o ganho.

**Visual:** quatro cartões em sequência: **Passo 1 · Linha de base** (medir como é hoje, sem o app), **Passo 2 · Operação assistida** (alertas, chamados e mapa em uso), **Passo 3 · Avaliação** (comparar em condições equivalentes) e, em laranja, **Próximo passo eficiente · Ampliar com eficiência** (levar o VoltMap para toda a unidade, depois de comprovar o ganho). Abaixo, três etiquetas do que o piloto mede: tempo até o alerta, tempo para achar a máquina e energia evitada.

**Rodapé:** “Piloto proposto pela equipe; prazos e quantidade de máquinas a combinar com a unidade.”

**Fala:** “Os próximos passos: um piloto de 90 dias em 20 máquinas. Primeiro medimos a linha de base, como é hoje, sem o app. Depois, a operação assistida, com alertas, chamados e mapa em uso. Por fim, a avaliação, comparando o consumo em condições equivalentes e convertendo a energia evitada em reais. O próximo passo eficiente é ampliar o VoltMap para toda a unidade, só depois de comprovar o ganho.”

## Tela 26 — Fechamento · 20 s

**Na tela:**
> A máquina avisa.
> A equipe age.
> A economia aparece.
>
> VoltMap

**Fala:** “O Cris continua sendo essencial. Com o VoltMap, ele recebe informação para agir mais cedo, encontra a máquina e registra o resultado. Queremos transformar desperdício invisível em uma oportunidade mensurável de eficiência para o Pecém.”

## Tela 27 — Conheça nosso app · 0 s (visual)

**Na tela (fundo claro, só o título):**
> Conheça nosso app

**Visual:** quatro telas do aplicativo lado a lado, em celulares: **Painel** (demanda total e alertas ativos), **Mapa** (com o caminho até a AC-02), **Chamados** (com “Pegar chamado”) e **Analytics** (economia do mês). Sem legendas e sem outro texto além do título. Arquivos: `imagens/app-painel.png`, `app-mapa.png`, `app-chamados.png` e `app-analytics.png`.

**Rodapé:** “Protótipo do aplicativo; dados simulados.”

**Fala:** “Conheça nosso app: o painel com a demanda e os alertas ativos, o mapa com o caminho até a máquina, os chamados para a equipe do turno e o Analytics com a economia do mês.”

## Tela 28 — Referências · dados · 0 s (consulta)

**Na tela (fundo claro, só dados):** tabela com quatro colunas (Dado, Valor, Tipo, Origem). O “Tipo” vai em etiquetas coloridas: **Fonte** (verde), **Cálculo** (cinza), **Premissa/Meta/Proposta** (laranja), **Estimativa** (marrom) e **Simulado** (amarelo). Sem texto corrido.

| Dado | Valor | Tipo | Origem |
|---|---|---|---|
| Área da usina Pecém | 571 ha = 5.710.000 m² | Fonte | [Global Energy Monitor (gem.wiki)](https://www.gem.wiki/ArcelorMittal_Pec%C3%A9m_steel_plant) · [O Povo, 29/07/2022](https://mais.opovo.com.br/jornal/economia/2022/07/29/compra-da-csp-pela-arcelormittal-por-uss-22-bi-eleva-expectativas-sobre-a-economia-do-ceara.html) |
| Fornos elétricos a arco do grupo | 27 fornos · 24 Mt/ano de capacidade · 14,6 Mt produzidas em 2025 | Fonte | [Relatório anual 2025 (20-F), p. 60](https://www.sec.gov/Archives/edgar/data/1243429/000124342926000020/mt-20251231.htm) |
| Consumo de um forno a arco | 400–500 kWh por tonelada de aço | Fonte | [Journal of Sustainable Metallurgy (Springer)](https://doi.org/10.1007/s40831-021-00390-y), trecho a confirmar |
| Produção por forno | ≈ 45 mil t/mês (14,6 Mt ÷ 27 ÷ 12) | Cálculo | Equipe |
| Tarifa de referência | R$ 0,50/kWh | Premissa | Hipotética, só para comparação |
| Gasto de um forno | ≈ R$ 9 mi/mês (45 mil t × 400 kWh/t × R$ 0,50) · +15% = R$ 1,35 mi | Cálculo | Equipe |
| 3 de 27 fornos | ≈ 11% · 3 × R$ 1,35 mi ≈ R$ 4 mi no mês · ≈ 1,7% da eletricidade dos 27 fornos | Cálculo | Equipe |
| Aumento de consumo do defeito | +15% de potência | Premissa | Exemplo do protótipo (AC-02) |
| Tempo sem identificar o desvio | 24 h a 720 h (720 h = 30 dias) | Premissa | Cenário ilustrativo |
| Defeito com inspeção semanal | 159 h com +15% (seg 18h até a seg seguinte 09h) | Cálculo | Equipe |
| Defeito com inspeção mensal | 711 h com +15% ⇒ ≈ +14,8% no mês (15% × 711 ÷ 720) | Cálculo | Equipe |
| Gasto de 27 fornos (pátio hipotético) | ≈ R$ 243 mi/mês (27 × ≈ R$ 9 mi) | Cálculo | Equipe |
| Economia no pátio hipotético | 0,5% ≈ R$ 1,2 mi/mês · 1% ≈ R$ 2,4 mi/mês · 3 fornos desregulados por 1 mês ≈ R$ 4 mi evitados | Cálculo | Equipe |
| Investimento do 1º ano | ≈ R$ 141 mil (27 multimedidores de até R$ 5 mil + R$ 499 × 12) | Estimativa | equipamentos.md (medidor de média tensão: R$ 1.550–5.000, instalação à parte) |
| ROI e retorno | ROI ≈ 10.000% no 1º ano com 0,5% (≈ 10.200%) · retorno em menos de 1 semana | Cálculo | (economia − custo) ÷ custo × 100; ganho bruto |
| Alerta do VoltMap | 1 min, para desvios elegíveis | Meta | A validar no piloto |
| Ganho de velocidade | 720 h ÷ 1 min = 43.200× · 720 h − 1 min = 719 h 59 min · 24 h ÷ 1 min = 1.440× | Cálculo | Equipe |
| Assinatura | R$ 499 por pátio industrial | Proposta | Equipe (periodicidade a confirmar) |
| Sensores no piloto | R$ 900 a R$ 1.500 por máquina em baixa tensão | Estimativa | Pesquisa de mercado de 29/10/2026 |
| Piloto | 90 dias · 20 máquinas | Proposta | Equipe |
| Telas do app | R$ 48,3 mil · 231 MWh (Analytics) e demais valores do protótipo | Simulado | Dados simulados, não são reais |

**Rodapé:** “Nada aqui é medição na ArcelorMittal: são fontes públicas, cálculos e premissas da equipe.”

**Uso:** slide de consulta na etapa de perguntas; não entra na contagem de tempo. O 20-F foi aberto no sec.gov e confirma 27 fornos, 24,0 Mt de capacidade e 14,6 Mt em 2025 (Electric Arc Furnace | 27 | 24.0 | 14.6). O artigo do Springer (Logar e Škrjanc, 2021) é do mesmo periódico, mas não confirmei nele o trecho de 400–500 kWh/t; outras fontes públicas citam essa faixa.

## Mudanças em relação à v2

- Os blocos agora seguem a ordem **oportunidade → produto → ganhos**. Na v2 o 52 h aparecia antes do 1%; na v3 ele abre o bloco de ganhos.
- Nova tela 06 com **720 h** (tempo que uma máquina pode ficar sem revisão), antes dos números de energia. O slide isolado do 1% foi removido e o R$ 2 milhões/ano foi substituído (tela 10) pelo cálculo de 3 fornos de 27 com +15% por 1 mês.
- As telas 11 a 18 explicam o app (11), mostram do sensor ao celular do Cris (12) e do alerta ao conserto (13), comparam o mês com inspeção mensal e com VoltMap (14) e dão uma tela a cada funcionalidade (monitoramento, chamados, mapa, Analytics).
- O bloco de ganhos (telas 19 a 22) mostra um número por tela, com “até” para marcar o máximo: até 720 h hoje (faixa de 24 h a 720 h), 1 min com o VoltMap, até 43.200× mais rápido e até 719 h 59 min de antecipação. Os ganhos agora são calculados sobre 720 h, não mais sobre 52 h.
- Nova tela 23 de custo e precificação: R$ 499 por pátio industrial.
- Novas telas 03 a 05 (rotina do Cris, problema na segunda e problema na inspeção mensal) mostram o custo do defeito invisível antes de qualquer número de oportunidade; a comparação de um mês com e sem VoltMap (tela 14) vem depois de “Da máquina à ação”. Na inspeção mensal, o defeito dura 711 h (dia 1 às 18h até o dia 31 às 09h).
- Duração total (telas 01 a 25, sem a referência): ≈ 480 s (≈ 8 min). Para chegar perto de 5 min, cortar as telas 03, 08, 09, 14, 24 e uma das duas 12/13.

## Notas de sustentação — fora dos slides

- **Base econômica:** [dados do Pecém](../../dados/pecem.md), seção sobre valor de 1% de eficiência. O documento estima consumo interno de 1.200–1.360 GWh/ano. A ponta inferior, 1.200 GWh × 1% = 12 GWh = 12.000 MWh, a R$ 178/MWh, resulta em R$ 2.136.000/ano. A tela arredonda para aproximadamente R$ 2 milhões. É potencial bruto condicionado ao aproveitamento da energia liberada, não receita garantida ou ganho líquido do app. Valores herdados da pesquisa do projeto; não representam cotação atual.
- **720 horas:** hipótese pedida para o roteiro (720 h = 30 dias), sem evidência de intervalo real de revisão. Serve para dar a dimensão do tempo em que um desvio pode passar despercebido; o piloto mede o intervalo real. Não confundir com os 52 h, que são o tempo até identificar um desvio.
- **24 h a 720 h:** faixa hipotética pedida para o roteiro, sem evidência de média operacional. O valor máximo (720 h) é o teto usado nos ganhos; por isso aparecem com “até”. Medir o intervalo entre início do desvio e identificação; não confundir com procura física da máquina.
- **1 minuto:** meta nova, ainda sem validação. A v1 usa persistência de 5 minutos para o exemplo de sobreuso; essa regra não pode ser anunciada como detecção em 1 minuto. Validar aquisição, persistência, latência e falsos alertas antes de alterar a regra. Se a demonstração mantiver 5 min, usar 5 min na tela 20, até 8.640× na tela 21 (720 h ÷ 5 min) e até 719 h 55 min na tela 22.
- **Cálculos:** 720 × 60 = 43.200 min; 43.200 ÷ 1 = 43.200×; 43.200 − 1 = 43.199 min = 719 h 59 min. Para 24 h: 24 × 60 = 1.440×. São projeções matemáticas, não resultados experimentais.
- **Precificação:** R$ 499 por pátio industrial é valor proposto pela equipe; a periodicidade (mensal/anual) ainda precisa ser confirmada. Sensores: R$ 900–1.500 por máquina, estimativa de busca de 29/10 em [equipamentos.md](../equipamentos.md), não conferida. Não calcular ROI sem custo de instalação e linha de base medida.
- **Três fornos (tela 10):** 3 ÷ 27 = 11,1% ≈ 11%. Por forno: 45.062 t/mês × 400 kWh/t = 18,0 GWh × R$ 0,50 = R$ 9,0 mi; +15% = R$ 1,35 mi; × 3 = R$ 4,05 mi ≈ R$ 4 mi em 1 mês. Sobre o total de 27 fornos (≈ R$ 243 mi/mês): 4,05 ÷ 243 = 1,67% (= 11,1% × 15%). Mesmas atenções da tela 07 e 08: fornos são do grupo, o Pecém não tem forno elétrico a arco; tarifa hipotética; média entre fornos. A conta do 1% de eficiência do Pecém (≈ R$ 2,14 mi/ano) saiu dos slides e continua no [pecem.md](../../dados/pecem.md).
- **ROI (tela 24):** gasto = 27 × R$ 9,0 mi = R$ 243 mi/mês (R$ 2,92 bi/ano). Economia: 0,5% = R$ 1,22 mi/mês; 1% = R$ 2,43 mi/mês; 3 fornos com +15% por 1 mês corrigidos em < 1 h ≈ R$ 4,04 mi (99,86% de R$ 4,05 mi). Investimento: multimedidor de média tensão R$ 1.550–5.000 ([equipamentos.md](../equipamentos.md)); usado o teto, 27 × R$ 5.000 = R$ 135 mil + R$ 499 × 12 = R$ 6 mil ⇒ R$ 141 mil. Com 0,5%: economia/ano R$ 14,6 mi ⇒ ROI = (14,6 mi − 0,141 mi) ÷ 0,141 mi ≈ 102 vezes o custo líquido, ou ≈ 10.200% (mostrado como ≈ 10.000%); retorno 141 mil ÷ (1,22 mi ÷ 30 dias) ≈ 3,5 dias. Com 1%: ROI ≈ 20.600%, retorno ≈ 1,7 dia. **Atenções:** pátio hipotético (o Pecém não tem forno a arco); tarifa hipotética R$ 0,50/kWh (com R$ 0,209 os valores caem ≈ 58%, mas o ROI continua na casa de dezenas de vezes); ganho bruto, sem instalação com NR-10, TCs/TPs, integração, rede, reparos, equipe e parada; o ROI é alto porque o sensor é muito barato frente ao gasto do forno; nenhum percentual de economia está comprovado, a validar no piloto.
- **Larga escala (tela 09):** ilustração sem números; a proporção de máquinas em laranja é só visual e não representa dado nem o 1% do pitch.
- **Forno elétrico a arco (telas 07 e 08):** dados colados pelo Luan (pesquisa de outro chat, não verificada por nós). Relatório anual 2025 do grupo (p. 60): 27 fornos elétricos a arco, 24 Mt/ano de capacidade e 14,6 Mt produzidos em 2025, ≈ 45.062 t/forno/mês. Consumo típico 400–500 kWh/t (Journal of Sustainable Metallurgy). Com 400 kWh/t e R$ 0,50/kWh: 18,0 GWh = R$ 9,0 mi/forno/mês (R$ 9–11,3 mi com 400–500 kWh/t); +15% = R$ 1,35 mi (R$ 1,35–1,7 mi). **Atenções:** (1) o Pecém é usina integrada (alto-forno + convertedor), **não tem forno elétrico a arco**; os 27 fornos são de outras unidades do grupo, então os slides dizem “do grupo” e nunca “do Pecém”; (2) R$ 0,50/kWh é tarifa hipotética e destoa do R$ 209/MWh (R$ 0,209/kWh) do resto do projeto; com R$ 0,209/kWh seriam ≈ R$ 3,8 mi por mês e +15% ≈ R$ 0,56 mi; (3) média por forno, sem diferença de porte; (4) só o processo de fusão, sem auxiliares; (5) forno é carga 100% elétrica, o que combina melhor com o VoltMap do que o forno de coque; (6) para achar desperdício é preciso normalizar por tonelada produzida. O soprador (R$ 2,3 mi/mês; +15% = R$ 345 mil) está em [consumo-mensal-maquinas.md](../consumo-mensal-maquinas.md) e o forno de coque (≈ R$ 128 mil/mês; +15% ≈ R$ 19 mil) ficou na versão anterior destes slides.
- **Rotina e defeito (telas 03 a 05 e 14):** frequências diária/semanal/mensal e a inspeção na segunda são hipóteses ilustrativas, a validar com a manutenção. 159 h = de segunda 18h até a próxima segunda 09h (6 dias e 15 h). Tela 14: 15% × 711 ÷ 720 = 14,81% do consumo mensal da máquina com inspeção mensal. (Para a inspeção semanal, 15% × 159 ÷ 720 = 3,31%, não usado mais na tela 14.) Os +15% são o exemplo do protótipo (AC-02), não um valor típico: ver [estimativas.md](../estimativas.md), onde a maioria dos percentuais base é menor.
- **Mapa:** redução de procura é benefício esperado sem percentual comprovado. Medir separadamente da detecção. Por isso não há número de ganho na tela 17.
- **Economia:** energia evitada exige linha de base ajustada à produção, carga e horas de operação. Descontar custos para calcular ganho líquido. Não somar a oportunidade de 1% a economias de máquinas que já estejam incluídas nela.
- **Produto:** funcionalidades baseadas em [app.md](../app.md). Mockups não comprovam implantação. Persona adaptada de [pitch_prototipov1.md](pitch_prototipov1.md).
