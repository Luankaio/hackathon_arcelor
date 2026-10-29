# Solução principal: monitoramento elétrico por máquina, com mapa da planta e chamados para o responsável

> 29/10/2026. Base: ideia do Luan (sensores elétricos por máquina + app com cadastro, métricas em tempo real, times/cargos, alertas que viram chamado, mapa editável e rota até a máquina).
> Nome provisório: **MapaVolt** (10 sugestões em §0; trocar quando o time escolher).
> Decisões do Luan em 29/10: app para celular e PC, **foco em mobile**; aviso **só dentro do próprio app**; ponto de partida da rota = **ponto de referência criado no mapa desenhado**; alerta vai para o **time** (todos os membros) ou, se a máquina só tem cargo, para **todos daquele cargo**. Pitch e linguagem/stack ficam para depois.

## 0. Sugestões de nome
| # | Nome | Ideia por trás |
|---|---|---|
| 1 | **MapaVolt** | Mapa da planta + energia; diz exatamente o que o app faz |
| 2 | **Kilowatch** | kW + *watch* (vigiar): "de olho em cada kilowatt" |
| 3 | **Ronda** | A ronda do técnico, só que digital e contínua |
| 4 | **VigiaWatt** | Vigia que nunca dorme, olhando os watts |
| 5 | **Pulso** | O "pulso" de cada máquina, medido ao vivo |
| 6 | **Sentinela** | Guarda que dá o alarme na hora certa |
| 7 | **Amperia** | De ampère; nome curto, soa como marca |
| 8 | **Faísca** | Brasileiro, fácil de lembrar, ligado a eletricidade |
| 9 | **NoPátio** | Leva a pessoa certa até a máquina no pátio |
| 10 | **Plantão Volt** | O plantão da manutenção recebendo o chamado da máquina |

Favoritos (opinião do Claude): **Kilowatch** (trocadilho forte, une energia e vigilância) e **Ronda** (curto, em português, fala do ciclo alerta → técnico vai até a máquina). Antes de fechar, checar se o nome está livre (INPI, domínio, loja de apps): não verificado.
> Marcação: **[Fato]** visto em fonte · **[Estimativa]** nossa · **[Decidir]** ponto em aberto (ver §12).
> Equipamentos e preços: `equipamentos.md` nesta pasta. Dados da ArcelorMittal: `../dados/`.

---

## 1. Resumo em uma frase
Um sensor elétrico em cada máquina mede tensão, corrente, potência, fator de potência e energia. O app mostra cada máquina ao vivo, numa lista e num mapa da planta. Quando uma máquina consome mais que o normal, para ou se comporta de forma estranha, o app **avisa o time ou o cargo responsável**, alguém **pega o chamado** e o app **traça o caminho até a máquina**.

## 2. Problema
- O desperdício de energia não é percebido: uma máquina que passa a puxar 20% a mais (atrito, rolamento, válvula em bypass, ligada sem produzir) continua "funcionando" e ninguém vê. [Fato: enunciado do desafio 8, `../docs/desafio-08-eficiencia-energetica.jpeg`]
- No Pecém, o kWh economizado vira **excedente de energia vendido**. Cada 1% de eficiência elétrica vale ≈ 12–14 GWh/ano ≈ R$ 2–3 mi/ano, e 1 MW contínuo vale ≈ R$ 1,6–2,2 mi/ano. [Estimativa derivada de dados públicos, ver `../dados/RANKING-DADOS-POR-IMPORTANCIA.md`, itens 3 e 5]
- Quando um problema aparece, há duas perdas além da energia: **quem deveria agir não fica sabendo**, e **encontrar a máquina** numa planta grande (pátio, correias, casas de bomba) leva tempo.
- O critério de compra que a própria ArcelorMittal já usou: app fácil para o operador, que meça o impacto das ações e tenha ROI em menos de 2 anos. [Fato: caso Belval, `../dados/RANKING-DADOS-POR-IMPORTANCIA.md`, item 9]

## 3. Como funciona (fluxo)

```
 Máquina ──► Sensor elétrico ──► Gateway ──► Broker MQTT ──► Backend ──► Banco de séries temporais
 (motor,     (V, I, P, FP, kWh,   (Wi-Fi,     (fila de        (regras de        │
 bomba,      frequência)          cabo RS485  leituras)       anomalia,         ▼
 compressor)                      ou 4G)                      chamados)  ──► App (lista, gráficos,
                                                                             mapa, chamados, rota)
                                                                                   │
                                                                                   ▼
                                                                      Notificação dentro do app
                                                                      para o time ou cargo responsável
```

1. O sensor lê as grandezas elétricas a cada 1–5 s e envia uma média a cada 5–15 s. [Decidir: frequência; ver §7]
2. O backend guarda a leitura, atualiza o estado da máquina (normal, atenção, sobreuso, parada, sem sinal) e roda as regras de anomalia (§6).
3. Se uma regra dispara, o sistema cria um **alerta**, que vira **chamado** e aparece **no próprio app** para os responsáveis da máquina: todos os membros do time responsável ou, se a máquina só tem cargo, todas as pessoas daquele cargo.
4. A primeira pessoa que tocar em **"Pegar chamado"** assume, o resto do time vê que já tem dono, e o app oferece **"Ir até a máquina"** com a rota no mapa.

## 4. Hardware (resumo; detalhes e preços em `equipamentos.md`)
Três níveis, conforme a máquina:

| Caso | O que usar | Custo por ponto [Estimativa, preços de 29/10/2026] |
|---|---|---|
| Protótipo e demo do hackathon | ESP32 + PZEM-004T (mede V, I, P, FP, kWh, Hz) | R$ 150–500 |
| Máquina de baixa tensão (220/380 V) no piloto | Medidor trifásico com Modbus RS485 (genérico 100 A, Kron, Siemens PAC, Schneider) + gateway | R$ 900–2.500 |
| Motor grande ou média tensão (6,6/13,8 kV) | Medidor com entrada de 5 A ligado nos **TCs e TPs que já existem** no painel (ex.: Kron Mult-K 05) | R$ 1.600–2.500 + instalação |
| Máquina que **já tem** medidor ou relé de proteção com rede | Só software: ler via Modbus TCP / OPC UA pelo gateway | ≈ R$ 0 em hardware |

Instalação sempre por eletricista habilitado (NR-10), com sensor de alicate (não invasivo) sempre que possível.

## 5. O app: módulos e telas
**Foco em mobile:** as telas são desenhadas primeiro para o celular (lista, chamados, mapa e rota com uma mão, botões grandes) e se adaptam ao PC. O **editor do mapa** também funciona no celular, mas desenhar a planta inteira é mais confortável no PC.

### 5.1 Cadastro de máquina
**Como começa** (ideia do protótipo do Luan, ver `prototipo-claude-design.md`): a aba **Dispositivos** lista os sensores que o gateway detectou na rede e que ainda não têm máquina (ID, gateway, setor, leitura ao vivo, sinal). O usuário toca em **"Cadastrar máquina"**, preenche os dados com os **limites já sugeridos a partir da leitura atual** do sensor e, na 2ª etapa, posiciona a máquina no mapa. A máquina passa a ser monitorada na hora.

Cada máquina tem uma ficha com:

| Grupo | Campos |
|---|---|
| Identificação | Nome, TAG da planta, tipo (motor, bomba, compressor, ventilador, correia, forno…), fabricante/modelo, foto, setor/área |
| Dados nominais (placa) | Tensão nominal (V), corrente nominal (A), potência nominal (kW), fator de potência nominal, nº de fases |
| Comportamento esperado | **Potência média esperada** (kW), faixa normal (mín.–máx.), potência de "parada/standby", horário/turnos em que deve estar ligada, tempo normal de partida |
| Limites de alerta | % acima do esperado que conta como sobreuso (padrão 15%), tempo mínimo para disparar (padrão 5 min), limites de tensão, desbalanço e FP (padrões em §6) |
| Responsáveis | **Time responsável** ou **cargo responsável** (regra de quem recebe em §5.5); **gestor responsável** (recebe quando não há ninguém no turno ou ninguém pega); tempo para escalar (padrão 15 min) |
| Ligação | Sensor/medidor vinculado (ID), canal/fase, data da instalação |
| Localização | Posição no mapa (preenchida ao arrastar no mapa), área/camada |
| Criticidade | Baixa, média ou alta (muda a urgência da notificação) |

Opção **"Aprender o normal"**: depois de 7–14 dias de leitura, o app sugere a potência média e a faixa normal com base no histórico, e o usuário aceita ou ajusta. [Decidir: se os dados nominais são obrigatórios no cadastro ou só aprendidos]

### 5.2 Lista de máquinas (tempo real)
- Um cartão por máquina: nome, área, **estado (cor)**, potência atual vs. esperada (ex.: `48,2 kW / 40 kW esperado (+21%)`), corrente, tensão, FP e hora da última leitura.
- Filtros: por área, time, estado, criticidade. Ordenação: as que têm problema primeiro.
- Atualização ao vivo (WebSocket), sem recarregar.

**Cores de estado** (as mesmas na lista e no mapa):

| Estado | Cor | Quando |
|---|---|---|
| Normal | Verde | Dentro da faixa esperada |
| Atenção | Amarelo | Começou a sair da faixa, mas ainda não pelo tempo mínimo; ou FP/tensão/desbalanço fora do limite |
| **Sobreuso** | **Vermelho** | Consumo acima do esperado pelo tempo mínimo (pedido do Luan) |
| **Parada** | **Cinza** | Potência abaixo do nível de parada (pedido do Luan) |
| Sem sinal | Cinza com contorno tracejado e ícone | Sensor sem enviar há mais de 2 min (separado de "parada", porque não sabemos o estado real) |

[Decidir: se "parada" fora do horário de operação deve ser cinza normal, e só gerar alerta quando a máquina para **dentro** do horário]

### 5.3 Detalhe da máquina e gráficos
- Um gráfico **por métrica, separado**, com o tempo no eixo horizontal: potência ativa (kW), corrente por fase (A), tensão por fase (V), fator de potência, energia acumulada (kWh por hora/dia) e frequência (Hz).
- Períodos: ao vivo (últimos 15 min), 1 h, 24 h, 7 dias, 30 dias e intervalo livre.
- No gráfico de potência, **faixa sombreada do esperado** e linha do limite de sobreuso, para ver a hora em que a máquina "saiu do normal".
- Marcadores dos alertas/chamados no próprio gráfico.
- Resumo: kWh hoje / no mês, custo estimado (R$/MWh configurável), horas ligada, horas em sobreuso e **energia gasta acima do esperado** (kWh e R$). Esse último número é o que mostra o desperdício.

### 5.4 Times e funcionários
- **Funcionário:** nome, cargo, time(s), matrícula, turno (turma A/B/C/D ou administrativo), disponível/indisponível (férias, folga, afastado). O contato é só pelo app.
- **Cargo:** ex.: Eletricista, Mecânico, Técnico de manutenção, Supervisor de turno, Engenheiro de energia.
- **Time:** ex.: Manutenção Elétrica Aciaria, Utilidades; membros e líder.
- Perfis de acesso: **Administrador** (cadastra tudo), **Gestor** (edita o time, as máquinas do time e o mapa; recebe escalonamentos), **Técnico** (vê e pega chamados), **Leitura** (só consulta). Telas de Governança e Analytics detalhadas em `app.md`.

### 5.5 Alertas e chamados
Ciclo de vida:

```
Anomalia detectada → Alerta ABERTO → notificação aos responsáveis
        → alguém toca "Pegar chamado" → EM ATENDIMENTO (dono definido)
        → "Ir até a máquina" (rota) → RESOLVIDO (causa + observação) → FECHADO
   └─ ninguém responsável no turno → vai direto para o GESTOR RESPONSÁVEL
   └─ ninguém pegou em N min → ESCALA para o gestor responsável
   └─ a anomalia sumiu sozinha antes de alguém pegar → fica registrada como "normalizou sozinha"
```

- **Quem recebe** (decidido):
  - A máquina tem **time responsável** → o chamado vai para o time e **cada pessoa do time** recebe.
  - A máquina tem **só um cargo responsável** → o chamado vai para **todas as pessoas com aquele cargo**.
  - **Só quem está no turno** recebe (o app usa o turno cadastrado do funcionário e o status disponível/indisponível).
  - **Ninguém responsável disponível** (ninguém do time/cargo no turno, ou máquina sem responsável) → o chamado vai para o **gestor responsável**.
  - [Decidir: se a máquina tiver time **e** cargo, avisar só quem tem aquele cargo dentro do time, ou o time todo? Proposta: só o cargo dentro do time.]
- **Onde chega:** só **dentro do app**: caixa de chamados com contador, banner/som com o app aberto e notificação do próprio app no celular (push do PWA/app) para quando ele estiver em segundo plano. Sem WhatsApp, SMS ou e-mail.
- **Pegar chamado:** só uma pessoa vira dona; os outros veem "Pego por Fulano às 14:07". Dá para devolver ou passar para outra pessoa.
- **Mensagem de exemplo:**
  `⚠ Sobreuso · Bomba 03 – Casa de bombas AF · 48,2 kW (esperado 40 kW, +21%) há 12 min · corrente fase B 92 A · [Pegar chamado] [Ver gráfico] [Ir até a máquina]`
- **Ao resolver:** o técnico escolhe a causa numa lista (ex.: rolamento, desalinhamento, válvula, ligada sem necessidade, ajuste de processo, falso alarme). Isso alimenta um histórico por máquina e, mais tarde, uma IA que sugere a causa provável.
- **Indicadores:** tempo até alguém pegar, tempo até resolver, kWh evitados após a correção (comparar antes/depois).
- **Anti-spam:** um alerta aberto por máquina e por tipo; ele é atualizado e não repetido; "silenciar por X h" com motivo (ex.: manutenção programada).

### 5.6 Mapa da planta (editor + visão ao vivo)
**Modo edição** (administrador/líder):
- Fundo opcional: imagem da planta baixa, foto aérea do pátio ou fundo em branco.
- Ferramentas de desenho: **linhas** (paredes, correias, cercas), **formas** (retângulo, polígono, círculo para áreas como "Casa de bombas", "Subestação 3"), **texto/rótulo**, cor e espessura.
- **Áreas por partes:** o mapa é dividido em áreas e sub-mapas (ex.: Visão geral → Aciaria → Casa de bombas). Clicar numa área abre o detalhe. Isso resolve a planta ser grande demais para uma tela só.
- **Máquinas:** arrastar da lista para o mapa para posicionar; arrastar de novo para mover; a posição é salva no cadastro.
- **Caminhos (para a rota):** desenhar os corredores e vias por onde as pessoas andam (linhas conectadas), marcar portas/acessos e **pontos de referência** (portaria, sala de controle, oficina, estacionamento).
- Escala: marcar dois pontos e dizer a distância real, para o app mostrar metros e tempo de caminhada.

**Modo visão (todos):**
- Cada máquina é um ícone com a **cor do estado** (verde, amarelo, vermelho, cinza), atualizado ao vivo. Máquina em sobreuso pisca.
- Áreas mostram um resumo ("2 em sobreuso, 1 parada") e herdam a pior cor das máquinas de dentro, para achar o problema de longe.
- Clicar na máquina abre um cartão com as métricas atuais e os botões "Ver detalhes" e "Ir até a máquina".

### 5.7 Rota até a máquina
- O técnico toca **"Ir até a máquina"** (no chamado ou no mapa).
- O **ponto de partida** é um **ponto de referência criado no mapa desenhado do pátio** (ex.: portaria, sala de controle, oficina). O administrador cria esses pontos no modo edição; o técnico escolhe de qual está saindo (o app lembra o último usado). Sem GPS nesta versão.
- O app calcula o **menor caminho sobre os corredores desenhados** (grafo de caminhos + algoritmo de Dijkstra/A*) e abre o mapa com a rota destacada, distância e tempo estimado. Se a rota passa por várias áreas, mostra o trecho de cada área.
- **Por que não GPS:** dentro de galpões e casas de bombas o GPS falha. A rota pelo mapa desenhado funciona sem sinal e é o que dá para entregar no hackathon. Evolução: QR Code em cada ponto de referência ("li o QR da porta 4 → estou aqui").

## 6. Detecção de sobreuso e anomalias (tempo real)
Regras simples e explicáveis primeiro; IA depois, por cima delas.

| # | Regra | Como calcula (padrão, ajustável por máquina) | Estado/alerta |
|---|---|---|---|
| R1 | **Sobreuso vs. esperado** | Potência média móvel de 1 min > esperado × (1 + 15%) por ≥ 5 min | Vermelho, alerta "Sobreuso" |
| R2 | **Sobreuso vs. nominal** | Corrente > 100% da nominal da placa por ≥ 2 min (ou > 120% por ≥ 10 s) | Vermelho, alerta "Acima da nominal" (risco de queimar) |
| R3 | **Fora do padrão aprendido** | Potência fora da faixa histórica daquela máquina para aquele horário/turno (ex.: acima do percentil 95 dos últimos 14 dias) por ≥ 10 min | Amarelo → vermelho se persistir |
| R4 | **Parada inesperada** | Potência < nível de parada **dentro** do horário de operação por ≥ 2 min | Cinza, alerta "Parada" |
| R5 | **Ligada sem necessidade** | Potência acima do standby **fora** do horário/turno de operação por ≥ 15 min | Amarelo, alerta "Ligada fora de horário" (desperdício puro) |
| R6 | **Tensão fora da faixa** | Fora de ≈ 0,92–1,05 da tensão nominal [faixa "adequada" do PRODIST, módulo 8, para 220/380 V; Verificar a tabela vigente] | Amarelo |
| R7 | **Desbalanço de corrente** | (maior fase − média) ÷ média > 10% por ≥ 5 min | Amarelo (sinal de defeito no motor ou na alimentação) |
| R8 | **Fator de potência baixo** | FP < 0,92 por ≥ 15 min [Fato: referência de FP mínimo da ANEEL] | Amarelo |
| R9 | **Partida anormal** | Corrente de partida acima do normal ou demorando mais que o tempo normal da máquina | Amarelo |
| R10 | **Sem sinal** | Nenhuma leitura há > 2 min | Cinza tracejado, alerta para o time de instrumentação |

Detalhes que evitam alarme falso:
- **Tempo mínimo + histerese:** só dispara depois de X minutos e só volta ao normal quando fica abaixo do limite − 5% por alguns minutos (não fica "piscando").
- **Partida ignorada:** os primeiros segundos após ligar não contam para R1/R2.
- **Severidade** = tamanho do desvio × criticidade da máquina → define se a notificação no app é silenciosa, com som ou com alerta insistente (repete até alguém pegar).

Evolução com IA [Estimativa de esforço: depois do hackathon]:
- Baseline que considera a produção (kWh por tonelada ou por hora de operação), para não confundir "mais carga" com "defeito".
- Classificador da causa provável, treinado com as causas que os técnicos marcam ao fechar os chamados (§5.5).

## 7. Arquitetura de software (sugestão; linguagem e stack ficam para depois)
| Camada | Sugestão | Por quê |
|---|---|---|
| Firmware do sensor (protótipo) | ESP32 com **ESPHome** ou Arduino + biblioteca do PZEM | ESPHome lê PZEM e medidores Modbus quase sem código |
| Transporte | **MQTT** (Mosquitto ou EMQX), tópico `planta/<area>/<maquina_id>/leitura`, payload JSON | Padrão de IoT, leve, funciona em rede ruim |
| Backend | A definir (ex.: Node.js ou Python) | API REST + WebSocket para o tempo real |
| Banco | PostgreSQL + **TimescaleDB** (leituras) no mesmo banco do cadastro | Um banco só; agregações por minuto/hora prontas |
| Regras de anomalia | Serviço no backend que roda a cada leitura (janela móvel) | Regras da §6 |
| App | Uma base só para celular e PC, **mobile first** (ex.: PWA ou framework multiplataforma; a definir) | Atende o foco em mobile sem duas versões |
| Gráficos | Recharts ou Apache ECharts | Séries temporais com zoom |
| Mapa | **Leaflet com CRS.Simple** (mapa sobre imagem/plano, sem GPS) + **Leaflet-Geoman** (desenhar linhas e formas, arrastar marcadores) | Editor de mapa pronto, gratuito |
| Rota | Grafo dos corredores desenhados + Dijkstra/A* (ex.: biblioteca `ngraph.path`) | Simples, roda no próprio navegador |
| Notificação | **Só no app:** caixa de chamados em tempo real (WebSocket) + push do próprio app no celular | Decisão do Luan: o aviso chega no app |

Modelo de dados (principais tabelas):
`maquina` (dados de §5.1, `time_id`, `cargo_id`, `x`, `y`, `area_id`) · `sensor` · `leitura` (hypertable: `maquina_id`, `ts`, `v_a/b/c`, `i_a/b/c`, `p_kw`, `fp`, `kwh`, `hz`) · `funcionario` · `cargo` · `time` · `time_membro` · `alerta` (`tipo`, `severidade`, `inicio`, `fim`) · `chamado` (`alerta_id`, `estado`, `dono_id`, `pego_em`, `resolvido_em`, `causa`) · `mapa_area` (geometria, `pai_id`) · `mapa_desenho` (linhas/formas) · `mapa_caminho` (arestas do grafo) · `ponto_referencia`.

## 8. O que entregar no hackathon (09–12/11, 4 noites)
| Item | Real ou simulado |
|---|---|
| 1 bancada real: ESP32 + PZEM-004T medindo um aparelho (ventilador, furadeira, secador ou motorzinho) | **Real.** Na demo, frear o ventilador ou ligar a potência máxima → o ícone fica vermelho no mapa e chega o chamado no celular de um jurado ou do time |
| 10–20 máquinas "virtuais" da planta (bombas, compressores, correias) | **Simulador** que publica leituras realistas no MQTT, com botões para forçar sobreuso, parada e sem sinal |
| Cadastro de máquina, times e cargos | Real |
| Lista ao vivo + gráficos por métrica | Real |
| Regras R1, R4, R5 e R10 | Real (as outras podem ficar para depois) |
| Chamado com "Pegar" + notificação no app | Real |
| Mapa editável + cores + arrastar máquinas | Real |
| Rota a partir de ponto de referência | Real, sobre corredores desenhados à mão no mapa de exemplo |
| IA de causa, baseline por tonelada | Só no slide, como evolução |

Divisão sugerida para 3–5 pessoas: (1) hardware + simulador + MQTT; (2) backend + regras + chamados; (3) app: lista, gráficos e cadastro; (4) mapa + rota; (5) negócio, pitch e números.

## 9. Valor e impacto (para o pitch; fora do foco por enquanto)
- **Energia:** o app mostra a "energia gasta acima do esperado" por máquina. Exemplo: um motor de 75 kW em sobreuso de 15% durante 8.000 h/ano gasta ≈ 90 MWh/ano a mais ≈ R$ 16–22 mil/ano (a R$ 178–250/MWh). [Estimativa; trocar pelo preço interno da ArcelorMittal]
- **Escala:** em 100 máquinas com ganho médio de 5% em ~5 MW monitorados → ≈ 2,2 GWh/ano ≈ R$ 0,4–0,55 mi/ano. [Estimativa, premissas a validar]
- **Manutenção:** sobreuso, desbalanço e partida anormal costumam aparecer antes da quebra → menos parada não planejada (é aqui que costuma estar o maior valor; números a validar com a empresa).
- **Tempo de resposta:** alerta direto para o cargo certo + "pegar chamado" + rota → menos tempo entre o problema e a pessoa chegar na máquina (medir no piloto).
- **CO₂:** usar o fator da própria empresa, 46,0 gCO₂/kWh. [Fato: `../dados/RANKING-DADOS-POR-IMPORTANCIA.md`, item 10]
- **Diferencial frente aos vencedores de 2025 (WeVoltz, Enerlize: sensores + IA):** o nosso fecha o ciclo **detectar → avisar a pessoa certa → levar a pessoa até a máquina → registrar a causa**, com o mapa da planta. [Fato sobre os vencedores: `../reports/2026-10-27-hackathons-eficiencia-energetica.md`]

## 10. Modelo de negócio (rascunho)
- **Hardware** a preço de custo + instalação (ou cliente usa os medidores que já tem).
- **Assinatura por máquina monitorada por mês** (SaaS). [Decidir: faixa de preço; ex.: R$ 30–80/máquina/mês para PME e contrato anual para grande indústria]
- Opção **shared savings** (parte da economia medida), como o caso da ArcelorMittal na África do Sul. [Fato: `../dados/RANKING-DADOS-POR-IMPORTANCIA.md`, item 7]
- Segmentos: grande indústria (ArcelorMittal e fornecedores do CIPP), depois PMEs, escolas e prédios (mesmo app, menos máquinas).

## 11. Riscos e limitações
- **Rede dentro da usina:** Wi-Fi ruim em área metálica → preferir cabo RS485 até um gateway por painel; LoRaWAN ou 4G como alternativa.
- **Segurança da rede industrial (OT):** o sistema só **lê**, nunca comanda a máquina; gateway numa rede separada; nada entra na rede de automação.
- **Máquinas de média tensão:** não se mede direto; usa-se o secundário dos TCs/TPs do painel (trabalho de eletricista qualificado).
- **Alarme falso** cansa o time → começar com limites folgados, tempo mínimo e "aprender o normal".
- **Mapa desatualizado:** quem move a máquina na planta precisa mover no app; o mapa mostra "última edição por X em DD/MM".
- **Dados da ArcelorMittal:** quantas máquinas, potências e se já existe medição por equipamento são lacunas (`../dados/lacunas-perguntas-para-ideathon.md`).

## 12. Decisões e perguntas em aberto
**Decidido (29/10):** celular e PC com foco em mobile · aviso só no app · rota parte de ponto de referência criado no mapa desenhado · alerta para todos do time, ou para todos do cargo quando a máquina só tem cargo · pitch e linguagem ficam para depois.

**Escopo fechado (29/10, 3ª rodada):** as features são as que estão neste documento, em `app.md` e em `prompt-claude-design.md`; nada novo por enquanto. A entrega agora é **só protótipo, com tudo mockado (dados simulados)**: regras de backend e casos muito específicos (ex.: gestor indisponível) ficam de fora. **Gestor responsável é por time**; o cadastro de máquina pode continuar mostrando o gestor (vem do time). Para o mock, valem as propostas como padrão: máquina com time e cargo avisa o cargo dentro do time; escala ao gestor em 15 min; parada fora do horário fica cinza sem alerta.

**Em aberto:**
1. **Nome:** escolher entre as 10 sugestões de §0 (ou outro).
