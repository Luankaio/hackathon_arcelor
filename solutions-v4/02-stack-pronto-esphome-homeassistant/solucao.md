# 02 — Stack pronta: ESPHome + Home Assistant + Node-RED (a mais simples e robusta)

## Ideia
Em vez de escrever firmware, backend e app, usar ferramentas abertas maduras e escrever só o que é nosso: **baseline/defeito por equipamento e o fluxo de aviso ao técnico**.

## Arquitetura
1. **Sensor:** ESP32 + PZEM-004T v3 com TC. O ESPHome tem suporte nativo a PZEM-004T v3 e o Home Assistant descobre o dispositivo automaticamente [Fato, via guia; conferir doc oficial]. Vários PZEM no mesmo barramento exigem endereços distintos antes da instalação [Fato]. Alternativa: Shelly Pro 3EM (trifásico, DIN, Modbus TCP, FP por fase, integração local push no Home Assistant) [Fato, fontes de revenda e blog; conferir mapa de registradores].
2. **Hub:** Home Assistant num mini PC/Raspberry (local, funciona sem nuvem).
3. **Lógica:** Node-RED ou automações do HA para: pico (limiar + derivada), deriva vs. baseline (sensor de estatística/`statistics`, ou script Python no AppDaemon/Node-RED), estado do aparelho por faixa de potência.
4. **App no celular:** app oficial do Home Assistant (notificações push com ação "Assumir/Resolvido") e dashboards prontos; Grafana opcional.
5. **Aviso ao técnico:** notificação push no app e/ou bot do Telegram; escalonamento por temporizador.

## Licenças e referências
- ESPHome: runtime C++ GPLv3 e código Python MIT [Fato, listagens de pacote]. Usar como ferramenta é livre; atenção se redistribuir firmware modificado.
- Exemplos: [ESPHome + PZEM + MQTT](https://esp32.co.uk/esp32-pzem-004t-energy-monitor-esphome-mqtt/), [fórum HA](https://community.home-assistant.io/t/how-to-use-pzem004t-energy-monitor-with-esphome/107083/1), [3 PZEM em ESPHome](https://github.com/BNAP-3D/PZEM-ESPHome), [alerta SMS + MQTT](https://hackaday.io/project/204801-smart-energy-meter-with-mqtt-dashboard-sms-alert).
- A guia da esp32.co.uk traz automação de alerta ao passar de 3 kW; um manual de PZEM cita detectar fim de ciclo de máquina pela queda de potência [Fato].
- Home Assistant companion app/emonPi: licença e recursos **não verificados** nesta pesquisa [Verificar].

## MVP em 2–3 dias (mais rápido que a 01)
Flashar 2–3 ESP32 com YAML, subir o HA, montar o dashboard por equipamento, criar a automação de pico e de deriva, testar notificação com botões. Sobra tempo para pitch e M&V.

## Prós e contras
- (+) Quase nenhum código, app pronto, comunidade grande, fácil de explicar à banca.
- (−) Menos "nosso": diferencial vira a lógica de defeito + fluxo do técnico + R$ do desperdício. Home Assistant é pensado para casa; para planta grande, a evolução é MQTT + Grafana/Node-RED ou plataforma industrial.
- (−) PZEM mede AC e é módulo barato; para ambiente industrial pesado, preferir medidor com Modbus (Shelly Pro 3EM ou similar).

## Pitch
"Em dias, qualquer pequeno negócio ou área da fábrica tem monitoramento por equipamento com alerta ao técnico, usando componentes abertos e baratos."
