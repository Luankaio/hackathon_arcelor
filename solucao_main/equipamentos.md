# Equipamentos para a solução principal (sensores, medidores, gateways)

> Pesquisa de 29/10/2026 para `solucao.md`. Preços vêm de anúncios e lojas indexados por busca na web nesta data: **podem ter mudado**, então confirme antes de comprar. Preços em US$/€ são de lojas estrangeiras e **não incluem frete, câmbio nem impostos de importação**.
> Marcação: **[Fato]** visto em fonte · **[Estimativa]** nossa · **[Verificar]** não confirmado.
> O que cada um precisa medir para a solução: tensão (V), corrente (A), potência ativa (kW), fator de potência, energia (kWh) e, de preferência, por fase (trifásico).

---

## 1. Resumo: o que usar em cada caso

| Caso | Recomendação | Custo por máquina [Estimativa] |
|---|---|---|
| **Demo do hackathon** | ESP32 DevKit + 1 PZEM-004T v3 (com TC) num aparelho monofásico | ≈ R$ 150 |
| Demo trifásica / piloto barato | ESP32 + 3× PZEM-004T, ou 1 Shelly Pro 3EM | R$ 450–1.300 |
| **Piloto na indústria (baixa tensão, até 100 A direto)** | Medidor trifásico DIN com Modbus RS485 (genérico 100 A ou Metaltex KWX) + gateway RS485→MQTT compartilhado | R$ 900–1.500 |
| Piloto com marca reconhecida (exigência de compras/qualidade) | Siemens PAC1020, Schneider EM3155 ou PM5110 | R$ 2.300–5.000 + gateway |
| **Motor grande / média tensão** | Multimedidor com entrada 5 A nos TCs/TPs existentes (Kron Mult-K 05, Schneider PM5110) | R$ 1.550–5.000 + instalação |
| Máquina que já tem medidor ou relé com rede | Integrar o que existe (Modbus TCP / OPC UA) via gateway | só software |
| Complemento (vibração/temperatura no motor) | WEG Motor Scan ou sensor LoRaWAN | R$ 700–1.430 (ou US$ 73–160 importado) |

Ordem de grandeza: **um piloto de 10 máquinas de baixa tensão** ≈ R$ 9–15 mil em hardware (10 medidores genéricos + 1–2 gateways + caixas, disjuntores e cabos), sem a mão de obra do eletricista. [Estimativa]

---

## 2. Sensores e medidores elétricos

### 2.1 Para protótipo e demo (baixo custo, faça você mesmo)

| Equipamento | O que faz | Mede | Comunicação | Preço (29/10/2026) | Prós / contras |
|---|---|---|---|---|---|
| **PZEM-004T v3.0 100 A** (Peacefair) | Módulo medidor de energia **monofásico** com TC de alicate (núcleo dividido ou fechado) | V (80–260 V), I (até 100 A com TC), P, kWh, Hz, FP [Fato] | Serial TTL (UART) → ESP32 | **R$ 99–140** em lojas brasileiras (MSS Eletrônica R$ 98,90 com TC; Smart Kits, AutoCore R$ 129,90; Nefeltech R$ 139,90; RoboBuilders R$ 172,95). Importado da China a partir de ≈ R$ 48 [Fato] | ✔ Mede tudo que a solução precisa, biblioteca pronta (`PZEM-004T-v30`, ESPHome). ✘ Monofásico (trifásico = 3 módulos), sinal em 5 V (ESP32 é 3,3 V: usar divisor/conversor de nível), precisão de hobby, ligação na tensão da rede (cuidado) |
| **SCT-013-000 100 A** | Sensor de corrente de alicate, não invasivo | Só corrente (saída 0–50 mA) [Fato] | Analógico → ESP32 (precisa de resistor de carga e circuito) | **R$ 45–80** (A2 Robotics R$ 45,50; Bit Maker R$ 49,90; MakerHero R$ 59,40) [Fato] | ✔ Barato, zero risco elétrico para instalar. ✘ Sem tensão nem FP: a potência sai estimada. Bom como complemento, não como sensor principal |
| **ESP32 DevKit** (WROOM-32) | Microcontrolador com Wi-Fi e Bluetooth; lê os sensores e envia por MQTT | — | Wi-Fi, BLE, UART, RS485 (com módulo) | **R$ 35–75** (WJ Componentes R$ 33,22; MakerHero R$ 51,90; Fermarc R$ 65,90) [Fato] | ✔ Barato, ESPHome/Arduino. ✘ Precisa de caixa e fonte; não é produto industrial |
| **CircuitSetup Energy Meter (chip ATM90E32)** | Placa medidora de energia para ESP32 (2 a 6 canais de corrente) | V, I, P, FP, kWh por canal | SPI → ESP32 (ESPHome) | ≈ US$ 29–90 (preços antigos de lançamento/SparkFun) [Verificar preço atual] | ✔ Vários circuitos numa placa só, boa precisão. ✘ Importado; modelo trifásico precisa medir as 3 tensões [Verificar] |

**Kit da demo sugerido:** ESP32 (≈ R$ 50) + PZEM-004T com TC (≈ R$ 100–130) + fonte 5 V, caixa, borne e cabo (≈ R$ 30–50) ≈ **R$ 180–230**. Ligar num ventilador ou motorzinho para mostrar sobreuso (frear) e parada (desligar) ao vivo. [Estimativa]

### 2.2 Medidores prontos (piloto e produção)

| Equipamento | O que faz | Ligação | Comunicação | Preço (29/10/2026) | Observação |
|---|---|---|---|---|---|
| **Shelly Pro 3EM** (120 A e 400 A) | Medidor trifásico de trilho DIN com 3 TCs de alicate | Direta (tensão) + TCs de alicate | Wi-Fi, Ethernet, Bluetooth; API local, MQTT [Fato] | **120 A: R$ 1.040–1.300** (4Tronics R$ 1.095 / R$ 1.040 no Pix; AV Controls R$ 1.299,99). **400 A: R$ 2.740** (4Tronics) [Fato] | ✔ Já fala MQTT e tem app; instala sem abrir o cabo; precisão de 1% [Fato]. ✘ Pensado para residência/comércio; alimentação de 230 V [Verificar compatibilidade com 220/380 V do CE] |
| **Medidor trifásico genérico 100 A Modbus** (marketplace) | Medidor de energia trifásico de trilho DIN | Direta até 100 A | RS485 Modbus RTU | **≈ R$ 598** no Mercado Livre (220 V, 100 A); importado de 380/400 V a partir de ≈ R$ 152 [Fato, anúncio antigo: Verificar] | ✔ Mais barato com Modbus. ✘ Marca desconhecida, sem certificação verificada |
| **Eastron SDM630 Modbus (V2/V3, MID)** | Medidor trifásico DIN muito usado em solar e carregadores de VE | Direta até 100 A (ou versão com TC) | RS485 Modbus RTU [Fato] | **≈ € 100–123** na Europa (Voltus € 100,25; Invibit € 123) [Fato]. Não encontrei preço em R$ | ✔ Bem suportado (ESPHome, evcc, biblioteca Python `sdm-modbus`). ✘ Importação; INMETRO [Verificar] |
| **Metaltex KWX(-M)** | Multimedidor de painel 96 × 96 mm | 50–500 VCA; mono, bi ou trifásico, com TC [Fato] | RS485 Modbus RTU [Fato] | **≈ R$ 837** (Mercado Livre) [Fato] | ✔ Marca brasileira, barato para painel. ✘ Precisa de TC externo |
| **Kron Mult-K 05** | Multimedidor e transdutor de grandezas elétricas, trifásico | **Entrada de 5 A** (secundário de TC) e até 500 V; ideal com TCs/TPs existentes | RS485 Modbus | **R$ 1.550–2.140** (Junção R$ 1.549 no Pix; Eletrostar R$ 1.660; Mercado Livre R$ 1.750–2.140) [Fato] | ✔ Marca brasileira comum em painéis industriais, aceita os TCs que já existem (motores grandes, média tensão via TP). ✘ Instalação em painel |
| **Siemens SENTRON PAC1020** | Medidor de energia trifásico DIN | 230/400 V | RS485 Modbus RTU [Fato] | **≈ R$ 2.338** (Eco Automação, fora de estoque) [Fato] | ✔ Marca que a indústria já compra |
| **Schneider EM3155** | Medidor de energia e potência trifásico DIN | Direta até 63 A | RS485 Modbus [Fato] | **≈ R$ 2.970** (Dimensional) [Fato] | ✔ Marca reconhecida. ✘ 63 A máx. em ligação direta |
| **Schneider PowerLogic PM5110 / PM5111** | Multimedidor de painel com harmônicos até a 15ª e 33 alarmes [Fato] | Com TC (5 A) | RS485 Modbus | **PM5110 R$ 4.830–4.980; PM5111 R$ 4.850–5.000** (CMC Importação) [Fato] | ✔ Padrão de mercado em grande indústria; mede harmônicos (qualidade de energia). ✘ Caro para colocar em toda máquina |
| **Schneider PM5330** | Multimedidor de painel, versão superior | Com TC | RS485 Modbus | **R$ 6.272–6.602** (Mais Industrial) [Fato] | Só para alimentadores e painéis principais |

### 2.3 Transformadores de corrente (para motores grandes)
- Em motores e painéis industriais grandes, a corrente passa de 100 A e muitas vezes é média tensão. A ligação certa é usar o **secundário de 5 A dos TCs** (e dos TPs, na média tensão) que já existem no painel, ou instalar TCs de janela / núcleo dividido / bobina de Rogowski. [Fato técnico; preços não pesquisados: Verificar]
- Por isso os medidores com entrada de 5 A (Kron Mult-K 05, Metaltex KWX, Schneider PM5110) são a escolha para os motores da usina.

---

## 3. Gateways e comunicação (do medidor até o servidor)

| Equipamento | O que faz | Interfaces | Preço | Observação |
|---|---|---|---|---|
| **PUSR USR-DR404** | Conversor de trilho DIN RS485 → Wi-Fi/Ethernet; também gateway Modbus RTU → Modbus TCP e MQTT [Fato] | RS485, Wi-Fi 802.11 b/g/n, Ethernet | **≈ US$ 37** (Alibaba / Amazon) [Fato] | ✔ Barato; 1 gateway lê vários medidores no mesmo par RS485. ✘ Sem 4G |
| **Waveshare RS485 to WiFi/ETH** | Servidor serial de trilho DIN, gateway Modbus/MQTT [Fato] | RS485, Wi-Fi, Ethernet | **≈ US$ 35** [Fato] | Alternativa ao DR404 |
| **Gateway Modbus RTU → MQTT 4G** (Puneet Productions, Tindie) | Lê Modbus e publica em MQTT pela rede celular [Fato] | RS485, 4G | **US$ 99** [Fato] | Para área sem rede da empresa (pátio, correia longa) |
| **ModbusCloud Gateway** | Gateway RS485/Ethernet/4G + portal | RS485, Ethernet, 4G | **a partir de € 295 + € 149/ano** [Fato] | Referência de produto pronto; o nosso app substitui o portal |
| **NORVI IIoT (ESP32 industrial DIN, 24 V)** | Controlador ESP32 em caixa de trilho DIN, para painel | RS485, Wi-Fi, BLE, E/S; versões com Ethernet/LTE [Fato] | **US$ 66–136** (NORVI X: US$ 79–101 por CPU) [Fato] | ✔ "ESP32 de verdade para indústria": roda ESPHome, aguenta painel 24 V |
| **KinCony (ESP32 DIN, RS485)** | Placas ESP32 de trilho DIN com RS485 e Ethernet | RS485, Ethernet, Wi-Fi | **US$ 130–255** conforme modelo [Fato] | Mais voltado a relés/automação; opção se precisar de E/S |
| **Milesight UG65 (gateway LoRaWAN)** | Gateway LoRaWAN de 8 canais, IP65, 4G/Ethernet [Fato] | LoRaWAN, 4G, Ethernet | **US$ 467–777 / € 374** [Fato]. RAK7268: sem preço encontrado | Só se usar sensores LoRaWAN (longo alcance, bateria). Para energia, o normal é RS485 cabeado |

**Recomendação de arquitetura física [Estimativa]:** em cada painel/CCM, um par RS485 ligando até ~10–30 medidores Modbus → **1 gateway** (USR-DR404 ou NORVI) → rede da empresa (Ethernet/Wi-Fi) ou 4G → broker MQTT. Cabo é mais confiável que Wi-Fi dentro de área metálica.

---

## 4. Complementos: vibração e temperatura (opcional)
Não fazem parte do núcleo (que é elétrico), mas ajudam a confirmar defeito mecânico quando o sobreuso aparece.

| Equipamento | O que faz | Comunicação | Preço | Observação |
|---|---|---|---|---|
| **WEG Motor Scan** (WMSC) | Sensor preso na carcaça do motor; mede temperatura, vibração e horas de operação, com alertas; motores WEG carcaça 63 a 450; IP66 [Fato] | Bluetooth (app WEG) | **R$ 714–760** só o sensor; **R$ 1.348–1.430** com 1 ano de assinatura [Fato] | ✔ Muito comum em motor WEG no Brasil. ✘ Dados ficam na plataforma WEG (integração com o nosso app: Verificar API) |
| **Banner QM42VT1** (via Movimatic) | Sensor de vibração e temperatura para motores | Conforme kit (fio/sem fio) [Verificar] | **a partir de R$ 822** (página com ~1 ano) [Fato] | Sem mensalidade, segundo a loja |
| **Advantech WISE-2410** | Acelerômetro 3 eixos + temperatura, a bateria (~2 anos), IP66 [Fato] | LoRaWAN | **R$ 5.981** (Eletroflash) [Fato] | Industrial, caro |
| **Minew LSV01** | Vibração e temperatura | LoRaWAN (US915/EU868) [Fato] | **US$ 160** [Fato] | Verificar se tem a faixa AU915 usada no Brasil |
| **Netvox R718EC** | Vibração/temperatura | LoRaWAN | **US$ 99** (promoção) [Fato] | Idem |
| **Dragino LHT65N-VIB** | Vibração e temperatura | LoRaWAN | **US$ 73** [Fato] | Mais barato; idem |

---

## 5. Cuidados antes de comprar
- **Tensão do Ceará:** a rede comercial é 220 V (fase-neutro) / 380 V (fase-fase). Conferir se o medidor aceita isso (vários importados são 230/400 V, o que normalmente cobre, mas Verificar no manual).
- **Faixa de frequência LoRaWAN no Brasil:** AU915. Sensores EU868 não servem. [Verificar cada modelo]
- **Certificação:** para gestão interna de energia não é preciso medidor de faturamento; para cobrança/rateio, exigir certificação (INMETRO/IEC 62053).
- **Instalação:** em painel energizado, só profissional com NR-10. Preferir sensor de alicate e TCs já existentes.
- **Pergunta para a ArcelorMittal:** os CCMs e painéis do Pecém já têm multimedidores ou relés de proteção em rede (Modbus/Profibus/IEC 61850)? Se tiverem, boa parte das máquinas pode entrar no app **sem hardware novo**. (Ver `../dados/lacunas-perguntas-para-ideathon.md`.)

---

## 6. Fontes (consultadas em 29/10/2026)
- PZEM-004T: [MSS Eletrônica](https://www.msseletronica.com.br/detalhes/modulo-wattimetro-voltimetro-amperimetro-100a-pzem-004t-rs232-ttl_pid1321.html) · [Smart Kits](https://www.smartkits.com.br/modulo-medidor-de-energia-pzem-004t-100a-260v) · [Nefeltech](https://nefeltech.com/produtos/modulo-de-monitoramento-eletrico-pzem-004t/) · [RoboBuilders](https://www.robobuilders.com.br/produto/pzem-004t-modulo-corrente-invasivo.html) · [AutoCore Robótica](https://www.autocorerobotica.com.br/modulo-de-monitoramento-eletrico-voltimetro-ac-wattimetro-amperimetro-pzem-004t) · [Saravati](https://www.saravati.com.br/voltimetro-amperimetro-pzem-004t-v3-0-100a-260v-ac-saida-ttl.html) · [How2Electronics (ligação no ESP32)](https://how2electronics.com/iot-ac-energy-meter-with-pzem-004t-esp32-webserver/)
- SCT-013: [A2 Robotics](https://www.a2robotics.com.br/sensor-de-corrente-nao-invasivo-sct-013-000-100a) · [Bit Maker](https://www.bitmaker.com.br/sensor-de-corrente-nao-invasivo-100a-sct-013) · [MakerHero](https://www.makerhero.com/produto/sensor-de-corrente-nao-invasivo-100a-sct-013/)
- ESP32: [WJ Componentes](https://www.wjcomponentes.com.br/esp32-wroom-32d-devkit-v4) · [MakerHero](https://www.makerhero.com/produto/placa-esp32-devkitc-v4/) · [Fermarc](https://www.fermarc.com/esp32-devkitc-wroom-32d)
- ATM90E32: [ESPHome devices](https://devices.esphome.io/devices/CircuitSetup-Expandable-6-Channel-ESP32-Energy-Meter-(ATM90E32)) · [CNX Software](https://cnx-software.com/?p=65617)
- Shelly Pro 3EM: [4Tronics 120 A](https://loja.4tronics.com.br/produtos/shelly-pro-3em/) · [4Tronics 400 A](https://loja.4tronics.com.br/produtos/shelly-pro-3em-400/) · [AV Controls](https://avcontrols.com.br/products/shelly-pro-3em)
- Medidores Modbus: [Mercado Livre – medidor trifásico RS485](https://lista.mercadolivre.com.br/medidor-trifasico-rs-485) · [Mercado Livre – medidor Modbus](https://lista.mercadolivre.com.br/medidor-de-energia-modbus) · [Oferta Viva](https://www.ofertaviva.com.br/produto/medidor-eletrico-trifasico-rs485-kwh-medidor-de-consumo-de-energia-eletrico-monitor-modbus-rtu-380v-400v-v-v.html) · [Metaltex KWX (PDF)](https://www.metaltex.com.br/assets/produtos/pdf/kwx.pdf) · [Siemens PAC1020 – Eco Automação](https://ecoautomacao.com.br/produto/multimedidor-pac1020-230-400v-modbus-rtu-rs485-7km1020-0ba01-1da0-siemens/) · [Schneider EM3155 – Dimensional](https://www.dimensional.com.br/medidor-energ-pot-eletronico-3f-modbus-rs485-63-a-em3155-schneider/p) · [Schneider PM5110 – CMC](https://www.cmcimportacao.com/multimedidor-metsepm5110-modbus-rs485-schneider) · [Schneider PM5111 – CMC](https://www.cmcimportacao.com/multimedidor-metsepm5111-modbus-rs485-schneider) · [Schneider PM5330 – Mais Industrial](https://www.lojamaisindustrial.com.br/metsepm5330-multimedidor-pm5330-modbus-rs485/p/metsepm5330)
- Eastron SDM630: [Voltus](https://www.voltus.com/en/eastron-sdm630modbus-v3-modbus-ac-meter-sdm630-v3.html) · [Invibit](https://invibitshop.com/products/eastron-sdm630mct-mod-mid-3-phase-ct-energy-meter-with-modbus-rtu-mid-certified) · [evcc docs](https://docs.evcc.io/en/meters/eastron-sdm630-modbus)
- Kron Mult-K 05: [Junção](https://www.juncao.com.br/mult-k-05-5a-500v-120220v-multimedidor-de-energia-z021815511100-kron-medidores) · [Eletrostar Campinas](https://www.eletrostarcampinas.com.br/mult-k-05-multimedidor-e-transdutor-digital-de-grandezas-eletricas-z021815511100-kron-medidores) · [Mercado Livre](https://produto.mercadolivre.com.br/MLB-4714291202-multimedidor-multi-k-05-trifasico-5a-rs485-120220vca-kron-_JM)
- Gateways: [PUSR USR-DR404](https://www.pusr.com/products/rs485-to-80211-a-b-g-n-wlan-serial-device-server-usr-dr404.html) · [Amazon USR-DR404](https://www.amazon.com/PUSR-Converters-802-11-Servers-USR-DR404/dp/B0BX39Y6W6) · [Waveshare](https://www.waveshare.com/rs485-to-wifi-eth.htm) · [Tindie 4G gateway](https://www.tindie.com/products/puneetproductions/modbus-rtu-to-mqtt-4g-gateway/) · [ModbusCloud](https://www.modbuscloud.com/gateway) · [NORVI](https://norvi.io/products/norvi-iiot-esp32-industrial-controller/) · [KinCony](https://shop.kincony.com/) · [Milesight UG65 – MCCI](https://store.mcci.com/products/milesight-ug65-semi-industrial-lorawan-gateway) · [Elmark](https://elmark-automation.com/shop/milesight/ug65-semi-industrial-lorawan-gateway)
- Vibração/temperatura: [WEG Motor Scan – RR Bombas](https://www.rrbombasemotores.com.br/produtos/sensor-inteligente-motor-scan-partes-motor-15521739/) · [CSA Automação](https://loja.csaautomacao.com.br/produto/weg-motor-scan/) · [Viewtech](https://www.viewtech.ind.br/motor-scan-weg-sensor-inteligente-para-motor-com-assinatura-de-1-ano) · [Unitek](https://www.unitek.ind.br/sensor-motor-scan-weg-inteligente-para-motor-wmsc-1) · [Movimatic](https://movimatic.com.br/monitoracao-de-vibracao-e-temperatura-de-motores/) · [Advantech WISE-2410 – Eletroflash](https://www.eletroflash.com.br/wise2410nb--sensor-de-vibracao-sem-fio-lorawan-56009-1) · [Minew LSV01](https://www.minewstore.com/product/lsv01-industrial-vibration-sensor) · [CHOOVIO (Netvox, Dragino)](https://www.choovio.com/product-category/lorawan-vibration-sensors/)
