# Prompt para o Claude Design (evolução do protótipo `Monitoramento.dc.html`)

> 29/10/2026. Colar no chat do projeto "Monitoramento de máquinas industriais" no Claude Design.
> Dica: o chat de lá já sugeriu abrir um **New chat** para economizar contexto (ele leva um resumo e os arquivos ficam). Vale abrir um novo antes de colar.
> Se ficar grande demais de uma vez, mande em 3 partes: (1) Navegação + Unidade + Painel + Detalhe + Mapa; (2) Chamados + Preventivas + Cadastro de máquina; (3) Governança + Analytics.
> **Reais:** nomes das unidades da ArcelorMittal Brasil e o tipo de cada uma, e as áreas do Pecém (`../dados/`). **Fictícios:** nomes de pessoas e de times, quantidades de máquinas por unidade, o status "Em implantação" e todos os números de economia/KPIs (contas consistentes com R$ 209/MWh e 46 gCO₂/kWh).
> Base do que está pedido: `solucao.md`, `prototipo-claude-design.md` e a pesquisa sobre a ArcelorMittal em `../dados/`.

---

## Texto para colar (tudo abaixo da linha)

---

Quero evoluir o protótipo `Monitoramento.dc.html` (app para celular de monitoramento elétrico de máquinas da ArcelorMittal). **Mantenha a identidade visual atual** (tema claro, Archivo + JetBrains Mono, laranja de destaque, cartões arredondados) e o que já funciona (painel ao vivo, detalhe, mapa com rota, dispositivos e cadastro a partir do sensor detectado). Continue com dados simulados ao vivo. Tudo em português do Brasil. Foco é **celular**; as telas devem continuar funcionando se abertas no PC, mas não precisa de layout de desktop agora.

### 1. Navegação nova (barra inferior com 5 itens)
**Painel · Mapa · Chamados · Analytics · Mais**
- "Mais" abre uma lista com: **Dispositivos** (a tela que já existe), **Governança**, **Meu turno/Perfil** e **Configurações**.
- Badge com número de chamados abertos em "Chamados" e de sensores novos em "Mais".

### 2. Escolher a unidade (topo de todas as telas)
A ArcelorMittal chama suas plantas de **unidades** (ou usinas). Hierarquia: **Unidade → Área → sub-área**.
- No topo, troque "Pecém · Turno B" por um chip **"ArcelorMittal Pecém · CE ▾"** + turno e hora ("Turno B · 11:50").
- Ao tocar, abre uma **bottom sheet** "Escolher unidade" com busca e cards de unidade: nome, estado, tipo, nº de máquinas monitoradas, alertas abertos e um ponto de status (verde/amarelo/vermelho). Unidades:
  - ArcelorMittal **Pecém** (CE) · usina integrada · 48 máquinas · 3 alertas (a principal, com dados completos)
  - ArcelorMittal **Tubarão** (ES) · usina integrada · 112 máquinas · 5 alertas
  - ArcelorMittal **Vega** (SC) · laminação a frio e galvanização · 36 máquinas · 0 alertas
  - **João Monlevade** (MG) · usina integrada · 40 máquinas · 1 alerta
  - **Juiz de Fora** (MG) e **Piracicaba** (SP) · aciaria elétrica (mini-mill) · "Em implantação" (cinza, sem dados)
- Trocar a unidade muda painel, mapa, chamados, analytics e governança. Só o Pecém precisa ter dados completos; as outras podem mostrar painel com números e o resto em "dados de exemplo".

### 3. Corrigir as áreas do Pecém
O Pecém é uma usina integrada que produz **placas**: ela **não tem laminação**. Troque os setores do mapa e dos dados por:
**Pátio de Matérias-Primas, Sinterização, Coqueria, Alto-Forno, Aciaria, Lingotamento Contínuo, Termelétrica/Utilidades, Subestação** (e, se couber, Pátio de Placas e a Correia até o Porto).
Ajuste as máquinas de exemplo para essas áreas (ex.: o "Forno de reaquecimento" da Laminação sai; entram "Exaustor principal SN-01" na Sinterização, "Correia transportadora PM-03" no Pátio de Matérias-Primas, "Bomba de alimentação da caldeira TE-02" na Termelétrica). Mostre a tensão nominal junto da medida para não parecer erro (ex.: "6,57 kV · nominal 6,6 kV").

### 4. Estados e cores (painel, lista e mapa)
- Verde **Normal**, amarelo **Atenção**, vermelho **Sobreuso/Crítico**, **cinza Parada** (potência abaixo do nível de parada) e **Sem sinal** (cinza com contorno tracejado e ícone de sinal cortado).
- No Painel, os contadores passam a ser: Críticos · Atenção · Parada · Sem sinal · Normais (pode ser uma linha rolável).
- No Painel, adicione um cartão pequeno **"Economia este mês: R$ 48,3 mil · 231 MWh"** que leva para Analytics.

### 5. Detalhe da máquina
- **Um gráfico por métrica**, em abas ou empilhados: Potência (kW), Corrente por fase (A, 3 linhas), Tensão (V), Fator de potência, Energia (kWh por hora) e Frequência (Hz).
- Seletor de período: **Ao vivo · 1 h · 24 h · 7 d · 30 d**.
- No gráfico de potência, **faixa sombreada do esperado** + linha tracejada do limite de sobreuso; marcadores onde houve alerta.
- Cartão **"Acima do esperado hoje: 412 kWh · R$ 86"** (energia gasta além do normal).
- Seções novas: **Chamados desta máquina** (últimos 3) e **Preventivas** (próxima e última).
- Ficha: trocar "Responsável: Rafael Lima" por **"Responsável: Time Manutenção Elétrica – Aciaria"** (ou "Cargo: Técnico de Manutenção Elétrica") + **Gestor: Ana Paula Ribeiro**.

### 6. Mapa: modo visão e modo edição
- **Visão** (todos): igual hoje, com as cores novas (inclusive cinza e sem sinal). Cada área mostra um resumo ("2 em sobreuso · 1 parada") e herda a pior cor.
- **Rota:** em vez de sempre sair da Portaria, um seletor **"Saindo de: Portaria Sul ▾"** com os **pontos de referência** da unidade (Portaria Sul, Sala de Controle da Aciaria, Oficina Central, Estacionamento). O app lembra o último usado.
- **Botão "Editar mapa"** (só para gestor/admin), com barra de ferramentas embaixo: **Linha** (paredes, correias, cercas), **Forma** (retângulo/polígono para áreas), **Texto**, **Ponto de referência** (ícone de bandeira), **Caminho** (corredores por onde as pessoas andam; a rota usa esses caminhos), **Mover máquina** (arrastar o pino) e **Desfazer/Salvar**. Mostre o mapa em modo edição com alças nas formas e uma máquina sendo arrastada.
- **Áreas por partes:** tocar numa área dá zoom e abre o sub-mapa dela (ex.: Aciaria → Convertedores, Despoeiramento, Sala elétrica).

### 7. Aba Chamados (nova)
Filtros no topo (segmented): **Abertos · Meus · Preventivas · Resolvidos**. Busca e filtro por área/time.

**Card de chamado:** ID, tipo (ícone: corretivo por alerta ou preventivo), título da anomalia, máquina + área, há quanto tempo, severidade (cor), status (**Aberto, Em atendimento, Escalado, Resolvido**), para quem foi ("Time Manutenção Elétrica – Aciaria · 3 no turno") e botão **"Pegar chamado"**. Quando alguém pega: "Pego por Carlos Menezes às 14:15".

**Chamados de exemplo:**
| ID | Anomalia | Máquina · área | Situação |
|---|---|---|---|
| CH-1042 | Sobreuso +17% há 12 min | Ventilador de despoeiramento AC-02 · Aciaria | Aberto · Time Manutenção Elétrica – Aciaria (3 no turno) |
| CH-1041 | Queda de tensão (399 V, mín. 418 V) | Ponte rolante 80 t LC-02 · Lingotamento Contínuo | Em atendimento · Carlos Menezes |
| CH-1039 | Ligada fora do horário há 2 h | Compressor de ar 3 UT-04 · Utilidades | **Escalado para o gestor** (ninguém do cargo no turno) |
| CH-1038 | Fator de potência 0,81 há 40 min | Bomba de recalque TE-05 · Termelétrica | Aberto · Cargo Técnico de Manutenção Elétrica |
| CH-1037 | Parada inesperada | Bomba de resfriamento AF-02 · Alto-Forno | Resolvido · causa: disjuntor desarmado · 18 min |
| CH-1035 | Desbalanço de corrente 14% | Exaustor principal SN-01 · Sinterização | Resolvido · causa: mau contato em borne · −6% de consumo depois |
| CH-1033 | Sem sinal há 25 min | Sensor PM-2B11 · Aciaria | Aberto · Time Instrumentação |

**Detalhe do chamado:** cabeçalho com status e severidade; mini gráfico do momento do alerta; **linha do tempo** (14:12 alerta disparado pela regra "sobreuso +15% por 5 min" → 14:12 notificados 3 técnicos do Turno B → 14:15 pego por Carlos Menezes → 14:16 rota iniciada da Portaria Sul (180 m, ~3 min) → 14:52 resolvido: "rolamento com folga, trocado" → depois: "−9% de consumo, 270 kWh/dia evitados"); botões **Ir até a máquina**, **Devolver**, **Transferir** e **Resolver**. Ao resolver: lista de causas (rolamento, desalinhamento, válvula/damper, ligada sem necessidade, ajuste de processo, falha elétrica, falso alarme) + observação + foto opcional.

**Regra de quem recebe** (mostre num "i" de ajuda no chamado): máquina com **time** → todos do time que estão **no turno**; máquina só com **cargo** → todos daquele cargo **no turno**; **ninguém disponível** ou ninguém pega em **15 min** → vai para o **gestor responsável** (selo "Escalado").

### 8. Revisão preventiva (dentro de Chamados, filtro "Preventivas")
- **Card de preventiva:** ID, máquina, tipo de gatilho, prazo e status (**Programada, Vencendo, Atrasada, Concluída**), responsável.
  - PV-210 · Compressor centrífugo UT-01 · **a cada 500 h de operação** (o sensor conta: 468/500 h) · vence em 2 dias · Vencendo
  - PV-208 · Bomba de alimentação da caldeira TE-02 · **termografia mensal** · Atrasada 1 dia
  - PV-205 · Correia transportadora PM-03 · **por condição**: "consumo +8% há 7 dias, inspeção sugerida" · Programada
  - PV-201 · Exaustor principal SN-01 · checklist trimestral · Concluída em 12/10
- **Execução:** checklist com marcação (medir corrente por fase, inspeção termográfica, reaperto de bornes, lubrificação, limpeza de filtros/ventilação), campo de medição, foto, "Concluir". A preventiva vira chamado do mesmo jeito (mesma regra de quem recebe).
- **Criar plano:** gatilho por **calendário** (a cada X dias), por **horas de operação** ou por **condição** (tendência de consumo/desbalanço), checklist e responsável.

### 9. Cadastro de máquina (modificar o fluxo atual a partir do sensor detectado)
Continua começando em Dispositivos → "Cadastrar máquina", mas passa a ter **4 etapas** com barra de progresso:
1. **Identificação:** unidade e área (pré-selecionadas pelo gateway), nome, **TAG** (ex.: AC-02), tipo (chips atuais), fabricante, modelo, **criticidade** (baixa/média/alta).
2. **Dados nominais e comportamento:** tensão, corrente, potência e FP nominais, nº de fases; **potência média esperada** e **faixa normal** (sugeridas a partir da leitura do sensor, editáveis); potência de parada; **horário/turnos de operação**; interruptor **"Aprender o normal nos próximos 14 dias"**; limites: sobreuso (% acima do esperado + tempo mínimo, ex.: 15% por 5 min), tensão mín./máx., desbalanço máx., FP mínimo.
3. **Responsáveis:** alternar **Time** ou **Cargo** (segmented), escolher na lista; o **gestor responsável** aparece preenchido a partir do time (o gestor é do time) e o tempo para escalar é 15 min. Opcional: **adicionar plano de preventiva**.
4. **Posição no mapa:** arrastar o pino no mapa da unidade, dentro da área escolhida.
No fim: "AC-07 cadastrada e monitorada", e a máquina aparece no painel e no mapa.

### 10. Governança (dentro de "Mais"; só gestor/admin)
Sub-abas: **Times · Funcionários · Cargos · Turnos**.
- **Times em cards** (grade de 1 coluna no celular): nome, ícone/cor, área(s), gestor (avatar + nome), nº de membros, **"3/8 no turno agora"**, máquinas sob responsabilidade e chamados abertos. Exemplos:
  - **Manutenção Elétrica – Aciaria** · gestora Ana Paula Ribeiro · 8 membros · 3 no turno · 14 máquinas · 2 chamados
  - **Manutenção Mecânica – Aciaria e Lingotamento** · gestor Marcos Teixeira · 10 · 4 no turno · 18 máquinas · 1 chamado
  - **Manutenção Mecânica – Pátio de Matérias-Primas e Sinterização** · gestor João Victor Alves · 9 · 3 · 16 · 0
  - **Instrumentação** · gestora Fernanda Lopes · 6 · 2 · 48 sensores · 1 chamado
  - **Utilidades e Termelétrica** · gestor Ricardo Sampaio · 7 · 2 · 12 máquinas · 2 chamados
  - **Inspeção Preditiva** · gestora Luiza Martins · 4 · 1 · todas · preventivas
  - **Engenharia de Energia** · gestor Paulo Henrique · 3 · administrativo · analytics
  - Card "+ Novo time".
- **Detalhe do time:** membros (nome, cargo, turma, status), máquinas do time, regra de escalonamento, editar.
- **Funcionários:** lista com busca e filtros (time, cargo, turno, status); avatar, nome, cargo, time, chip do turno (Turma A/B/C/D ou ADM) e status (**No turno**, Folga, Férias, Afastado). Botão "+ Funcionário" com formulário: nome, matrícula, cargo, time(s), turma/escala, perfil de acesso (**Administrador, Gestor, Técnico, Leitura**), unidades com acesso.
- **Cargos:** lista (Técnico de Manutenção Elétrica, Técnico de Instrumentação, Mecânico de Manutenção, Líder de Manutenção, Supervisor de Turno, Coordenador de Manutenção, Engenheiro de Energia) com nº de pessoas e quantas no turno.
- **Turnos:** escala de revezamento de 4 turmas (A, B, C, D) em turnos de 8 h + administrativo; mostrar "Agora: Turno B (06h–14h), Turma C" e quem está de turno.

### 11. Analytics (aba nova)
Filtros no topo: período (**Mês · Trimestre · Ano**, com setas para navegar: "Outubro 2026") e área. Todos os números são exemplo.
- **Cartão herói:** "Economia em outubro: **R$ 48,3 mil** · 231 MWh · +18% vs. setembro" com pequena explicação: "consumo esperado − consumo real depois das correções, × R$ 209/MWh (configurável)".
- **KPIs em grade:** Economia no ano (R$ 312 mil · 1,49 GWh) · Desperdício identificado vs. recuperado (310 MWh / 231 MWh = 75%) · CO₂ evitado (10,6 t, fator 46 gCO₂/kWh da própria empresa) · Chamados resolvidos (64 de 71) · Tempo até pegar (MTTA 4 min) · Tempo até resolver (MTTR 47 min) · Escalados (6%) · Preventivas em dia (92%) · Horas de parada inesperada (11 h).
- **Gráficos:** (1) economia mensal em barras dos últimos 12 meses com linha de meta; (2) consumo real × esperado (linhas) no mês; (3) **ranking das 10 máquinas que mais desperdiçam** (kWh e R$, toque abre a máquina); (4) desperdício por área (barras horizontais); (5) horas por estado (normal/sobreuso/parada, barras empilhadas); (6) causas mais comuns dos chamados; (7) **desempenho por time** (MTTA, MTTR, chamados no mês).
- Botão "Exportar relatório" (só visual).

### 12. Configurações e Meu turno
- **Configurações:** preço do MWh (R$ 209, com nota "faixa pública R$ 178–250; usar o preço interno"), limites padrão de alerta, tempo padrão de escalonamento, unidade padrão.
- **Meu turno/Perfil:** nome, cargo, time, turno atual, alternar "Disponível / Indisponível", meus chamados.

### O que entregar
- Atualize o `Monitoramento.dc.html` com todas as telas acima navegáveis.
- No painel de ajustes (tweaks), acrescente: unidade inicial, perfil do usuário (Técnico/Gestor, para mostrar ou esconder Governança e Editar mapa) e um botão "simular novo alerta" que cria um chamado novo e mostra a notificação dentro do app.
- No fim, liste o que ficou simulado e o que eu devo revisar.
