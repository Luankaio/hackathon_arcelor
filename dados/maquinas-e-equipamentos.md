# Máquinas e equipamentos: o que é público (Pecém primeiro, depois Tubarão e referências)

> Pesquisa de 28/10/2026. **Resumo honesto:** quase nada sobre utilidades elétricas do Pecém (compressores, bombas, ventiladores, motores) é público. O que existe é sobre o "núcleo" (alto-forno, termelétrica, gases). Isso é uma **lacuna** e, ao mesmo tempo, uma **oportunidade de pergunta** no Ideathon.
> Fontes em `fontes.md`.

---

## 1. ArcelorMittal Pecém

| Área | Equipamento | Dado público | Fonte | Confiança |
|---|---|---|---|---|
| Pátio/logística | Correias transportadoras de alta capacidade (matérias-primas e placas); correia até o Porto do Pecém (~10 km) | Existência; distância | [S13], [S20] | Alta (sem kW) |
| Coqueria | Fornos de 7,63 m de altura ("a maior do país"); capacidade 1.130 kt/ano | Dimensão e capacidade | [S14] | Média (GEM) |
| Sinterização | 4.747 kt/ano; sensores/câmeras + IA para antecipar falhas (2025) | Capacidade; projeto digital | [S14], [S19] | Média/Alta |
| Alto-forno 1 | 3.800 m³, ~100 m, projeto POSCO, ~3,1–3,2 Mt gusa/ano, vida útil ~30 anos | Dimensão | [S02], [S14] | Alta |
| TRT (recuperação de pressão do gás de topo) | **16 MW** ("16 MW/h" no texto) | Potência | [S02] p.15 | Alta (dado da CSP, ~2020) |
| Gasômetro de BFG | Existe (volume não publicado) | — | [S10] | Alta |
| Planta de tratamento de gases (GTP), gasodutos | Existe | — | [S02] | Alta |
| Aciaria | 2 BOF de 300 t; dessulfuração do gusa; refino secundário | Tamanho (GEM) | [S13], [S14] | Média |
| Lingotamento contínuo | Placas até 300 mm; secador e 2 pré-aquecedores de distribuidor a gás (37 m³/h cada) | Espessura; consumo de gás dos aquecedores | [S13], [S11] | Alta |
| Termelétrica | 218 MW outorgados: **3 unidades de 18 + 100 + 100 MW**; caldeiras queimando BFG/COG/LDG; vapor de processo 90 t/h (65 t/h médios no início) | Potência e unidades | [S03], [S01] | Alta |
| Subestação/conexão | Elevadora + LT de 230 kV até a SE Pecém II (Rede Básica) | Tensão | [S03] | Alta |
| Proteção elétrica | Sistema "barra segura" (alívio automático rápido contra distúrbios de frequência); presença de **motores síncronos** de grande porte | Existência | [S12] | Alta |
| Torre de resfriamento, casa de bombas | Existem na termelétrica | Existência | [S03] | Alta |
| Oxigênio, nitrogênio, argônio | Fornecimento da White Martins (ZPE Ceará, mais de 2.000 t/dia de gases, 2020–21). O escopo ResponsibleSteel 2026 inclui "gas plant for O2, argon" | Fornecedor | [S47], [S13] | Média (situação atual a validar) |
| Escória | BSSF (Baosteel Slag Short Flow) | Tecnologia | [S02] | Alta |
| **Compressores de ar** | Nada público | — | — | **LACUNA** |
| **Bombas de água (resfriamento AF, aciaria, lingotamento)** | Nada público | — | — | **LACUNA** |
| **Exaustores/despoeiramento (sínter, aciaria, coqueria)** | Nada público | — | — | **LACUNA** |
| **Sopradores do alto-forno** | Nada público (elétrico ou a vapor?) | — | — | **LACUNA** |
| **Fabricantes (Siemens, ABB, Atlas Copco, Primetals, SMS, Danieli, Paul Wurth etc.)** | Só POSCO E&C (EPC) e Primetals (máquina de reparo de refratário citada pelo GEM) | — | [S55], [S14] | Baixa |

### Inferências úteis (rotuladas)
- **[DERIVADO, qualitativo]** Planta com motores síncronos grandes, termelétrica com casa de bombas e torre de resfriamento, sínter com exaustores, aciaria com despoeiramento: as cargas típicas que a EPE lista como maiores consumidores elétricos numa integrada (grandes ventiladores de exaustão, sopradores, bombeamento de água, despoeiramento, bombas de caldeira, compressores) [S25] p.87. **As soluções 01 e 03 miram exatamente essas cargas.**
- **[DERIVADO]** O consumo de gás de cada aquecedor de distribuidor (37 m³/h × 57,3 MJ/m³ ≈ 0,59 MW térmico) mostra que há **cargas térmicas pequenas e intermitentes** no lingotamento, com ganho de 20–40% só com controle [S11]. Também é um alvo para a lógica "ligado sem necessidade" da solução 01 (aquecedor ligado sem distribuidor).

## 2. ArcelorMittal Tubarão (referência mais detalhada do Grupo no Brasil) [S21] (2018)
| Equipamento | Dado |
|---|---|
| Geração total | 500 MW instalados |
| CTE 1 e 2 | 2 × 68 MW (72 MVA), caldeiras de 260–270 t/h (88 kgf/cm², 513 °C); turbina acoplada a **soprador de ar do alto-forno** |
| CTE 3 e 4 | 2 × 75 MW (80 MVA), caldeiras de 250–260 t/h (100 kgf/cm², 540 °C); uma com soprador de 17 MW |
| Termelétrica Sol (coqueria heat recovery) | 320 fornos, 8 HRSG, 2 × 98 MW (115 MVA), 1.226 GWh/ano, 1.553 kt coque/ano |
| TRT do AF1 | 25 MW instalados, 16 MW médios; BFG a 2,3 kgf/cm² e 590.000 Nm³/h |
| TRT AF2 e AF3 (projeto) | 5 MW e 6 MW (210.000 Nm³/h, 1,6 bar) |
| CDQ | 5 caldeiras × 25 t/h (23 kgf/cm²) |
| Recuperação de LDG | 40 MW |
| PCH no canal de água do mar | 1,4 MW médios |
| Gasômetros | COG 40.000 m³; LDG 80.000 m³; BFG 150.000 m³ |
| Vapor de processo | Perdas de distribuição de ~3 t/h; fábricas de oxigênio próprias consomem 5 t/h |
| Gestão | **Centro de Energia** (gerenciamento central de eletricidade, combustíveis, águas e vapor) |

Uso no pitch: mostrar que a ArcelorMittal já domina a recuperação de energia "grande" (TRT, CDQ, heat recovery, cogeração). O espaço que sobra é a **perda difusa** em utilidades e na operação.

## 3. Referências de equipamentos e casos transferíveis do Grupo
- **Vanderbijlpark (África do Sul):** 5 bombas de alta pressão de 1.225 kW no resfriamento do laminador a quente, em bypass 50% do tempo; VSD → −53% de eletricidade [S30].
- **Saldanha (África do Sul):** ar comprimido da ASU, bombas da estação de água, desligamento de equipamentos ociosos [S31].
- **Fos-sur-Mer (França):** VSDs de média e baixa tensão, torres de resfriamento, ar de combustão das caldeiras, **despoeiramento, ar comprimido** [S28].
- **Bissen (Luxemburgo):** rede de ar comprimido a 6 bar (estudo para 5 bar) [S29].

## 4. Perguntas de equipamento para o Ideathon
Ver `lacunas-perguntas-para-ideathon.md`, bloco B.
