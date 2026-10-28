# Pitch — VazioZero (máx. 5 min)

Tempo total planejado: **4 min 50 s**, com 10 s de folga. Detalhes e fontes em `solucao.md`.
Regra de ouro: todo número de estimativa aparece no slide com o rótulo **"estimativa"**.

---

## Slide 1 — Problema: máquinas que giram sem produzir (40 s)

**Na indústria, cerca de 68% da eletricidade vai para motores** (Procel).

O maior desperdício não é o motor ruim. É o motor bom **ligado sem necessidade**: compressor em alívio, exaustor ligado com a linha parada, duas bombas onde uma basta, ar comprimido vazando.

Um compressor em alívio ainda gasta **~25% da potência**. Vazamentos levam **20–30%** do ar (DOE).

Ninguém vê esse desperdício, porque a medição é por subestação, não por máquina e por estado.

**Fala sugerida:** "Imaginem um compressor de 110 kW girando a noite inteira só para alimentar vazamentos. Ele não aparece em nenhum relatório. A própria ArcelorMittal nos EUA premiou funcionários que acharam exatamente isso: duas bombas do lingotamento ligadas 24 horas quando uma bastava."

---

## Slide 2 — Solução: VazioZero (35 s)

**Um sensor de alicate por máquina + regras + IA, que achou → avisou → alguém agiu → provou.**

1. Mede potência ativa, reativa e fator de potência de cada motor, sem cortar cabo.
2. Classifica o estado: desligado, **em vazio/alívio**, em carga.
3. Cruza com o processo (linha parada? turno?) e acusa **operação improdutiva**.
4. Faz sozinho o **teste de vazamento** do ar comprimido em toda parada.
5. Manda a ação certa para a pessoa certa e **mede o antes/depois**.

**Fala sugerida:** "O VazioZero não é mais um painel de consumo. Ele responde três perguntas: qual máquina está girando sem produzir, quanto isso custa por hora e quanto economizamos depois que alguém agiu."

---

## Slide 3 — Demo (60 s)

**Bancada ao vivo (ou vídeo de backup):** ESP32 + medidor PZEM + um compressor com tanque.

- **Tela 1, Mapa do Desperdício:** "R$ perdidos hoje", com ranking por máquina.
- **Simulamos a linha parada:** o compressor entra em alívio. Em segundos chega o alerta no celular: *"C-02 em alívio há 10 min, linha parada. Custo R$ 6,90/h. Desligar?"*
- **Abrimos uma válvula (vazamento):** o ciclo do compressor muda e o sistema calcula **vazamento % = 100·T/(T+t)**, a fórmula do DOE.
- **Toque em "Feito":** o relé desliga a carga e a tela de Verificação mostra a curva de economia subindo.

**Fala sugerida:** "Aqui o compressor está em alívio. Vejam o fator de potência cair: é assim que sabemos que ele gira sem produzir. Agora abro um vazamento… e o sistema já calculou: 25%. Isso vira uma ordem de serviço."

---

## Slide 4 — Como medimos o ganho (45 s)

**Método: IPMVP Opção B.** Economia = consumo da linha de base ajustado à produção − consumo medido depois.

**Exemplo numérico (estimativa com premissas, não são dados da ArcelorMittal):**
- 1 compressor de 110 kW: 4 h/dia em alívio evitadas → **40 MWh/ano**
- Vazamento medido de 25% → 12% após reparo → **64 MWh/ano**
- 4 auxiliares de 22 kW, 2 h/dia ligados sem processo → **51 MWh/ano**
- **Total ≈ 156 MWh/ano**

Valor: **≈ R$ 39 mil/ano** se o kWh valer R$ 250/MWh (premissa para o excedente vendido pelo Pecém). Para uma PME na tarifa A4 Verde da Enel CE (R$ 369/MWh sem tributos), **≈ R$ 58 mil/ano**. Emissões evitadas: **6 a 8,5 tCO2e/ano**, pelo fator do SIN.

**Fala sugerida:** "No Pecém a energia é autogerada e o excedente é vendido. Então cada kWh que economizamos é um kWh a mais para vender. E não prometemos: medimos quatro semanas antes e oito depois, no padrão internacional IPMVP, o mesmo princípio de baseline que a ArcelorMittal já usa."

---

## Slide 5 — Clientes e receita (35 s)

**Clientes**
1. ArcelorMittal Pecém: piloto em utilidades.
2. Indústrias do Complexo do Pecém: ~30 com presença física, ~90 na região.
3. PMEs industriais do Ceará com compressor e motores.

**Como ganhamos dinheiro**
- Kit instalado: **R$ 2.500/ponto**
- Assinatura: **R$ 150/ponto/mês** (alertas, relatórios, M&V)
- Ou **shared savings**: o cliente não investe nada e paga **35% da economia verificada** por 3 anos.

**Ponto de equilíbrio:** ≈ **86 pontos ativos** (estimativa).

**Fala sugerida:** "Quem não quer investir paga só sobre o que a gente provar que economizou. O risco fica com a gente, e é por isso que medimos com rigor."

---

## Slide 6 — Viabilidade e custo (30 s)

- **Protótipo:** ≈ **R$ 300** em peças (ESP32, PZEM, relé, OLED). Software 100% gratuito: Mosquitto, Node-RED, InfluxDB, Grafana, Python.
- **Piloto de 6 pontos:** ≈ **R$ 21 mil** (medidor industrial Modbus, instalação, reparo de vazamentos) + R$ 10,8 mil/ano de assinatura.
- **Payback estimado ≈ 9 meses** no cenário central. Mesmo com metade do desperdício, ≈ 2,4 anos.
- **Segurança:** instalação só por eletricista autorizado (NR-10); rede separada da automação, sem nenhum comando remoto em máquina de processo.

**Fala sugerida:** "O sistema só lê e só recomenda. Desligar automaticamente só acontece via CLP do cliente, com aprovação da engenharia, como a ArcelorMittal fez com as bombas do lingotamento."

---

## Slide 7 — Por que nós e por que diferente (25 s)

- **Vencedores de 2025 monitoravam energia em geral.** Nós caçamos **um desperdício nomeado** e **provamos o ganho**.
- Diferente de soluções de saúde de ativos (como a Tractian), cobramos **pela economia verificada**.
- **Time:** [Nome], negócios; [Nome], design; [Nome], hardware; [Nome], dados. Estudantes do IFCE [campus].
- Arquitetura inspirada no projeto aberto VoltIA (sem licença declarada, por isso código 100% nosso).

**Fala sugerida:** "Monitorar energia todo mundo monitora. Nós transformamos o fator de potência de cada motor em uma pergunta simples: ele está produzindo ou só girando?"

---

## Slide 8 — Pedido (20 s)

**Queremos 90 dias e 5 máquinas** nas utilidades da ArcelorMittal Pecém:
- 4 semanas de linha de base
- 8 semanas de ações
- **Relatório IPMVP assinado pelo seu gestor de energia**

Se não acharmos desperdício que pague o piloto, o relatório mostra isso também.

**Fala sugerida:** "Nos deem cinco máquinas e noventa dias. Ao final, vocês vão ter um número medido, não uma promessa, de quanta energia a mais o Pecém pode vender."

---

### Conferência de tempo
| Slide | Tempo |
|---|---|
| 1 Problema | 40 s |
| 2 Solução | 35 s |
| 3 Demo | 60 s |
| 4 Ganho (M&V + exemplo) | 45 s |
| 5 Clientes e receita | 35 s |
| 6 Viabilidade e custo | 30 s |
| 7 Diferencial e time | 25 s |
| 8 Pedido | 20 s |
| **Total** | **290 s = 4 min 50 s** |

### Mapa para os critérios da banca
- **(a) Problemática:** slide 1
- **(b) Proposta de valor:** slides 2 e 3
- **(c) Segmento de clientes:** slide 5
- **(d) Monetização:** slide 5
- **(e) Viabilidade:** slides 4, 6 e 8

### Perguntas prováveis da banca (respostas curtas)
- **"A ArcelorMittal já mede isso no supervisório?"** Pode medir os grandes. Nosso alvo é a cauda de motores sem medição individual. Se já houver medidor, lemos via Modbus e o custo cai. (Premissa a validar.)
- **"E a IA?"** Regras decidem os alertas, porque precisam ser confiáveis. A IA aprende os níveis de cada máquina, monta a linha de base e detecta deriva. NILM só em PME/escola, onde faz sentido.
- **"Esses números são reais?"** São estimativas com premissas explícitas e análise de 50% a 150%. O pedido do slide 8 existe justamente para medi-los.
