# Notes (mais recente no topo)

## 2026-10-29 (pitches)
- Criada solucao_main/pitches/: pitch_tecnico.md (10 páginas, ~680 palavras ≈ 4,8 min: medição, arquitetura, regras, chamados, mapa/rota, analytics, governança, custo, piloto) e pitch_prototipov1.md (storytelling com a persona fictícia Francisco "Chico" Holanda, técnico de manutenção elétrica da Aciaria, ronda toda quarta; ~630 palavras ≈ 4,5 min).
- Conta do storytelling: defeito na quinta → 144 h até a ronda; 5 máquinas (ventilador despoeiramento, exaustor sinterização, compressor, bomba AF, correia) = 196,2 MWh = R$ 41.006 a R$ 209/MWh; potências são estimativas. Planos propostos: piloto 90 dias sem licença, R$ 89/máquina/mês, ou 20% da economia (proposta do Claude, a validar).

## 2026-10-29 (escopo fechado)
- Luan fechou o escopo nas features atuais (solucao.md + app.md + prompt-claude-design.md). Entrega agora é só protótipo com tudo mockado; sem regras de backend nem casos específicos (ex.: gestor indisponível). Gestor responsável é por time; o cadastro pode mostrar o gestor. Só o nome segue em aberto.

## 2026-10-29 (app.md pronto)
- Agente entregou solucao_main/app.md (~870 linhas): visão geral, glossário, perfis/permissões, mapa de navegação, 16 telas, 8 fluxos, regras de detecção e notificação, modelo de dados, métricas de Analytics, hardware, evolução, decisões e 12 perguntas em aberto.
- Corrigidas em solucao.md as contradições que ele achou: contato WhatsApp/telefone no funcionário e "ligação/WhatsApp" na severidade (aviso é só no app); perfis padronizados em Administrador/Gestor/Técnico/Leitura.

## 2026-10-29 (prompt do Claude Design + doc do app)
- Criado solucao_main/prompt-claude-design.md: nova navegação (Painel, Mapa, Chamados, Analytics, Mais), seletor de unidade (a ArcelorMittal chama as plantas de "unidades"/usinas), correção das áreas do Pecém (usina integrada de placas, sem laminação), cores parada/sem sinal, detalhe com gráficos por métrica e período, mapa com modo edição e pontos de referência, aba Chamados com 7 exemplos, revisão preventiva (calendário, horas, condição), cadastro de máquina em 4 etapas, Governança (times em cards, funcionários, cargos, turnos A–D) e Analytics (economia mensal R$ 48,3 mil / 231 MWh de exemplo, MTTA/MTTR, ranking de desperdício).
- Agente (Sonnet, medium) disparado para escrever solucao_main/app.md (documento completo do app: telas e fluxos).

## 2026-10-29 (protótipo Claude Design)
- Li o protótipo do Luan pelo Chrome (Monitoramento.dc.html, projeto 22b249b9… no Claude Design): abas Painel, Mapa (grade fixa de 6 setores + rota da Portaria) e Dispositivos (sensor detectado → cadastro em 2 etapas com limites sugeridos). Nada alterado lá; mudei o startTab só para navegar e voltei para "painel", sem salvar.
- Comparação em solucao_main/prototipo-claude-design.md: faltam times/cargos/turno/gestor, chamados (pegar, escalar, causa), editor de mapa, cinza para parada/sem sinal, escolha do ponto de referência, dados nominais, gráficos por métrica/período, regras com tempo mínimo e energia acima do esperado. O fluxo de Dispositivos foi levado para solucao.md §5.1.
- Claude Design standalone fecha em 14/12/2026.

## 2026-10-29 (turno e gestor)
- Luan decidiu: só quem está no turno recebe o chamado; se não houver ninguém responsável disponível, o gestor responsável é chamado. solucao.md §5.1, §5.5 e §12 atualizados.
- Tentei achar o protótipo do Claude Design: não aparece na lista de artifacts do Luan nem entre os artifacts do tipo Design. Pedido o link.

## 2026-10-29 (decisões da solução principal)
- Luan decidiu: celular e PC com foco em mobile; aviso só dentro do app; rota parte de ponto de referência criado no mapa desenhado do pátio; alerta vai para todos do time responsável ou, se a máquina só tem cargo, para todos daquele cargo. Pitch e linguagem/stack ficam para depois.
- solucao.md atualizado com isso + 10 sugestões de nome (§0; favoritos do Claude: Kilowatch e Ronda; disponibilidade dos nomes não checada).

## 2026-10-29 (solucao_main)
- Soluções antigas (solutions/, v2, v3, v4) movidas para a branch `archive`; a main ficou só com dados/, docs/, reports/, STATUS e notes.
- Luan definiu a solução principal: sensores elétricos por máquina (V, I, P, FP…), app com cadastro de máquina (dados nominais, potência esperada, time/cargo responsável), lista e gráficos em tempo real, times e funcionários com cargo, alerta de anomalia que vira chamado ("pegar chamado"), mapa editável da planta (linhas/formas, arrastar máquinas, vermelho = sobreuso, cinza = parada) e rota até a máquina a partir de um ponto de referência.
- Criados solucao_main/solucao.md (nome provisório MapaVolt; regras R1–R10; arquitetura MQTT + TimescaleDB + PWA React + Leaflet/Geoman; MVP do hackathon; 9 perguntas em aberto) e solucao_main/equipamentos.md (preços de 29/10 via busca: PZEM-004T R$ 99–140, Kron Mult-K 05 R$ 1.550–2.140, Shelly Pro 3EM R$ 1.040–1.300, Schneider PM5110 ≈ R$ 4.900, gateways US$ 35–99, WEG Motor Scan R$ 714–1.430). Preços não conferidos na loja.

## 2026-10-28 (solutions-v4)
- Pesquisado o repo LudwinS/voltia: ESP32+MicroPython, MQTT/Adafruit IO, Telegram, RF só com dados simulados, SEM licença (não copiar código, 110 V). Criado solutions-v4/ (README + 3): 01 VoltIA reescrito (nó por aparelho + defeito + técnico), 02 stack ESPHome+Home Assistant (mais rápida), 03 NILM medidor único (mais incerta). Recomendação: base 02 + lógica de defeito/técnico da 01. Licença do app HA/emonPi não verificada.

## 2026-10-28 (solutions-v3)
- Criado solutions-v3/ com 3 soluções IA+hardware+software: 01 motores/sensor de corrente (Faraday Predictive, Forgis, Semiotic Labs), 02 baseline IA kWh/t com gateway (Energiency, METRON, Edgecom), 03 vazamentos ultrassom+IA (FLIR Si1-LD, Conagra, Lumitos). Validação de 03 é fraca em startups premiadas (só produto premiado/casos). Página da ABB deu timeout; Forgis só via resumo de busca.

## 2026-10-28 (ranking)
- Ranking das 9 soluções em reports/2026-10-28-ranking-solucoes.md (notas = julgamento do Claude). Topo: RotaCerta e Sibilo (empate, 17). Sugestão: núcleo RotaCerta+Sibilo, SGE como casca, HoraCerta de reserva. Aguardando decisão do Luan.

## 2026-10-28 (solutions-v2)
- 6 agentes (Sonnet 5.5, medium) geraram 6 ideias em solutions-v2/ (só solucao.md, sem pitch): TermoRadar (calor residual), RotaCerta (motores/VSD), TonaZero (IA de processo), SGE-Pecém (ISO 50001), SolMatch Pecém (renováveis/PPA), manutenção preditiva energética. Nenhuma tem hackathon vencedor idêntico; validação vem de startups/fornecedores. Ganhos são estimativas dos agentes. SolMatch se sobrepõe à HoraCerta (v1). Não revisadas pelo Luan.

## 2026-10-28 (dados)
- Agente Opus levantou dados públicos da ArcelorMittal (11 docs + CSV em dados/). Ranking por importância e 13 correções às soluções ainda não aplicadas.

## 2026-10-28
- 3 agentes (Opus) geraram 3 soluções completas em solutions/ (VazioZero, HoraCerta, Sibilo), cada uma com solucao.md e pitch.md. Estimativas de ganho são ilustrativas; falta revisar fontes e validar premissas.

## 2026-10-27 (pesquisa)
- Pesquisados hackathons de eficiência energética; relatório em reports/. Confirmado: 1º e 2º da Trilha 2025 (WeVoltz, Enerlize) foram energia.

## 2026-10-27
- Bancada criada. Edital lido e desafio 8 (Eficiência Energética e Fontes Renováveis) escolhido pelo Luan.
