# SGE-Pecém: gestão de energia ISO 50001 com baseline automático, M&V e ranking de áreas

> Estimativas e premissas estão marcadas como **[EST]**. Dados da ArcelorMittal vêm de `dados/` (≈ 500 kWh/t; 1% ≈ 12–14 GWh/ano ≈ R$ 2–3 mi/ano).

## Problema
- Em siderúrgica, "economia de energia" costuma ser declarada sem prova: o baseline é uma planilha, não é normalizado por produção (t de placa, mix, parada de alto-forno), e o resultado do projeto é discutido de ouvido.
- Anomalias (um compressor fora da curva, uma área que consome mais por tonelada que o normal) só aparecem no fechamento mensal ou na fatura. O operador não vê o efeito do que faz.
- Faltam comparação justa entre áreas/turnos e um jeito de provar o ganho dos projetos (M&V) para auditoria ISO 50001 e para o CFO.

## Como funciona
1. **Dados**: medidores existentes (SCADA/historiador, PI/OSIsoft ou similar) + produção por área + fatura/CCEE. Sem sensor novo. No hackathon: CSV sintético/público.
2. **Baseline automático (EnB)**: regressão por área, kWh ~ t produzidas + mix + temperatura + dia/turno. Janelas de comportamento estável são detectadas sozinhas (quebras estruturais) para não contaminar o baseline.
3. **EnPI e desvio**: kWh/t por área em tempo quase real, com banda de incerteza. Desvio acima da banda gera alerta com custo estimado em R$/dia e provável causa (variável que mais mudou).
4. **M&V automatizado (IPMVP, Opção B/C)**: ao registrar um projeto (data, área), o app calcula economia = baseline ajustado − medido, com incerteza, em kWh, R$ e tCO2 (fator 46 g/kWh).
5. **Anomalias de fatura**: compara demanda/consumo faturado com o medido e flags de ultrapassagem, reativo e bandeira/tarifa.
6. **Gamificação**: ranking entre áreas/turnos por "kWh/t vs. baseline", metas semanais, selos, feed no celular/TV de sala de controle. Foco em equipes, não em indivíduos.
7. **Relatórios ISO 50001**: revisão energética, EnPIs e evidências exportadas em PDF para auditoria.

## Referências validadas
| Nome | País | O que faz | O que está validado | URL |
|---|---|---|---|---|
| Ento | Dinamarca (inferido de "ApS" e clientes; a página não declara) | Software ISO 50001 sobre dados de medidores existentes: baseline normalizado, M&V (IPMVP/ASHRAE 14) com incerteza, alertas de anomalia com custo | Produto real com clientes; **claims são de marketing do próprio vendor**, sem auditoria independente | https://ento.ai/product/iso-50001-certification |
| ecorize | Alemanha | Monitoramento e gestão de energia industrial para ISO 50001: curvas de carga, EnPI, relatórios de auditoria | Expositor da Hannover Messe; só descrição de vendor, **não li a fundo** | https://www.hannovermesse.de/aussteller/ecorize/N1611659 |
| Power Laws: Anomaly Detection (DrivenData / Schneider Electric) | Competição global | Detectar uso anômalo de energia em prédios; vencedor usou Isolation Forest + XGBoost (1º: €10 mil, time PINGANAI, jun/2018) | Validação de **competição**, em prédios (não indústria); prova viabilidade da técnica | https://blog.drivendata.org/blog/power-laws-anomalies-winners |
| Opower / National Grid | EUA | Relatórios comparativos de consumo entre vizinhos (benchmark social) | Reportado: ≈ 2% de redução média; National Grid cita US$ 73,7 mi e 800 GWh economizados desde 2009. Fonte é blog/imprensa antiga, não relatório oficial. Residencial, não industrial | https://www2.cio.co.nz/article/558268/gamification-helps-utility-companies-change-customer-behavior/ |
| ABB Startup Challenge 2026 | Global | Vencedores citados em IA para energia industrial: Forgis, Sesame Sustainability, MorphoAI, Faraday Predictive, eRoots Analytics | **Só vi a lista em resultado de busca**; a página (timeout) não foi lida, então não afirmo o que cada uma faz | https://www.abb.com/global/en/news/134787 |

**Lacunas honestas**: não achei hackathon vencido por produto de gestão de energia **industrial** com ISO 50001; o que há é competição de anomalia em prédios (DrivenData), startups comerciais (Ento, ecorize) e evidência de benchmark comportamental residencial (Opower). Gamificação industrial: só achei literatura acadêmica com resultado misto (feedback 4–12% no residencial, durabilidade incerta), sem caso siderúrgico.

## Adaptação ao Pecém / indústria cearense
- Siderúrgica de placas com termelétrica a gás de processo (218 MW, TRT 16 MW): o baseline precisa separar **consumo** de **geração própria**, e normalizar por t de placa e disponibilidade de gás.
- Áreas candidatas a ranking: aciaria, lingotamento, sinterização/coqueria, utilidades (ar comprimido, água), laminador. kWh/t por área é o EnPI natural.
- ISO 50001 já é cultura do grupo (confirmar certificação do site). O diferencial é automatizar a evidência.
- Para fornecedores/PMEs da cadeia no Ceará (alvo do Sebrae): versão leve, só com fatura + 1 medidor, mesma lógica.

## Estimativa de ganho **[EST]**
- Premissas: ≈ 500 kWh/t (derivado, ver `dados/`); economia típica de gestão sistemática de energia **[EST]** 1–3% em 2–3 anos (premissa nossa, a validar; Opower sugere ≈ 2% em contexto residencial).
- 1% ≈ 12–14 GWh/ano ≈ R$ 2–3 mi/ano → cenário 1–3% ≈ **R$ 2–9 mi/ano [EST]**.
- Ganhos adicionais não quantificados: evitar multa de demanda/reativo, tempo de engenheiro na auditoria, projetos que hoje "não provam" ganho passam a ser financiáveis.
- Risco de atribuição: parte da economia ocorreria sem a ferramenta; só um piloto com área-controle diz o ganho real.

## Monetização
- SaaS por site/área monitorada (ex.: faixa mensal por planta industrial, valor a definir após piloto).
- Opção success-fee: % da economia comprovada pelo próprio M&V (o M&V é o que torna isso possível).
- Para PMEs: assinatura baixa via Sebrae/associações; serviço de preparação para ISO 50001.

## Viabilidade e riscos
- Técnica: alta (regressão + detecção de anomalia são maduros, ver DrivenData e Ento). Integração com historiador industrial é o gargalo real.
- Dados: qualidade de medição e rastreio de produção por área; acesso OT/TI e cibersegurança (rede industrial isolada).
- Concorrência: Ento, ecorize, Siemens, Schneider e outros já existem; o diferencial seria foco em siderurgia/Nordeste, preço e rapidez de implantação.
- Gamificação em planta pesada é a parte menos validada; tratar como complemento, não pilar.
- Confiança: auditores só aceitam M&V com incerteza e metodologia (IPMVP) explícita.

## MVP em hackathon (5 dias, 3–5 alunos)
- **Dia 1**: definir dataset (sintético de 5 áreas, 12 meses, com produção, temperatura, 3 projetos "reais" injetados + 3 anomalias). Quem: dados.
- **Dia 2**: baseline por área (regressão + intervalo de confiança) e cálculo de desvio kWh/t. Quem: ML.
- **Dia 3**: M&V automático de um projeto (antes/depois ajustado) e detector de anomalia (Isolation Forest/resíduo). Quem: ML + backend.
- **Dia 4**: app web/mobile: ranking de áreas, alertas em R$/dia, tela de economia comprovada, export PDF. Quem: front.
- **Dia 5**: pitch, demo ao vivo, slide de ganho com premissas e plano de piloto em 1 área. Quem: negócio.
- Stack sugerida: Python (statsmodels/scikit-learn), Streamlit ou React, SQLite/CSV.

## Perguntas a validar com a ArcelorMittal
1. Existe historiador (PI?) com kWh por área e produção por área em frequência horária? Quem é dono?
2. A planta é certificada ISO 50001? Como hoje é calculado e auditado o baseline dos projetos?
3. Há submedição por área (aciaria, laminador, utilidades) ou só medição geral?
4. Como é tratado o consumo versus geração própria (TRT, termelétrica) nos indicadores?
5. Aceitam um piloto read-only em uma área (sem tocar em controle)?
6. Os operadores têm algum incentivo/meta de energia hoje? Receptividade a ranking entre turnos?
7. Quanto tempo de engenharia vai hoje em fechar a verificação de economia de projetos?
