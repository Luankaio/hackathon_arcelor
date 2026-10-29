# 02 — TonaZero Edge: gateway + IA de baseline que alerta quando o consumo foge do esperado

> v3 (28/10/2026). Evolui `solutions-v2/03` e `04`. **[Fato]** = visto em fonte; **[Estimativa]** = nossa; **[Verificar]** = incerto.

## Problema
Na siderurgia o consumo depende de produto, temperatura, tempo de aquecimento etc. Análise manual em planilha acha o desvio tarde (fim do mês). Sem baseline por condição de operação, ninguém sabe o que é "normal".

## Como funciona
- **Hardware:** gateway de borda (Raspberry/industrial) lendo OPC UA/Modbus de medidores e PLCs já existentes, mais medidores de energia/vazão de vapor onde faltar. Em hackathon: simulação + ESP32 com medidor.
- **IA:** modelo de consumo esperado (kWh/t, GJ/t) por tipo de produto/condição; alerta em tempo real quando o real desvia; sugestão de causa (ex.: porta de forno danificada).
- **Software:** painel para operador (impacto em R$ e kWh/t), ranking entre áreas, M&V automático.

## Validação (startups e prêmios)
| Referência | Validação | Fonte |
|---|---|---|
| Energiency (França) | Vencedora do Digital Industry Awards 2018 (Smart Energy, Atos/Siemens/CEA) [Fato]. Na ArcelorMittal Belval: mais de 3% da fatura de energia, cerca de €150 mil/ano numa versão do caso; 1.600+ fluxos de dados de um forno a 1 s por 1 ano [Fato]. ArcelorMittal assinou contrato de 3 anos visando ≥5%/ano [Fato] | [InnoEnergy](https://innoenergy.com/news-resources/smart-energy-energiency-wins-the-digital-industry-awards-2018), [ArcelorMittal Bélgica](https://belgium.arcelormittal.com/en/?p=4075) |
| METRON (França) | Plataforma SaaS de gestão de energia. Na Industeel (ArcelorMittal): cerca de €340 mil em 12 meses; 3.000+ pontos/s de 7 servidores OPC; baseline por tipo de tratamento térmico, dimensão e tempo; alerta achou porta de forno de reaquecimento danificada [Fato]. A página não cita IA nem sensores novos, é software | [METRON](https://www.metron.energy/?p=5295) |
| Edgecom Energy (Canadá) | Vencedora do ABB Startup Challenge 2024 com Energy Manager de IA generativa; 980+ MW de carga em 205+ instalações C&I [Fato, via resumo de busca] | [The Manufacturer](https://www.themanufacturer.com/articles/abb-startup-challenge-winners-drive-ai-powered-energy-innovation/) |

## Contexto ArcelorMittal Pecém
O Grupo já compra esse produto: critério da Belval foi app fácil para operador, mede impacto das ações, ROI < 2 anos. Intensidade energética do Grupo piorou (22,03→23,00 GJ/t, `dados/`).

## Ganho
Referência externa: 3%+ (Belval) e €340 mil/12 meses (Industeel). Para o Pecém, não há número confiável sem dados internos: [Estimativa] 0,5–1% de 1,2–1,36 TWh ≈ R$ 1–3 mi/ano, a validar.

## MVP em 5 dias
Dados públicos/simulados de forno e vapor, modelo de baseline (gradient boosting), painel com alerta de desvio e custo em R$, gateway demonstrando coleta Modbus/OPC. Não prometer dado real da planta.

## Risco
Maior dependência de dados internos de todas as 3. Sem acesso, é só demo. Concorrentes maduros (Energiency, METRON) já estão na ArcelorMittal.

## Perguntas ao Ideathon
Quais medidores/OPC existem por área? Há historian? Qual kWh/t atual por etapa? Quem é o dono do dado?
