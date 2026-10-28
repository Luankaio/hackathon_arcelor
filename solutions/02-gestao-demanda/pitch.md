# Pitch HoraCerta: 5 minutos

**Tempo total planejado: 4 min 25 s.** Sobram cerca de 35 s de folga para transições e para a demo.
Os números marcados como *estimativa* devem ser falados como estimativa. As fontes estão em `solucao.md`, seção 12.

---

## Slide 1 — O desperdício que ninguém vê (0:30)

**Mesmo MWh, mesmo dia: R$ 57 de manhã, R$ 1.437 à noite.**
Foi o PLD de 15/10/2026 (CCEE).

Na Enel CE, a indústria A4 verde paga **R$ 1.544/MWh na ponta** e **R$ 369 fora dela**: 4,2 vezes mais.

O desperdício não é só o kWh a mais. **É o kWh consumido na hora errada.**

> **Fala:** "No mesmo dia deste mês, o mesmo megawatt-hora custou R$ 57 de manhã e R$ 1.437 à noite. Ninguém na fábrica vê esse número. O desperdício que a gente ataca é o do horário."

---

## Slide 2 — Por que isso importa para a ArcelorMittal Pecém (0:30)

A usina é **autossuficiente**: a termelétrica a gases do processo gerou **1.367 GWh em 2024** e **vende o excedente**.

Então **cada MWh consumido às 19h é um MWh que deixa de ser vendido às 19h.**

E quando a geração cai à noite, a planta pode **passar a importar** justamente no pico de preço. Além disso, exportar acima do contrato em mais de 1% gera multa (REN ANEEL 1.000).

> **Fala:** "A ArcelorMittal gera a própria energia e vende o que sobra. Para ela, consumir na hora cara é deixar dinheiro na mesa. E uma queda de geração às 19h pode virar uma conta muito alta."

---

## Slide 3 — A solução: HoraCerta (0:35)

**Prever → Recomendar → Provar.**

1. **Prevê** consumo, geração e risco de pico com 15 min a 48 h de antecedência (IA de séries temporais com faixa de incerteza).
2. **Recomenda** o que mudar de horário, usando o PLD do dia seguinte (a CCEE publica na véspera) e as regras de contrato. Um otimizador gera ordens como *"mova a carga X das 18h para as 11h: +R$ Y"*.
3. **Prova** o ganho em reais com o protocolo IPMVP de medição e verificação.

Dois modos com o mesmo motor: **Autoprodutor** (ArcelorMittal) e **Grupo A** (PMEs, fornecedores, escolas).

> **Fala:** "A HoraCerta não para no gráfico de consumo. Ela diz o que mudar amanhã, quanto isso vale e prova o resultado no fim do mês."

---

## Slide 4 — Demo (0:50)

**Tela 1: Amanhã.** Geração e consumo previstos, saldo, PLD por hora e o cartão *"valor em jogo amanhã: R$ X"*.

**Tela 2: Ordens.** "Mover moagem (5 MW) de 18h–21h para 10h–13h: +R$ ..." e botão **Aceitar**.

**Tela 3: Radar de 15 min (modo PME).** A demanda projetada encosta no limite, o alerta chega no Telegram, o operador desliga o compressor 2 e a multa é evitada.

**Tela 7: Resultados.** R$ evitados, kWh deslocados, pico reduzido.

*Demo com PLD e tarifas reais e planta sintética, rotulada como tal.*

> **Fala:** "Tudo o que vocês estão vendo usa preço e tarifa reais. A planta é sintética porque ainda não temos os dados da usina, e cada parâmetro é editável para a ArcelorMittal colocar o valor real."

---

## Slide 5 — Como medimos o ganho (0:45)

**Medição e Verificação (IPMVP):** ganho = (linha de base ajustada − real) × preço de cada hora. Para provar a causa: **dias de controle sorteados** sem recomendação.

**PME A4 verde, Enel CE (estimativa):** 80 kW saindo da ponta por 3 h/dia → **≈ R$ 71 mil/ano**. Somando a multa de ultrapassagem evitada → **≈ R$ 77 mil/ano**. A ferramenta custa ≈ R$ 8,6 mil no primeiro ano: **payback de ≈ 1,3 mês**.

**ArcelorMittal (estimativa):** 5 MW deslocados 3 h/dia = **0,33% da geração anual**. Com diferencial de PLD de R$ 100, 250 ou 500/MWh → **R$ 0,45 / 1,1 / 2,25 milhões por ano**. No cenário base, **ROI de 3,7×**.

> **Fala:** "Mudar de horário 0,33% da energia já paga a ferramenta várias vezes no cenário base. Esses números são estimativas com premissas abertas. O número real sai do piloto, com dias de controle."

---

## Slide 6 — Mercado e receita (0:30)

**Âncora:** ArcelorMittal Pecém, com **piloto pago de 90 dias** e depois licença **ou 20–30% da economia verificada**.

**Escala:** outros autoprodutores e eletrointensivos, e **cerca de 202 mil unidades do Grupo A no Brasil** (CCEE). No Pecém, mais de 60 empresas associadas à AECIPP.

**PME:** diagnóstico grátis pela fatura → *Essencial* R$ 290/mês → *Pro* R$ 590/mês + kit IoT.

**Ponto de equilíbrio:** cerca de **34 PMEs** ou **1 contrato âncora**.

> **Fala:** "Começamos com a ArcelorMittal e escalamos para os fornecedores dela e para todo o Grupo A. Uma âncora ou 34 PMEs pagam a operação."

---

## Slide 7 — Viabilidade e diferencial (0:25)

**Viável hoje:** dados públicos reais (CCEE, ONS, ANEEL), stack gratuita (Python, LightGBM, otimizador aberto, FastAPI, Streamlit), kit ESP32 de cerca de R$ 150.

**Seguro:** **somente leitura**, nada escreve na automação, dados fora da rede OT.

**Diferencial:** WeVoltz e Enerlize mostram *onde* se gasta. A HoraCerta diz **em que hora gastar, quanto vale e prova**, e é feita para quem **gera e vende** energia.

> **Fala:** "Os vencedores do ano passado mostraram onde a energia é gasta. Nós mostramos quando gastar, quanto isso vale, e provamos. Tudo isso sem tocar na automação da usina."

---

## Slide 8 — Time e pedido (0:20)

**Time:** [Nome], negócios · [Nome], design · [Nome], dados/IA · [Nome], backend/otimização · [Nome], IoT. IFCE [campus].

**Pedido:** **12 meses de dados horários anonimizados e 90 dias de piloto** na ArcelorMittal Pecém, com M&V e dias de controle.

> **Fala:** "Pedimos dados e 90 dias. Em troca entregamos um número verificado: quanto a ArcelorMittal ganha colocando cada megawatt-hora na hora certa."

---

### Soma dos tempos
0:30 + 0:30 + 0:35 + 0:50 + 0:45 + 0:30 + 0:25 + 0:20 = **4:25** (≤ 5:00).

### Perguntas prováveis da banca e respostas curtas
- **"A ArcelorMittal já tem sistema de energia."** Somos uma camada de decisão econômica e de verificação independente sobre o que já existe. Também temos o Modo Grupo A para os fornecedores dela.
- **"Quanto de carga é flexível?"** Essa é a primeira pergunta do piloto. Se for pouca, o ganho vem do contrato, da ultrapassagem e dos eventos de queda de geração.
- **"E a segurança OT?"** No MVP é somente leitura, por exportação agendada em DMZ, sem escrita em PLC, com NDA e opção on-premises.
- **"E o CO2?"** Com a rede brasileira limpa (38,5 kgCO2/MWh em 2023, MCTI), deslocar carga quase não muda as emissões pelo fator médio. Nosso argumento é custo e confiabilidade, e não prometemos CO2.
