# 01 — VoltIA reescrito: nó ESP32 por aparelho, IA de defeito e aviso ao técnico

## Ideia
Mesma arquitetura do VoltIA (ESP32 → MQTT → dashboard → Telegram), escrita do zero, com três acréscimos: medição real em 220/380 V, **baseline por equipamento com detecção de defeito** e **fluxo de ordem de serviço para o técnico**.

## Arquitetura
1. **Nó de campo:** ESP32 + PZEM-004T v3 (V, I, P, FP, energia) com TC de alicate; 1 nó por aparelho ou circuito. Alerta crítico (sobrecorrente, tensão) decidido **no próprio nó**, offline, como no VoltIA.
2. **Transporte:** MQTT (broker Mosquitto local ou HiveMQ/EMQX Cloud).
3. **Backend leve:** Python (FastAPI) + SQLite/TimescaleDB. Calcula baseline (média/desvio por equipamento e estado), pico, deriva e score de defeito.
4. **IA:**
   - *Estado do aparelho* (desligado/vazio/carga/sobrecarga): regras + Random Forest sobre P, FP, ΔP (a ideia do VoltIA).
   - *Defeito:* detecção de anomalia (EWMA/z-score ou Isolation Forest) sobre corrente, FP e duração de partida, comparada ao baseline dos últimos dias.
5. **App no celular:** PWA (instalável, funciona no navegador) com lista de equipamentos em verde/amarelo/vermelho, gráfico do pico, histórico e botões de assumir/resolver.
6. **Alertas:** bot do Telegram (e-mail/WhatsApp Business como opção), mensagem com equipamento, pico, suspeita e link; escalonamento se ninguém assumir.

## Referências e licença
- VoltIA (referência de arquitetura; sem licença, **não copiar código**): https://github.com/LudwinS/voltia
- PZEM-004T com ESP32/MQTT, guias: [esp32.co.uk](https://esp32.co.uk/esp32-pzem-004t-energy-monitor-esphome-mqtt/), [atomic14](https://www.atomic14.com/esp32/sensors/pzem-004t/). Um guia indica YAML desatualizado; usar a doc oficial.
- Detecção de anomalia em motor com TinyML (Edge Impulse): [Arduino blog](https://blog.arduino.cc/?p=34592), [Edge Impulse](https://docs.edgeimpulse.com/projects/expert-network/brushless-dc-motor-anomaly-detection). Resultados de artigos são indicativos; um estudo de falhas em motor DC citou 73% em dados não vistos [EPJ](https://www.epj-conferences.org/articles/epjconf/pdf/2025/28/epjconf_aimace2025_05014.pdf).
- Produto comercial equivalente em indústria: Verdigris (hardware + ML, alertas de equipamento com falha); não encontrei integração nativa com ordem de serviço [Verificar].

## MVP em 5 dias
- 2–3 nós (ventilador, bomba ou furadeira) com carga provocada: rotor travando, filtro entupido simulado, sobrecarga.
- Dashboard PWA + Telegram com a mensagem completa ao técnico.
- Métrica honesta: tempo até alertar e falsos positivos numa bancada, **não** F1 de dado simulado.

## Riscos
Defeito por assinatura elétrica é indicativo; sem histórico real, o baseline demora dias. Mais código para manter que a solução 02.

## Pontos para o pitch
"Mostra qual máquina, qual pico e manda para o técnico certo": tradução de energia em ação e R$.
