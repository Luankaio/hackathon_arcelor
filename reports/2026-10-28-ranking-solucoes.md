# Ranking das 9 soluções (v1 + v2) — 28/10/2026

> Notas de 1 a 5 são **julgamento meu**, baseado nos `solucao.md` e em `dados/RANKING-DADOS-POR-IMPORTANCIA.md`. Não são medições. Ganhos em R$ são estimativas dos próprios documentos. Nada revisado pelo Luan.

Critérios (cada um de 1 a 5):
- **Valor**: tamanho do ganho para a ArcelorMittal Pecém.
- **Validação**: casos reais que sustentam a ideia (a própria ArcelorMittal pesa mais).
- **MVP**: dá para demonstrar em 5 dias (09–12/11) com 3–5 alunos, sem dados internos.
- **Diferencial**: distância de WeVoltz/Enerlize (vencedoras de 2025, monitoramento com sensores + IA).

| # | Solução | Valor | Valid. | MVP | Dif. | Total |
|---|---|---|---|---|---|---|
| 1 | v2-02 RotaCerta (motores/bombas/VSD) | 5 | 5 | 4 | 3 | **17** |
| 1 | v1-03 Sibilo (vazamentos de ar comprimido) | 3 | 5 | 5 | 4 | **17** |
| 3 | v1-01 VazioZero (equipamento ligado sem produzir) | 4 | 4 | 4 | 2 | 14 |
| 3 | v1-02 HoraCerta (demanda/PLD) | 4 | 3 | 4 | 3 | 14 |
| 5 | v2-01 TermoRadar (calor/vapor) | 3 | 3 | 3 | 4 | 13 |
| 5 | v2-03 TonaZero (IA de processo) | 5 | 3 | 1 | 4 | 13 |
| 5 | v2-04 SGE-Pecém (ISO 50001) | 3 | 3 | 5 | 2 | 13 |
| 8 | v2-05 SolMatch (renováveis/PPA) | 3 | 3 | 3 | 3 | 12 |
| 9 | v2-06 Manutenção preditiva | 2 | 4 | 3 | 2 | 11 |

## Por que cada uma ficou onde ficou
- **RotaCerta**: maior ganho estimado (R$ 5–16 mi/ano), e o Grupo já tem o caso (Vanderbijlpark, −53% com VSD e shared savings). Risco: ganhos dos casos são autodeclarados por fornecedores.
- **Sibilo**: melhor evidência (DOE/CAC, Bissen −7%, siderúrgica em MG −57%), hardware de ~R$ 350 e método de prova do ganho. Ganho menor (R$ 84 mil/ano numa área-piloto).
- **VazioZero**: forte, mas é o mais parecido com o que o júri já premiou. Sobrepõe a RotaCerta (as duas medem corrente por máquina).
- **HoraCerta**: só software e dados públicos, mas o valor depende do excedente e do preço do MWh no Pecém, que são lacunas críticas (perguntas A1/A2 do Ideathon).
- **TonaZero**: maior potencial, mas sem dados de processo não há demo honesta.
- **SGE-Pecém**: fácil de demonstrar e casa com o critério de compra da Belval (app para operador, ROI < 2 anos), mas é genérico. Funciona melhor como camada de outra solução.
- **SolMatch**: sobrepõe a HoraCerta; ganho de R$ 0,5–2 mi/ano é premissa nossa.
- **Manutenção preditiva**: ganho de energia pequeno (~90 MWh/ano no recorte); o pitch teria de ir por parada evitada.

## Recomendação
1. **Núcleo: RotaCerta + Sibilo** como "caça ao desperdício + prova do ganho" (sensor de corrente para motores, ultrassom para ar comprimido, mesma fila de ordens de serviço em R$/ano e mesma verificação M&V). Um produto, duas fontes de achados, ambos com caso dentro da ArcelorMittal.
2. **SGE-Pecém como casca**: baseline, ranking e painel que juntam os achados.
3. **Reserva**: HoraCerta, se no Ideathon a ArcelorMittal confirmar excedente e preço do MWh.
4. Deixar TonaZero e TermoRadar como "próximos passos" no pitch, não como escopo.

## Antes de decidir
- Checar as URLs e os ganhos de fornecedor (várias referências foram só lidas em trecho de busca; o `04` e o `05` listam quais).
- Perguntar no Ideathon: motores/bombas com bypass ou sem VSD, medição por equipamento, preço do excedente (`dados/lacunas-perguntas-para-ideathon.md`).
- Confirmar se a combinação cabe em ~5 min de pitch.
