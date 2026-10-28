# Benchmarks do setor (para calibrar as estimativas)

> Escopo: indústria do aço mundial e brasileira, e referências técnicas de utilidades. **Não são dados do Pecém.** Fontes em `fontes.md`.

---

## 1. worldsteel (mundo)
| Indicador | Valor | Ano | Fonte |
|---|---|---|---|
| Intensidade energética média | **20,95 GJ/t aço bruto** (21,01 em 2022; 21,30 em 2023) | 2024 | [S23] Sustainability Indicators 2025 / World Steel in Figures 2026 |
| Intensidade de CO₂ | **1,92 tCO₂/t** (base CO₂ original) | 2024 | [S23] |
| Intensidade de GEE (metodologia ampliada) | 2,18 tCO₂e/t | 2024 | [S23] |
| Por rota (CO₂) | **BF-BOF 2,34**; DRI-EAF 1,47; sucata-EAF 0,69 tCO₂/t | 2024 | [S23] |
| **Energia no custo do aço** | **"from 20% to 40%"** do custo de produção | fact sheet (c. 2018) | [S24] |
| Energia no custo (fala do diretor-geral) | 15–20% | 2015 | Mining Weekly (citado na solução 03) |
| Origem da energia numa integrada | ~50% carvão, **35% eletricidade**, 5% gás natural, 5% outros gases | fact sheet | [S24] |
| Até 75% da energia do carvão vai para o alto-forno | — | fact sheet | [S24] |
| Queda de ~60% na energia por tonelada desde 1960 | — | fact sheet | [S24] |

Comparação: Grupo ArcelorMittal 23,00 GJ/t (2025) [S19]; ArcelorMittal Brasil 19,39 GJ/t (2024, tabela) ou 20,78 GJ/t (texto) [S18]. As metodologias podem diferir (o Grupo usa equivalente primário para eletricidade).

## 2. Brasil
| Indicador | Valor | Ano | Fonte |
|---|---|---|---|
| Produção de aço bruto | 33,9 Mt; capacidade 51,0 Mt/ano | 2024 | [S22] Aço Brasil, folder 2025 |
| **Autogeração no setor** | **48% do consumo elétrico das usinas** | 2024 | [S22] |
| Eletricidade autogerada (associadas) | ~7 milhões de MWh | 2024 | [S22] |
| Eletricidade comprada (associadas) | ~7,7 milhões de MWh | 2024 | [S22] |
| **[DERIVADO]** Consumo elétrico médio do setor | (7 + 7,7) TWh ÷ 33,9 Mt ≈ **434 kWh/t** (média de todas as rotas, incluindo EAF) | 2024 | conta nossa |
| Indústria no consumo final de eletricidade do Brasil | 36,1% | 2025 | EPE via Cenário Energia (citado na solução 01) |
| Motores na eletricidade industrial | ~68% (Procel/Eletrobras, via WEG) | — | solução 01 [F20] |

Comparação: Pecém ≈ **500 kWh/t de placa** (2017–2019, dado derivado da própria CSP; ver `pecem.md` §4.2). Fica acima da média setorial, o que é coerente para uma integrada com coqueria, sínter e alto-forno (sem laminação).

## 3. EPE, cadeia siderúrgica (Rota 1: integradas com coqueria própria) [S25]
Estudo "Análise da eficiência energética em segmentos industriais selecionados, Produto 5: cadeia siderúrgica" (EPE/Qualitec, contrato CT-EPE-004/2017; dados IABr de 2015).

**Consumo de energia elétrica por etapa (GJ/t aço bruto), Tabela 37:**
| Coqueria | Sinterização | Alto-forno | Aciaria | Laminação | Sistema de energia e outros | Total |
|---|---|---|---|---|---|---|
| 0,204 | 0,552 | 0,488 | 0,466 | 1,110 | 1,197 | **4,017** |

- Eletricidade = 11,49% do consumo final da Rota 1; o resto é térmico (coque, carvão, gases) [S25] p.86.
- Maiores consumidores elétricos numa integrada: "grandes ventiladores (exaustão); sopradores das ventaneiras e regeneradores; sistemas de geração (cogeração); laminadores; tratamento e bombeamento de água; despoeiramento primário e secundário; bombas de caldeira; gaseificação e **compressores**" [S25] p.87.
- **Medidas e paybacks (BNDES 2012, citados na Tabela 71):** **inversores (VSD) nas utilidades: investimento de US$ 0,05/t, economia de 0,02 GJ/t, payback de 0,5 ano**; aumento de eficiência da cogeração: US$ 22,7/t, 0,38 GJ/t, payback de 6 anos [S25] p.115.
- **[DERIVADO]** VSD nas utilidades aplicado ao Pecém: 0,02 GJ/t × 3,0 Mt = 60.000 GJ ≈ **16,7 GWh/ano** (se for GJ elétrico final) ≈ R$ 3,0–4,2 mi/ano (R$ 178–250/MWh), com investimento de ~US$ 150 mil (0,05 × 3 Mt). Ordem de grandeza só, com dados de 2012.
- Potencial total de eficiência na Rota 1: 10,54%, principalmente térmico; na força motriz, só 0,62% (troca de motores) [S25] Tab. 72. **Leitura:** o potencial elétrico "por troca de equipamento" é pequeno; o grande ganho elétrico está na **operação** (ociosidade, controle, vazamentos), que é o foco das soluções 01 e 03.
- Ferro-gusa (Rota 2, carvão vegetal): ~107 kWh/t gusa de eletricidade; o soprador das ventaneiras é o principal consumidor elétrico [S25] p.66.

## 4. Ar comprimido
| Referência | Valor | Fonte | Confiança |
|---|---|---|---|
| Fatia típica da eletricidade industrial | ~10% (DOE/EPA); faixa de 10–35% na literatura | solução 01 [F10]; MDPI 2025 (busca) | Alta (DOE) |
| Siderúrgica integrada | 5–15% (fabricantes); 15–20% (fornecedor de software); faixa de trabalho razoável **5–20%** | busca, fontes comerciais | **Baixa** (sem estudo independente) |
| Vazamento típico / meta | 20–30% sem manutenção; abaixo de 10% com programa ativo | CAC/DOE Fact Sheet #7 (solução 01 [F9]) | Alta |
| Alívio (parafuso carga/alívio) | ~25% da potência plena (20–35%) | DOE Tip Sheet #1 (solução 01 [F10]) | Alta |
| **Energia padrão do ar comprimido na ArcelorMittal** | **1,01 GJ/1.000 m³ ⇒ 0,1097 kWh/m³** | [S19] Basis of Reporting | Alta |
| Padrão DOE | 18 kW/100 cfm ≈ 6,36 kW por m³/min ≈ 0,106 kWh/m³ | solução 03 | Alta |
| Siderúrgica em MG (ultrassom + reparo) | −57,2% no consumo dos compressores do alto-forno | [S32] | Alta (resumo de artigo revisado) |
| ArcelorMittal Bissen | −7% na eletricidade para ar comprimido | [S29] | Alta |

**[DERIVADO] Custo do ar comprimido na régua ArcelorMittal:** 0,1097 kWh/m³ × R$ 178–250/MWh = **R$ 0,020–0,027 por m³**; 1 m³/min contínuo = 57,7 MWh/ano ≈ **R$ 10–14 mil/ano** e ≈ 2,7 tCO₂/ano (46 g/kWh).

## 5. Motores e VSD (referência geral)
- VSD em bombas e ventiladores: economias de 10–75% por unidade, conforme carga (CEMEP/Fraunhofer 2023); estima-se que 75% dos sistemas de bombeamento são superdimensionados, muitos em mais de 20% (DOE) (busca; ver `fontes.md`).
- Motor de indução em vazio tem FP baixo, abaixo de ~0,3 (solução 01 [F21]).

## 6. Benchmarks de gestão de energia
- ISO 50001 na Dofasco: +6,16% em 3 anos, custo de US$ 250 mil, US$ 15,3 mi poupados [S26].
- Better Plants (DOE): parceiros se comprometem com −25% de intensidade em 10 anos (ArcelorMittal USA escolheu −10%) [S33b].
- Saldanha: 6,6% de 160 MW em ~2 anos de programa [S31].
- Energiency (fornecedor): "até 15% de novas economias sem capex" (marketing, não usar como fato) [S27b].
