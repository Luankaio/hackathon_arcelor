# Pitch — SIBILO (máx. 5 min)

> Tempo total planejado: **4 min 40 s** (20 s de folga). Cada seção abaixo é um slide.
> Os números do Slide 5 são **estimativa ilustrativa**, e o slide precisa dizer isso. As fontes estão em `solucao.md`, seção 13.

---

## Slide 1 — O dinheiro que ninguém ouve (0:25)

**Um chiado de 3 milímetros.**

Na planta, com o barulho de tudo, ninguém ouve. Mas um único vazamento de ar comprimido de 1/8" (3 mm) a 7 bar consome cerca de 2,8 kW, dia e noite.

**≈ R$ 5,6 mil e 1,3 tCO₂e por ano. Um furo.**

*(Visual: foto de um engate pneumático com a onda sonora "invisível" desenhada.)*

**Fala sugerida:** "Isso aqui é um vazamento de 3 milímetros. Ninguém na usina ouve, mas ele custa cerca de 5 mil e 600 reais por ano, sozinho. E uma rede de ar comprimido tem dezenas deles."

---

## Slide 2 — O problema (0:25) · *critério: Problemática*

Vazamentos jogam fora **20–30 % do ar** que o compressor produz (DOE / Compressed Air Challenge). Uma planta bem mantida fica abaixo de 10 %.

Energia é **15–20 % do custo do aço** (worldsteel).

O problema não é achar o vazamento. **É fechar o ciclo**: muita planta etiqueta e nunca volta para consertar, e ninguém prova quanto ganhou.

No Pecém a usina gera a própria energia com gases do processo. **Cada kWh economizado é um kWh a mais para vender.**

**Fala sugerida:** "Até 30 % do ar comprimido vaza. Na ArcelorMittal Pecém isso pesa mais ainda, porque cada kWh poupado vira energia excedente para vender. O gargalo não é achar o vazamento, é garantir que ele seja consertado e provar o ganho."

---

## Slide 3 — A solução: Sibilo (0:30) · *critério: Proposta de valor*

**Achar → Consertar → Provar.**

1. **Sonda ultrassônica de 40 kHz** (ESP32, cerca de R$ 350): acha o vazamento à distância, do chão, sem tocar em nada elétrico.
2. **App de rota e OS**: cada vazamento vira foto + QR + **R$/ano + tCO₂e/ano** e entra numa fila priorizada para a manutenção.
3. **Prova do ganho**: teste de vazamento padronizado (DOE/CAC) + Medição e Verificação no protocolo **IPMVP**.

*(Visual: os 3 ícones em sequência; abaixo, "câmera acústica: US$ 22 mil · Sibilo: ~R$ 350 + método".)*

**Fala sugerida:** "O Sibilo faz três coisas: acha o vazamento com uma sonda de 350 reais, transforma cada um numa ordem de serviço com valor em reais e CO₂, e prova o ganho com um protocolo internacional de medição."

---

## Slide 4 — Demo (1:00)

**Ao vivo na câmera / vídeo de 60 s:**

1. Bancada com 3 furos calibrados (0,8 / 1,6 / 3,2 mm) sob pressão. A sonda varre e o app mostra a intensidade subindo.
2. "Registrar": foto + QR → **"Classe G · ≈ 0,44 m³/min · R$ 5,6 mil/ano · 1,3 tCO₂e"**.
3. Vai para a **fila da manutenção**, ordenada por R$/ano.
4. "Conserto" (fecha o furo) → re-medição → **vazamento fechado**.
5. **Painel do gerente**: R$ e tCO₂e evitados, taxa de fechamento, ranking por área.

**Fala sugerida:** "Olhem: a sonda acha o furo de 3 milímetros, o app calcula 5 mil e 600 reais por ano, a manutenção recebe a ordem já priorizada, e quando o furo é fechado a re-medição dá baixa e o painel do gerente atualiza na hora."

---

## Slide 5 — Como medimos o ganho (0:50) · *critério: Viabilidade (custo/benefício)*

**Três níveis de prova:**
- **Ponto:** re-medição ultrassônica após o reparo.
- **Área:** teste de vazamento DOE/CAC antes e depois → vazamento em % e m³/min (meta < 10 %).
- **Planta:** energia dos compressores × linha de base ajustada pela produção (IPMVP Opção B).

**Exemplo — ESTIMATIVA ILUSTRATIVA (área-piloto hipotética):**
60 vazamentos, 47 consertados · tabela oficial do DOE · 8.760 h/ano · R$ 233/MWh · fator do SIN 2024 = 0,0545 tCO₂/MWh

| Cenário | MWh/ano | R$/ano | tCO₂e/ano | Payback |
|---|---|---|---|---|
| Conservador | 181 | 24 mil | 10 | 9 meses |
| **Base** | **362** | **84 mil** | **20** | **3 meses** |

Os 10 maiores vazamentos dão ~70 % da economia.

**Fala sugerida:** "O som serve para achar e priorizar; quem prova é o teste padronizado de vazamento e a medição de energia pelo protocolo IPMVP. Num cenário ilustrativo, uma área com 60 vazamentos economiza 84 mil reais e 20 toneladas de CO₂ por ano, com payback de 3 meses. Mesmo no conservador, se paga em 9 meses."

---

## Slide 6 — Clientes e receita (0:35) · *critérios: Segmento de clientes + Monetização*

**Quem paga:** gerente de utilidades/energia. **Quem usa:** inspetor, manutenção e operação.

**Entrada:** ArcelorMittal Pecém → indústrias médias do CIPP e da RMF (kWh mais caro: +9,6 % na média tensão em 2026) → PMEs via Sebraetec.

**Receita:**
- Campanha por área: **R$ 15 mil** (diagnóstico + linha de base + relatório M&V)
- Assinatura por planta: **R$ 2.500/mês**
- Ou **20 % da economia verificada**, viável porque nós medimos
- PME: R$ 249/mês

Equilíbrio estimado: ~2 indústrias + ~20 PMEs + 1 campanha a cada 2 meses.

**Fala sugerida:** "Começamos com a ArcelorMittal, numa campanha de 15 mil reais que se paga em meses, e escalamos para as indústrias do Pecém, onde o kWh é ainda mais caro. Como a gente mede o ganho, podemos até cobrar só uma parte da economia comprovada."

---

## Slide 7 — Viabilidade e segurança (0:25) · *critério: Viabilidade (desenvolver e operar)*

**Desenvolver:** ESP32 + transdutor + amp-op; app PWA + Supabase gratuitos; bancada calibrada pela tabela do DOE. Protótipo funcionando em 4 noites.

**Operar:** encaixa na rota de inspeção que já existe. Reparo imediato quando simples, OS quando não.

**Segurança desde o projeto:** sem contato elétrico (NR-10), sem abrir proteções (NR-12), teste de pressão dentro do procedimento (NR-13), varredura do chão (NR-35). **Não usar em área classificada nem em gás de processo.**

**Demanda real:** o governo federal abriu chamada só para eficiência em ar comprimido (até 170 indústrias).

**Fala sugerida:** "É hardware de prateleira e software gratuito, e encaixa na rotina de inspeção da usina. Pensamos a segurança desde o início: a sonda não toca em nada elétrico e não entra em área classificada."

---

## Slide 8 — Por que somos diferentes (0:15)

**2025 premiou medidores de consumo. O Sibilo não é medidor.**

Medidor diz *quanto* se gasta. O Sibilo diz **onde está vazando, o que consertar e quanto valeu**, com prova.

**Fala sugerida:** "Ano passado venceram ideias que medem consumo. A nossa acha a perda física, manda consertar e prova o ganho em reais e CO₂."

---

## Slide 9 — Time e pedido (0:15)

**Time:** [Nome] negócios · [Nome] design · [Nome] hardware · [Nome] software (IFCE [campus]).

**Pedido:** **uma área-piloto na ArcelorMittal Pecém por 30 dias**, com acesso à casa de compressores e a uma parada programada para o teste de linha de base. Entregamos um relatório de M&V com o ganho medido.

**Fala sugerida:** "Nosso pedido é simples: uma área-piloto por 30 dias. Em troca, entregamos o ganho medido, em reais e em CO₂, num relatório que a ArcelorMittal pode auditar."

---

### Soma dos tempos

| Slide | Tempo |
|---|---|
| 1 Gancho | 0:25 |
| 2 Problema | 0:25 |
| 3 Solução | 0:30 |
| 4 Demo | 1:00 |
| 5 Medição do ganho | 0:50 |
| 6 Clientes e receita | 0:35 |
| 7 Viabilidade | 0:25 |
| 8 Diferencial | 0:15 |
| 9 Time e pedido | 0:15 |
| **Total** | **4:40** |

### Perguntas prováveis da banca (respostas curtas)

- **"Como vocês sabem o tamanho do vazamento pelo som?"** Não confiamos só no som. Ele **prioriza**; o teste de vazamento padronizado mede o total, e um fator de reconciliação ajusta as estimativas.
- **"E se a economia não aparecer no medidor?"** O controle do compressor precisa responder à demanda menor. Isso faz parte do processo (fase 6), e as estimativas já usam f_c = 0,7.
- **"Isso já não existe?"** Existem detectores e câmeras (de US$ 280 a US$ 32 mil). Falta o **programa contínuo**, com fila, fechamento e prova. O app aceita leitura de detectores que a planta já tem.
- **"Vocês sabem o tamanho da rede do Pecém?"** Não, e não inventamos. Esse é o primeiro dado que o piloto levanta. Trouxemos a lista de perguntas.
