# Hackathon ArcelorMittal — Trilha da Inovação (Sebrae/CE + ArcelorMittal Pecém)

## Contexto
- Edital: `docs/edital-trilha-da-inovacao.pdf`. Alunos IFCE (Caucaia, Fortaleza, Paracuru, Pecém), times de 3 a 5 (ideal: negócios + design + dev).
- Desafio escolhido: **8. Eficiência Energética e Fontes Renováveis** (`docs/desafio-08-eficiencia-energetica.jpeg`).
  - Problema: energia pesa nos custos industriais/domésticos e o desperdício não é percebido.
  - Desafio: ferramenta/dispositivo que identifique desperdícios e proponha otimização (indústria, escolas, pequenos negócios, residências).
  - Possibilidades: medidores inteligentes, IoT, apps de gestão, IA, automação de iluminação/climatização, solar, gamificação.
  - Impacto esperado: menos consumo, menos custo, mais consciência.

## Fluxo e datas
- Ideathon (2 dias, por campus): Caucaia 20–23/10 (noite) · Pecém 26–27/10 (manhã/tarde) · Fortaleza 26, 27, 29, 30/10 (noite) · Paracuru 01 e 06/10.
- Hackathon online (5 melhores times por campus): 09–12/11, à noite. Premiação a definir; pagamento até 12/12.
- Prêmios: 1º R$5.000 · 2º R$4.000 · 3º R$3.000 (dividido igualmente; conta em nome próprio).
- Pitch ~5 min. Critérios: problemática, proposta de valor, segmento de clientes, monetização, viabilidade (pontuação divulgada no 1º dia).
- Workshops do hackathon: ideação, validação, modelagem (BMC), prototipação (Figma etc.).

## Pesquisa
- `reports/2026-10-27-hackathons-eficiencia-energetica.md`: 8 soluções de hackathons. A edição 2025 desta mesma Trilha foi vencida por WeVoltz (1º) e Enerlize (2º), ambas monitoramento de energia com sensores + IA. Quase nenhuma fonte traz métrica de economia.

## Soluções propostas (`solutions/`, cada uma com solucao.md + pitch.md de ≤5 min)
- 01-voltia-industrial (VazioZero): medidor de alicate + ESP32 por máquina, detecta equipamento ligado sem produzir; ganho exemplo ≈ R$ 39 mil/ano (estimativa).
- 02-gestao-demanda (HoraCerta): previsão + deslocamento de carga por PLD/tarifa; ganho PME ≈ R$ 77 mil/ano, ArcelorMittal R$ 0,45–2,25 mi/ano (estimativas).
- 03-vazamentos-ar-comprimido (Sibilo): sonda ultrassônica ESP32 + app de rota; cenário base ≈ R$ 84 mil/ano numa área-piloto (estimativa).
- Todos com números ilustrativos e premissas a validar com a ArcelorMittal no Ideathon. Conteúdo e fontes ainda NÃO revisados pelo Luan.

## Dados públicos (`dados/`)
- Começar por `dados/00-indice.md` e `dados/RANKING-DADOS-POR-IMPORTANCIA.md` (Top 10 para o pitch, lacunas, 13 correções às soluções).
- Lacunas críticas (perguntar no Ideathon): consumo interno e excedente atuais do Pecém, preço do excedente, compressores/motores/medição por equipamento, ISO 50001. Ver `dados/lacunas-perguntas-para-ideathon.md`.
- Números ainda NÃO revisados pelo Luan; as soluções em `solutions/` ainda usam premissas que o ranking corrige.

## Pendências
- Definir em qual campus/Ideathon o Luan está (hoje, 27/10, é o 2º dia do Pecém).
- Escolher qual das 3 soluções seguir (ou combinar) depois de ouvir o desafio real da ArcelorMittal.
- Formar time (negócios/design/dev) e detalhar a ideia para o desafio 8.

## Próximo passo
- Luan dizer o campus e como quer abordar o desafio (indústria vs. escola/pequeno negócio vs. residência).
