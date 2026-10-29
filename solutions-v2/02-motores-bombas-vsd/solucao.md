# RotaCerta: raio-X de motores, bombas e ventiladores (superdimensionamento + VSD)

> Legenda: **[CONFIRMADO]** tem fonte; **[ESTIMATIVA]** conta nossa com premissas; **[LACUNA]** perguntar à ArcelorMittal.
> Não repete: 01 (equipamento ligado sem produzir), 02 (demanda/PLD), 03 (vazamento de ar comprimido). Foco aqui: o motor **está produzindo, mas gasta mais do que precisa** (estrangulado por válvula/damper, bypass, superdimensionado).

## 1. Problema
- Bombas e ventiladores de utilidades (água de resfriamento, exaustores, despoeiramento, bombas de descarepação) costumam rodar a rotação fixa e regular a vazão com válvula, damper ou bypass. A energia da "folga" vira calor e ruído.
- Lei de afinidade: reduzir 20% da rotação reduz a potência em cerca de 49% (P ~ n³). Uma válvula fechada não captura esse ganho.
- Na ArcelorMittal Vanderbijlpark, 5 bombas de 1.225 kW ficavam em bypass 50% do tempo; com VSD, **-53% de eletricidade** [CONFIRMADO, ver `dados/RANKING...` item 12]. Em Pecém não se sabe quais motores estão nessa situação [LACUNA].
- EPE (Rota 1): VSD nas utilidades de siderúrgica tem payback de ~0,5 ano [CONFIRMADO, ver dados item 30].

## 2. Como funciona
1. **Triagem de baixo custo (sem parar nada):** pinça/sensor de corrente + tensão por motor (ou leitura dos CCMs, dos inversores e do historian que já existirem) e, onde possível, pressão/vazão. Prioridade: motores acima de 75 kW.
2. **Diagnóstico por IA/regras:** compara carga real (kW, fator de carga, curva da bomba) com a nominal. Marca: (a) fator de carga baixo constante (superdimensionado), (b) carga variável sem inversor (candidato a VSD), (c) bypass/recirculação (corrente alta com pouca vazão útil), (d) ponto de operação longe do BEP (melhor eficiência da bomba), (e) inversor existente rodando a 50/60 Hz fixo.
3. **Recomendação priorizada:** ranking por R$/ano e payback, com a ação (instalar VSD, trocar rotor/motor por IE3/IE4, ajustar setpoint de pressão, desligar a bomba redundante).
4. **Otimização em operação (fase 2):** onde já há VSD, setpoint dinâmico (menor pressão aceitável, sequenciamento de bombas em paralelo) com IA em modo **sugestão ao operador**, nunca em malha fechada no início.
5. **M&V contínuo:** baseline pré-ação vs. depois, em kWh e R$, no padrão que a ArcelorMittal cobra (Belval: app fácil, impacto medido, ROI < 2 anos).
- **App:** painel por área, lista de "motores ordenados por desperdício", relatório mensal em kWh, R$ e tCO2 (fator 46 g/kWh da própria empresa).

## 3. Referências validadas
Nenhum caso exatamente igual ("IA que acha motor superdimensionado em siderúrgica brasileira") foi achado. Há validação de partes: tecnologia (VSD em aço), startups e prêmios. Resultados de fornecedor são autodeclarados.

| # | Referência | País | O que faz / resultado | URL |
|---|---|---|---|---|
| 1 | ABB Startup Challenge 2026, vencedor **Faraday Predictive** (Cambridge) | Reino Unido (cidade citada; país não informado na fonte) | Monitora motor só com tensão e corrente, embutido nos inversores ABB; detecta falhas e **desperdício de energia**. Prêmio de US$ 30 mil + piloto com clientes ABB | https://www.electronicspecifier.com/?p=205714 |
| 2 | ABB Startup Challenge 2026, vencedor **Forgis** | Europa (país não informado) | Plataforma de IA para configuração, comissionamento e diagnóstico de sistemas de fábrica, com meta de eficiência energética | https://www.electronicspecifier.com/?p=205714 |
| 3 | ABB Startup Challenge India 2025, vencedor **Cloudworx** (Bengaluru) | Índia | Gêmeo digital com IA; simplifica seleção/comissionamento de motores e inversores ABB e manutenção. Sem número de economia publicado | https://themachinemaker.com/news/cloudworx-wins-abb-startup-challenge-india-2025-for-advancing-ai-driven-smart-drive-solutions/ |
| 4 | **iPUMPNET** (Pump Academy), Bootstrap Startup Award, National Startup Awards 5.0 (2026) | Índia | IoT + IA + controle de bombas; economia anual esperada > ₹40 crore (~US$ 4,4 mi) em 78 estações de bombeamento da BWSSB (**projeção do fornecedor**) | https://www.wateronline.com/doc/ipumpnet-wins-national-startup-award-bootstrap-innovation-digital-management-critical-pumping-systems-0001 |
| 5 | **Siemens, Sidenor** (aço) | Grécia | Auditoria + 15 inversores SINAMICS G120 + controle por temperatura em ~80 bombas de 30-132 kW: **-46% de energia medido** (kWh e payback não informados) | https://references.siemens.com/en/reference/sidenor-greece?id=40892 |
| 6 | **ABB / Halcyon Drives, Tata Steel Rotherham** | Reino Unido | 5 inversores em bombas antes em partida direta: ~**£68 mil/ano** (ex.: filtro 355 mil para 131 mil kWh). Custo do projeto não informado | https://www.operationsengineer.org.uk/content/features/steel-maker-set-to-save-68-000-on-pumping-energy-costs-with-abb-drives |
| 7 | **ArcelorMittal Vanderbijlpark** (AMSA) | África do Sul | VSD em bombas de 1.225 kW em bypass: **-53%**, contrato de economia compartilhada | https://www.crown.co.za/latest-news/mechchem-africa-latest-news/7984-industrial-efficiency-initiatives-an-amsa-success-story |
| 8 | **eBigData** (startup de IA para bombas e compressores) | n/d | Alega -11% em média; só material do fornecedor, não verificado de forma independente | (encontrado via busca; verificar o site antes de citar) |
| 9 | Hackathon Saudi Digital Machines, 2º lugar (alunos PSAU) | Arábia Saudita | Projeto de eficiência de ventiladores de usina com IoT e IA; só notícia universitária, sem resultados | https://np.psau.edu.sa/en/psaus-students-achieve-2nd-place-saudi-digital-machines-hackathon |

Leitura: o mercado já premia "IA em cima de motor/inversor" (ABB, 2025 e 2026), e o ganho de VSD em aço é medido (46-53%). O que é novo é a combinação triagem + ranking de R$ + M&V para uma planta que não tem medição por motor.

## 4. Adaptação à ArcelorMittal Pecém
- Alvos prováveis [LACUNA, confirmar]: bombas de água de resfriamento/recirculação, exaustores do despoeiramento (sínter, aciaria), ventiladores, correias até o porto (~10 km), bombas de descarepação/lingotamento.
- Narrativa: a equipe do Pecém já otimiza a geração com os gases (BFG/COG); o "fino" está no consumo das utilidades. Cada kWh poupado é kWh a mais de excedente para vender (declaração do CEO, dados item 4).
- Métrica na régua deles: kWh, R$ (R$ 178-250/MWh), tCO2 (46 g/kWh), GJ (9,208 GJ/MWh).
- Cuidado: motor de processo crítico (alto-forno, lingotamento) não se mexe sem a operação; começar por utilidades com redundância.

## 5. Estimativa de ganho [ESTIMATIVA]
Premissas: (a) Pecém consome ~1.200-1.360 GWh/ano (derivado, ver dados item 3); (b) utilidades acionadas por motor com controle por válvula/damper ou fixas representam 20% do consumo (chute, a validar); (c) 10-30% desse bloco é recuperável com VSD/ajuste, de acordo com casos de 46-53% em bombas específicas, mas com cobertura parcial; (d) R$ 200/MWh.
- Bloco: ~1.300 GWh x 20% = 260 GWh. Ganho 10%-30% = **26-78 GWh/ano = R$ 5-16 mi/ano**, ~1,3-4 mil tCO2/ano.
- Conservador (só EPE, 0,02 GJ/t x 3 Mt): ~16,7 GWh/ano = R$ 3-4 mi/ano (dados item 30).
- Piloto (5 bombas de 90 kW, 8.000 h, fator de carga 0,8 e 30% de corte): 5 x 90 x 0,8 x 8.000 x 0,30 = **864 MWh/ano, ~R$ 173 mil/ano**. Custo de 5 VSD de 90 kW ~R$ 150-250 mil [ESTIMATIVA]: payback ~1-1,5 ano.
- Os números dependem do inventário de motores [LACUNA]; apresentar como faixa.

## 6. Monetização
- **SaaS de diagnóstico:** R$ 3-8 mil/mês por planta/área (sensores em comodato ou revenda).
- **Economia compartilhada (como em Vanderbijlpark):** 20-30% da economia medida por 24-36 meses, sem capex para a ArcelorMittal; o VSD/hardware é financiado pelo parceiro (integrador/fabricante).
- **Canal:** indicar integradores e fabricantes de inversor (WEG é brasileira, ABB, Siemens) com comissão; PMEs do CIPP/Ceará como segundo segmento (Sebrae).

## 7. Viabilidade e riscos
- Técnica: média. Triagem por corrente é simples; o ganho vem do VSD, que exige parada, projeto elétrico e NR-10.
- Risco de processo: reduzir vazão/pressão pode afetar resfriamento ou despoeiramento; por isso sugestão ao operador e testes escalonados.
- Medição: sem medidor por motor, depende de sensores de terceiros ou do historian [LACUNA]; TI/OT pode barrar rede.
- Concorrência: ABB, Siemens e WEG têm sensores/IA próprios (a ABB co-investe em startups no tema). Nosso diferencial: ranking financeiro independente de marca, M&V e foco na planta.
- Honestidade: o hackathon não prova o ganho real; a economia vem da ação física (VSD), o software prioriza e comprova.
- Banca 2025 premiou monitoramento genérico: diferenciar com R$ por motor e ação concreta.

## 8. MVP em 5 dias (3-5 alunos)
- Dia 1: escolher 3 perfis de carga (bomba com válvula, exaustor com damper, bomba com bypass) e definir fórmulas (lei de afinidade, curva de bomba).
- Dia 2: **simulador/dataset sintético** de ~30 motores (kW, horas, fator de carga, estrangulamento), calibrado com Vanderbijlpark/Tata/Sidenor.
- Dia 3: motor de regras + modelo simples (detecção de baixo fator de carga e ponto longe do BEP; opcional: ML em dados públicos de bombas).
- Dia 4: app web (Streamlit ou React): ranking de motores, economia em R$/kWh/tCO2, payback do VSD, simulação "e se" de queda de rotação.
- Dia 5 (opcional, demo física): ESP32 + sensor de corrente (SCT-013) em um ventilador/bomba pequena com dimmer/inversor mostrando kW em tempo real e curva.
- Pitch: "Vanderbijlpark -53% numa usina de vocês. Nós achamos os próximos 30 motores e provamos o ganho em kWh."

## 9. Perguntas a validar
1. Existe inventário/medição por motor (CCM, historian, PI)? Quantos motores acima de 75 kW sem VSD?
2. Há bombas em bypass/recirculação ou válvulas estranguladas nas utilidades (água, despoeiramento)?
3. Qual o payback máximo aprovado (2 anos como em Belval)? Aceitam economia compartilhada?
4. Quanto vale 1 MWh poupado (PLD, contrato ou preço intragrupo)?
5. Quem é o dono do piloto (Utilidades, Manutenção, iNO.VC) e por qual canal a startup entra (Açolab)?
6. Dos 12 projetos de eficiência (R$ 63 mi/ano), algum já cobre VSD no Pecém?
7. Sensor externo em CCM é permitido (NR-10, rede isolada 4G/LoRa)?
