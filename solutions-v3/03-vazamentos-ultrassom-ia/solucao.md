# 03 — Sibilo 2: ultrassom + IA para vazamentos de ar comprimido, com prova do ganho

> v3 (28/10/2026). Evolui `solutions/03-vazamentos-ar-comprimido`. **[Fato]** = visto em fonte; **[Estimativa]** = nossa; **[Verificar]** = só trecho de busca ou claim de fornecedor.

## Problema
Vazamentos desperdiçam 20–30% da produção do compressor; programas falham porque etiquetam e não fecham o ciclo (conserto + verificação). Ar comprimido na ArcelorMittal Brasil ≈ 92 GWh/ano (derivado em `dados/`).

## Como funciona
- **Hardware:** sonda ultrassônica 40 kHz (ESP32 + transdutor, ~R$ 350 de materiais) ou módulo plugado em celular; opcional: sensores fixos de vazão/pressão no header.
- **IA:** classifica o som (vazamento vs. ruído de fundo), estima gravidade, prioriza por R$/ano.
- **Software:** app de rota e ordem de serviço, mapa de vazamentos, teste de carga/descarga do compressor para provar o ganho (método CAC/DOE + IPMVP).

## Validação
| Referência | Validação | Fonte |
|---|---|---|
| FLIR Si1-LD (câmera acústica, não é startup) | "Product of the Year 2026", Computer & Automation; matriz MEMS de microfones para priorizar reparos [Fato] | [FLIR](https://www.flir.com/news-center/corporate-news/flir-si1-ld-acoustic-imaging-camera-wins-product-of-the-year-2026-award-from-computer--automation/) |
| Conagra (com ultrassom Fluke) | Projeto de redução de vazamentos ficou em 2º lugar em prêmio de sustentabilidade da ProFood World [Fato] | [Healthcare Packaging](https://www.healthcarepackaging.com/home/article/21615310/conagra-brands-leak-project-is-2nd-place-in-sema-program-category) |
| Lumitos / WRS Energie (startup) | Sensores digitais + IA para vazamento; afirma ~30% de potencial médio [Verificar: claim da empresa, sem prêmio visto] | [chemeurope](https://www.chemeurope.com/en/news/1182748/htts:/www.lumitos.com/en/terms-and-conditions/) |
| NL Acoustics LF10 | Câmera com 124 microfones e IA, estima tamanho e custo do vazamento [Verificar: claim de fornecedor] | [Smart Manufacturing Week](https://www.smartmanufacturingweek.com/news/next-generation-air-leak-detector-lf10-uses-ai-deliver-actionable-data) |
| ArcelorMittal Bissen / siderúrgica em MG | −7% de eletricidade do ar comprimido; −57,2% nos compressores do alto-forno (do `dados/`) | `dados/RANKING-DADOS-POR-IMPORTANCIA.md` |

Observação honesta: não achei startup de vazamentos que tenha ganhado prêmio de startup/hackathon; a validação é de produto premiado, caso de planta e claims de fornecedor.

## Ganho
Cenário base da v1: ~R$ 84 mil/ano numa área-piloto (60 vazamentos), payback ~3 meses [Estimativa]. Escalar para toda a planta exige dado de rede de ar do Pecém.

## MVP em 5 dias
Sonda ESP32 + bancada com furos de tamanho conhecido, modelo de classificação de som, app PWA com rota e R$/ano, protocolo de verificação.

## Perguntas ao Ideathon
Quantos compressores e qual vazão? Há medição de ar por área? Quem faz a ronda hoje? Preço interno do kWh?
