# Pitch técnico: MapaVolt (nome provisório)

> 29/10/2026. Até **5 minutos** (≈ 700 palavras faladas, ritmo de ~140 palavras/min). Uma seção por página/slide: o que aparece na tela e a fala.
> Público: banca técnica (engenharia, manutenção, TI/automação da ArcelorMittal).
> Números: preço de **R$ 209/MWh** (meio da faixa pública R$ 178–250; trocar pelo preço interno) e fator de **46 gCO₂/kWh** (inventário da própria ArcelorMittal Brasil). Potências das máquinas são **estimativas** para ilustrar. Fontes em `../solucao.md`, `../app.md`, `../equipamentos.md` e `../../dados/`.
> Trocar "MapaVolt" pelo nome escolhido.

---

## Página 1 · O problema técnico (0:00–0:30)
**Na tela:** gráfico de potência de um exaustor subindo 15% e ficando assim por dias, com a legenda "ninguém viu".

**Fala:** No Pecém, a energia que a usina não gasta vira excedente vendido. Mas uma máquina que passa a puxar 15% a mais (rolamento, damper travado, ligada sem produzir) continua "funcionando" e não dispara nenhum alarme de processo. O desperdício só aparece na próxima inspeção. Medindo energia por máquina, esse desvio fica visível em minutos, e não na semana seguinte.

## Página 2 · O que medimos (0:30–1:00)
**Na tela:** foto do sensor de alicate e do multimedidor no painel; lista V, I por fase, kW, FP, kWh, Hz.

**Fala:** Em cada máquina, um medidor elétrico trifásico lê tensão, corrente por fase, potência, fator de potência, energia e frequência a cada poucos segundos. Em baixa tensão usamos medidor com Modbus e TC de alicate, sem parar a máquina. Em motor grande e média tensão, ligamos no secundário dos TCs que já existem no painel. E onde já houver multimedidor ou relé em rede, só lemos o dado: hardware zero.

## Página 3 · Arquitetura (1:00–1:30)
**Na tela:** sensor → gateway → MQTT → servidor (regras + séries temporais) → app.

**Fala:** Os medidores de um painel vão por cabo RS485 até um gateway, porque cabo é mais confiável que Wi-Fi em área metálica. O gateway publica as leituras por MQTT. No servidor, as leituras ficam num banco de séries temporais e passam pelas regras de detecção. O app recebe tudo ao vivo. O sistema **só lê e nunca comanda máquina**, fica numa rede separada e não entra na rede de automação.

## Página 4 · Detecção explicável (1:30–2:05)
**Na tela:** tabela curta das regras: sobreuso vs. esperado, acima da nominal, parada inesperada, ligada fora de horário, tensão, desbalanço, FP baixo, sem sinal.

**Fala:** Começamos com regras que o técnico entende, não com caixa-preta. Cada máquina tem potência esperada, faixa normal e horário de operação, que podem ser sugeridos pela própria leitura do sensor. Sobreuso é, por exemplo, 15% acima do esperado por 5 minutos. Tempo mínimo e histerese evitam alarme falso, e a partida do motor é ignorada. Todo alerta mostra qual regra disparou, o valor medido e o esperado. A IA vem depois, treinada com as causas que os técnicos registram.

## Página 5 · Do alerta à pessoa certa (2:05–2:40)
**Na tela:** fluxo alerta → chamado → time no turno → "Pegar chamado" → escala para o gestor em 15 min.

**Fala:** O alerta vira um chamado dentro do app. Se a máquina tem um time responsável, todos do time que estão no turno recebem; se tem só um cargo, todos daquele cargo no turno. O primeiro que tocar em "Pegar chamado" vira o dono. Se ninguém pegar em 15 minutos, o chamado vai para o gestor do time. Ao resolver, o técnico registra a causa. Assim medimos tempo até pegar, tempo até resolver e a energia evitada depois da correção.

## Página 6 · Mapa e rota (2:40–3:05)
**Na tela:** mapa da unidade com máquinas coloridas; rota da Portaria até a máquina.

**Fala:** Cada unidade tem um mapa desenhado no próprio app, com áreas, linhas e formas. As máquinas ficam vermelhas em sobreuso, cinza paradas e verdes normais. Os corredores desenhados formam um grafo, e o app calcula o menor caminho a partir de um ponto de referência, como a portaria ou a sala de controle. Funciona sem GPS, dentro de galpão.

## Página 7 · Analytics e cálculo da economia (3:05–3:35)
**Na tela:** cartão "Economia em outubro: R$ 48,3 mil · 231 MWh"; ranking das máquinas que mais desperdiçam.

**Fala:** A economia é calculada assim: consumo antes da correção menos consumo depois, vezes o preço do MWh. No exemplo do protótipo, 231 MWh num mês, a R$ 209, são R$ 48 mil e 10,6 toneladas de CO₂ evitadas, com o fator da própria ArcelorMittal. O gestor vê o ranking de desperdício, a economia por área, o tempo de resposta por time e se as preventivas estão em dia.

## Página 8 · Governança, preventivas e escala (3:35–4:00)
**Na tela:** cards de times, plano de preventiva por horas de operação, seletor de unidades.

**Fala:** O app cadastra times, funcionários, cargos e turnos. As preventivas podem ser por calendário, por horas de operação (o próprio sensor conta) ou por condição, quando o consumo começa a subir. E a mesma estrutura escala para as outras unidades do grupo: Tubarão, Vega e Monlevade, trocando só o mapa e o cadastro.

## Página 9 · Protótipo e custo (4:00–4:35)
**Na tela:** celular com o protótipo; tabela de custo.

**Fala:** O protótipo já tem painel ao vivo, detalhe da máquina, mapa com rota, chamados, preventivas, governança e analytics, com dados simulados. Na bancada, um ESP32 com um medidor de R$ 150 mostra o alerta acontecendo ao vivo. Num piloto, o custo é de R$ 900 a R$ 1.500 por máquina em baixa tensão, mais a assinatura. Um único exaustor da sinterização com 10% de sobreuso desperdiça cerca de R$ 15 mil por semana. O retorno fica dentro do critério de menos de 2 anos que a própria ArcelorMittal já usou.

## Página 10 · Próximo passo (4:35–5:00)
**Na tela:** "Piloto de 90 dias · 20 máquinas · Aciaria".

**Fala:** Propomos um piloto de 90 dias em 20 máquinas da Aciaria, começando pelas que já têm medição no painel. Em três meses, entregamos a economia medida em kWh e em reais, com a mesma régua de energia que vocês usam no relatório de sustentabilidade. O MapaVolt não espera a próxima inspeção.

---

### Apoio para perguntas da banca
| Pergunta provável | Resposta curta |
|---|---|
| E se a rede cair? | O gateway guarda as leituras e reenvia; o app mostra "sem sinal" separado de "parada". |
| Mexe na automação? | Não. Só leitura, rede separada, nenhum comando para máquina. |
| Precisa trocar medidores? | Não onde já existe multimedidor/relé em rede; nas demais, sensor de alicate. |
| E alarme falso? | Tempo mínimo, histerese, partida ignorada e limites aprendidos da própria máquina. |
| Quem instala? | Eletricista habilitado (NR-10); sensor não invasivo sempre que possível. |
