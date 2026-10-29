# solutions-v4 — identificar aparelho, pico e defeito, e avisar o técnico

> 28/10/2026. Pedido do Luan: a partir do VoltIA (ou algo mais robusto e simples), identificar picos de aparelhos, identificar qual aparelho é, dashboard no celular, alerta de qual aparelho está com defeito e qual foi o pico, e aviso ao técnico.
> Marcação: **[Fato]** visto em fonte · **[Estimativa]** nossa · **[Verificar]** não confirmado.

## O que descobri sobre o VoltIA
[Fato, lido no README de https://github.com/LudwinS/voltia]
- ESP32 + MicroPython; mede V, I, P, Q, S, FP e energia; publica 6 feeds MQTT a cada 15 s no Adafruit IO; dashboard público e alerta no Telegram (antispam 60 s).
- Alertas são **regras locais** (consumo alto ≥1500 W, sobrecarga ≥2500 W ou ≥20 A, tensão <108 V ou >132 V), funcionam sem internet.
- Identificação do aparelho: Random Forest (500 árvores) sobre FP, potência reativa e variação de potência; F1 macro 0,918, mas com **dados simulados** (303 leituras rotuladas, 93 episódios). Hardware real (ZMPT101B + SCT-013, ou PZEM-004T) só previsto.
- **Sem licença declarada** e 0 estrelas, 1 commit. Sem licença, não dá para copiar o código: usamos só como referência de arquitetura e escrevemos do zero (ou pedimos licença ao autor).
- Limites para o nosso caso: tensão de 110 V (Brasil industrial/CE é 220/380 V), sem alerta que nomeie técnico, sem defeito (só "consumo alto"), sem app próprio, sem histórico/ordem de serviço.

## As 3 soluções
| | Ideia | Dificuldade | Precisão de "qual aparelho" | Melhor para |
|---|---|---|---|---|
| 01 | VoltIA reescrito: 1 nó ESP32 por aparelho/circuito, regras + IA de defeito, PWA + Telegram | Média | Alta (você sabe qual sensor está em qual máquina) | Hackathon e piloto industrial |
| 02 | Stack pronta: ESPHome + Home Assistant + Node-RED | Baixa | Alta (idem) | Entregar mais rápido, app de celular pronto |
| 03 | Um medidor trifásico + NILM para descobrir qual aparelho ligou | Alta | Média, incerta | Pequeno negócio/escola; quando não dá para instrumentar tudo |

## Lógica comum a todas (o que o técnico recebe)
- **Pico:** potência acima de limiar do próprio equipamento, ou subida brusca (derivada) além da inrush normal aprendida. Registra valor, duração e hora.
- **Defeito (suspeita):** desvio persistente frente ao **baseline do equipamento**: corrente/potência sobem sem aumento de carga, FP cai, desbalanço entre fases, partida mais longa, ciclo liga/desliga anormal. É sinal de suspeita (atrito, rolamento, bypass, vazamento), **não diagnóstico**.
- **Mensagem ao técnico** (Telegram ou WhatsApp): `Equipamento X · suspeita: corrente +18% vs. baseline há 3 h · pico 32 A às 14:05 · local · link do gráfico · [Assumir] [Resolvido]`. Escala para o supervisor se ninguém assumir em N minutos.
- **Segurança:** instalar com TC de alicate (não-invasivo) por eletricista habilitado; PZEM-004T mede AC e usa TC externo [Fato].

## Recomendação
Fazer a **02 como base (rápida, app pronto)** e **escrever em cima a lógica de defeito e de aviso ao técnico da 01**. Deixar a 03 como evolução. Ver cada pasta.
