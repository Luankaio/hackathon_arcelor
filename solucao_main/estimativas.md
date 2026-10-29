# Estimativas: quanto custa uma máquina trabalhar com defeito sem ninguém perceber

> Pesquisa e contas de 29/10/2026. Para o VoltMap (Trilha da Inovação, ArcelorMittal Pecém). **Nada aqui é resultado medido na ArcelorMittal.** Potências, fatores de carga e número de máquinas são estimativas nossas; os percentuais de aumento de consumo têm nível de evidência marcado um a um (A, B ou C).

---

## 1. Resumo e como ler

- O documento responde a duas perguntas: (1) quanto uma máquina gasta a mais quando opera com defeito e ninguém vê, durante 1 mês; (2) quanto disso se evitaria se o defeito fosse corrigido em menos de 1 hora.
- Há 18 tipos de máquina em 19 linhas de defeito (o compressor de ar aparece duas vezes, com defeitos diferentes). Cada linha traz faixa mín–base–máx de aumento de consumo, o nível de evidência e a fonte.
- **Achado importante de honestidade:** dados medidos e publicados de aumento percentual de consumo por defeito são escassos. Poucos percentuais têm evidência A (vazamento de ar comprimido, pressão do compressor, perda em correia em V, um caso de bomba desgastada). A maioria é B (analogia ou conta de engenharia com premissa explícita) ou C (premissa nossa). Para siderurgia, não achei medição publicada de nenhum tipo de máquina; os casos de usina siderúrgica que encontrei (Howden: Erdemir, Donawitz, Schwelgern) são qualitativos.
- O DOE afirma que desalinhamento de eixo **não tem efeito mensurável** na eficiência do motor (ele reduz a vida do rolamento, não aumenta o kW). Por isso a linha de "motor com rolamento/desalinhamento" tem base baixa (1,5%).
- Leitura dos resultados: a conta da seção 5 (1% das máquinas com defeito por 1 mês, corrigido em 1 h) dá um valor pequeno (ordem de 0,01% a 0,09% do consumo elétrico da escala). Isso é uma consequência da própria premissa, e a seção 6 compara com o 1% de eficiência do Pecém.

### Premissas globais

| Premissa | Valor | Origem / observação |
|---|---|---|
| Horas do mês | 720 h | 30 dias × 24 h (premissa do pedido) |
| Preço do MWh, base | **R$ 209/MWh** | Meio da faixa pública; usado em `pitches/pitch_tecnico.md` e `app.md`. **Estimativa**, trocar pelo preço interno |
| Preço do MWh, mínimo e máximo | R$ 178 e R$ 250 | R$ 178 = PLD NE médio jan–nov/2025; R$ 250 = teto da faixa de contratos longos (`dados/RANKING-DADOS-POR-IMPORTANCIA.md`, item 21) |
| Fator de emissão (só onde usado) | 46,0 gCO₂/kWh (0,046 tCO₂/MWh) | Inventário 2024 da ArcelorMittal Brasil (`dados/RANKING-DADOS-POR-IMPORTANCIA.md`, item 10). Só aplicável ao Brasil |
| Fator de carga (FC) | Por máquina, coluna própria na seção 2 | **Premissa C** (nossa). FC = potência média ÷ potência típica |
| Potência (kW) | Por máquina, seção 2 | **Estimativa C** (ordem de grandeza). Os arquivos do projeto não trazem kW por máquina (só o exemplo de 75 kW e o ventilador 48,2 vs. 40 kW, ilustrativos). Referências públicas usadas só para ordem de grandeza: TRT do Pecém 16 MW (`dados/pecem.md`); soprador de 17 MW em Tubarão (`dados/arcelormittal-brasil.md`, fonte [S21]); bombas de 1.225 kW em Vanderbijlpark (`dados/benchmarks-setor.md`, [S30]) |

### Níveis de evidência

- **A** = medido ou publicado em fonte confiável (guia DOE/CAC, estudo de campo), para aquele tipo de defeito ou de equipamento. Mesmo com A, a potência e o número de horas são nossos.
- **B** = estimativa de engenharia: conta com lei física ou guia técnico e premissa explícita, ou analogia com medição de outro equipamento.
- **C** = premissa nossa, sem fonte que dê o percentual. A faixa pode ter apoio qualitativo.

### Fórmulas

```
kW médio            = kW típico × FC
Energia extra/mês   = kW médio × 720 h × (% aumento ÷ 100) ÷ 1000        [MWh]
Custo extra/mês     = Energia extra/mês × preço do MWh                     [R$]
Extra de 1 hora     = kW médio × 1 h × (% aumento ÷ 100) ÷ 1000            [MWh]
Economia evitada    = Extra do mês − Extra de 1 hora
```

---

## 2. Catálogo por tipo de máquina

Tabela-resumo (todos os valores de kW e FC são **estimativas C**; o "% base" é o usado nos cálculos):

| # | Máquina | kW típico | FC | % mín | **% base** | % máx | Evidência | Defeito principal considerado |
|---|---|---|---|---|---|---|---|---|
| 1 | Correia transportadora (pátio) | 400 | 0,65 | 3 | **8** | 20 | C (faixa com apoio B) | Roletes travados ou desalinhados, acúmulo de material |
| 2 | Recuperadora de minério | 500 | 0,45 | 2 | **5** | 12 | C | Atrito em rodas/trilho, redutor, desgaste de caçambas |
| 3 | Máquina desenfornadora de coque | 300 | 0,30 | 2 | **5** | 10 | C | Atrito em guias, trilho, redutor |
| 4 | Exaustor de gás de coqueria (COG) | 2.000 | 0,85 | 2 | **5** | 10 | B | Incrustação (alcatrão/naftaleno) e desgaste do rotor |
| 5 | Exaustor principal da sinterização | 5.000 | 0,90 | 2 | **5** | 10 | B | Erosão e incrustação do rotor, falso ar, damper preso |
| 6 | Turbo-soprador do alto-forno (se motor elétrico) | 17.000 | 0,90 | 1 | **3** | 6 | B | Incrustação/erosão do compressor, folgas, filtro de entrada |
| 7 | Bomba de resfriamento | 800 | 0,80 | 3 | **6** | 12 | A (caso único) | Desgaste de anéis de desgaste e impelidor |
| 8 | Bomba de alimentação de caldeira | 2.500 | 0,85 | 2 | **5** | 10 | B | Desgaste interno, válvula de recirculação passando |
| 9 | Bomba de recalque | 400 | 0,60 | 3 | **6** | 15 | B | Desgaste, cavitação, estrangulamento por filtro entupido |
| 10 | Compressor de ar: vazamentos | 1.000 | 0,75 | 6 | **12,5** | 29 | A (vazamento) | Vazamento de 15% a 30% da produção de ar |
| 11 | Compressor de ar: pressão alta / filtro sujo | 1.000 | 0,75 | 1 | **2** | 4 | A (regra DOE) | +2 a +8 psi de pressão ou perda de carga |
| 12 | Despoeiramento primário do convertedor LD | 3.500 | 0,60 | 3 | **6** | 12 | C | Incrustação do rotor e do sistema de lavagem/filtro |
| 13 | Ventilador de despoeiramento da aciaria | 1.800 | 0,80 | 3 | **8** | 18 | B | Mangas colmatadas (perda de carga alta) |
| 14 | Despoeiramento da casa de corrida do AF | 2.500 | 0,80 | 3 | **8** | 18 | B | Mangas colmatadas |
| 15 | Ponte rolante 80 t | 250 | 0,15 | 3 | **10** | 25 | C | Freio arrastando, rodas desalinhadas, redutor |
| 16 | Ventiladores da torre de resfriamento | 660 | 0,80 | 3 | **8** | 20 | C | Incrustação no enchimento, ventiladores compensando |
| 17 | Motor de uso geral | 200 | 0,70 | 0,5 | **1,5** | 4 | C (A para resultado nulo de desalinhamento) | Rolamento defeituoso, desbalanço de tensão |
| 18 | Ventilador com correia em V | 90 | 0,70 | 2 | **5** | 10 | A | Correia frouxa/gasta (perda de transmissão) |
| 19 | Exaustor de ventilação com vazamento de duto | 250 | 0,80 | 5 | **10** | 16 | A/B | Vazamento no duto, mais vazão para o mesmo efeito |

### Detalhe por tipo

**1. Correia transportadora (pátio de matérias-primas).** Potência: 400 kW é estimativa nossa para um acionamento de correia de pátio (o Pecém tem correias de alta capacidade e uma de ~10 km até o porto, sem kW publicado; `dados/pecem.md`). FC 0,65: correia carregada parte do tempo. Mecanismo: roletes travados ou desalinhados aumentam a resistência ao rolamento. Dado publicado: segundo um artigo de Allen Reicks na Rock Products (faixas baseadas no CEMA), a resistência de rolamento dos roletes responde por cerca de 10% a 50% da potência total e o desalinhamento de roletes por 10% a 60%; um artigo de conferência (E3S, 2018) diz que a resistência ao rolamento pode ser até 60% das resistências principais em correias com mais de 80 m. **Esses números são parcelas da potência, não o aumento por defeito**, então o percentual de aumento (3–8–20%) é premissa nossa. A premissa de +8% por 7 dias já existia em `app.md` (preventiva por condição), também nossa. Não achei medição antes/depois de troca de roletes. Evidência **C**. Fontes: <https://rockproducts.com/2016/08/19/idler-misalignment-on-belt-conveyors/> (a página deu erro 403; li só o resumo da busca), <https://www.coalage.com/?p=6814>, <https://www.e3s-conferences.org/10.1051/e3sconf/20187100004> (resumo da busca; não abri o artigo).

**2. Recuperadora de minério.** 500 kW e FC 0,45 são estimativas nossas (acionamentos de roda de caçambas, translação e esteira somados). Sem fonte específica de aumento por defeito; usamos a lógica de atrito mecânico (rodas, trilho, redutor) com faixa conservadora. Evidência **C**.

**3. Máquina desenfornadora de coque.** 300 kW e FC 0,30 (operação intermitente, ciclo por forno) são estimativas nossas. Sem fonte publicada de aumento por defeito. Evidência **C**.

**4. Exaustor de gás de coqueria (COG).** 2.000 kW e FC 0,85 são estimativas nossas. O DOE Fan Sourcebook trata desgaste e sujeira como causas de queda de desempenho do ventilador, sem percentual. Como analogia medida: um caso de compressor de gás úmido na Indonésia (2014) mostrou queda de eficiência politrópica e aumento de 8,5% na potência no eixo, atribuído principalmente a incrustação de pás. A base de 5% é nossa (cerca de dois terços abaixo do caso). Evidência **B** (analogia). Fontes: <https://www.energy.gov/sites/prod/files/2014/05/f16/fan_sourcebook.pdf>; <https://garuda.kemdikbud.go.id/documents/detail/1008459> (o link veio da lista de resultados da busca; não confirmei que é este o artigo do caso, **confirmar antes de citar**).

**5. Exaustor principal da sinterização.** 5.000 kW e FC 0,90 são estimativas nossas, escolhidas para ficar coerentes com `pitches/pitch_tecnico.md` (que diz que 10% de sobreuso custam cerca de R$ 15 mil por semana: 5.000 × 0,90 × 10% × 168 h = 75,6 MWh × R$ 209 = R$ 15,8 mil). Em siderurgia, os estudos de caso da Howden (Erdemir, voestalpine Donawitz, ThyssenKrupp Schwelgern) descrevem erosão do rotor, damper que só abre 90% e perda de vazão, mas **sem percentual de potência**. A lei de ventiladores do DOE dá a sensibilidade: 5% a mais de vazão exige 16% a mais de potência (ver linha 19). Base de 5% é nossa. Evidência **B**. Fontes: <https://www.energy.gov/sites/prod/files/2014/05/f16/fan_sourcebook.pdf>; <https://files.chartindustries.com/Howden_Steel_Case_Erdemir.pdf>; <https://files.chartindustries.com/Howden_CentrifFan_Steel_Case_Donawitz.pdf> (casos de fornecedor, só qualitativos).

**6. Turbo-soprador do alto-forno.** 17.000 kW é analogia com o soprador de 17 MW da Tubarão (`dados/arcelormittal-brasil.md`, [S21]); **não se sabe se o do Pecém é motor elétrico ou turbina a vapor** (lacuna em `dados/pecem.md`). Se for turbina, a máquina sai da conta elétrica. Dados de analogia: caso de compressor com +8,5% de potência por incrustação (ver linha 4) e citação de que compressor axial sujo de turbina a gás perde até 4% de potência. Base de 3% é nossa. Evidência **B**. Fonte: <https://ijeecs.iaescore.com/index.php/IJEECS/article/view/18553> (resumo da busca).

**7. Bomba de resfriamento (água de circulação).** 800 kW e FC 0,80 são estimativas nossas. **Único caso medido encontrado:** Pumps & Systems (artigo da coluna "Pumping Prescriptions") mostra uma bomba centrífuga com anéis de desgaste folgados: eficiência de 65,2% para 53,6%, vazão de 4.100 para 3.900 gpm, **potência de 270 hp para 285 hp (+5,6%)**, apesar de entregar menos vazão (cálculo no artigo supõe perdas do motor zero). O guia DOE de bombas só descreve o mecanismo (folga do anel aumenta vazamento interno e reduz eficiência), sem percentual. Outro caso, da ERIKS (bomba de 22 kW), fala em desempenho pelo menos 30% abaixo do ensaio original, mas não dá potência. Base de 6% ≈ caso medido; faixa 3–12% é nossa. Evidência **A (caso único)**. Fontes: <https://pumpsandsystems.com/what-happens-power-efficiency-when-pump-wears-out> (lido); <https://www.energy.gov/sites/prod/files/2014/05/f16/pump.pdf> (lido, qualitativo); <https://eriks.co.uk/content/dam/uk/problem-solvers/pdf-files/Problem-Solver-129-Henkel.pdf> (só resumo da busca).

**8. Bomba de alimentação de caldeira.** 2.500 kW e FC 0,85 são estimativas nossas (caldeiras de ~100 MW na termelétrica de 218 MW; sem dado de bomba). Mesmo mecanismo da linha 7 mais válvula de recirculação passando. Base de 5% (um pouco abaixo do caso medido) é nossa. Evidência **B**. Fontes: as da linha 7.

**9. Bomba de recalque.** 400 kW e FC 0,60 são estimativas nossas. Desgaste, cavitação e estrangulamento por filtro entupido; faixa maior porque sistemas de recalque tendem a ter válvulas de controle abertas parcialmente. Base de 6% é a mesma do caso da linha 7. Evidência **B**.

**10. Compressor de ar: vazamentos.** 1.000 kW e FC 0,75 são estimativas nossas (um compressor centrífugo de médio porte). Para dimensionar: a linha reportada de ar comprimido da ArcelorMittal Brasil é ~92 GWh/ano ≈ 10,5 MW médios (`dados/arcelormittal-brasil.md`), o que sugere que o ar comprimido é uma carga pequena frente à usina. **Dado publicado (A):** a ficha #7 do Compressed Air Challenge (DOE, rev. maio/2026) diz que um sistema sem boa manutenção costuma ter vazamento de cerca de 20% da produção, que pode chegar a 20–30%, e que detecção e reparo reduzem para menos de 10%; sistemas mal mantidos perdem até 20–30% da capacidade e da potência. **Conta nossa:** a produção P atende a demanda D mais o vazamento L·P; energia ∝ P = D ÷ (1 − L). Com saudável em 10%: vazamento de 15% dá +5,9%, 20% dá +12,5%, 30% dá +28,6%. Base = 12,5% (vazamento típico de 20% contra 10% saudável). Supõe energia proporcional à vazão; em compressores com controle ruim o efeito pode ser menor ou maior. Evidência **A** para os percentuais de vazamento, conta nossa. Fonte: <https://www.compressedairchallenge.org/data/sites/1/media/library/factsheets2026/fact-sheet-7-compressed-air-system-leaks_updated2026.pdf> (lida).

**11. Compressor de ar: pressão de descarga alta ou filtro de sucção sujo.** Mesma máquina da linha 10. O DOE Compressed Air Sourcebook (v3) traz a regra para sistemas de ~100 psig: a cada 2 psi de aumento na pressão de descarga, a energia sobe cerca de 1% (pode diferir em centrífugos), e chega a 1,6–2% a cada 2 psi quando 30–50% do consumo é não regulado (vazamentos, sopro). Filtro de entrada sujo aumenta perda de carga e reduz capacidade e eficiência (sem número). Premissa nossa: perda de carga extra equivalente a +2, +4 ou +8 psi. Base 2% (4 psi extras); mín 1%; máx 4%. Evidência **A** (regra DOE); os psi são premissa. Fonte: <https://www.energy.gov/sites/prod/files/2016/03/f30/Improving%20Compressed%20Air%20Sourcebook%20version%203.pdf> (lida).

**12. Despoeiramento primário do convertedor LD.** 3.500 kW e FC 0,60 (ventilador atua durante o sopro) são estimativas nossas. Mecanismo: incrustação no rotor, na garganta do venturi ou no sistema de lavagem eleva a pressão necessária. Sem fonte de percentual. Evidência **C**.

**13 e 14. Ventiladores de despoeiramento com filtro de mangas (aciaria e casa de corrida do alto-forno).** 1.800 kW e 2.500 kW, FC 0,80, estimativas nossas. **Conta B:** a potência do ventilador é proporcional à pressão total × vazão. Premissa nossa: sistema com 4,0 kPa de pressão total, dos quais o filtro representa 1,5 kPa; mangas colmatadas elevam o filtro para 2,2 kPa (+0,7 kPa). Se a vazão se mantém (por controle de velocidade ou damper), a potência sobe 0,7 ÷ 4,0 = 17,5% (máx 18%); 3% e 8% são faixas menores (colmatação parcial ou vazão que cai um pouco). Apoio qualitativo: estudo piloto do KIT atribui cerca de 59% da perda de carga ao bolo de pó; a Gore (fornecedora de mangas) estima que 15% a menos de pressão diferencial em um filtro de forno de cimento economiza cerca de US$ 45 mil/ano (dado de fornecedor, não verificado). Se o ventilador não controla vazão, a vazão cai e a potência pode até cair, mas o despoeiramento fica pior; então o aumento de kW só é visível quando há controle de vazão. Evidência **B**. Fontes: <https://publikationen.bibliothek.kit.edu/1000168211/152210383> (resumo da busca), <https://www.gore.com/system/files/2018-09/Article_WorldCementMagazine_What-a-Drag_Filter-Bag-Drag_May2016.pdf> (resumo da busca).

**15. Ponte rolante 80 t.** 250 kW é a potência instalada estimada (elevação + translação); FC 0,15 reflete uso intermitente. **Não achei fonte séria** para aumento de consumo por freio arrastando ou roda desalinhada. Um blog de 2026 fala em +25–40% por manutenção ruim, sem estudo por trás; **não usei**. Os ganhos publicados vêm de troca de acionamento (ABB, New Zealand Steel: 40–45% com acionamento regenerativo, dado de fornecedor), que não é defeito. Base de 10% é nossa. Evidência **C**. Fonte de contexto: <https://www.abb.com/global/en/news/136755/40-45-energy-savings-achieved-in-new-zealand-steel-crane-operation-after-modernisation-of-large-gantry-crane-with-abb-regenerative-drives>.

**16. Ventiladores da torre de resfriamento.** 660 kW (6 células × 110 kW) e FC 0,80 são estimativas nossas (a termelétrica do Pecém tem torre de resfriamento, sem kW publicado). Fontes encontradas são blogs de fornecedores (incrustação leve reduz eficiência da torre 5–10%, moderada 10–25%), que falam em eficiência térmica e não em kW. Base de 8% é nossa. Evidência **C**. Fonte de contexto (fraca): <https://longpartspros.com/blog/is-your-cooling-tower-costing-you-energy>.

**17. Motor de uso geral com rolamento defeituoso, desalinhamento ou desbalanço de tensão.** 200 kW e FC 0,70 são estimativas nossas. Achados: (a) o DOE (Motor Systems Tip Sheet #4) diz que desalinhamento **não tem efeito mensurável** na eficiência do motor, mas aumenta vibração, temperatura e reduz a vida de rolamento e acoplamento; um estudo da Univ. do Tennessee (1999) não achou perda de eficiência mensurável e estimou até 50% de perda de vida do rolamento com 5 mil de desalinhamento; (b) um estudo acadêmico de motores com rolamento defeituoso reporta queda de eficiência de cerca de 1–2% (número visto só em resumo de perfil acadêmico, **não verificado**); (c) desbalanço de tensão: o DOE dá o aquecimento adicional como 2 × (% desbalanço)² em °C e recomenda no máximo 1% (resumo de busca; não consegui abrir a ficha), e a NEMA MG-1 cita corrente 6 a 10 vezes o desbalanço de tensão. (d) Rebobinagem bem feita não muda a eficiência (média −0,1%, dentro da incerteza do ensaio, estudo EASA/AEMT 2019 com 10 motores). Conclusão: o defeito mecânico simples quase não aparece em kW; base 1,5% é nossa. Evidência **C** (e **A** para o resultado nulo de desalinhamento). Fontes: <https://www.energy.gov/sites/prod/files/2014/04/f15/importance_motor_shaft_motor_systemts4.pdf> (lida); <https://efficientplantmag.com/1999/04/study-shows-shaft-misalignment-reduces-bearing-life> (resumo da busca); <https://journals.rcsi.science/1068-3712/article/view/230974> (resumo da busca, qualitativo); <https://www.theaemt.com/resource/revisited-the-effect-of-repairs-on-motor-efficiency.html> (resumo da busca); <https://electrical-engineering-portal.com/voltage-unbalance-nema-motor-performance> (resumo da busca).

**18. Ventilador com acionamento por correia em V.** 90 kW e FC 0,70 são estimativas nossas (ventilação de utilidades; os grandes exaustores usam acoplamento direto). **Dado publicado (A):** o DOE Fan Sourcebook diz que mesmo correias novas e bem ajustadas perdem 5% a 10% e que as perdas aumentam com o desgaste; exemplo: queda de 5% na eficiência de transmissão de um ventilador de 200 hp equivale a 10 hp de perda. Base de 5% = o exemplo do DOE; faixa 2–10% é nossa. Evidência **A**. Fonte: <https://www.energy.gov/sites/prod/files/2014/05/f16/fan_sourcebook.pdf> (lida).

**19. Exaustor de ventilação com vazamento de duto.** 250 kW e FC 0,80 são estimativas nossas. **Dado publicado (A):** o DOE Fan Sourcebook calcula que, se o duto vaza e a vazão precisa subir 5%, a velocidade sobe 5% e a potência 16% (lei dos ventiladores), com a ressalva de que na prática o aumento é um pouco menor porque o vazamento alivia a resistência. Usamos 16% como máximo, 5% como mínimo e 10% como base (nossa). Evidência **A** para o limite superior, **B** para a base. Fonte: <https://www.energy.gov/sites/prod/files/2014/05/f16/fan_sourcebook.pdf> (lida).

---

## 3. Cálculo de 1 mês com o problema, por máquina

**Fórmula:** `MWh extra/mês = kW × FC × 720 × (% base ÷ 100) ÷ 1000`; `R$ = MWh × preço`.

**Exemplo resolvido (exaustor da sinterização, linha 5):** 5.000 kW × 0,90 = 4.500 kW médios. 4.500 × 720 h = 3.240.000 kWh. × 5% = 162.000 kWh = **162,0 MWh**. × R$ 209 = **R$ 33.858**; × R$ 178 = R$ 28.836; × R$ 250 = R$ 40.500.

| # | Máquina | kW | FC | kW médio | % base | MWh extra/mês | R$ (178) | **R$ (209)** | R$ (250) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Correia transportadora | 400 | 0,65 | 260 | 8,0% | 15,0 | 2.666 | **3.130** | 3.744 |
| 2 | Recuperadora de minério | 500 | 0,45 | 225 | 5,0% | 8,1 | 1.442 | **1.693** | 2.025 |
| 3 | Máquina desenfornadora | 300 | 0,30 | 90 | 5,0% | 3,2 | 577 | **677** | 810 |
| 4 | Exaustor de gás de coqueria | 2.000 | 0,85 | 1.700 | 5,0% | 61,2 | 10.894 | **12.791** | 15.300 |
| 5 | Exaustor da sinterização | 5.000 | 0,90 | 4.500 | 5,0% | 162,0 | 28.836 | **33.858** | 40.500 |
| 6 | Turbo-soprador do alto-forno | 17.000 | 0,90 | 15.300 | 3,0% | 330,5 | 58.825 | **69.070** | 82.620 |
| 7 | Bomba de resfriamento | 800 | 0,80 | 640 | 6,0% | 27,6 | 4.921 | **5.778** | 6.912 |
| 8 | Bomba de alimentação de caldeira | 2.500 | 0,85 | 2.125 | 5,0% | 76,5 | 13.617 | **15.988** | 19.125 |
| 9 | Bomba de recalque | 400 | 0,60 | 240 | 6,0% | 10,4 | 1.846 | **2.167** | 2.592 |
| 10 | Compressor: vazamentos | 1.000 | 0,75 | 750 | 12,5% | 67,5 | 12.015 | **14.108** | 16.875 |
| 11 | Compressor: pressão/filtro | 1.000 | 0,75 | 750 | 2,0% | 10,8 | 1.922 | **2.257** | 2.700 |
| 12 | Despoeiramento primário LD | 3.500 | 0,60 | 2.100 | 6,0% | 90,7 | 16.148 | **18.960** | 22.680 |
| 13 | Despoeiramento da aciaria | 1.800 | 0,80 | 1.440 | 8,0% | 82,9 | 14.764 | **17.335** | 20.736 |
| 14 | Despoeiramento da casa de corrida | 2.500 | 0,80 | 2.000 | 8,0% | 115,2 | 20.506 | **24.077** | 28.800 |
| 15 | Ponte rolante 80 t | 250 | 0,15 | 38 | 10,0% | 2,7 | 481 | **564** | 675 |
| 16 | Torre de resfriamento (ventiladores) | 660 | 0,80 | 528 | 8,0% | 30,4 | 5.413 | **6.356** | 7.603 |
| 17 | Motor de uso geral | 200 | 0,70 | 140 | 1,5% | 1,5 | 269 | **316** | 378 |
| 18 | Ventilador com correia em V | 90 | 0,70 | 63 | 5,0% | 2,3 | 404 | **474** | 567 |
| 19 | Exaustor com vazamento de duto | 250 | 0,80 | 200 | 10,0% | 14,4 | 2.563 | **3.010** | 3.600 |

(Os kW médios das linhas 15 e 17 foram arredondados na tabela; a conta usa 37,5 e 140 kW. Os MWh de cada linha foram calculados com os valores exatos e arredondados depois.)

### Faixa mín–máx de aumento (apenas para mostrar a incerteza)

Extremo inferior com R$ 178 e extremo superior com R$ 250.

| # | % mín | MWh mín | R$ mín (178) | % máx | MWh máx | R$ máx (250) |
|---|---|---|---|---|---|---|
| 1 | 3,0% | 5,6 | 1.000 | 20,0% | 37,4 | 9.360 |
| 2 | 2,0% | 3,2 | 577 | 12,0% | 19,4 | 4.860 |
| 3 | 2,0% | 1,3 | 231 | 10,0% | 6,5 | 1.620 |
| 4 | 2,0% | 24,5 | 4.357 | 10,0% | 122,4 | 30.600 |
| 5 | 2,0% | 64,8 | 11.534 | 10,0% | 324,0 | 81.000 |
| 6 | 1,0% | 110,2 | 19.608 | 6,0% | 661,0 | 165.240 |
| 7 | 3,0% | 13,8 | 2.461 | 12,0% | 55,3 | 13.824 |
| 8 | 2,0% | 30,6 | 5.447 | 10,0% | 153,0 | 38.250 |
| 9 | 3,0% | 5,2 | 923 | 15,0% | 25,9 | 6.480 |
| 10 | 6,0% | 32,4 | 5.767 | 29,0% | 156,6 | 39.150 |
| 11 | 1,0% | 5,4 | 961 | 4,0% | 21,6 | 5.400 |
| 12 | 3,0% | 45,4 | 8.074 | 12,0% | 181,4 | 45.360 |
| 13 | 3,0% | 31,1 | 5.537 | 18,0% | 186,6 | 46.656 |
| 14 | 3,0% | 43,2 | 7.690 | 18,0% | 259,2 | 64.800 |
| 15 | 3,0% | 0,8 | 144 | 25,0% | 6,8 | 1.688 |
| 16 | 3,0% | 11,4 | 2.030 | 20,0% | 76,0 | 19.008 |
| 17 | 0,5% | 0,5 | 90 | 4,0% | 4,0 | 1.008 |
| 18 | 2,0% | 0,9 | 161 | 10,0% | 4,5 | 1.134 |
| 19 | 5,0% | 7,2 | 1.282 | 16,0% | 23,0 | 5.760 |

**Leitura:** o custo mensal de um defeito vai de centenas de reais (ponte rolante, motor pequeno) a dezenas de milhares (sopradores e grandes exaustores). Duas máquinas (turbo-soprador e exaustor da sinterização) respondem por boa parte do total; se o soprador do Pecém for movido a vapor, ele sai da conta elétrica.

---

## 4. Cenário "resolvido em menos de 1 hora"

**Premissa:** o problema duraria 1 mês sem ser percebido; com o VoltMap, a correção ocorre em menos de 1 h. Economia = energia extra do mês − energia extra de 1 hora de operação com defeito (kW médio × 1 h × % base).

**Observação sobre a conta:** como a economia é (720 − 1) ÷ 720 do extra mensal, o percentual evitado é **99,86% para todas as máquinas**. A coluna é igual por construção; o que diferencia as máquinas é o valor absoluto.

| # | Máquina | Extra do mês (MWh) | Extra de 1 h (MWh) | Economia (MWh) | Economia R$ (209) | Faixa R$ (178–250) | % do custo evitado |
|---|---|---|---|---|---|---|---|
| 1 | Correia transportadora | 15,0 | 0,021 | 15,0 | 3.126 | 2.662 – 3.739 | 99,86% |
| 2 | Recuperadora de minério | 8,1 | 0,011 | 8,1 | 1.691 | 1.440 – 2.022 | 99,86% |
| 3 | Máquina desenfornadora | 3,2 | 0,004 | 3,2 | 676 | 576 – 809 | 99,86% |
| 4 | Exaustor de gás de coqueria | 61,2 | 0,085 | 61,1 | 12.773 | 10.878 – 15.279 | 99,86% |
| 5 | Exaustor da sinterização | 162,0 | 0,225 | 161,8 | 33.811 | 28.796 – 40.444 | 99,86% |
| 6 | Turbo-soprador do alto-forno | 330,5 | 0,459 | 330,0 | 68.974 | 58.744 – 82.505 | 99,86% |
| 7 | Bomba de resfriamento | 27,6 | 0,038 | 27,6 | 5.770 | 4.915 – 6.902 | 99,86% |
| 8 | Bomba de alimentação de caldeira | 76,5 | 0,106 | 76,4 | 15.966 | 13.598 – 19.098 | 99,86% |
| 9 | Bomba de recalque | 10,4 | 0,014 | 10,4 | 2.164 | 1.843 – 2.588 | 99,86% |
| 10 | Compressor: vazamentos | 67,5 | 0,094 | 67,4 | 14.088 | 11.998 – 16.852 | 99,86% |
| 11 | Compressor: pressão/filtro | 10,8 | 0,015 | 10,8 | 2.254 | 1.920 – 2.696 | 99,86% |
| 12 | Despoeiramento primário LD | 90,7 | 0,126 | 90,6 | 18.934 | 16.126 – 22.648 | 99,86% |
| 13 | Despoeiramento da aciaria | 82,9 | 0,115 | 82,8 | 17.311 | 14.744 – 20.707 | 99,86% |
| 14 | Despoeiramento da casa de corrida | 115,2 | 0,160 | 115,0 | 24.043 | 20.477 – 28.760 | 99,86% |
| 15 | Ponte rolante 80 t | 2,7 | 0,004 | 2,7 | 564 | 480 – 674 | 99,86% |
| 16 | Torre de resfriamento (ventiladores) | 30,4 | 0,042 | 30,4 | 6.347 | 5.406 – 7.593 | 99,86% |
| 17 | Motor de uso geral | 1,5 | 0,002 | 1,5 | 316 | 269 – 377 | 99,86% |
| 18 | Ventilador com correia em V | 2,3 | 0,003 | 2,3 | 473 | 403 – 566 | 99,86% |
| 19 | Exaustor com vazamento de duto | 14,4 | 0,020 | 14,4 | 3.005 | 2.560 – 3.595 | 99,86% |

**Isto é potencial bruto.** Não desconta custo de reparo, mão de obra, peça e parada de produção; não considera que talvez a máquina precise continuar em operação (muitos desses defeitos só se corrigem com parada programada, e o soprador e os exaustores principais dificilmente param em 1 h); e supõe que o defeito seria de fato detectado (ver Limitações: com limiar de alerta de 15%, a maioria dos percentuais base acima não dispararia).

---

## 5. Cenário de frota: 1% das máquinas com o problema por 1 mês, corrigido em < 1 h

### 5.1 Método (igual nas três escalas)

1. **Consumo elétrico anual** da escala (GWh) → potência média P_med = GWh × 1000 ÷ 8.760 h (MW).
2. **Fração monitorável s** = parcela do consumo que está em motores/ventiladores/bombas/compressores grandes que o VoltMap monitoraria. Referência: motores respondem por ~68% da eletricidade industrial (Procel/Eletrobras, via WEG; fonte secundária citada em `dados/benchmarks-setor.md`); só parte deles seria monitorada (por exemplo, acima de ~75 kW). **Premissa C:** conservador 40%, base 55%, otimista 68%.
3. P_mon = s × P_med (MW monitorados).
4. **Número de máquinas** N = P_mon × 1000 ÷ P_m, onde P_m é a potência média por máquina (**premissa C**): conservador 500 kW, base 250 kW, otimista 100 kW. Máquinas com problema = 1% × N.
5. **% de aumento médio** por defeito = média simples das 19 linhas do catálogo: conservador = média dos mínimos = 2,6%; base = média dos "% base" = 6,3%; otimista = média dos máximos = 13,7% (cálculos com os valores exatos 2,605%, 6,263% e 13,737%). Média ponderada pela energia do "% base" dá 4,7%, menor que a simples porque o soprador (3%) pesa muito; a simples foi mantida por supor máquinas médias.
6. **Energia extra no mês** = 1% × P_mon × (% ÷ 100) × 720 h (MWh). **Extra de 1 h** = 1% × P_mon × (% ÷ 100) × 1 h. **Economia mensal** = extra do mês − extra de 1 h.
7. **Anualização (cuidado):** o ano usa 12 meses, **cada um com um subconjunto diferente de 1% das máquinas**. Isso equivale a 1% de todos os máquina-meses do ano em defeito (cada máquina teria, em média, ~3,6 dias de defeito por ano). Não é "as mesmas máquinas com defeito o ano inteiro". Economia anual = 12 × economia mensal.
8. R$ = MWh × R$ 209 (e faixa 178–250). CO₂ = MWh × 0,046 (só Brasil).

**Propriedade importante:** o N cancela no resultado em MWh (1% × N × P_m = 1% × P_mon). Ele só serve para dimensionar quantas máquinas seriam monitoradas. O resultado depende de consumo, s e % de aumento.

### 5.2 (a) ArcelorMittal Pecém

**Consumo:** `dados/pecem.md` estima 1.200–1.360 GWh/ano (≈ 137–155 MW médios), derivado da geração de 1.367 GWh em 2024 (fonte: Informativo ZPE/Kogake/imprensa da própria empresa) e da autossuficiência declarada; o consumo "168 MW" da CEPAL daria 1.471 GWh. **Estimativa derivada, não dado da empresa.** Conservador 1.200, base 1.280, otimista 1.360 GWh.

| Passo | Conservador | Base | Otimista |
|---|---|---|---|
| Consumo anual (GWh) | 1.200 | 1.280 | 1.360 |
| P_med = GWh × 1000 ÷ 8.760 (MW) | 137,0 | 146,1 | 155,3 |
| s (fração monitorável) | 40% | 55% | 68% |
| P_mon = s × P_med (MW) | 54,8 | 80,4 | 105,6 |
| P_m (kW por máquina) | 500 | 250 | 100 |
| N = P_mon × 1000 ÷ P_m | 110 | 321 | 1.056 |
| Máquinas com problema (1%) | 1,1 | 3,2 | 10,6 |
| % de aumento médio | 2,6% | 6,3% | 13,7% |
| Extra no mês (MWh) | 10,3 | 36,2 | 104,4 |
| Extra de 1 h (MWh) | 0,014 | 0,050 | 0,145 |
| **Economia mensal (MWh)** | **10,3** | **36,2** | **104,3** |
| Economia mensal (R$ a 209) | 2.145 | 7.564 | 21.792 |
| **Economia anualizada (MWh)** | **123** | **434** | **1.251** |
| **Economia anualizada (R$ a 209)** | **25.742** | **90.765** | **261.509** |
| Anual, faixa R$ 178 – R$ 250 | 21.924 – 30.792 | 77.302 – 108.571 | 222.721 – 312.810 |
| CO₂ evitado por ano (t, a 46 g/kWh) | 6 | 20 | 58 |

**Conta de conferência (base):** 146,1 MW × 55% = 80,4 MW; × 1% = 0,804 MW; × 6,263% = 0,0503 MW = 50,3 kW; × 720 h = 36,2 MWh; menos 0,05 MWh (1 h) = 36,2 MWh/mês; × 12 = 434 MWh/ano; × R$ 209 = R$ 90.765/ano.

### 5.3 (b) ArcelorMittal Brasil

**Consumo, duas vias que concordam:**
- Via 1 (imprensa): "cerca de 715 MW médios" de consumo em 2023 (Diário do Comércio, citado em `dados/arcelormittal-brasil.md`, fonte [S56]; **não abri a matéria, só a citação do arquivo**): 715 MW × 8.760 h ≈ 6.263 GWh. Usado no cenário base (6.260 GWh).
- Via 2 (produção × intensidade): a ArcelorMittal Brasil responde por ~42% do aço bruto do país em 2025 (`dados/arcelormittal-brasil.md`, [S45]); o Brasil produziu 33,9 Mt em 2024 (Aço Brasil, `dados/benchmarks-setor.md`, [S22]); 42% × 33,9 ≈ 14 Mt. A intensidade elétrica média do setor é ≈ 434 kWh/t (conta nossa em `dados/benchmarks-setor.md`) e a do Pecém ≈ 500 kWh/t. Conservador: 14 Mt × 400 kWh/t = 5.600 GWh. Otimista: 14 Mt × 500 kWh/t = 7.000 GWh. (A base pela via 2 daria 14 × 434 = 6.076 GWh, perto da via 1.)

**Atenção:** o consumo do Brasil inclui o Pecém, minimills elétricas (Resende, Piracicaba, Juiz de Fora) e mineração; a fração monitorável s poderia diferir.

| Passo | Conservador | Base | Otimista |
|---|---|---|---|
| Consumo anual (GWh) | 5.600 | 6.260 | 7.000 |
| P_med (MW) | 639,3 | 714,6 | 799,1 |
| s | 40% | 55% | 68% |
| P_mon (MW) | 255,7 | 393,0 | 543,4 |
| P_m (kW) | 500 | 250 | 100 |
| N (máquinas) | 511 | 1.572 | 5.434 |
| Máquinas com problema (1%) | 5,1 | 15,7 | 54,3 |
| % de aumento médio | 2,6% | 6,3% | 13,7% |
| Extra no mês (MWh) | 48,0 | 177,2 | 537,4 |
| Extra de 1 h (MWh) | 0,067 | 0,246 | 0,746 |
| **Economia mensal (MWh)** | **47,9** | **177,0** | **536,7** |
| Economia mensal (R$ a 209) | 10.011 | 36.991 | 112.167 |
| **Economia anualizada (MWh)** | **575** | **2.124** | **6.440** |
| **Economia anualizada (R$ a 209)** | **120.130** | **443.898** | **1.346.003** |
| Anual, faixa R$ 178 – R$ 250 | 102.312 – 143.696 | 378.056 – 530.978 | 1.146.357 – 1.610.052 |
| CO₂ evitado por ano (t, a 46 g/kWh) | 26 | 98 | 296 |

**Conta de conferência (base):** 714,6 MW × 55% = 393,0 MW; × 1% = 3,93 MW; × 6,263% = 246 kW; × 720 h = 177,2 MWh; − 0,25 MWh = 177,0 MWh/mês; × 12 = 2.124 MWh/ano; × R$ 209 = R$ 443.898/ano.

### 5.4 (c) ArcelorMittal global

**Consumo:** não achei o consumo elétrico total do Grupo em fonte que eu conseguisse abrir (o relatório de sustentabilidade 2024 deu erro 403; `dados/grupo-global-energia.md` só traz energia primária em PJ e avisa que os GWh de eletricidade do Brasil não são confiáveis). Então **derivei por produção × intensidade**, com intensidade como **premissa C**.
- **Produção:** 55,6 Mt de aço bruto em 2025 (queda de 3,9%), segundo a Metal.com (<https://news.metal.com/newscontent/103914858-crude-steel-output-fell-4-yet-iron-ore-business-soared-26-arcelormittal-performed-in-2025>). Outro resumo da imprensa dá 57,9 Mt para 2025, que parece ser o número de 2024 (<https://www.steelradar.com/en/haber/arcelormittal-closed-2025-with-strong-financial-results/> cita produção e embarques; **os dois diferem e não consultei o Annual Report**). Se 57,9 Mt fosse o correto, os resultados globais subiriam ~4%.
- **Intensidade elétrica (kWh/t de aço bruto), premissa C:** conservador 350, base 420, otimista 500. Faixa ancorada em dois pontos do projeto: média do setor brasileiro ≈ 434 kWh/t e Pecém ≈ 500 kWh/t (`dados/benchmarks-setor.md`, `dados/pecem.md`); o Grupo mistura altos-fornos e fornos elétricos (~25% da produção do Grupo em 2024, por resultado da busca), por isso a faixa é larga. Não achei fonte publicada confiável de kWh/t por rota (buscas retornaram só GJ/t, com convenções diferentes de conversão).
- Contas: 55,6 Mt × 350 = 19.460 GWh; × 420 = 23.352 GWh; × 500 = 27.800 GWh. Usados 19.500, 23.400 e 27.800 GWh (arredondados).
- Mineração e laminadoras não estão na conta de forma explícita.
- **Moeda:** o R$ 209/MWh é referência do Brasil; preços de eletricidade em outros países diferem (em geral mais altos na Europa). O valor em R$ é só uma régua comum.

| Passo | Conservador | Base | Otimista |
|---|---|---|---|
| Consumo anual (GWh) | 19.500 | 23.400 | 27.800 |
| P_med (MW) | 2.226,0 | 2.671,2 | 3.173,5 |
| s | 40% | 55% | 68% |
| P_mon (MW) | 890,4 | 1.469,2 | 2.158,0 |
| P_m (kW) | 500 | 250 | 100 |
| N (máquinas) | 1.781 | 5.877 | 21.580 |
| Máquinas com problema (1%) | 17,8 | 58,8 | 215,8 |
| % de aumento médio | 2,6% | 6,3% | 13,7% |
| Extra no mês (MWh) | 167,0 | 662,5 | 2.134,4 |
| Extra de 1 h (MWh) | 0,232 | 0,920 | 2,964 |
| **Economia mensal (MWh)** | **166,8** | **661,6** | **2.131,4** |
| Economia mensal (R$ a 209) | 34.859 | 138.275 | 445.463 |
| **Economia anualizada (MWh)** | **2.001** | **7.939** | **25.577** |
| **Economia anualizada (R$ a 209)** | **418.310** | **1.659.297** | **5.345.557** |
| Anual, faixa R$ 178 – R$ 250 | 356.264 – 500.371 | 1.413.181 – 1.984.805 | 4.552.675 – 6.394.206 |

**Conta de conferência (base):** 2.671,2 MW × 55% = 1.469,2 MW; × 1% = 14,69 MW; × 6,263% = 920 kW; × 720 h = 662,5 MWh; − 0,92 MWh = 661,6 MWh/mês; × 12 = 7.939 MWh/ano; × R$ 209 = R$ 1.659.297/ano.

**Nota sobre N na escala global:** 5.877 máquinas no cenário base supõe 250 kW médios por máquina em todas as usinas do Grupo; é só ordem de grandeza e não afeta o resultado em MWh.

---

## 6. Sanidade

**Referência:** 1% de eficiência elétrica no Pecém ≈ 12.000 MWh/ano ≈ R$ 2,1 milhões/ano a R$ 178/MWh (`dados/pecem.md`, §4.2; a R$ 209 seria R$ 2,5 milhões).

| Comparação | Resultado |
|---|---|
| Pecém, economia anualizada vs. 1% de eficiência | Conservador 123 MWh (1,0% de 12.000 MWh); base 434 MWh (3,6%); otimista 1.251 MWh (10,4%) |
| Quantas vezes o cenário base precisa crescer para chegar a 1% | 12.000 ÷ 434 ≈ 28 vezes; equivale a ~28% dos máquina-meses em defeito (em vez de 1%) ou a todas as máquinas monitoradas com o defeito médio (80,4 MW × 6,263% × 8.760 h = 44.094 MWh/ano ≈ 3,4% do consumo) cerca de 27% do tempo (12.000 ÷ 44.094) |
| Efeito como fração do consumo, por construção | ≈ 0,010% (conservador), 0,034% (base), 0,092% (otimista) do consumo elétrico, igual nas três escalas (a conta é linear no consumo) |

**Diagnóstico:**
- **Os números não estão inflados; ao contrário, são pequenos.** O cenário "1% das máquinas, 1 mês, corrigido em 1 h" captura só 0,01% a 0,09% do consumo, muito abaixo do 1% de eficiência. Chegar a 1% exigiria defeitos bem mais frequentes ou duradouros, ou outras fontes de perda (máquina ligada sem produzir, vazamentos crônicos, setpoints altos), não só os defeitos deste catálogo.
- O cenário **otimista** do Pecém soma P_mon de 105,6 MW (68% do consumo) com 13,7% de aumento médio, que é o extremo da faixa de cada linha ao mesmo tempo; é um teto improvável, não um valor esperado.
- **Global e Brasil não são "mais promissores" que o Pecém em termos percentuais:** são o mesmo percentual do consumo multiplicado por um consumo maior. O valor global em R$ (R$ 1,7 milhão/ano no base) é pequeno diante do porte do Grupo.
- Comparação com números internos antigos: `solucao.md` cita 100 máquinas com ganho de 5% em ~5 MW monitorados ≈ 2,2 GWh/ano. Aquela conta supõe ganho contínuo de 5% o ano inteiro; esta supõe 1% do tempo. As duas respondem a perguntas diferentes e não devem ser misturadas no pitch.
- Comparação com a linha 5: um único exaustor da sinterização com 5% de excesso por um mês custa ~R$ 34 mil, ou ~37% da economia anualizada base do Pecém inteiro (R$ 90.765); o valor da frota é dominado por poucas máquinas grandes. Por isso a sensibilidade ao kW médio e ao mix de máquinas monitoradas é alta.
- Soma das 19 linhas com base 6,3% operando juntas: 1.113 MWh/mês, mas é hipotética (uma máquina de cada tipo, e o soprador sozinho é 30% do total).

---

## 7. Lista de fontes (acesso em 29/10/2026)

Marcação: **lida** = abri o documento ou a página e conferi o trecho; **resumo da busca** = só vi o resultado da ferramenta de busca (não abri a página, ou a página deu erro) e o dado precisa ser conferido antes de citar publicamente.

| Fonte | URL | Uso | Status |
|---|---|---|---|
| DOE/AMO, Improving Fan System Performance (Fan Sourcebook) | <https://www.energy.gov/sites/prod/files/2014/05/f16/fan_sourcebook.pdf> | Perda de 5–10% em correias; vazamento de duto: 5% de vazão = 16% de potência | lida |
| DOE/AMO, Improving Compressed Air System Performance, v3 | <https://www.energy.gov/sites/prod/files/2016/03/f30/Improving%20Compressed%20Air%20Sourcebook%20version%203.pdf> | 1% por 2 psi; 1,6–2% com consumo não regulado; filtro sujo (qualitativo) | lida |
| Compressed Air Challenge, Fact Sheet #7 (rev. maio/2026) | <https://www.compressedairchallenge.org/data/sites/1/media/library/factsheets2026/fact-sheet-7-compressed-air-system-leaks_updated2026.pdf> | Vazamentos: 20% típico, 20–30% máx., <10% após reparo | lida |
| DOE/AMO, Improving Pumping System Performance, 2nd ed. | <https://www.energy.gov/sites/prod/files/2014/05/f16/pump.pdf> | Mecanismo de folga de anel de desgaste (sem percentual) | lida |
| Pumps & Systems, "Pumping Prescriptions" | <https://pumpsandsystems.com/what-happens-power-efficiency-when-pump-wears-out> | Caso de bomba: 270 → 285 hp, eficiência 65,2% → 53,6% | lida |
| DOE/AMO, Motor Systems Tip Sheet #4 (alinhamento) | <https://www.energy.gov/sites/prod/files/2014/04/f15/importance_motor_shaft_motor_systemts4.pdf> | Desalinhamento sem efeito mensurável na eficiência | lida |
| ERIKS, Problem Solver 129 | <https://eriks.co.uk/content/dam/uk/problem-solvers/pdf-files/Problem-Solver-129-Henkel.pdf> | Bomba de 22 kW ≥30% abaixo do ensaio | resumo da busca |
| Rock Products (Reicks), idler misalignment | <https://rockproducts.com/2016/08/19/idler-misalignment-on-belt-conveyors/> | Parcelas de potência por resistência (CEMA) | resumo da busca (403) |
| Coal Age | <https://www.coalage.com/?p=6814> | Idem | resumo da busca |
| E3S Web of Conferences (2018) | <https://www.e3s-conferences.org/10.1051/e3sconf/20187100004> | Resistência de rolamento até 60% das principais | resumo da busca |
| Univ. Tennessee, estudo de desalinhamento (1999) | <https://efficientplantmag.com/1999/04/study-shows-shaft-misalignment-reduces-bearing-life> | Sem perda de eficiência mensurável; vida do rolamento | resumo da busca |
| Safin et al., Russian Electrical Engineering (2017) | <https://journals.rcsi.science/1068-3712/article/view/230974> | Rolamento defeituoso reduz eficiência (qualitativo) | resumo da busca |
| AEMT/EASA, efeito de reparo na eficiência | <https://www.theaemt.com/resource/revisited-the-effect-of-repairs-on-motor-efficiency.html> | Rebobinagem: média −0,1% | resumo da busca |
| Electrical Engineering Portal (NEMA MG-1) | <https://electrical-engineering-portal.com/voltage-unbalance-nema-motor-performance> | Corrente 6–10× o desbalanço de tensão | resumo da busca |
| IJEECS, compressor axial com incrustação | <https://ijeecs.iaescore.com/index.php/IJEECS/article/view/18553> | Até 4% de perda de potência (turbina a gás) | resumo da busca |
| Garuda (repositório indonésio) | <https://garuda.kemdikbud.go.id/documents/detail/1008459> | Compressor de gás úmido: +8,5% de potência (correspondência não confirmada) | resumo da busca |
| KIT, filtro de mangas (piloto) | <https://publikationen.bibliothek.kit.edu/1000168211/152210383> | ~59% da perda de carga no bolo de pó | resumo da busca |
| Gore, "What a Drag" (World Cement, 2016) | <https://www.gore.com/system/files/2018-09/Article_WorldCementMagazine_What-a-Drag_Filter-Bag-Drag_May2016.pdf> | Dado de fornecedor, só apoio qualitativo | resumo da busca |
| Howden, caso Erdemir | <https://files.chartindustries.com/Howden_Steel_Case_Erdemir.pdf> | Siderurgia: desgaste, damper a 90% (qualitativo) | resumo da busca |
| Howden, caso voestalpine Donawitz | <https://files.chartindustries.com/Howden_CentrifFan_Steel_Case_Donawitz.pdf> | Siderurgia: erosão do rotor (qualitativo) | resumo da busca |
| ABB, New Zealand Steel (ponte regenerativa) | <https://www.abb.com/global/en/news/136755/40-45-energy-savings-achieved-in-new-zealand-steel-crane-operation-after-modernisation-of-large-gantry-crane-with-abb-regenerative-drives> | Contexto de ponte rolante (dado de fornecedor, não é defeito) | resumo da busca |
| Long Parts Pros (blog) | <https://longpartspros.com/blog/is-your-cooling-tower-costing-you-energy> | Torre de resfriamento, fonte fraca | resumo da busca |
| Metal.com, ArcelorMittal 2025 | <https://news.metal.com/newscontent/103914858-crude-steel-output-fell-4-yet-iron-ore-business-soared-26-arcelormittal-performed-in-2025> | Produção de 55,6 Mt em 2025 | resumo da busca |
| SteelRadar, ArcelorMittal 2025 | <https://www.steelradar.com/en/haber/arcelormittal-closed-2025-with-strong-financial-results/> | Produção de 57,9 Mt (conflito) | resumo da busca |
| Arquivos do projeto | `dados/pecem.md`, `dados/arcelormittal-brasil.md`, `dados/benchmarks-setor.md`, `dados/grupo-global-energia.md`, `dados/RANKING-DADOS-POR-IMPORTANCIA.md`, `solucao_main/solucao.md`, `solucao_main/app.md`, `solucao_main/pitches/pitch_tecnico.md` | Premissas de preço, consumo, fator de emissão, máquinas | lidos; os dados externos citados neles ([S21], [S22], [S45], [S56]) não foram reverificados |

Não consegui abrir: DOE Motor Tip Sheet #7 (desbalanço de tensão; erro de certificado) e o Relatório de Sustentabilidade 2024 do Grupo (erro 403).

---

## 8. Limitações

- **Potência e FC são nossas.** Não há kW por máquina do Pecém em fonte pública. Um erro de 2× no kW dobra o resultado da linha correspondente. O piloto precisa medir kW real, horas ligada e FC.
- **Quase nenhum percentual é medido em siderurgia.** Só vazamento de ar, regra de pressão do compressor e perda em correia em V têm fonte confiável, e são de indústria geral (guias do DOE, majoritariamente dos EUA e anteriores a 2010 nas versões que consultei). O caso de bomba é único. Os demais são analogia (B) ou premissa (C).
- **Os defeitos podem ficar abaixo do limiar de alerta.** O pitch técnico usa sobreuso de 15% por 5 minutos como exemplo de regra. Dos percentuais base do catálogo, só o vazamento no compressor (12,5%, perto) e valores máximos chegam perto de 15%. Para pegar defeitos de 3–8% é preciso baseline por regime (kWh por tonelada ou por hora de operação) e limiar menor, o que aumenta o risco de falso alarme. Isso precisa ser medido no piloto.
- **Aumento de kW nem sempre é visível.** Em bombas e ventiladores sem controle de vazão, o desgaste pode reduzir vazão e deixar o kW quase igual ou menor; o dano aparece como perda de desempenho, não como consumo (caso das mangas colmatadas sem controle de vazão e do caso da bomba, em que a vazão caiu 4,9%).
- **Efeitos misturados:** mudança de carga de produção, partida e sazonalidade (temperatura da água, umidade) também alteram o kW. Os percentuais deste documento assumem que o resto fica igual.
- **A hipótese de correção em menos de 1 h é otimista.** Reparos mecânicos em soprador, exaustor e convertedor normalmente exigem parada programada. O potencial da seção 4 é bruto.
- **Escala:** o consumo do Pecém (1.200–1.360 GWh) é derivado; o do Brasil vem de uma citação de imprensa que não abri; o global é produção × intensidade assumida, com duas fontes de produção em conflito. A fração monitorável s e a potência média por máquina são premissas C. Mineração e minimills do Brasil têm perfil de carga diferente.
- **Preço:** R$ 209/MWh é referência pública, não o preço interno do Pecém (pode ser preço de transferência intragrupo; `dados/pecem.md`). O R$ global usa o preço do Brasil só como régua.
- **Anualização:** 12 × o mês significa 1% dos máquina-meses, com máquinas diferentes a cada mês. Não é uma previsão de frequência real de defeitos, que também precisa ser medida.
- **Não incluído:** custo do VoltMap, do reparo, perda de produção, ganhos de vida útil e de manutenção evitada, e benefícios fora da energia ativa (por exemplo, fator de potência baixo, que eleva perdas na rede mas não foi quantificado aqui).

---

**Aviso:** nada neste documento é resultado medido na ArcelorMittal. Os valores são estimativas de ordem de grandeza feitas a partir de dados públicos e de premissas nossas, nos níveis de evidência indicados, e devem ser substituídos por medições do piloto e pelo preço interno antes de qualquer uso externo.
