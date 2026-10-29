# 03 — NILM: um medidor no quadro descobre qual aparelho ligou

## Ideia
Em vez de um sensor por aparelho, medir **o total** (trifásico) e identificar cada aparelho pela assinatura do degrau de potência (P, Q, FP), como o VoltIA tenta. Útil quando não dá para instrumentar tudo (escola, pequeno negócio, quadro geral).

## Arquitetura
1. **Medidor:** Shelly Pro 3EM ou ESP32 + PZEM no quadro; leituras de 1 s ou mais rápidas [Fato: Pro 3EM tem Modbus e FP por fase; conferir taxa de amostragem e registradores].
2. **Detecção de eventos:** detectar degraus em P/Q (liga/desliga) e picos de partida (inrush).
3. **Identificação:** classificador (Random Forest, como no VoltIA) ou modelo de desagregação. Referências:
   - NILMTK, toolkit aberto para comparar algoritmos de desagregação, licença Apache-2.0 [Fato]: [artigo](https://arxiv.org/abs/1404.3878). É ferramenta de pesquisa/benchmark, não um identificador embarcado pronto.
   - CNN de baixa taxa de amostragem que roda em placa como ESP32 [Fato, artigo; código não verificado]: [arXiv 2111.05120](https://arxiv.org/abs/2111.05120).
   - NILM com ML clássico no ESP32 + PZEM-004T [Fato, artigo]: [IJERT](https://www.ijert.org/non-intrusive-load-monitoring-via-edge-based-tinyml-on-esp32-microcontrollers-ijertv15is030304); relata que o ruído de transiente de chaveamento atrapalha.
4. **Defeito:** após identificar o aparelho, comparar sua assinatura (potência de regime, FP, duração da partida) com o histórico dele.
5. **App e aviso:** igual às soluções 01/02 (PWA ou Home Assistant + Telegram).

## Referências comerciais
Sense usa ML para identificar aparelhos (foco residencial); Verdigris combina hardware e ML para dados por dispositivo e falhas, com alertas por e-mail e site/app [Fato, trechos de busca]. Nada visto sobre ordem de serviço ao técnico [Verificar].

## Prós e contras
- (+) Instala-se em um ponto, barato, sem entrar em cada máquina.
- (−) Precisão incerta: aparelhos parecidos, ligados juntos ou com inversor confundem o modelo; precisa de dados rotulados reais. Sem rotulagem em campo, o F1 do VoltIA (0,918, dados simulados) **não vale como promessa**.
- (−) Em fábrica com muitas cargas simultâneas, NILM puro é fraco; servir como "triagem" e usar sensor dedicado nos críticos (híbrido com 01/02).

## MVP em 5 dias
Casa/laboratório com 5–7 cargas conhecidas (ventilador, bomba, ferro, compressor pequeno), coleta rotulada de 2–3 dias, classificador, demo ao vivo ligando e desligando e mostrando "qual aparelho ligou e que pico fez". Apresentar a taxa de acerto real da bancada.

## Recomendação
Tratar como evolução ou módulo de apoio, não como espinha do hackathon.
