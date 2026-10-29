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

## Solução principal (`solucao_main/`), definida pelo Luan em 29/10
- `solucao.md` (nome provisório **MapaVolt**): sensor elétrico por máquina (V, I, P, FP, kWh) → MQTT → app com cadastro de máquina (dados nominais, potência esperada, time/cargo responsável), lista e gráficos por métrica em tempo real, times/funcionários/cargos, alerta → chamado ("pegar chamado", escalonamento), mapa editável (linhas/formas, áreas por partes, arrastar máquinas, verde/amarelo/vermelho sobreuso/cinza parada) e rota até a máquina sobre corredores desenhados a partir de um ponto de referência. Regras R1–R10, arquitetura sugerida, MVP do hackathon e números de impacto (estimativas).
- `equipamentos.md`: medidores, gateways e sensores com preço de 29/10 (demo ≈ R$ 150–230 com ESP32 + PZEM-004T; piloto BT R$ 900–1.500 por máquina; motor grande com Kron Mult-K 05 nos TCs existentes). Preços de busca, não conferidos.
- `prototipo-claude-design.md`: o que o protótipo do Luan no Claude Design (Painel, Mapa, Dispositivos) já cobre e as 10 lacunas em relação ao `solucao.md`.
- `prompt-claude-design.md`: prompt pronto para evoluir o protótipo (unidade, chamados, preventivas, governança, analytics, cadastro em 4 etapas, mapa editável).
- `app.md`: documento completo do app (telas e fluxos), escrito por um agente.
- `pitches/pitch_tecnico.md` (≈ 4,8 min) e `pitches/pitch_prototipov1.md` (storytelling com a persona Chico, ≈ 4,5 min). Preços da assinatura são proposta.
- Soluções antigas (v1–v4) e o ranking delas estão na branch `archive`; `reports/2026-10-28-ranking-solucoes.md` ainda está na main.

## Dados públicos (`dados/`)
- Começar por `dados/00-indice.md` e `dados/RANKING-DADOS-POR-IMPORTANCIA.md` (Top 10 para o pitch, lacunas, 13 correções às soluções).
- Lacunas críticas (perguntar no Ideathon): consumo interno e excedente atuais do Pecém, preço do excedente, compressores/motores/medição por equipamento, ISO 50001. Ver `dados/lacunas-perguntas-para-ideathon.md`.
- Números ainda NÃO revisados pelo Luan; as soluções em `solutions/` ainda usam premissas que o ranking corrige.

## Decisões (29/10)
- Foco em mobile (também roda no PC); aviso só no app; rota a partir de ponto de referência criado no mapa; alerta para todos do time ou, sem time, para todos do cargo; só quem está no turno recebe; sem ninguém responsável disponível, vai para o gestor responsável. Pitch e stack ficam para depois. Escopo fechado: só protótipo mockado; gestor por time.

## Pendências
- Escolher o nome (10 sugestões em `solucao_main/solucao.md` §0).
- Colar `solucao_main/prompt-claude-design.md` no Claude Design (de preferência num New chat; standalone fecha em 14/12/2026).

## Próximo passo
- Escopo fechado (29/10): só protótipo com dados mockados, sem backend. Evoluir o protótipo no Claude Design com o prompt e revisar o resultado contra `solucao_main/app.md`.
