# Consumo mensal por tipo de máquina e custo de um aumento de +15%

> Pesquisa e contas de 29/10/2026, para o VoltMap (Trilha da Inovação, ArcelorMittal Pecém). Parte do catálogo de 18 tipos de máquina (19 linhas de defeito) de `solucao_main/estimativas.md`. **Nada aqui é medição na ArcelorMittal.** Potências de máquinas do Pecém não são públicas: todas as linhas são "máquina típica desse tipo".

---

## 1. Resumo e premissas

- Pergunta: quanto uma máquina típica consome por mês em condições normais e quanto custaria a mais, em R$, se a potência subisse 15% durante o mês.
- **Achado principal de honestidade:** a pesquisa na internet não encontrou potência publicada para a maior parte dos tipos (correia de pátio, recuperadora, bombas, despoeiramento de LD e da casa de corrida, ponte rolante, torre de resfriamento). Só 4 tipos ganharam apoio real de catálogo ou de usina (exaustor de coqueria, despoeiramento secundário da aciaria, compressor, soprador/exaustor por analogia). O fator de carga (FC) é premissa nossa (C) em todas as linhas.
- **Mudanças em relação ao estudo anterior (só 2 linhas):** exaustor de COG (2.000 kW × 0,85 → 1.250 kW × 0,72) e bomba de alimentação de caldeira (2.500 kW → 2.000 kW). As demais mantêm kW e FC anteriores; a pesquisa não deu base para trocar.
- Preço: R$ 209/MWh (base), R$ 178 e R$ 250/MWh (faixa), como em `estimativas.md`. Horas: 720 h/mês para todas (ver nota abaixo).

### Fórmulas

```
Consumo mensal (kWh) = kW × FC × horas
Consumo mensal (MWh) = kW × FC × 720 ÷ 1000
Custo mensal normal  = MWh × R$/MWh
Energia extra (+15%) = consumo mensal × 0,15
Custo extra (+15%)   = energia extra × R$/MWh
```

**Exemplo resolvido (exaustor da sinterização):** 5.000 kW × 0,90 = 4.500 kW médios; × 720 h = 3.240.000 kWh = **3.240 MWh/mês**. Custo normal: 3.240 × R$ 209 = **R$ 677.160**. Extra de 15%: 3.240 × 0,15 = **486,0 MWh**; × R$ 209 = **R$ 101.574** (a R$ 178: R$ 86.508; a R$ 250: R$ 121.500).

**Nota sobre as horas:** usei 720 h (30 dias × 24 h) em todas as linhas. Para máquinas intermitentes (desenfornadora, recuperadora, ponte rolante, correia) o efeito de "não operar 24 h" já está dentro do FC (FC = potência média ÷ potência típica), então ajustar também as horas contaria duas vezes. Paradas programadas (manutenção, parada do alto-forno) não foram descontadas, o que superestima um pouco as máquinas contínuas.

### Níveis de evidência (aplicados ao kW usado; o FC é C em todas as linhas)

- **A** = dado publicado ou catálogo de fabricante para esse tipo de máquina.
- **B** = estimativa de engenharia (conta física com premissa explícita) ou analogia com usina real.
- **C** = premissa nossa, sem fonte que dê a potência.

---

## 2. Tabela final (uma linha por máquina, +15% de potência por 720 h)

| # | Máquina | kW usado | FC | Horas/mês | Consumo mensal (MWh) | Custo mensal normal (R$ 209) | Energia extra +15% (MWh) | Extra R$ (178) | **Custo extra +15%/mês (R$ 209)** | Extra R$ (250) | Evid. | Fonte principal (detalhes na seção 3) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Correia transportadora (pátio) | 400 | 0,65 | 720 | 187,2 | 39.125 | 28,1 | 4.998 | **5.869** | 7.020 | C | Premissa nossa; sem kW publicado |
| 2 | Recuperadora de minério | 500 | 0,45 | 720 | 162,0 | 33.858 | 24,3 | 4.325 | **5.079** | 6.075 | C | Premissa nossa |
| 3 | Máquina desenfornadora de coque | 300 | 0,30 | 720 | 64,8 | 13.543 | 9,7 | 1.730 | **2.031** | 2.430 | B | Tese VŠB (acionamento do êmbolo ≈ 200 kW): <https://dspace.vsb.cz/items/6fbce2f9-5070-427b-b4ec-1834b381edc5> |
| 4 | Exaustor de gás de coqueria (COG) | 1.250 | 0,72 | 720 | 648,0 | 135.432 | 97,2 | 17.302 | **20.315** | 24.300 | A (tipo) / B (porte) | Dalenergomash, catálogo: <https://www.dalenergomash.ru/en/node/218> |
| 5 | Exaustor principal da sinterização | 5.000 | 0,90 | 720 | 3.240,0 | 677.160 | 486,0 | 86.508 | **101.574** | 121.500 | B | INVT (motor de 5.200 kW, caso a confirmar): <https://www.invt.com/solutions/invt-gd5000-mv-vfd-blast-furnace-main-exhaust-fan-algerian-steel-plant-391> |
| 6 | Turbo-soprador do alto-forno (se motor elétrico) | 17.000 | 0,90 | 720 | 11.016,0 | 2.302.344 | 1.652,4 | 294.127 | **345.352** | 413.100 | B | Soprador de 17 MW de Tubarão (`dados/arcelormittal-brasil.md`, [S21]) |
| 7 | Bomba de resfriamento | 800 | 0,80 | 720 | 460,8 | 96.307 | 69,1 | 12.303 | **14.446** | 17.280 | C | Premissa nossa |
| 8 | Bomba de alimentação de caldeira | 2.000 | 0,85 | 720 | 1.224,0 | 255.816 | 183,6 | 32.681 | **38.372** | 45.900 | B | Conta de engenharia (seção 3, item 8) |
| 9 | Bomba de recalque | 400 | 0,60 | 720 | 172,8 | 36.115 | 25,9 | 4.614 | **5.417** | 6.480 | C | Premissa nossa |
| 10 | Compressor de ar (vazamentos) | 1.000 | 0,75 | 720 | 540,0 | 112.860 | 81,0 | 14.418 | **16.929** | 20.250 | B | Cruzamento com kWh/m³ (seção 3, item 10); mesma máquina da linha 11 |
| 11 | Compressor de ar (pressão/filtro) | 1.000 | 0,75 | 720 | 540,0 | 112.860 | 81,0 | 14.418 | **16.929** | 20.250 | B | Idem linha 10 (não somar as duas) |
| 12 | Despoeiramento primário do convertedor LD | 3.500 | 0,60 | 720 | 1.512,0 | 316.008 | 226,8 | 40.370 | **47.401** | 56.700 | C | Premissa nossa; busca não achou kW |
| 13 | Despoeiramento da aciaria (secundário) | 1.800 | 0,80 | 720 | 1.036,8 | 216.691 | 155,5 | 27.683 | **32.504** | 38.880 | B | Linz, ventilador de 2.300 kW: <https://chemengonline.com/primetals-technologies-receives-final-acceptance-for-new-secondary-dedusting-system-in-linz> |
| 14 | Despoeiramento da casa de corrida do AF | 2.500 | 0,80 | 720 | 1.440,0 | 300.960 | 216,0 | 38.448 | **45.144** | 54.000 | C | Premissa nossa; busca não achou kW |
| 15 | Ponte rolante 80 t | 250 | 0,15 | 720 | 27,0 | 5.643 | 4,0 | 721 | **846** | 1.012 | C | Conta física com velocidade assumida (seção 3, item 15) |
| 16 | Ventiladores da torre de resfriamento | 660 | 0,80 | 720 | 380,2 | 79.453 | 57,0 | 10.150 | **11.918** | 14.256 | C | Premissa nossa; pode estar subestimado |
| 17 | Motor de uso geral | 200 | 0,70 | 720 | 100,8 | 21.067 | 15,1 | 2.691 | **3.160** | 3.780 | C | Premissa nossa |
| 18 | Ventilador com correia em V | 90 | 0,70 | 720 | 45,4 | 9.480 | 6,8 | 1.211 | **1.422** | 1.701 | C | Premissa nossa |
| 19 | Exaustor de ventilação (duto com vazamento) | 250 | 0,80 | 720 | 144,0 | 30.096 | 21,6 | 3.845 | **4.514** | 5.400 | C | Premissa nossa |

Os valores foram calculados por script (Python) com kW, FC e 720 h exatos e arredondados só na impressão; custo normal = MWh × R$ 209.

---

## 3. Pesquisa por máquina: o que achei, comparação com o estudo anterior e recomendação

Resumo da comparação (kW × FC → kW médio): "Antes" = `estimativas.md`; "Agora" = esta tabela.

| # | Antes (kW × FC) | Agora (kW × FC) | Mudou? |
|---|---|---|---|
| 4 COG | 2.000 × 0,85 = 1.700 kW | 1.250 × 0,72 = 900 kW | Sim, reduzido (consumo de 1.224 → 648 MWh/mês) |
| 8 Bomba caldeira | 2.500 × 0,85 = 2.125 kW | 2.000 × 0,85 = 1.700 kW | Sim, reduzido (1.530 → 1.224 MWh/mês) |
| Demais | iguais | iguais | Não |

Total anterior (18 máquinas, compressor contado uma vez) 23.284 MWh/mês; total agora 22.402 MWh/mês.

**1. Correia transportadora (pátio).** Não achei kW publicado de acionamento de correia de pátio de usina. O único número encontrado, 37 kW de um acionamento de correia na mina de Erzberg (WEG), é de outro porte e serviço, e não usei. Mantido 400 kW × 0,65 (C). Recomendação: tratar como ordem de grandeza e medir no piloto.

**2. Recuperadora de minério.** Busca (acionamento de roda de caçambas) não retornou potência. Mantido 500 kW × 0,45 (C).

**3. Máquina desenfornadora de coque.** Uma tese checa (VŠB, Ostrava) descreve o motor principal do acionamento do êmbolo desenfornador em cerca de 200 kW. Como a máquina completa soma também nivelador, extrator de porta e translação, 300 kW é coerente com isso. Kw com apoio parcial (B); FC 0,30 é nosso. Fonte: <https://dspace.vsb.cz/items/6fbce2f9-5070-427b-b4ec-1834b381edc5> (resumo da busca; não abri a tese).

**4. Exaustor de gás de coqueria (COG).** **Catálogo de fabricante:** Dalenergomash (Rússia) lista dois exaustores de gás de coqueria: modelo 750-23-8 (450 a 900 m³/min, motor de 800 kW, consumo de 270 a 490 kW conforme o ponto de operação) e modelo 1200-27-2 (750 a 1.380 m³/min, motor de 1.250 kW, consumo de 600 a 950 kW). A página não rotula as colunas; conferi a ordem com Q × ΔP ÷ η (ex.: 750 m³/min a 3.000 mm c.a. dá ≈ 460 kW, que bate com os 450 kW da tabela). O estudo anterior usava 2.000 kW × 0,85 (1.700 kW médios), **3 a 6 vezes acima** do consumo de catálogo. Para o porte do Pecém: coqueria de 1.130 kt/ano (GEM, `dados/pecem.md`) com rendimento de gás de ~400 Nm³/t de coque (**premissa nossa, sem fonte**) dá ≈ 860 Nm³/min na base normal, ou mais na condição de sucção (gás quente), o que cai na faixa do modelo maior. **Recomendo 1.250 kW (motor do modelo 1200) e consumo médio de 900 kW (FC 0,72, valor alto do catálogo)**. Evidência A para o tipo de máquina, B para a escolha do porte. Pecém tem provavelmente exaustor reserva; conta-se um só em operação.

**5. Exaustor principal da sinterização.** Dados encontrados: (a) página da INVT (VFD de média tensão) cita um ventilador centrífugo com motor síncrono de **5.200 kW** em usina siderúrgica argelina; **o título da página fala em "exaustor de alto-forno", mas o texto fala em linha de sinterização, então não está claro a que ventilador se refere** (B, a confirmar); a mesma página diz que o motor do exaustor responde por quase dois terços da energia da linha de sinterização; (b) um projeto pequeno de 500 t/dia (sinterizadora de 32 m²) usa fan de 1.250 kW, sem relevância para o porte do Pecém (SlideShare, resumo da busca); (c) norma chinesa de projeto GB 50408-2015 recomenda 90 ± 5 m³/min por m² de área de sucção, com pressão de entrada de -16 a -18 kPa em máquinas médias e grandes (resumo da busca). **Conta de engenharia nossa:** se a esteira do Pecém tivesse 450 m² (hipótese nossa a partir de 4.747 kt/ano de sínter do GEM, `dados/pecem.md`, e produtividade de ~1,3 t/m²/h, que não é fonte publicada), a potência no eixo seria 90 × 450 ÷ 60 × 17.000 ÷ 0,82 ≈ 14 MW (se houver mais de um ventilador ou mais de uma esteira, o valor se divide). **Recomendo manter 5.000 kW × 0,90**: bate com o único motor real encontrado (5.200 kW) e é conservador diante da conta física (5 a 14 MW). Evidência B. Se o Pecém tiver porte maior, o custo extra sobe proporcionalmente.

**6. Turbo-soprador do alto-forno.** Exemplos reais encontrados: **17 MW** (soprador da CTE 3/4 de Tubarão, `dados/arcelormittal-brasil.md`, [S21]); **19 MW** (turbo-soprador nº 3 da Metinvest/MMKI, 4.000 m³/min, acionado por **turbina**, não por motor elétrico): <https://www.aist.org/metinvest-revamps-mmki-heat-station-no-1> (lido); **8,4 MW** (acionamento ABB do soprador do alto-forno em Donawitz, voestalpine; informação de resumo da busca, o PDF da ABB não foi legível): <https://library.e.abb.com/public/d3666fc6b41e90a6c12579bc0033526e/Case%20note_voestalpine_EN_lowres.pdf>. Os exemplos mostram a faixa de 8 a 19 MW, mas **nenhum confirma o Pecém**, e **não se sabe se o soprador do Pecém é a motor elétrico ou a turbina a vapor** (`dados/pecem.md`, lacuna). Mantido 17.000 kW × 0,90 (B por analogia). **Aviso para o pitch:** se for turbina a vapor, o custo extra não aparece na conta de energia elétrica; para a banca, usar como exemplo de ordem de grandeza, não como número do Pecém.

**7. Bomba de resfriamento.** Sem fonte de potência para esse tipo de bomba em siderurgia. Referência do projeto: bombas de 1.225 kW em Vanderbijlpark (`dados/benchmarks-setor.md`, [S30]), de porte coerente. Mantido 800 kW × 0,80 (C).

**8. Bomba de alimentação de caldeira.** Dados externos achados: a Ebara lista uma bomba principal de 1.200 t/h com acionamento de 17.500 kW (usina supercrítica, porte muito maior) e uma SOP com bombas de 375 kW para 91,8 t/h (porte pequeno), sem relevância direta. **Conta de engenharia nossa:** caldeira de ~100 MW elétrico ≈ 350 t/h (premissa nossa), pressão de descarga ~12 MPa (premissa), densidade ~900 kg/m³, η bomba+motor 75%: 350 ÷ 3,6 ÷ 900 × 12.000 kPa ÷ 0,75 ≈ **1.700 kW de eixo, ~2.000 kW de motor**. Recomendo **2.000 kW × 0,85** (B), um pouco menor que os 2.500 kW anteriores. Fonte de contexto: <https://ebara.co.jp/en/jihou/no/list/detail/251-4.html> (resumo da busca). O uso depende de quantas bombas operam em paralelo; contei uma por caldeira.

**9. Bomba de recalque.** Sem fonte. Mantido 400 kW × 0,60 (C).

**10 e 11. Compressor de ar (mesma máquina, dois defeitos).** Cruzamento com consumo específico: o Grupo ArcelorMittal converte ar comprimido a 1,01 GJ/1.000 m³ ≈ **0,110 kWh/m³** (`dados/arcelormittal-brasil.md`, §2.4, citando o Basis of Reporting do Grupo [S19]); um caso de compressor centrífugo de usina de aço inoxidável europeia mostra **0,1125 → 0,104 kWh/m³** antes e depois de reforma (FS-Elliott, estudo de fornecedor; não diz se o m³ é normal ou real): <https://www.fs-elliott.com/blog/steel-manufacturer-achieves-40k-savings-with-centrifugal-compressor-upgrade> (lido). Com o nosso 1.000 kW × 0,75 = 750 kW médios e 0,11 kWh/m³, a máquina entrega ≈ 6.800 m³/h (≈ 4.000 CFM), dentro da faixa de um compressor centrífugo de médio porte (a mesma página cita unidades de 1.500–3.400 e 6.000–12.000 CFM). **Mantido 1.000 kW × 0,75** (B: kW é nosso, mas coerente com o kWh/m³ publicado). Uma vez por máquina física, não somar as linhas 10 e 11.

**12. Despoeiramento primário do convertedor LD.** A busca não retornou kW de ventilador de gás primário de convertedor de 300 t (só descrições de projeto Primetals/Siemens). Mantido 3.500 kW × 0,60 (C).

**13. Despoeiramento da aciaria.** Caso real: o sistema de despoeiramento secundário da voestalpine Linz (Primetals, 2016) usa **um ventilador de tiragem induzida de 2.300 kW com controle de velocidade, para 610.000 m³/h (máx. 700.000 m³/h)** e filtro de mangas de ~9.900 m²: <https://chemengonline.com/primetals-technologies-receives-final-acceptance-for-new-secondary-dedusting-system-in-linz> (lido). Linz é uma usina maior que o Pecém (3 Mt/ano). Mantido **1.800 kW × 0,80** (B), um pouco abaixo do exemplo real, mostrando 2.300 kW como cenário alto (consumo de 1.325 MWh/mês com FC 0,8).

**14. Despoeiramento da casa de corrida do AF.** Não achei kW publicado de ventilador de casa de corrida. Mantido 2.500 kW × 0,80 (C). Valor provavelmente alto; se o ventilador for menor (1.000 a 2.000 kW), o custo extra cai proporcionalmente.

**15. Ponte rolante 80 t.** Sem fonte de kW para ponte de 80 t. Referência de escala: pontes de 10 t em aciaria têm içamento de 30 a 37 kW (especificação e dado da BHEL, <https://tenders.bhel.com/sites/default/files/crane-scope-of-work-1511236114.pdf>, resumo da busca). Conta física nossa: içamento de 80 t a 10 m/min (velocidade assumida) = 80.000 × 9,81 × 0,167 ÷ 0,85 ≈ 154 kW, mais translação, o que sustenta ~250 kW instalados. Mantido 250 kW × 0,15 (C: velocidade e FC são premissas).

**16. Ventiladores da torre de resfriamento.** Referências achadas: ventilador de torre de uma usina indiana (BHEL) com motor de 30 kW por célula, e torres comerciais Marley de 11 a 15 kW por célula (resumo da busca). Um blog (sem autoridade) sugere 12 a 18 kW por MW de calor rejeitado em torres grandes, o que para uma termelétrica de 218 MW daria **bem mais que 660 kW** (da ordem de 2 a 5 MW), mas não confio na fonte. Mantido 660 kW × 0,80 (C) como **valor conservador**; pode estar subestimado. Fonte: <https://chem-casts.com/knowledge/cooling-tower-fan-power-calculation-the-definitive-guide> (blog, não verificado).

**17, 18, 19. Motor de uso geral, ventilador com correia em V, exaustor de ventilação.** São máquinas pequenas e genéricas; o kW é nossa premissa. Mantidos como estavam (C).

---

## 4. Resumo e frases para slide

### Maiores custos extras de +15% (R$/mês, a R$ 209/MWh)

| Posição | Máquina | Extra (R$/mês) | Faixa 178–250 |
|---|---|---|---|
| 1 | Turbo-soprador do alto-forno (se elétrico) | 345.352 | 294.127 a 413.100 |
| 2 | Exaustor principal da sinterização | 101.574 | 86.508 a 121.500 |
| 3 | Despoeiramento primário do convertedor LD | 47.401 | 40.370 a 56.700 |
| 4 | Despoeiramento da casa de corrida do AF | 45.144 | 38.448 a 54.000 |
| 5 | Bomba de alimentação de caldeira | 38.372 | 32.681 a 45.900 |

(Em seguida: despoeiramento da aciaria R$ 32.504; exaustor de COG R$ 20.315; compressor de ar R$ 16.929.)

### Menores custos extras de +15%

| Máquina | Extra (R$/mês) |
|---|---|
| Ponte rolante 80 t | 846 |
| Ventilador com correia em V | 1.422 |
| Máquina desenfornadora de coque | 2.031 |
| Motor de uso geral | 3.160 |
| Exaustor de ventilação (duto) | 4.514 |

### Total se uma máquina de cada tipo tivesse +15% ao mesmo tempo

Contando 18 máquinas físicas (o compressor de ar uma só vez; as 19 linhas teriam 2 defeitos na mesma máquina):

| Item | Valor |
|---|---|
| Consumo normal somado | 22.402 MWh/mês (≈ 22,4 GWh) |
| Custo normal somado (R$ 209) | R$ 4.681.959/mês |
| Energia extra (+15%) | 3.360 MWh/mês |
| **Custo extra (+15%), R$ 209** | **R$ 702.294/mês** |
| Faixa R$ 178 a R$ 250 | R$ 598.126 a R$ 840.065 |

O soprador sozinho responde por 49% desse total (345.352 de 702.294); sem ele, o total cai para R$ 356.942/mês. Cenário hipotético (todas ao mesmo tempo), não uma previsão.

### Frases prontas para slide (R$ 209/MWh, máquina típica, estimativa)

1. "Um exaustor de sinterização com +15% de consumo custa **R$ 101,6 mil a mais por mês** (486 MWh)."
2. "Um turbo-soprador de alto-forno de ~17 MW com +15% custa cerca de **R$ 345 mil a mais por mês**, se for acionado por motor elétrico."
3. "Um ventilador de despoeiramento de casa de corrida com +15% custa **R$ 45 mil a mais por mês**: mangas entupidas fazem o ventilador gastar mais sem ninguém ver."
4. "Um compressor de ar com +15% custa **R$ 16,9 mil a mais por mês**, e vazamento é o defeito mais comum desse equipamento."
5. (exemplo pequeno, fácil de visualizar) "Até uma correia de pátio com +15% custa **R$ 5,9 mil a mais por mês**."

**Melhores 3 a 4 para a banca:** (1) exaustor de sinterização, por ser um equipamento conhecido e ter o motor com apoio de dado real (B); (2) compressor de ar, o mais fácil de explicar (vazamento) e com o kWh/m³ publicado (B); (3) despoeiramento da aciaria ou da casa de corrida, porque o mecanismo (mangas entupidas) é intuitivo; (4) o soprador, só com o aviso "se for elétrico, ordem de grandeza", por ser o maior valor mas o mais incerto. Todas devem ser ditas como "uma máquina típica", nunca "no Pecém".

---

## 5. Sanidade

**Ordem de grandeza.** A soma de uma máquina de cada tipo dá **22.402 MWh/mês**. O consumo do Pecém é estimado em 1.200 a 1.360 GWh/ano (`dados/pecem.md`, §4.2, estimativa derivada), isto é, 100,0 a 113,3 GWh/mês (137 a 155 MW médios). A soma representa **cerca de 20% a 22%** do consumo mensal do Pecém. Faz sentido: é só uma máquina de cada tipo (a usina real tem várias correias, bombas e ventiladores) e as 18 não cobrem laminação, oxigênio (planta de terceiros), iluminação, etc. Se a soma passasse de 100% haveria erro; 20% para as maiores cargas é plausível. Para o Brasil (≈ 6.260 GWh/ano ≈ 522 GWh/mês, estimativa do estudo anterior baseada em imprensa), a soma é de ~4%, também coerente. Nem de longe é um dado do Pecém.

**Cruzamento por consumo específico:** com o exaustor de sinterização a 3.240 MWh/mês (38,9 GWh/ano) e produção de sínter de 4.747 kt/ano (GEM), o consumo é ≈ 8,2 kWh/t de sínter apenas para esse ventilador. Não achei kWh/t de sínter publicado para comparar, então este cruzamento não valida nem refuta; ele só mostra que o valor não é absurdo. O ar comprimido (1.000 kW × 0,75) ≈ 540 MWh/mês, equivalente a 6.480 MWh/ano, é ~7% das 92 GWh/ano de ar comprimido da ArcelorMittal Brasil (`dados/arcelormittal-brasil.md`): coerente com uma máquina entre muitas.

**Verificação do +15%:** com 5.000 kW × 0,90 × 720 h = 3.240.000 kWh, +15% de potência dá 4.500 → 5.175 kW médios; 5.175 × 720 = 3.726.000 kWh; diferença = 486.000 kWh = 15,0% exato do consumo mensal (486,0 MWh). Confirmado por script: (b − a) ÷ a = 0,15 para o exemplo. Vale para qualquer linha da tabela, já que energia extra = consumo × 0,15 por construção, com horas fixas.

---

## 6. Fontes (acesso em 29/10/2026)

"lido" = abri a página e conferi o dado. "resumo da busca" = só vi o resultado da busca, o dado deve ser conferido antes de citar publicamente.

| Fonte | URL | Uso | Status |
|---|---|---|---|
| Dalenergomash, exaustores de gás de coqueria | <https://www.dalenergomash.ru/en/node/218> | Motores de 800 e 1.250 kW; consumo de 270 a 950 kW (colunas não rotuladas) | lido (tabela) |
| Chemical Engineering, Primetals/voestalpine Linz | <https://chemengonline.com/primetals-technologies-receives-final-acceptance-for-new-secondary-dedusting-system-in-linz> | Ventilador de 2.300 kW, 610.000 m³/h | lido |
| AIST, Metinvest Heat Station 1 | <https://www.aist.org/metinvest-revamps-mmki-heat-station-no-1> | Turbo-soprador de 19 MW, 4.000 m³/min, acionado por turbina | lido |
| INVT, exaustor em usina da Argélia | <https://www.invt.com/solutions/invt-gd5000-mv-vfd-blast-furnace-main-exhaust-fan-algerian-steel-plant-391> | Motor de 5.200 kW; "dois terços da energia da linha de sinterização" | lido (identificação do ventilador ambígua) |
| INVT, exaustor de sinterização | <https://www.invt.com/solutions/invt-gd5000-mv-vfd-for-sintering-exhaust-fan-in-ironmaking-plants-438> | Motor síncrono excitado; sem kW | lido |
| FS-Elliott, compressor em usina de aço inoxidável | <https://www.fs-elliott.com/blog/steel-manufacturer-achieves-40k-savings-with-centrifugal-compressor-upgrade> | 0,1125 → 0,104 kWh/m³; faixas de vazão de compressores | lido (dado de fornecedor) |
| ABB, case voestalpine (Donawitz) | <https://library.e.abb.com/public/d3666fc6b41e90a6c12579bc0033526e/Case%20note_voestalpine_EN_lowres.pdf> | Acionamento de 8,4 MW do soprador (via resumo da busca) | resumo da busca (PDF ilegível) |
| Tese VŠB (acionamento do êmbolo desenfornador) | <https://dspace.vsb.cz/items/6fbce2f9-5070-427b-b4ec-1834b381edc5> | Motor principal de ≈ 200 kW | resumo da busca |
| GB 50408-2015, projeto de sinterização (via fwdbook.qq.com) | <https://fwdbook.qq.com/read/1033688946/17> | 90 ± 5 m³/min por m²; -16 a -18 kPa | resumo da busca |
| Projeto de 500 t/dia (SlideShare) | <https://www.slideshare.net/slideshow/500-tpd-mn-ore-sinter-plant-46346816/46346816> | Fan de 1.250 kW para esteira de 32 m² | resumo da busca |
| Ebara, bombas de alimentação | <https://ebara.co.jp/en/jihou/no/list/detail/251-4.html> | Escala de bomba de 17.500 kW (porte maior) | resumo da busca |
| BHEL, ponte rolante | <https://tenders.bhel.com/sites/default/files/crane-scope-of-work-1511236114.pdf> | Escala de motores de ponte de 10 t | resumo da busca |
| Chem-casts (blog) | <https://chem-casts.com/knowledge/cooling-tower-fan-power-calculation-the-definitive-guide> | 12 a 18 kW por MW de calor rejeitado | resumo da busca (fonte fraca) |
| Penn State, apêndice de torres Marley | <https://www.engr.psu.edu/ae/Thesis/portfolios/2006/ntp111/finalreport/patrick-appendix-b.pdf> | Ventiladores de 15 a 20 BHP por célula | resumo da busca |
| Arquivos do projeto | `dados/pecem.md`, `dados/arcelormittal-brasil.md`, `solucao_main/estimativas.md` | Preço, consumo do Pecém, soprador de Tubarão (17 MW), 0,110 kWh/m³ | lidos (os dados externos citados neles não foram reverificados) |

Não achei fonte (e disse isso na seção 3) para: correia de pátio, recuperadora, bombas de resfriamento e de recalque, despoeiramento primário do LD, despoeiramento da casa de corrida, torre de resfriamento, motor geral, ventilador com correia, exaustor de duto.

---

## 7. Limitações

- **Nada é medição na ArcelorMittal.** Potências de máquinas do Pecém não são públicas; cada linha é "máquina típica desse tipo". Um erro de 2× no kW dobra o custo da linha.
- **O FC é premissa nossa (C) em todas as linhas.** Quando houve consumo de catálogo (exaustor de COG), usei o ponto alto da faixa; não é média medida.
- **As fontes encontradas são poucas:** a maior parte dos resultados da busca é de fornecedores, patentes e blogs; vários só vi como resumo da busca (marcados). Dados de fornecedor não foram auditados.
- **Evidência concentrada em equipamentos de outros países e portes.** Linz (aciaria) e Metinvest/Tubarão (soprador) são usinas diferentes do Pecém; a Argélia é um caso de identificação ambígua.
- **Soprador:** se for turbina a vapor no Pecém, o custo extra de R$ 345 mil/mês não existe na conta elétrica. É 49% do total somado.
- **Exaustor da sinterização:** a conta física sugere que o motor real pode ser bem maior que 5.000 kW (até ~14 MW para uma esteira de 450 m², que é hipótese nossa); mantido o valor conservador.
- **Aumento de potência nem sempre é visível** (bombas e ventiladores sem controle de vazão podem até reduzir a potência com o defeito), e nem sempre +15% é o que cada defeito produz; o valor de +15% é o cenário do pitch, não uma estimativa por defeito (para isso, ver `estimativas.md`).
- **Preço:** R$ 209/MWh é referência pública, não o preço interno do Pecém. A faixa 178–250 é só sensibilidade.
- **Horas:** 720 h para todas, sem descontar paradas programadas.
- **Soma de uma máquina de cada tipo** é hipotética e serve só para dar escala.
