# TermoRadar: mapa vivo de perdas térmicas (purgadores, vapor, isolamento) com ranking de payback

> Status: proposta v2 (28/10/2026). Todo número de ganho é ESTIMATIVA com premissas marcadas. Dados da ArcelorMittal vêm de `dados/` (fontes lá).

## 1. Problema
- O Pecém já recupera o calor "grosso" (termelétrica com gases de processo, 1.367 GWh em 2024; TRT de 16 MW). Sobra o calor "fino" das utilidades: vapor de processo (~65-90 t/h), purgadores com falha, linhas de vapor/condensado sem isolamento, gases quentes de fornos e chaminés sem recuperação.
- Cada t/h de vapor perdida vira gás de processo queimado que não vai para a termelétrica, ou seja, menos excedente de energia vendável. Tubarão (usina-irmã) cita perdas de vapor de ~3 t/h (Fenergia 2018).
- Hoje a inspeção é manual e periódica (ronda de purgadores, termografia pontual): falha fica aberta por meses, e ninguém prioriza por R$.

## 2. Como funciona
1. **Sensores baratos, sem intervenção no processo:** (a) sensor acústico + temperatura clipado no tubo, antes de cada purgador (LoRa/bateria); (b) termografia periódica (câmera FLIR/celular com acessório térmico, drone ou ronda) de linhas, flanges, válvulas e carcaça de fornos; (c) leitura de medidores de vapor/temperatura de chaminé já existentes (historian, se houver).
2. **IA/regras:** classificador de estado do purgador (ok / vazando / entupido) por assinatura acústica+temperatura; visão computacional sobre imagem térmica para achar trechos sem isolamento e estimar perda (W/m² via diferença de temperatura superfície-ambiente, fórmula padrão de convecção+radiação); para gases quentes, balanço de energia (T, vazão, composição) para estimar kW recuperáveis.
3. **Motor de priorização:** converte cada achado em kg de vapor/h -> MWh -> R$ (preço do gás de processo/MWh excedente) e ordena por **payback** (custo de reparo/isolante vs. economia). Saída é uma fila de ordens de serviço, não só um alarme.
4. **App/dashboard (operador + engenheiro de energia):** mapa da planta com pontos coloridos, lista "conserte estes 10 primeiro", economia acumulada medida (M&V antes/depois), exportação para a OS da manutenção.

## 3. Referências validadas
Resultado da busca (28/10/2026): **não achei vencedor de hackathon** ligado a calor residual industrial com IA (só hackathons de calor urbano/data center, sem aderência). A validação abaixo é de **empresas e projetos reais**, não de hackathon.

| Referência | País | O que fazem / provam | URL |
|---|---|---|---|
| Armstrong AIM 5700 | EUA | Monitoramento sem fio de purgadores (guia de onda no tubo, WirelessHART): detecta entupido/vazando. Prova a tecnologia de sensor. | https://www.controlglobal.com/home/article/11306634/armstrong-offers-advanced-wireless-monitoring-solution-for-steam-traps |
| Spirax Sarco, monitoramento sem fio | Reino Unido | Sensores por purgador + dashboard de condição. Prova demanda industrial. | https://www.spiraxsarco.com/global/en-SG/promo/wireless-steam-trap-monitoring |
| Yokogawa sensor de purgador (acústico+temperatura) | Japão | Caso em processamento de milho; sensor sem fio acústico+temperatura. | https://yokogawa.com/mx/library/resources/application-notes/wireless-steam-trap-monitoring-conserves-energy-in-corn-processing |
| Feelit (piloto na ELSA-Mifroma) | país não confirmado na fonte | Startup de sensores de purgador: piloto com 25 de ~500 purgadores, ~25% dos monitorados falhando/subdesempenhando; cliente expandiu para 50. Prova achado + expansão de piloto pequeno. | https://feelit.tech/wp-content/uploads/2022/03/Elsa-Group-Feelit_final.pdf (PDF; lido só pelo resumo de busca, conferir) |
| I/O Sense | não confirmado | Algoritmos de vazamento/entupimento em hardware LoRa a bateria. Prova modelo de baixo custo. | https://www.faclon.com/iot-steam-trap (página do produto de purgador; confirmar autoria/país) |
| ArcelorMittal + Capgemini Engineering, projeto ANAGREEN | França | Modelos e analytics para achar calor residual e avaliar trocadores, bombas de calor e armazenamento; a página cita potencial de "2,4 TJ (0,67 TWh)" para usinas francesas (unidades inconsistentes na fonte, não usar o número); gera sistema de apoio à decisão com custo, payback e CO2. **Validação interna: a própria empresa investe nisso.** | https://www.casestudies.com/company/capgemini/case-study/arcelormittal-uses-data-and-analytics-to-pursue-energy-efficiency |
| ArcelorMittal Zenica + Endress+Hauser | Bósnia | Medição de vapor em 39 pontos reportando energia/fluxo, para reduzir custos sistematicamente. Prova que o Grupo já mede vapor. | https://www.casc.endress.com/en/Endress-Hauser-group/Case-studies-application-notes/steam-monitoring-energy-solutions |
| Fero Labs | EUA | Startup de IA para siderurgia/processo (clientes: Gerdau, Celsa Nordic, Ford etc.); relata >US$ 20 mi de economia a clientes. **Não achei caso específico de forno de reaquecimento.** | https://www.esgtoday.com/ai-tech-startup-fero-labs-raises-15-million-to-drive-manufacturing-decarbonization/ |
| ValueHeat (LIST) | Luxemburgo | Software que compara opções de recuperação de calor residual; estágio inicial (TRL/CRL inconsistentes na página). | https://ventures.list.lu/ventures/valueheat |
| Desafio Tata Steel (calor de baixa temperatura 150-200 C) | Índia/Singapura | Siderúrgica abriu desafio a startups (TRL 5-8) para reaproveitar calor de baixo grau. Prova demanda do setor. | https://sustainability.innovation-challenge.sg/en/page/tata-steel-low-grade-heat-waste-en (página retornou 404 no fetch; só vista na busca) |

Não validado: alegações de "5-12% de economia com IA em forno" (blog de fornecedor sem fonte). Não usar no pitch.

## 4. Adaptação ao Pecém
- Alvo 1 (mais fácil, sem parar produção): rede de vapor e condensado das utilidades; purgadores em coqueria, aciaria e área de gases.
- Alvo 2: isolamento de tubulações/carcaças por termografia (ronda de 1 dia gera mapa).
- Alvo 3 (fase 2): gases quentes de fornos/chaminés sem recuperação, usando o modelo de balanço e a comparação trocador vs. bomba de calor (linha ANAGREEN).
- Linguagem de valor da empresa: "kWh/GJ poupado = mais excedente vendido" (CEO, 2024; Tubarão 2018). Usar GJ/t, fator de vapor do Grupo (AP 3.350 MJ/t, BP 3.050 MJ/t) e CO2 com 46 g/kWh.
- Não repete 01-03 de `solutions/` (ocioso, PLD, ar comprimido): foco térmico/vapor.

## 5. Estimativa de ganho (ESTIMATIVA, premissas explícitas)
- Premissa A: 500 purgadores relevantes, 15-25% com falha (faixa observada no piloto Feelit; não é dado do Pecém). Vazamento médio 10-30 kg/h por purgador falho (premissa de engenharia, validar).
- Cálculo: 100 purgadores falhos x 20 kg/h = 2 t/h; vapor BP 3.050 MJ/t => ~6,1 GJ/h => ~1,7 MWh térmico/h => ~14,9 GWh/ano (8.760 h).
- Valor: se o MWh térmico equivale a gás de processo que viraria eletricidade com ~35% de eficiência (premissa), ~5 GWh elétricos/ano ≈ R$ 0,9-1,3 mi/ano (R$ 178-250/MWh, `dados/`). Isolamento: +R$ 0,3-1 mi/ano (premissa grosseira, sem dados de trechos).
- Ordem de grandeza total: **R$ 1-2 mi/ano e ~ 10-15 GWh térmicos recuperados**; custo de piloto na casa de dezenas de milhares de R$ (sensores). Payback esperado < 1 ano (estimativa; critério da empresa é < 2 anos, Belval).
- Cautela: Tubarão cita perdas de ~3 t/h, o que sustenta a ordem de grandeza.

## 6. Monetização
- Piloto pago / PoC com mentor de Utilidades; depois SaaS por ponto monitorado (R$/sensor/mês) + hardware em comodato.
- Alternativa: **economia compartilhada** (% do vapor/R$ economizado, medido por M&V), modelo já aceito no Grupo (Vanderbijlpark).
- Segmento secundário: PMEs com caldeira no CE (alimentos, têxtil, cerâmica) via Sebrae/CE.

## 7. Viabilidade e riscos
- Técnico: acústica em ambiente ruidoso de siderúrgica, calibração por tipo de purgador, emissividade em termografia (erro de temperatura), acesso em área classificada/ATEX (sensores certificados são mais caros).
- Concorrência: Spirax, Armstrong e Yokogawa vendem hardware; nosso diferencial seria o ranking em R$ + OS + M&V e foco no contexto siderúrgico/regional. Risco real de "mais um monitor".
- Organizacional: TI/OT, NR-10, dono do piloto, e dados de vapor possivelmente fechados. Banca 2025 premiou "monitoramento genérico": evitar tom genérico, mostrar R$.
- Ganho depende de dado de vazamento real do Pecém; a estimativa acima pode estar acima ou abaixo em ordem de grandeza.

## 8. MVP em 5 dias (3-5 alunos)
- Dia 1: definir modelo de custo (vapor -> kg/h -> R$) com dados públicos; coletar dataset aberto de purgadores/termografia.
- Dia 2: protótipo de hardware: ESP32 + microfone/acelerômetro + termopar em bancada com "purgador" simulado (válvula com vazamento) + dados sintéticos.
- Dia 3: classificador simples (RF/XGBoost em features espectrais) + detector de pontos quentes em imagens térmicas (limiar + estimativa de W/m²).
- Dia 4: dashboard (mapa/planta sintética, fila por payback, economia acumulada) e geração de OS.
- Dia 5: demo ao vivo (sensor + câmera térmica de celular), pitch com cálculo de R$ e comparação com a referência Feelit/ANAGREEN.
- Papéis: embarcado, ML/visão, back/front, negócio/pitch (+1 engenharia térmica).

## 9. Perguntas a validar com o mentor
1. Existe inventário e rotina de teste de purgadores? Qual % de falha medido, e quantos pontos?
2. Quanto vapor se gera/consome por área, e qual o preço interno (gás de processo/MWh excedente)?
3. Há termografia periódica hoje? Quem faz e com que frequência?
4. Fornos de reaquecimento ou chaminés com gases >200 C sem recuperação? Existe estudo de viabilidade?
5. Sensores sem fio (LoRa) são permitidos em área classificada? Quem instala?
6. Payback máximo para aprovar e canal de entrada (Açolab/iNO.VC)?
7. Algum dos 12 projetos de eficiência (R$ 63 mi/ano) já cobre vapor/purgadores no Pecém?
