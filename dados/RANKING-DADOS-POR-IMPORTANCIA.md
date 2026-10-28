# Ranking dos dados por importância (desafio 8, ArcelorMittal Pecém)

> Pesquisa de 28/10/2026. Critério de ordem: o quanto o dado ajuda a (1) **metrificar** o ganho das soluções 01 VazioZero, 02 HoraCerta e 03 Sibilo; (2) **calibrar** o exemplo numérico com números da própria ArcelorMittal; (3) **provar** à banca que o ganho é real e relevante; (4) dar **vantagem** sobre outros times.
> Confiança: **Alta** (documento oficial ou trabalho técnico da empresa, lido) · **Média** (imprensa ou base secundária confiável, ou conta derivada com premissas claras) · **Baixa** (trecho de busca, fornecedor, metodologia incerta).
> Itens marcados **[FALTA]** não são públicos, mas seriam críticos. As perguntas para obtê-los estão no fim.
> Detalhes e fontes completas: `pecem.md`, `arcelormittal-brasil.md`, `grupo-global-energia.md`, `projetos-eficiencia-ja-feitos.md`, `benchmarks-setor.md`, `precos-e-tarifas.md`, `inovacao-e-desafios-declarados.md`, `maquinas-e-equipamentos.md`, `fontes.md`.

---

## Top 10 para usar no pitch

1. **1.367 GWh gerados em 2024** pela termelétrica do Pecém, com gases do processo (≈ 156 MW médios). A usina é autossuficiente e vende o excedente ao SIN e a outras unidades do grupo. ([pecem.md §4](pecem.md))
2. **CEO do Pecém (balanço 2024):** a melhoria operacional "permitiu reduzir os custos operacionais e **aumentar o excedente de energia elétrica**". E Tubarão (2018): "melhoria da eficiência energética da planta… fazendo **maior volume de excedente para venda**". **A tese "kWh poupado = kWh vendido" é da própria ArcelorMittal.**
3. **[DERIVADO] Cada 1% de eficiência elétrica no Pecém ≈ 12–14 GWh/ano ≈ R$ 2–3 milhões/ano** (consumo de ≈ 500 kWh/t de placa, calculado a partir de dados da própria CSP; PLD NE 2025 a contrato de longo prazo). **1 MW contínuo = 8.760 MWh/ano ≈ R$ 1,6–2,2 mi/ano.**
4. **ArcelorMittal Brasil (RS 2024): "12 novos projetos em eficiência energética… economia estimada de R$ 63 milhões por ano".** Há apetite e orçamento para o tema.
5. **Grupo: US$ 1,163 bilhão em capex de eficiência energética aprovado em 2025.** E a intensidade energética **piorou** (22,03 → 23,00 GJ/t); a energia recuperada caiu de 27,6% para 24,2% (2023→2025). O problema não está resolvido.
6. **Ar comprimido na régua da ArcelorMittal: 1,01 GJ/1.000 m³ ⇒ 0,11 kWh/m³.** A ArcelorMittal Brasil reporta **845.705 GJ/ano** de ar comprimido (≈ 837 milhões de m³ ≈ **92 GWh/ano**, derivado). Um vazamento de 1 m³/min custa ≈ 58 MWh/ano.
7. **Vanderbijlpark (ArcelorMittal South Africa):** bombas de 1.225 kW ficavam em bypass 50% do tempo; com VSD, **−53% de eletricidade**, pago por **contrato de shared savings**. Ociosidade + modelo de negócio, dentro do Grupo.
8. **Vazamentos de ar comprimido:** ArcelorMittal Bissen **−7% de eletricidade** do ar comprimido numa parada de 3 dias; siderúrgica em MG com ultrassom: **−57,2%** no consumo dos compressores do alto-forno.
9. **Critério de compra da própria ArcelorMittal (Belval):** app fácil para operadores, que meça o impacto das ações, com **ROI em menos de 2 anos**. Resultado: >3%, 9 GWh/ano, ROI em menos de 6 meses.
10. **Fator de CO₂ da própria empresa: 46,0 gCO₂/kWh** (inventário 2024 da ArcelorMittal Brasil). Usar esse, e não fatores de terceiros.

---

## Ranking completo

### 1. Geração da termelétrica do Pecém: 1.367 GWh em 2024 (+7%); ≈ 155,6 MW médios
- **Fonte:** O Povo, 11/01/2025 e 01/05/2025: https://mais.opovo.com.br/jornal/economia/2025/05/01/arcelormittal-pecem-tem-lucro-de-rs-115-bilhao-em-2024-aponta-balanco.html ; ResponsibleSteel (2026): ">1.300 GWh/ano". **Escopo:** Pecém. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03.
- **Como usar:** escala da planta e denominador de "% do excedente". Frase: *"O Pecém gera 1,37 TWh por ano com gases que antes iam para o flare. Nossa ferramenta aumenta a parte desse total que sobra para vender."* Média: 1.367.000 MWh ÷ 8.784 h = 155,6 MW.
- **Detalhe:** [pecem.md §4.1](pecem.md)

### 2. [FALTA] Consumo elétrico interno atual e excedente líquido do Pecém (2024–2025)
- **Por que é crítico:** define quanto vale, em % do excedente, cada MWh poupado (01/03) e quanto há para deslocar ou proteger (02).
- **Como conseguir:** pergunta A1 (abaixo). Enquanto isso, usar o item 3.

### 3. Consumo interno histórico: 138 MW médios (~2017) e "168 MW" (~2019–2020) ⇒ ≈ 500 kWh por tonelada de placa
- **Fontes:** Kogake, ABM 2017 (geração de 155, consumo de 138, excedente de 17 MW médios): https://abmproceedings.com.br/en/article/inicio-da-operacao-da-termoeletrica-da-csp ; CEPAL 2020, p.15 (coautoria de funcionários da CSP): https://archivo.cepal.org/pdfs/bigpushambiental/Caso19-CSPCeara.pdf . **Escopo:** Pecém. **Confiança:** Alta (dados), Média (conta).
- **Ajuda:** 01, 02, 03.
- **Como usar:** [DERIVADO] 138 MW × 8.760 h ÷ 2,417 Mt (2017) = 500 kWh/t; 168 MW × 8.760 ÷ 2,94 Mt (2018) = 501 kWh/t. Hoje, como a planta se diz autossuficiente com 1.367 GWh, o consumo deve estar entre ~1.200 e 1.360 GWh/ano, e o **excedente é estreito (0 a ~170 GWh/ano)**. Frase: *"Pelos números publicados pela própria CSP, a usina consome cerca de 500 kWh por tonelada. Cada 1% disso são 12 a 14 GWh por ano."*
- **Detalhe:** [pecem.md §4.2](pecem.md)

### 4. Declaração do CEO: eficiência "permitiu reduzir os custos operacionais e aumentar o excedente de energia elétrica"; venda intragrupo do excedente (2024)
- **Fonte:** O Povo, 01/05/2025 (link no item 1). **Escopo:** Pecém. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03 (é a tese central das três).
- **Como usar:** abertura ou slide de problema. Frase: *"Em 2024 o Pecém mostrou que eficiência vira excedente vendido. A gente transforma isso em rotina, máquina por máquina."*
- **Detalhe:** [pecem.md §4.1](pecem.md)

### 5. [FALTA] Valor do MWh excedente (PLD, contrato ou preço intragrupo)
- **Por que é crítico:** multiplica todo o ganho em R$.
- **Faixa pública para usar enquanto isso:** R$ 178/MWh (PLD NE médio jan–nov/2025) a R$ 233–250 (contratos de longo prazo). Ver item 21.
- **Como conseguir:** pergunta A2.

### 6. Tubarão (ArcelorMittal, 2018): "melhorar o modelo pela melhoria da eficiência energética da planta, reduzindo nossas necessidades de energia externa e fazendo maior volume de excedente para venda de energia, agregando valor ao core business"
- **Fonte:** Assis, F. V., Gerência de Produção de Energia de Tubarão, X Fenergia/Findes 2018, slide 7: https://findes.com.br/wp-content/uploads/2018/07/X-Fenergia-Fabricio-Assis-Findes.pdf . **Escopo:** Tubarão (usina-irmã, mesmo modelo). **Confiança:** Alta.
- **Ajuda:** 01, 02, 03.
- **Como usar:** citação literal no slide de valor: *"A própria ArcelorMittal escreveu: eficiência = mais excedente para venda."*
- **Detalhe:** [arcelormittal-brasil.md §5](arcelormittal-brasil.md)

### 7. ArcelorMittal Brasil: 12 projetos de eficiência energética, economia estimada de R$ 63 mi/ano; Plano Diretor de eficiência energética
- **Fonte:** RS 2024 da ArcelorMittal Brasil, PDF p.64: https://brasil.arcelormittal.com/assets/pdf/arcelormittal/publications-reports/relatorio-de-sustentabilidade-2024.pdf . **Escopo:** Brasil. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03 (relevância e orçamento).
- **Como usar:** *"Vocês já têm 12 projetos de R$ 63 milhões por ano. A gente propõe o 13º: barato, rápido e com medição contínua."* Perguntar quais estão no Pecém (C23).
- **Detalhe:** [arcelormittal-brasil.md §4](arcelormittal-brasil.md)

### 8. Fator oficial do Grupo para ar comprimido: 1,01 GJ por 1.000 m³ ⇒ 0,1097 kWh/m³ (≈ 6,58 kW por m³/min)
- **Fonte:** ArcelorMittal Sustainability Report 2025, Basis of Reporting, PDF p.74 (Ut-09; eletricidade 9,208 GJ/MWh): https://cdn.arcelormittal.com/media/kyqeahax/2025-sd-report-22-april-2026-final-upload.pdf . **Escopo:** Grupo. **Confiança:** Alta.
- **Ajuda:** **03** (principal), 01.
- **Como usar:** `kWh evitados = m³ de vazamento evitados × 0,1097`; 1 m³/min contínuo = 57,7 MWh/ano. Frase: *"Usamos o mesmo fator de energia do ar comprimido que a ArcelorMittal usa no relatório de sustentabilidade."* Muito parecido com o padrão DOE da solução 03 (6,36 kW por m³/min); o fator da empresa é ~3,5% maior.
- **Detalhe:** [grupo-global-energia.md §3](grupo-global-energia.md)

### 9. Ar comprimido na ArcelorMittal Brasil: 845.705 GJ (2024); 844.369 (2023); 872.844 (2022) ⇒ ≈ 837 milhões de m³/ano ≈ 92 GWh/ano [derivado]
- **Fonte:** RS 2024 da ArcelorMittal Brasil, Caderno de Indicadores, PDF p.101 (link no item 7) + fator do item 8. **Escopo:** Brasil. **Confiança:** Alta (GJ), Média (conversão: não sabemos se cobre todo o ar comprimido nem se inclui todo o Pecém).
- **Ajuda:** **03**, 01.
- **Como usar:** 845.705 ÷ 1,01 = 837 M m³ ≈ 1.590 m³/min médios; × 0,1097 = 92 GWh ≈ 10,5 MW médios. Se o vazamento cair de 20% para 10% (CAC/DOE): ≈ 9,2 GWh/ano ≈ R$ 1,6–2,3 mi/ano. Frase: *"Só a linha de ar comprimido do relatório da ArcelorMittal Brasil equivale a ~90 GWh por ano. Dez pontos de vazamento a menos valem cerca de R$ 2 milhões."*
- **Detalhe:** [arcelormittal-brasil.md §2.4](arcelormittal-brasil.md)

### 10. [FALTA] Estação de ar comprimido do Pecém (nº de compressores, kW, controle, pressão, vazão, medidores, % de vazamento)
- **Por que é crítico:** substitui as premissas da solução 03 (60 vazamentos, f_c) e da 01 (compressor de 110 kW).
- **Como conseguir:** perguntas B8–B10.

### 11. Fator de emissão usado pela ArcelorMittal Brasil: 46,0 gCO₂/kWh (média do SIN out/2023–set/2024); Grupo usa 52,8 kgCO₂/MWh para o Brasil (2025)
- **Fonte:** RS 2024, PDF p.99 (link no item 7); SR 2025, PDF p.70. **Escopo:** Brasil/Grupo. **Confiança:** Alta.
- **Ajuda:** 01, 03 (CO₂ evitado; a 02 desloca carga e quase não reduz kWh).
- **Como usar:** `tCO₂ = MWh × 0,046`. Frase: *"Calculamos o CO₂ com o mesmo fator do inventário da ArcelorMittal Brasil."*
- **Detalhe:** [precos-e-tarifas.md §4](precos-e-tarifas.md)

### 12. Vanderbijlpark (ArcelorMittal South Africa): 5 bombas de 1.225 kW em bypass 50% do tempo; VSD ⇒ −53% de eletricidade, 13,6 mi de rands/ano; financiado por shared savings
- **Fonte:** MechChem Africa, set/2018: https://www.crown.co.za/latest-news/mechchem-africa-latest-news/7984-industrial-efficiency-initiatives-an-amsa-success-story . **Escopo:** Grupo (África do Sul). **Confiança:** Alta.
- **Ajuda:** **01** (ociosidade + monetização).
- **Como usar:** *"Numa usina da própria ArcelorMittal, bombas gigantes passavam metade do tempo girando à toa. Corrigir isso cortou 53% da energia, e foi pago com economia compartilhada, o modelo que propomos."*
- **Detalhe:** [projetos-eficiencia-ja-feitos.md C7](projetos-eficiencia-ja-feitos.md)

### 13. Belval (ArcelorMittal Luxemburgo): critério "ROI em menos de 2 anos"; resultado >3% de economia, € 150 mil/ano, 9 GWh/ano, ROI em menos de 6 meses
- **Fonte:** Energiency/InnoEnergy: https://innoenergy.com/uploads/2023/01/success-story-arcelormittal-energiency-eng.pdf . **Escopo:** Grupo. **Confiança:** Alta (case do fornecedor com falas da ArcelorMittal).
- **Ajuda:** 01, 02 (software + IA de energia).
- **Como usar:** slide de viabilidade: payback do piloto vs. o corte de 2 anos da ArcelorMittal. Frase: *"Nosso payback estimado é de meses, bem abaixo dos 2 anos que a ArcelorMittal exigiu em Belval."*
- **Detalhe:** [inovacao-e-desafios-declarados.md §2](inovacao-e-desafios-declarados.md)

### 14. Bissen (ArcelorMittal Luxemburgo): reparo de vazamentos de ar comprimido numa parada de 3 dias ⇒ ~7% menos eletricidade para ar comprimido; 35% dos vazamentos ainda abertos depois
- **Fonte:** https://www.klimapaktfirbetriber.lu/en/case-studies/economies-en-air-comprime-a-lusine-de-bissen-darcelormittal/ . **Escopo:** Grupo. **Confiança:** Alta.
- **Ajuda:** **03**.
- **Como usar:** *"Na ArcelorMittal Bissen, uma única campanha cortou 7%, mas um terço dos vazamentos continuou aberto. O Sibilo transforma a campanha em rotina."*
- **Detalhe:** [projetos-eficiencia-ja-feitos.md C6](projetos-eficiencia-ja-feitos.md)

### 15. Siderúrgica em MG: ultrassom + reparo de vazamentos nos compressores do alto-forno ⇒ −57,2% no consumo elétrico médio mensal (327.825 → 140.324 kWh/mês)
- **Fonte:** REM – International Engineering Journal, v.70, n.4, 2017, DOI 10.1590/0370-44672015700189: https://www.scielo.br/j/remi/a/fGPXZbrst9Qfrk69k4qSWDn/?lang=en . **Escopo:** setor (Brasil). **Confiança:** Alta para o percentual (resumo de artigo revisado por pares); Média para os kWh (vistos em trecho indexado).
- **Ajuda:** **03**.
- **Como usar:** prova de que o ultrassom funciona em siderúrgica brasileira; usar como teto otimista, não como base.
- **Detalhe:** [projetos-eficiencia-ja-feitos.md D1](projetos-eficiencia-ja-feitos.md)

### 16. Grupo: US$ 1.163 mi em capex de eficiência energética aprovados em 2025 (US$ 326 mi em 2024; US$ 1.716 mi em 2023)
- **Fonte:** SR 2025, Annex 1, PDF p.52 (link no item 8). **Escopo:** Grupo. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03 (relevância).
- **Como usar:** *"Eficiência energética é linha de investimento bilionária na ArcelorMittal."*
- **Detalhe:** [grupo-global-energia.md §1](grupo-global-energia.md)

### 17. Intensidade energética: Grupo 23,00 GJ/t (2025; era 22,03 em 2024); energia recuperada 24,2% (era 27,6% em 2023). Brasil: 20,46 → 20,78 GJ/t (2018→2024, +1,6%) e "não foram registradas reduções nos requisitos energéticos"
- **Fontes:** SR 2025, PDF p.52; RS 2024 da ArcelorMittal Brasil, PDF p.102. **Escopo:** Grupo/Brasil. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03 (problema).
- **Como usar (com tato):** *"Os relatórios mostram que a intensidade energética ficou estável ou subiu. O espaço está no consumo controlável do dia a dia."*
- **Detalhe:** [inovacao-e-desafios-declarados.md §4](inovacao-e-desafios-declarados.md)

### 18. Termelétrica do Pecém: 218 MW outorgados em 3 unidades (18 + 100 + 100 MW); 200 MW citados pela operação; TRT de 16 MW; conexão à Rede Básica em 230 kV (SE Pecém II); vapor de processo de 90 t/h (65 t/h médios no início)
- **Fontes:** Diário do Nordeste, 15/10/2016 (ANEEL): https://diariodonordeste.verdesmares.com.br/negocios/termeletrica-da-siderurgica-entra-em-operacao-1.1634642 ; CEPAL 2020 (TRT); ABM 2017. **Escopo:** Pecém. **Confiança:** Alta.
- **Ajuda:** **02** (restrições de geração, conexão), 03 (roadmap vapor).
- **Como usar:** parametrizar a "planta sintética" da 02 (teto de 200–218 MW, TRT ≈ 10% da geração). Mostra que a recuperação "grossa" já existe; sobra o "fino" (utilidades).
- **Detalhe:** [pecem.md §3](pecem.md), [maquinas-e-equipamentos.md §1](maquinas-e-equipamentos.md)

### 19. [FALTA] Inventário de motores de utilidades sem medição individual (bombas, exaustores, correias, ventiladores acima de 100 kW) e existência de historian/EMS
- **Por que é crítico:** define o tamanho do piloto da 01 e se a solução vira camada de software sobre medidores existentes.
- **Como conseguir:** perguntas A6, B11–B13.

### 20. Dofasco (ArcelorMittal Canadá): ISO 50001 ⇒ +6,16% de desempenho energético em 3 anos (1,72 mi GJ), US$ 15,3 mi poupados, custo de US$ 250 mil; gerente de energia: "~70% é termodinâmica… focamos nos ~30% restantes"
- **Fonte:** https://www.cleanenergyministerial.org/content/uploads/2022/03/cem-em-casestudy-arcelormittal-canada.pdf . **Escopo:** Grupo. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03.
- **Como usar:** frase de abertura ("30% é controlável") e prova de ROI de gestão de energia (60× o custo).
- **Detalhe:** [projetos-eficiencia-ja-feitos.md C1–C2](projetos-eficiencia-ja-feitos.md)

### 21. Preços para valorar o MWh: PLD NE médio jan–nov/2025 ≈ R$ 178 (de R$ 58,60 a 275,04 por mês); contrato convencional de longo prazo 2027–30 R$ 190,76 (nov/2025); Abraceel R$ 233 (mar/2026)
- **Fonte:** Amee, boletim de nov/2025: https://amee.com.br/boletim-informativo-mensal-novembro-2025/ ; solução 03 (Abraceel). **Escopo:** Nordeste/Brasil. **Confiança:** Alta (dados), média simples nossa.
- **Ajuda:** 01, 02, 03.
- **Como usar:** duas linhas no slide: conservadora (R$ 178) e base (R$ 233–250). `R$ = MWh × preço`.
- **Detalhe:** [precos-e-tarifas.md §1–2](precos-e-tarifas.md)

### 22. Limites e volatilidade do PLD 2026: piso R$ 57,31; teto horário R$ 1.611,04; 15/10/2026 de R$ 57 (dia) a R$ 1.437 (noite); 01/01/2026 de R$ 57,31 (8h–14h) a R$ 197,18 (20h)
- **Fontes:** Grugeen; solução 02 (Agência Infra); DGABC/CCEE. **Escopo:** Nordeste. **Confiança:** Alta.
- **Ajuda:** **02**.
- **Como usar:** `R$ = MWh deslocados × (PLD_origem − PLD_destino)`. Ainda é preciso medir o spread médio real com o CSV da CCEE (script da solução 02).
- **Detalhe:** [precos-e-tarifas.md §2](precos-e-tarifas.md)

### 23. Saldanha (ArcelorMittal South Africa): 10,6 MW (6,6%) poupados sobre 160 MW de linha de base em 2012; medidas: VSD, desligar equipamento ocioso, ar comprimido da ASU, bombas sem capex; ISO 50001. "Sustaining these savings can be quite difficult…"
- **Fonte:** https://www.powersystemsdesign.com/articles/western-capes-largest-electricity-consumer-saves-r90-million-in-one-year-with-energy-efficiency-project/8/4904 . **Escopo:** Grupo. **Confiança:** Alta.
- **Ajuda:** 01, 03.
- **Como usar:** ordem de grandeza de um programa sério: **~6–7% do consumo elétrico**. No Pecém, 6,6% de ~1.300 GWh ≈ 86 GWh/ano (derivado, só ilustrativo). A frase sobre sustentar o ganho justifica o M&V contínuo.
- **Detalhe:** [projetos-eficiencia-ja-feitos.md C8](projetos-eficiencia-ja-feitos.md)

### 24. Fos-sur-Mer (ArcelorMittal França, integrada parecida com o Pecém): 53 oportunidades elétricas, € 2,5–4,3 mi/ano; 3 quick wins sem capex (€ 120 mil/ano, payback menor que 1 ano); áreas incluem despoeiramento e ar comprimido
- **Fonte:** ABB CAS069a (2011): https://library.e.abb.com/public/33218edc3d91bf91852579270060c990/Case%20study%20-%20Energy%20Savings%20at%20Steel%20Milll(CAS069a)LowRes.pdf . **Escopo:** Grupo. **Confiança:** Alta (case do fornecedor com falas da ArcelorMittal).
- **Ajuda:** 01, 03.
- **Como usar:** *"Numa usina integrada da ArcelorMittal, um diagnóstico achou 53 oportunidades elétricas, três delas sem nenhum investimento."*
- **Detalhe:** [projetos-eficiencia-ja-feitos.md C5](projetos-eficiencia-ja-feitos.md)

### 25. Resultado do Pecém em 2025: prejuízo de R$ 168,6 mi; receita de R$ 9,248 bi (−11,9%); EBITDA de R$ 0,69 bi (−60%)
- **Fonte:** O Povo, 30/04/2026: https://mais.opovo.com.br/jornal/economia/2026/04/30/arcelormittal-pecem-sofre-com-tarifaco-e-tem-prejuizo-em-2025.html . **Escopo:** Pecém. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03 ("por que agora").
- **Como usar:** *"Num ano de margem apertada, receita extra de energia sem capex grande faz diferença."* (Sem tom alarmista.)
- **Detalhe:** [pecem.md §8](pecem.md)

### 26. Laminador de tiras a quente no Pecém: R$ 35 mi em engenharia (jul/2026); R$ 4–5 bi; 1,5 Mt/ano de bobinas; decisão no fim de 2026
- **Fontes:** O Povo, 03/07/2026; Bloomberg Línea, 30/09/2026 (ver `fontes.md` S17). **Escopo:** Pecém. **Confiança:** Alta (fato), qualitativa (efeito na energia).
- **Ajuda:** **02**, 01.
- **Como usar:** *"Se a laminação vier, a usina passa a consumir muito mais energia. O excedente encolhe, e cada MW gerenciado vale mais."*
- **Detalhe:** [pecem.md §9](pecem.md)

### 27. Excedente vendido no 1º ano: 436,2 mil MWh (out/2016–set/2017) ≈ 49,8 MW médios
- **Fonte:** Informativo ZPE nº 11 (MDIC): https://www.gov.br/mdic/pt-br/assuntos/zpe/arquivos/informativo_zpe_-_edicao011.pdf . **Escopo:** Pecém. **Confiança:** Alta (dado antigo, de ramp-up).
- **Ajuda:** 02.
- **Como usar:** mostra que o excedente varia muito com a produção (com menos aço, mais sobra). Não usar como valor atual.
- **Detalhe:** [pecem.md §4.1](pecem.md)

### 28. Projetos de energia já feitos no Pecém (ABM): queima simultânea BFG + COG (2023); operação sem gasômetro (2024); controle estequiométrico no lingotamento (−20% e −40% de gás, 2018); barra segura contra distúrbios de frequência (2017)
- **Fontes:** ABM Proceedings (S09–S12 em `fontes.md`). **Escopo:** Pecém. **Confiança:** Alta (resumos).
- **Ajuda:** 02 (gases, eventos), 01 (controle + medição).
- **Como usar:** mostrar que conhecemos o trabalho da equipe local. *"A equipe de energia do Pecém já otimizou a geração com os gases; o próximo passo é o consumo das utilidades."*
- **Detalhe:** [pecem.md §10](pecem.md)

### 29. worldsteel: energia = 20–40% do custo de produção do aço; intensidade média de 20,95 GJ/t; CO₂ de 1,92 t/t (2024); BF-BOF 2,34 tCO₂/t; numa integrada, ~35% da energia de entrada é eletricidade
- **Fontes:** fact sheet worldsteel: https://www.steel.org.au/getattachment/bfc722b0-1320-4d04-84df-30bdd500aa5b/fact_energy_2016.pdf ; Sustainability Indicators 2025. **Escopo:** mundo. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03 (problema).
- **Como usar:** frase de problema. Atenção à correção C2 (a solução 03 usa 15–20%).
- **Detalhe:** [benchmarks-setor.md §1](benchmarks-setor.md)

### 30. EPE (Rota 1): eletricidade por etapa (GJ/t): coqueria 0,204 · sínter 0,552 · alto-forno 0,488 · aciaria 0,466 · laminação 1,110 · sistema de energia e outros 1,197; **VSD nas utilidades: US$ 0,05/t, 0,02 GJ/t, payback de 0,5 ano**
- **Fonte:** EPE/Qualitec, Produto 5, Tab. 37 e 71: https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-314/topico-407/Produto%205%20-%20Relatorio%20da%20cadeia%20sider%C3%BArgica.pdf . **Escopo:** setor (Brasil, dados de 2015). **Confiança:** Alta (dados), Média (aplicação ao Pecém).
- **Ajuda:** 01.
- **Como usar:** [DERIVADO] 0,02 GJ/t × 3 Mt ≈ 16,7 GWh/ano ≈ R$ 3–4 mi/ano, com investimento de ~US$ 150 mil, só em VSD nas utilidades. Também mostra onde está o consumo (sínter, AF, aciaria, utilidades).
- **Detalhe:** [benchmarks-setor.md §3](benchmarks-setor.md)

### 31. Aço Brasil (2024): 48% da eletricidade das usinas vem de autogeração (~7 TWh autogerados, ~7,7 TWh comprados; 33,9 Mt) ⇒ ≈ 434 kWh/t no setor [derivado]
- **Fonte:** https://www.acobrasil.org.br/site/wp-content/uploads/2025/09/Folder_AcoBrasil_Sustentabilidade_2025.pdf . **Escopo:** Brasil. **Confiança:** Alta (dado), Média (conta).
- **Ajuda:** 01, 02 (o Pecém está acima da média do setor em kWh/t, o que é coerente para integrada; o mercado de autoprodutores é grande).
- **Detalhe:** [benchmarks-setor.md §2](benchmarks-setor.md)

### 32. Meta de CO₂ do Grupo para 2030 revisada: "up to a 10% reduction" na intensidade dos escopos 1+2 vs 2018 (antes −25%); net zero em 2050 mantido
- **Fonte:** SR 2025, PDF p.23 (link no item 8); ResponsibleSteel Pecém 2026. **Escopo:** Grupo. **Confiança:** Alta.
- **Ajuda:** 01, 03 (narrativa).
- **Como usar:** **não** citar "−25%". Frase: *"Com a meta de 2030 em até −10%, eficiência é a alavanca que entrega sem esperar tecnologia nova."*
- **Detalhe:** [grupo-global-energia.md §2](grupo-global-energia.md)

### 33. Autogeração da ArcelorMittal Brasil: 59–61% (2024); "Já atingimos 85%" (CEO de Aços Longos, mar/2026); Babilônia deve suprir 38% da eletricidade em 2030; R$ 5,8 bi em renováveis
- **Fontes:** RS 2024; Exame, 25/03/2026; Annual Report 2025. **Escopo:** Brasil. **Confiança:** Alta (com a contradição meta × fala registrada).
- **Ajuda:** 02 (valor do excedente intragrupo pode cair quando outras unidades passam a se autoabastecer).
- **Detalhe:** [arcelormittal-brasil.md §4](arcelormittal-brasil.md)

### 34. Inovação na ArcelorMittal Brasil: meta de ~R$ 1 bi em ganhos até 2028, com "impacto direto e mensurável no resultado"; iNO.VC com mais de US$ 90 mi validados em 5 anos e hub no Ceará; R$ 278 mi em ganhos digitais e de IA em 2025; IA com retorno de 18× (R$ 180 mil → R$ 3,3 mi)
- **Fontes:** RS 2024, PDF p.29; Jornal Empresarial (jul/2026); O Povo, 15/10/2026. **Escopo:** Brasil. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03 (canal de entrada e linguagem).
- **Como usar:** *"Vocês pedem inovação com impacto mensurável no resultado. Nossa métrica é kWh verificado em R$."*
- **Detalhe:** [inovacao-e-desafios-declarados.md §1](inovacao-e-desafios-declarados.md)

### 35. Pecém no programa digital do Grupo: uma das 4 unidades brasileiras do programa global (2024) e um dos 6 sites do Accelerated Digital Innovation (2025), com sensores + câmeras + IA na sinterização
- **Fontes:** RS 2024, PDF p.29; SR 2025, PDF p.31. **Escopo:** Pecém. **Confiança:** Alta.
- **Ajuda:** 01 (mesma arquitetura sensor + IA; já existe infraestrutura e cultura).
- **Detalhe:** [inovacao-e-desafios-declarados.md §1](inovacao-e-desafios-declarados.md)

### 36. Trilha 2025: 1º WeVoltz e 2º Enerlize (monitoramento genérico de energia); critérios (clareza da problemática, proposta de valor, segmento, monetização e sustentabilidade financeira, viabilidade técnica e operacional); banca com a gerente de Comunicação e RI da ArcelorMittal Pecém
- **Fontes:** SGA Notícias e Sebrae/CE (S41, S42). **Escopo:** Pecém. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03 (estratégia de pitch).
- **Como usar:** não repetir "monitoramento genérico". Falar para um público **misto (técnico e não técnico)**, com um número em R$ e uma história concreta.
- **Detalhe:** [inovacao-e-desafios-declarados.md §5](inovacao-e-desafios-declarados.md)

### 37. Conversões e fatores do Grupo: eletricidade 9,208 GJ/MWh (primária); vapor AP 3.350 MJ/t; vapor BP 3.050 MJ/t; O₂ 6,54 GJ/1.000 m³; N₂ e Ar 1,84 GJ/1.000 m³
- **Fonte:** SR 2025, PDF p.74. **Escopo:** Grupo. **Confiança:** Alta.
- **Ajuda:** 03 (roadmap vapor/N₂), 01.
- **Como usar:** converter qualquer economia para GJ "padrão ArcelorMittal", que é o indicador que ela reporta (Energy intensity, GJ/t).
- **Detalhe:** [grupo-global-energia.md §3](grupo-global-energia.md)

### 38. Tarifa Enel CE para PMEs: recálculo pelo Despacho ANEEL 3.324/2026 (desde 26/08/2026): efeito médio −5,87%; média e alta tensão −3,29 p.p. em relação a abril
- **Fonte:** FIEC: https://www1.sfiec.org.br/fiec-noticias/search/173808/aneel-aprova-recalculo-das-tarifas-da-enel-ceara-e-clientes-terao-reducao-media-de-587 . **Escopo:** Ceará. **Confiança:** Média (percentual em p.p.; tabela nova não lida).
- **Ajuda:** 01, 02, 03 (segmento PME).
- **Como usar:** atualizar os R$ 369/1.544 por MWh das soluções (ver correção C8).
- **Detalhe:** [precos-e-tarifas.md §3](precos-e-tarifas.md)

### 39. Equipamentos do Pecém: alto-forno de 3.800 m³; 2 BOF de 300 t; coqueria com fornos de 7,63 m; sínter de 4,7 Mt/ano; correias até o porto (~10 km); placas até 300 mm; 2.634 empregados diretos (6.986 com terceiros)
- **Fontes:** GEM, CEPAL, ResponsibleSteel, Annual Report 2025. **Escopo:** Pecém. **Confiança:** Média/Alta.
- **Ajuda:** 01 (correias e exaustores são alvos de ociosidade), 03.
- **Detalhe:** [maquinas-e-equipamentos.md §1](maquinas-e-equipamentos.md)

### 40. Oxigênio vindo da White Martins (ZPE, mais de 2.000 t/dia de gases; a CSP é a principal cliente, 2020–21); o escopo ResponsibleSteel 2026 cita "gas plant for O2, argon"
- **Fontes:** O Povo, 2021; ResponsibleSteel 2026. **Escopo:** Pecém. **Confiança:** Média (situação atual).
- **Ajuda:** 02 (se o O₂ for de terceiros, a maior carga elétrica de separação de ar não é da ArcelorMittal).
- **Detalhe:** [pecem.md §3](pecem.md)

### 41. Tubarão (referência de equipamentos): 500 MW de geração; TRT de 25 MW (16 MW médios); CDQ de 5 × 25 t/h; Sol com 2 × 98 MW (1.226 GWh/ano); Centro de Energia; perdas de vapor de ~3 t/h
- **Fonte:** Fenergia 2018 (item 6). **Escopo:** Tubarão. **Confiança:** Alta (dado de 2018).
- **Ajuda:** 02, 03 (vapor).
- **Detalhe:** [maquinas-e-equipamentos.md §2](maquinas-e-equipamentos.md)

### 42. "Power of 1" (então ArcelorMittal USA): automatizar 1 de 2 bombas hidráulicas do lingotamento contínuo (só CLP); desligar ar comprimido entre ciclos na LMF (−90% nesse uso); baseline antes e depois
- **Fonte:** DOE Better Buildings (via solução 01, F7; site fora do ar em 28/10/2026). **Escopo:** ex-Grupo (vendida à Cleveland-Cliffs em 09/12/2020). **Confiança:** Média.
- **Ajuda:** 01, 03.
- **Como usar:** citar como "na época, ArcelorMittal USA" e preferir os casos atuais (itens 12, 14, 23).
- **Detalhe:** [projetos-eficiencia-ja-feitos.md C11](projetos-eficiencia-ja-feitos.md)

### 43. Fornecedores locais e território: R$ 1,42 bi em compras de fornecedores cearenses (2024); Território Empreendedor com mais de 48 mil microempreendedores; CIPP com dezenas de indústrias
- **Fontes:** Diário do Nordeste, 10/06/2026; RS 2024. **Escopo:** Ceará. **Confiança:** Alta.
- **Ajuda:** 01, 02, 03 (segmento secundário: fornecedores/PMEs com apoio do Sebrae).
- **Detalhe:** [pecem.md §7](pecem.md)

### 44. Energia = 5–8% do custo de produção do aço (pv magazine, sobre a ArcelorMittal Brasil, sem atribuição clara)
- **Fonte:** https://www.pv-magazine-brasil.com/2025/12/09/arcelormittal-inaugura-parque-solar-de-320-mw-em-minas-gerais/ . **Escopo:** Brasil. **Confiança:** Baixa.
- **Ajuda:** — (usar só se perguntarem; provavelmente se refere à eletricidade).

### 45. Faixa de ar comprimido em siderúrgicas: 5–20% da eletricidade (fabricantes e fornecedores, sem estudo independente); ~10% na indústria típica (DOE)
- **Fontes:** ver `benchmarks-setor.md` §4. **Escopo:** setor. **Confiança:** Baixa (siderurgia), Alta (DOE geral).
- **Ajuda:** 03.
- **Como usar:** só como faixa de sensibilidade, nunca como número do Pecém.

---

## Correções às soluções atuais

> Os arquivos das soluções **não** foram editados. Abaixo está o que os dados públicos contradizem ou atualizam.

| # | Solução | Premissa atual | O que os dados mostram | Sugestão |
|---|---|---|---|---|
| C1 | 01, 02, 03 (pitch) | Qualquer menção a "meta de −25% de CO₂ até 2030" | O Grupo revisou para **"até −10%" até 2030 vs 2018** (SR 2025, abr/2026; ResponsibleSteel Pecém 2026) | Não citar −25% |
| C2 | 03 (solucao.md §1.2 e pitch) | "Energia é 15–20% do custo do aço (worldsteel)" | O fact sheet oficial da worldsteel diz **20–40%**. O 15–20% é uma fala de 2015 do diretor-geral. A imprensa brasileira cita 5–8% para a ArcelorMittal Brasil (provavelmente só eletricidade) | Usar "20–40% (worldsteel)" ou citar a faixa com a fonte |
| C3 | 01, 03 | Fator do SIN de 0,0545 (2024, de terceiros) ou 0,0385 (2023) | A **ArcelorMittal Brasil usou 46,0 gCO₂/kWh** no inventário 2024; o Grupo usa **52,8** para o Brasil (2025) | Usar 0,046 tCO₂/MWh ("fator da própria empresa"). Os resultados de CO₂ da 03 caem ~16% (0,046 ÷ 0,0545) |
| C4 | 02 (§1.2, "não confirmado") | Capacidade da termelétrica e ponto de conexão não confirmados | **218 MW outorgados (18 + 100 + 100 MW)**; 200 MW citados pela operação; **TRT de 16 MW**; **Rede Básica, LT de 230 kV até a SE Pecém II** (ANEEL via DN 2016; CEPAL 2020; ABM 2017) | Trocar "premissa" por "fato" nesses itens |
| C5 | 01, 02, 03 | "Excedente vendido ao SIN"; valor do kWh = PLD/mercado | Em 2024 houve **venda intragrupo** do excedente para outras unidades no Brasil (O Povo, 01/05/2025). O preço pode ser de transferência interna, não PLD. Pelos dados históricos (≈ 500 kWh/t), o **excedente atual deve ser estreito** (0–12% da geração) | Mostrar faixa de preço (R$ 178–250) e perguntar o preço interno. Reforçar que "1 MW poupado é uma fatia grande do excedente" |
| C6 | 02 | Planta sintética de 156 MW de geração com cargas flexíveis de 5 MW | Coerente com a geração (155,6 MW em 2024). Mas o consumo interno pode estar perto da geração. **O "Modo Autoprodutor" deve tratar o saldo como variável que pode ficar negativo** (risco de importação, já reconhecido pela planta: barra segura, gasômetro) | Dar mais peso ao cenário "evitar importação na hora cara" do que à arbitragem pura |
| C7 | 02 (§1.2) | "O oxigênio vem da White Martins, então a ASU não é carga da ArcelorMittal" | Confirmado por fontes de 2020–21 (planta de mais de 2.000 t/dia; CSP como principal cliente), mas o escopo ResponsibleSteel 2026 inclui "gas plant for O2, argon" | Manter como "provável", validar (pergunta B15) |
| C8 | 01, 02, 03 (segmento PME) | Tarifas A4 da REH 3.574/2026 (FP R$ 369,17; P R$ 1.543,97/MWh) | O **Despacho ANEEL 3.324/2026** (desde 26/08/2026) reduziu o efeito para média e alta tensão em **~3,29 p.p.** | Recalcular com a tabela vigente; a ordem de grandeza não muda |
| C9 | 01 (§1.2 e §6) | "Power of 1 da própria ArcelorMittal" | A ArcelorMittal USA foi **vendida à Cleveland-Cliffs em 09/12/2020** | Dizer "da então ArcelorMittal USA" e somar casos atuais do Grupo: Vanderbijlpark (−53%), Saldanha (6,6%), Bissen (−7%), Dofasco (+6,16%) |
| C10 | 01 | Exemplo do piloto: 156 MWh/ano ≈ R$ 39 mil | Correto como piloto, mas é ~0,01% da geração do Pecém. A banca pode achar pequeno | Mostrar a escala: "1% do consumo do Pecém ≈ 12–14 GWh/ano ≈ R$ 2–3 mi"; "programas do Grupo entregaram 6–7% (Saldanha)" |
| C11 | 03 | Potência específica do DOE: 6,36 kW por m³/min | O fator oficial da ArcelorMittal (1,01 GJ/1.000 m³) equivale a **6,58 kW por m³/min** (0,1097 kWh/m³) | Usar o fator da empresa ("mesma régua do relatório de sustentabilidade"); os resultados de energia sobem ~3,5% |
| C12 | 03 | Preço base R$ 233/MWh; conservador R$ 135 | O PLD NE médio jan–nov/2025 foi ≈ **R$ 178**; o contrato convencional de longo prazo (nov/2025) foi R$ 190,76 | Usar R$ 178 como "conservador com dado público" |
| C13 | 02 (§1.2) | "ISO 50001 no Pecém: não encontrada" | Continua não encontrada. O Grupo tem ISO 50001 em Dofasco, Gent/Genk/Geel, Belval/Differdange, Dabrowa e Warszawa; Saldanha também implantou | Manter como pergunta; citar os sites certificados como benchmark |

---

## Dados críticos que faltam e como conseguir no Ideathon

> Perguntas prontas, em ordem de prioridade. Lista completa (27 perguntas) em [lacunas-perguntas-para-ideathon.md](lacunas-perguntas-para-ideathon.md).

| Prioridade | Dado que falta | Pergunta pronta para o mentor ou representante | Ajuda |
|---|---|---|---|
| 1 | Consumo interno e excedente atuais | "A termelétrica gerou 1.367 GWh em 2024. Quanto disso a usina consome? O excedente médio é mais perto de 5, 20 ou 50 MW?" | 01, 02, 03 |
| 2 | Valor do MWh poupado | "Para vocês, 1 MWh economizado vale o PLD, o preço do contrato de venda ou o preço de transferência para outras unidades do grupo? Uma faixa basta: R$ 150, 250 ou 400?" | 01, 02, 03 |
| 3 | Ar comprimido do Pecém | "Quantos compressores, de quantos kW no total, com que controle (carga/alívio ou inversor), a que pressão? Vocês medem vazão e energia na central? Qual foi o último percentual de vazamento medido?" | 03, 01 |
| 4 | Medição existente | "Há medição de energia por equipamento ou só por subestação? Qual sistema (PI, EMS, SCADA)? Dá para exportar dados de 15 minutos de uma área para um piloto?" | 01, 02 |
| 5 | Motores ociosos | "Quais sistemas de utilidades (bombas de resfriamento, exaustores, correias) ficam ligados em parada de linha ou com redundância desnecessária? Há bombas em bypass?" | 01 |
| 6 | Horas de importação | "Quantas horas por ano a usina precisa comprar energia, por exemplo quando a geração cai? Quanto custa uma hora dessas?" | 02 |
| 7 | Critério de investimento | "Qual o payback máximo para aprovar um projeto de eficiência? É o 'ROI menor que 2 anos' usado em Belval?" | 01, 02, 03 |
| 8 | Dono do piloto e canal de compra | "Quem seria o dono de um piloto: Energia/Utilidades, Manutenção ou o time digital (iNO.VC)? Startups entram pelo Açolab, pelo iNO.VC ou pelo Habitat FIEC?" | 01, 02, 03 |
| 9 | Regras de TI/OT e NR-10 | "Sensor de terceiros com rede 4G/LoRa isolada da automação é permitido? A instalação em CCM seria feita pelo eletricista da planta?" | 01, 03 |
| 10 | Projetos de eficiência no Pecém | "Dos 12 projetos de eficiência energética (R$ 63 mi/ano) do relatório de 2024, algum é no Pecém? Envolve ar comprimido ou motores?" | 01, 03 |
| 11 | Modelo de contrato | "A ArcelorMittal Brasil aceita contrato de economia compartilhada, como o usado em Vanderbijlpark?" | 01, 03 |
| 12 | Métrica preferida | "No dia a dia vocês falam em kWh/t, MW médios de excedente, GJ/t ou R$? Qual fator de CO₂ preferem: 46 g/kWh ou 52,8?" | 01, 02, 03 |
