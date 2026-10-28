# Preços, tarifas e fatores para valorar o kWh economizado

> Pesquisa de 28/10/2026. **Ponto central:** no Pecém, o kWh economizado não reduz conta de luz. Ele aumenta o excedente, que é vendido ao SIN ou **transferido para outras unidades do grupo** [S06]. O preço certo é o **valor de venda ou transferência desse excedente, que não é público** [LACUNA]. Abaixo estão as referências públicas para montar uma faixa.
> Fontes em `fontes.md`.

---

## 1. Opções de valoração do MWh economizado no Pecém

| Opção | Valor (R$/MWh) | Quando usar | Fonte | Confiança |
|---|---|---|---|---|
| A. PLD Nordeste, média simples jan–nov/2025 | **≈ 178** [DERIVADO: (59,21 + 58,60 + 58,90 + 107,28 + 227,92 + 232,29 + 205,55 + 268,67 + 245,86 + 218,37 + 275,04) ÷ 11 = 177,97] | Se o excedente for liquidado no mercado de curto prazo | [S35] Amee, nov/2025 | Alta (dado), média nossa |
| B. Contrato de longo prazo, energia convencional 2027–2030 | **190,76** | Se o excedente for vendido em contrato bilateral | [S35] curva forward DCIDE de 26/11/2025 (via Amee) | Alta |
| C. Contrato de longo prazo, incentivada 50% 2027–2030 | 220,41 | Referência | [S35] | Alta |
| D. Longo prazo convencional (Abraceel) | 233 (mar/2026); PLD médio de R$ 236 | Usado na solução 03 | Abraceel via Cenário Energia (solução 03) | Alta |
| E. **Premissa central das soluções 01/03** | 233–250 | — | soluções | Premissa |
| F. Custo evitado de compra em outra unidade do grupo (venda intragrupo) | Desconhecido; provavelmente perto do preço de contrato que essa unidade pagaria (B–D) mais encargos | Se o excedente vai para Vega, aços longos etc. | [S06] (existência da venda intragrupo) | **LACUNA** |
| G. Tarifa A4 Verde Enel CE fora de ponta (PMEs do CIPP) | 369,17 sem tributos (REH 3.574/2026) | Segmento PME, **não o Pecém** | solução 01 [F14] | **Desatualizada**: ver §3 |

**Recomendação para o pitch:** mostrar **duas linhas**: (1) conservadora a **R$ 178/MWh** (PLD NE 2025) e (2) base a **R$ 233–250/MWh** (contratos). Dizer explicitamente: "a ArcelorMittal sabe o preço interno; trocamos pelo número dela em 1 minuto".

## 2. PLD (CCEE)

| Item | Valor | Fonte |
|---|---|---|
| PLD mensal NE 2025 | jan 59,21 · fev 58,60 · mar 58,90 · abr 107,28 · mai 227,92 · jun 232,29 · jul 205,55 · ago 268,67 · set 245,86 · out 218,37 · nov 275,04 | [S35] |
| PLD NE dez/2024 | 64,80 | [S35] |
| Limites 2026 | piso **R$ 57,31**; teto estrutural **R$ 785,27**; teto horário **R$ 1.611,04** | [S36] Grugeen; solução 02 |
| Dia 15/10/2026 | NE de R$ 57,31 (dia) a R$ 1.437 (noite) | solução 02 (Agência Infra) |
| 01/01/2026 | média de R$ 150,39 no NE; mínimo de R$ 57,31 entre 8h e 14h; máximo de R$ 197,18 às 20h | [S36b] DGABC/CCEE |
| 27/10/2026 | média diária NE de R$ 87,33; horário no piso | [S36c] snapshot da CCEE via busca (não aberto diretamente; site com bloqueio anti-robô) |
| Julho/2026 | PLD médio NE de R$ 125,15 | [S36d] Czapp (via busca) |
| Projeção CCEE para set/2026 | R$ 156 em todos os submercados | Canal Energia (via busca) |

**[DERIVADO] Padrão para a solução 02:** o PLD do NE em 2026 passa boa parte do dia no piso (R$ 57) e sobe à noite (quando a solar sai). **O spread dentro do dia é o ativo da solução 02.** Para o cálculo real, baixar o CSV `PLD_HORARIO` da CCEE pelo navegador (o portal bloqueia acesso automatizado; confirmado de novo em 28/10/2026, HTTP 403).

## 3. Tarifas Enel CE (para PMEs do CIPP; não se aplica ao Pecém, que está na Rede Básica)
- Valores usados nas soluções (REH ANEEL 3.574/2026, a partir de 22/04/2026): A4 Verde FP R$ 369,17/MWh; P R$ 1.543,97/MWh; demanda R$ 20,82/kW (sem tributos) (solução 01 [F14]).
- **Atualização:** o **Despacho ANEEL 3.324/2026** (DOU de 25/08/2026, vigente desde 26/08/2026) recalculou o reajuste. O efeito médio passou de **+5,78% para −5,87%**; para média e alta tensão, a redução estimada é de **3,29 p.p.** em relação ao efeito homologado em abril [S49] FIEC/Focus Poder. **As tarifas A4 das soluções estão ~3% acima das vigentes.** Conferir a tabela nova antes do pitch.
- O Pecém está conectado à Rede Básica em 230 kV [S03]: paga encargos de transmissão (TUST), não tarifa de distribuidora. Contratos e montantes (MUST): **LACUNA**.

## 4. Fatores de emissão (para tCO₂ evitado)
| Fator | Valor | Quem usa | Fonte |
|---|---|---|---|
| **SIN médio out/2023–set/2024** | **46,0 gCO₂/kWh** | **ArcelorMittal Brasil, inventário 2024** | [S18] PDF p.99 |
| Brasil 2025 (oficial do país 2024–25) | 52,8 kgCO₂/MWh | Grupo ArcelorMittal, Basis of Reporting 2025 | [S19] PDF p.70 |
| SIN 2023 (MCTI) | 38,5 kgCO₂/MWh | soluções 01/02 | MCTI via Agência Gov |
| SIN 2024 (inventários de terceiros) | 54,5 kgCO₂/MWh | soluções 01/03 | Bradesco/StoneX (secundário) |
| SIN 2025 mensal (nova metodologia MCTI) | 21,5–28,9 kgCO₂/MWh (jan–abr) | solução 02 | MCTI |

**Recomendação:** usar **46,0 g/kWh "o mesmo fator do inventário da ArcelorMittal Brasil"** ou 52,8 g/kWh "o fator do Grupo para o Brasil". **Ganho de credibilidade:** a banca reconhece o próprio número.

## 5. Valores de bolso (DERIVADOS)
| Quantidade | R$ 178/MWh | R$ 250/MWh | tCO₂ (46 g/kWh) |
|---|---|---|---|
| 1 MWh | R$ 178 | R$ 250 | 0,046 |
| 1 MW contínuo (8.760 MWh/ano) | R$ 1,56 mi/ano | R$ 2,19 mi/ano | 403 t/ano |
| 1% do consumo elétrico estimado do Pecém (12–13,6 GWh) | R$ 2,1–2,4 mi/ano | R$ 3,0–3,4 mi/ano | 550–630 t/ano |
| 1 m³/min de ar comprimido contínuo (57,7 MWh/ano, padrão ArcelorMittal) | R$ 10,3 mil/ano | R$ 14,4 mil/ano | 2,7 t/ano |
| Compressor de 110 kW 4 h/dia em alívio (27,5 kW; 40,15 MWh/ano, exemplo da solução 01) | R$ 7,1 mil/ano | R$ 10,0 mil/ano | 1,8 t/ano |
| Deslocar 5 MW por 3 h/dia, 300 dias (4.500 MWh/ano), por R$ 100 de spread | R$ 450 mil/ano | — | ~0 (deslocar não reduz kWh) |

## 6. Custos de energia na siderurgia (para a frase de problema)
- worldsteel: energia = **20–40% do custo de produção do aço** [S24].
- pv magazine (ArcelorMittal Brasil, sem atribuição clara): energia = 5–8% do custo de produção (provavelmente só eletricidade) [S39].
- Dofasco: energia está entre os **três maiores custos de insumo** [S26].
