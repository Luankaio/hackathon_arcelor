# 06 - Febre (nome provisório): degradação que vira kWh, detectada antes de virar parada

> Pesquisa de 28/10/2026. **[VALIDADO]** = achado em fonte com URL. **[ESTIMATIVA]** = conta nossa com premissa explícita. Números de fornecedores são alegações deles, não verificadas.

## Problema
Equipamento que degrada gasta mais energia antes de falhar: conexão elétrica frouxa (resistência sobe, vira calor/perda), motor com rolamento ruim, desbalanceamento ou desalinhamento (mais corrente para o mesmo trabalho), trocador de calor sujo (bomba/ventilador compensa), fator de potência e harmônicos ruins. Hoje isso só aparece em rota de inspeção periódica (termografia manual) ou depois da falha. O desperdício é silencioso e não tem dono. É diferente das soluções 01 (ocioso), 02 (demanda/PLD) e 03 (ar comprimido): aqui o equipamento está produzindo, mas ineficiente por desgaste.

## Como funciona
1. **Sensores baratos, retrofit, sem parar a planta:** pinça de corrente (TC split-core) no painel do motor (corrente e tensão -> kW, fator de potência, THD, desbalanceamento de fases); acelerômetro + temperatura (MEMS) no mancal; câmera térmica de baixa resolução (ex.: MLX90640/Lepton) ou sensor IR fixo em painel/CCM; termopar/PT100 na entrada e saída de trocadores.
2. **Borda (ESP32/Raspberry Pi):** coleta e calcula features (RMS, espectro de corrente - MCSA, kW/carga, delta-T), envia por MQTT/LoRa/Wi-Fi.
3. **IA em duas camadas:** (a) linha de base por equipamento e por regime de carga, com detecção de anomalia (Isolation Forest/autoencoder) sobre "kW por unidade de carga" e sobre as assinaturas de falha; (b) visão computacional para hotspot em imagem térmica (segmentar painel/conexão, acompanhar tendência de delta-T em relação à fase vizinha).
4. **App/painel (celular do técnico):** lista de ativos ordenada por **R$/mês desperdiçado + risco**, com a causa provável ("fase B com 4 °C acima das outras há 9 dias"), ação sugerida e botão para gerar ordem de manutenção. A métrica central é kWh evitado e parada evitada, não "alarme".

## Referências validadas
| # | Caso (país) | O que fazem / o que foi validado | URL |
|---|---|---|---|
| 1 | **Semiotic Labs SAM4** (Holanda) em **ArcelorMittal Gent** (Bélgica) | Sensor no armário do motor, análise de corrente (MCSA). Piloto de 12 meses nos motores dos transportadores do laminador a quente: 12 falhas em desenvolvimento detectadas, todas confirmadas pela manutenção (relato do fornecedor). Mesma empresa do grupo, mesma lógica de retrofit. | https://v2.iotone.com/case-study/arcelormittal-condition-monitoring/c1272 |
| 2 | Documento ISPT, caso de uso SAM4 (Holanda) | Cita ArcelorMittal Gent como usuário e explica por que corrente é usada onde vibração falha (alta temperatura). | https://ispt.eu/media/SAM4-use-case.pdf |
| 3 | **OneWatt Solutions** (Filipinas) | Vencedora do Delta Special Award (US$ 10 mil) no InnoVEX 2018 e da etapa filipina do Seedstars. Sensor acústico + IA em motores; alega -70% de falhas e +10% de eficiência energética (alegação da empresa). Projeto UE com TRL 7. | https://brandnews.deltaww.com/EN/BrandCircleDetail/1755 ; https://cordis.europa.eu/project/id/827712 |
| 4 | **Pioneers 4.0 Hackathon, equipe MBZUAI** (Emirados Árabes) | Time estudantil venceu (AED 25 mil) com caso de negócio de manutenção preditiva sobre séries temporais, com economia de energia e redução de paradas. Fonte não detalha sensores. | https://mbzuai.ac.ae/news/less-downtime-less-energy-in-predictive-maintenance-ai-solution/ |
| 5 | **Dynamox** (Brasil, Florianópolis) | Sensores sem fio de vibração/temperatura (DynaPredict) + app/plataforma, também corrente e tensão; roda em Google Cloud. Prova que há mercado e capacidade local. Não achei cliente siderúrgico na busca. | https://cloud.google.com/customers/intl/pt-br/dynamox |
| 6 | **InfraSensing** (EUA) e **ABB SensyCal FCU400-IR** | Monitoramento térmico contínuo de painéis/chaves (sensores IR em janelas de inspeção). Produtos reais; mostram a categoria "termografia contínua", cara e voltada a MT. | https://infrasensing.com/sensors/sensor_thermography_cylindrical.asp ; https://new.abb.com/products/measurement-products/zh/flow-computers/universal-measurement-computers/sensycal-fcu400-ir-universal-measurement-computer |
| 7 | Dissertação UFPR (Brasil) | Dispositivo com sensores de corrente, vibração e temperatura + microcontrolador IoT, custo ~R$ 450 (~90% abaixo de comerciais), erro de corrente <5%. Prova técnica do hardware barato. | https://acervodigital.ufpr.br/xmlui/handle/1884/99741 |
| 8 | Estudo ISB / FAU-Siemens (Índia / Alemanha) | Visão computacional sobre imagens térmicas para prever falha de painéis elétricos (acadêmico, não comercial). | https://blogs.isb.edu/iids/2023/06/22/ai-based-failure-prediction-of-industrial-electrical-systems-using-thermal-imaging/ ; https://lme.tf.fau.de/?p=23595 |

**Lacunas honestas:** (a) não achei hackathon vencedor que una câmera térmica de baixo custo + energia; o mais próximo são #3 e #4. (b) A ligação "degradação -> kWh extra" é física conhecida (perda I²R, motor degradado), mas as referências acima vendem mais "falha evitada" do que "kWh evitado"; o argumento energético deve ser medido por nós. (c) Páginas do tipo Oxmaint ("ArcelorMittal Sentinel", -40% de paradas) são marketing sem fonte; não usei.

## Adaptação ao Pecém
- A ArcelorMittal já testou o conceito em Gent (#1), logo há aceitação interna; o diferencial nosso é **custo baixo, foco em R$ de energia e app para o operador/eletricista** (critério de compra citado em `dados/RANKING`: app fácil, mede impacto, ROI < 2 anos).
- Alvos de maior retorno no Pecém: motores de bombas/ventiladores grandes (águas, despoeiramento, sopradores), centros de controle de motores e painéis de BT, trocadores de calor de circuitos de água de resfriamento, e fator de potência/harmônicos nos acionamentos (VSD) dos laminadores.
- A tese "kWh poupado = kWh vendido" (excedente da termelétrica) vale aqui também, e o aço aceita o argumento de segurança (conexão quente = risco de incêndio), que ajuda a vender internamente.
- Clima quente e poeira em Pecém: preferir sensor de corrente (fora do campo, #1/#2) e térmico em invólucro IP; vibração com cuidado perto de fornos.

## Estimativa de ganho (ESTIMATIVA, não dado)
Premissas: consumo ~500 kWh/t e 1% de eficiência = 12-14 GWh/ano = R$ 2-3 mi (derivado em `dados/`); PLD/valor do MWh ~R$ 150-200/MWh.
- Se 3-5% da carga de motores monitorados opera degradada e a correção recupera 3-8% da energia desses motores, num recorte piloto de **5 MW médios monitorados**: 5 MW x 8.760 h = 43.800 MWh; x 4% x 5% = **~90 MWh/ano (~R$ 15-20 mil)**. Pequeno; o ganho energético sozinho é modesto.
- O valor maior é **parada evitada**: uma falha de motor/painel crítico em linha de placas pode custar dezenas a centenas de milhares de reais por hora parada (valor a obter com a empresa). Pitch: **energia paga o sensor, parada evitada paga o projeto**.
- Fator de CO2 da empresa: 46 g/kWh, então o ganho de CO2 é pequeno; não usar como argumento principal.

## Monetização
- SaaS por ativo monitorado (R$/ativo/mês) + kit de sensores em comodato ou venda.
- Piloto com **shared savings** (percentual da economia verificada), como em Vanderbijlpark (`dados/projetos-eficiencia-ja-feitos.md`).
- Venda para fornecedores/PMEs da cadeia no Pecém (bomba, ventilador, compressor), onde Dynamox-like é caro demais.

## Viabilidade e riscos
- Concorrência forte (Semiotic, Dynamox, Tractian, ABB): mitigar com nicho "R$ de energia + painéis + preço baixo" e integração, não com sensor próprio.
- Poucos dados rotulados de falha: começar com detecção de anomalia e regras físicas (delta-T entre fases, kW/carga).
- Ambiente industrial: segurança elétrica (instalar TC split-core exige eletricista habilitado, NR-10), EMI, rede OT/ciberseguridade da planta.
- Falsos alarmes derrubam a adoção; priorizar poucos alertas com R$ associado.
- Ganho de energia isolado é pequeno (ver acima); o pitch precisa do argumento de confiabilidade.

## MVP em hackathon (5 dias, 3-5 alunos)
- Dia 1: escolher alvo (um motor + um painel/ventilador de bancada), definir sensores: ESP32 + SCT-013 (corrente) + MPU6050 + MLX90640 (térmica 32x24), custo < R$ 300.
- Dia 2: coleta e dashboard (MQTT -> InfluxDB/Grafana ou app simples). Simular defeito: carga desbalanceada, ventilador obstruído, conexão com resistência extra.
- Dia 3: modelo de anomalia (kW/carga, THD, delta-T) + detecção de hotspot na imagem térmica.
- Dia 4: app/tela "ranking de R$ desperdiçados" + ordem de manutenção; cálculo de kWh e R$ usando fator e PLD da pasta `dados/`.
- Dia 5: demo ao vivo (provocar defeito, ver alerta e R$) + pitch com casos #1, #3, #7. Dados sintéticos/públicos (ex.: datasets de rolamentos) como reserva.
- Papéis: hardware/firmware, dados/IA, visão computacional, app/UX, pitch/negócio.

## Perguntas a validar com a ArcelorMittal
1. Já existe termografia periódica e MCSA/vibração no Pecém? Quem faz (interno/terceiro) e onde os dados ficam?
2. Qual o custo médio por hora de parada da linha de placas/laminador e quais ativos são críticos?
3. Há medição de kW por motor/CCM (medidores, SCADA/PI)? Podemos acessar via OPC/Modbus?
4. Qual o histórico de falhas de painéis/motores por energia ou calor (incêndios, trip) e custo?
5. Há restrição de rede OT e de instalação de sensores sem fio na área?
6. Fator de potência e harmônicos geram multa ou perda hoje? Em quais barramentos?
7. Qual ROI/critério para um piloto e quem é o dono (manutenção elétrica, energia ou inovação)?
