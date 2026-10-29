# 01 — RotaCerta: IA + sensor de corrente para achar motores desperdiçando energia

> v3 (28/10/2026). Evolui `solutions-v2/02-motores-bombas-vsd`. Marcação: **[Fato]** = visto em fonte; **[Estimativa]** = conta nossa; **[Verificar]** = só li em resumo de busca.

## Problema
Motores, bombas e ventiladores concentram a maior parte da eletricidade industrial, e muitos operam superdimensionados, em bypass ou sem inversor (VSD). Ninguém vê, porque a medição costuma ser por alimentador, não por máquina.

## Como funciona (IA + hardware + software)
- **Hardware:** sensor de corrente (TC de alicate/Rogowski) + tensão por motor, num gateway ESP32/Raspberry (Modbus/MQTT). Sem parar o processo.
- **IA:** modelo que estima carga real vs. nominal, detecta bypass/estrangulamento e anomalias (desbalanceamento, perda de eficiência) a partir de assinatura de corrente.
- **Software:** ranking em R$/ano por motor, recomendação (trocar, instalar VSD, desligar), M&V (IPMVP) para provar o ganho.

## Validação (startups e prêmios)
| Referência | O que é | Validação | Fonte |
|---|---|---|---|
| Faraday Predictive | Monitora sistemas de motores só com sinais de tensão e corrente, sem sensor extra, com física + IA | Vencedora, categoria Motion High Power, ABB Startup Challenge 2026 [Fato] | [ABB](https://www.abb.com/global/en/news/134787/abb-startup-challenge-winners-drive-ai-powered-energy-innovation) |
| Forgis | IA embarcada em inversores ABB: transforma motor em monitor de condição, detecta falhas e desperdício de energia | Vencedora, Motion Drive Products, ABB 2026 [Fato, via resumo de busca; página da ABB deu timeout] | [ABB](https://www.abb.com/global/en/news/134787/abb-startup-challenge-winners-drive-ai-powered-energy-innovation) |
| Semiotic Labs (SAM4) | Sensor de corrente/tensão + nuvem/IA para motores | Projeto ERGO (ISPT): 303 motores analisados, mais da metade poderia ser redimensionada, economia de até 53% [Fato]. Piloto de 12 meses em motores de transportadores de laminação a quente da ArcelorMittal, 12 falhas detectadas [Fato]; o foco foi condição, não energia, e a unidade (Gent) não foi confirmada [Verificar] | [ISPT](https://ispt.eu/news/using-sam4-to-help-drive-sustainable-industry/), [IoT One](https://v2.iotone.com/case-study/arcelormittal-condition-monitoring/c1272) |
| Vanderbijlpark (ArcelorMittal SA) | VSD em bombas de 1.225 kW que ficavam em bypass 50% do tempo | −53% de eletricidade, shared savings (do `dados/`) | `dados/RANKING-DADOS-POR-IMPORTANCIA.md` |

## Contexto ArcelorMittal Pecém
Cada 1% de eletricidade poupada ≈ 12–14 GWh/ano ≈ R$ 2–3 mi/ano [Estimativa derivada em `dados/`]. kWh poupado vira excedente vendável (tese do próprio CEO do Pecém).

## Ganho
R$ 5–16 mi/ano no Pecém é estimativa do agente da v2, com premissas a validar. Ganho dos casos citados é autodeclarado por fornecedores.

## MVP em 5 dias
Bancada com 2–3 motores/cargas (ventilador com damper, bomba), sensores de corrente, ESP32, dashboard com ranking em R$ e "antes/depois" de um VSD ou redução de carga.

## Perguntas ao Ideathon
Quantos motores >75 kW sem VSD? Há bypass/estrangulamento com válvula? Existe medição por motor no SCADA? Preço do MWh excedente?
