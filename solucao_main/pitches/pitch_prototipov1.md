# Pitch do protótipo v1: storytelling (MapaVolt, nome provisório)

> 29/10/2026. Até **5 minutos** (≈ 720 palavras faladas). Cada bloco tem o que aparece na tela, a **Fala** e o tempo.
> **Persona fictícia** (inventada para o pitch): Francisco Holanda, "Chico". Times, nomes e números do app são dados simulados do protótipo.
> Conta do desperdício: **excesso de potência (kW) × horas até ser notado × R$ 209/MWh** (meio da faixa pública R$ 178–250; trocar pelo preço interno). Potências das máquinas são **estimativas** de ordem de grandeza para uma usina do porte do Pecém [Verificar com a ArcelorMittal].
> Trocar "MapaVolt" pelo nome escolhido.

---

## Persona
| Campo | Valor |
|---|---|
| Nome | Francisco Holanda, o **Chico** |
| Idade | 41 anos, 11 de usina |
| Cargo | **Técnico de Manutenção Elétrica** |
| Time | Manutenção Elétrica – Aciaria, ArcelorMittal Pecém |
| Turno | Turma B |
| Rotina | **Toda quarta-feira** faz a ronda de inspeção preventiva das ~40 máquinas da área: alicate amperímetro, termografia, ouvido no rolamento, prancheta |
| Dor | Vê cada máquina **uma vez por semana**. No resto do tempo, só fica sabendo de um problema quando ele vira quebra |

---

## 1. Apresentação (0:00–0:25)
**Na tela:** foto ilustrativa de um técnico de capacete e uniforme na aciaria; nome e cargo.

**Fala:** "Gostaríamos de apresentar para vocês o Francisco, o Chico. Ele tem 41 anos, 11 deles aqui na usina do Pecém, e é técnico de manutenção elétrica do time da Aciaria, na turma B. O Chico cuida de umas 40 máquinas: ventiladores, bombas, pontes rolantes, compressores."

## 2. Como é o trabalho do Chico hoje (0:25–0:55)
**Na tela:** calendário da semana com a **quarta-feira** destacada: "Ronda preventiva".

**Fala:** "Toda quarta-feira, o Chico faz a ronda. Passa em cada máquina com o alicate amperímetro, a câmera termográfica e a prancheta. Mede a corrente, sente a temperatura, escuta o rolamento. É um trabalho sério e bem feito. Mas tem um limite: o Chico vê cada máquina uma vez por semana. Nos outros seis dias, ninguém está olhando."

## 3. O problema: a quinta-feira (0:55–1:30)
**Na tela:** linha do tempo de quinta 14h até a quarta seguinte; gráfico de potência subindo 15% e ficando lá.

**Fala:** "Agora imagina que, numa quinta-feira, um dia depois da ronda, o rolamento do ventilador de despoeiramento começa a dar folga. O motor passa a puxar 15% a mais. Não para, não dispara alarme, a produção continua. Só que essa máquina vai ficar seis dias assim, cento e quarenta e quatro horas, até a próxima quarta, quando o Chico passar por ela. E durante esse tempo inteiro ela está queimando energia que a usina poderia vender."

## 4. Quanto custa esperar até quarta (1:30–2:10)
**Na tela:** a tabela abaixo, uma linha por máquina, com o total em destaque.

| Máquina (área) | Potência média [Estimativa] | Defeito | Excesso | Energia jogada fora em 6 dias (144 h) | Gasto desnecessário (R$ 209/MWh) |
|---|---|---|---|---|---|
| Ventilador de despoeiramento (Aciaria) | 2.600 kW | Rolamento com folga | +15% = 390 kW | **56,2 MWh** | **R$ 11.737** |
| Exaustor principal (Sinterização) | 5.000 kW | Damper travado | +10% = 500 kW | **72,0 MWh** | **R$ 15.048** |
| Compressor de ar centrífugo (Utilidades) | 1.300 kW | Válvula de alívio aberta / vazamento | +20% = 260 kW | **37,4 MWh** | **R$ 7.825** |
| Bomba de resfriamento (Alto-Forno) | 750 kW | Válvula estrangulada / rotor gasto | +15% = 112,5 kW | **16,2 MWh** | **R$ 3.386** |
| Correia transportadora (Pátio de Matérias-Primas) | 400 kW | Rolete travado | +25% = 100 kW | **14,4 MWh** | **R$ 3.010** |
| **Total, se os 5 casos acontecerem** | | | **1.362,5 kW** | **196,2 MWh** | **R$ 41.006** |

Contas: excesso (kW) × 144 h ÷ 1.000 = MWh; MWh × 209 = R$. Ex.: 390 × 144 = 56.160 kWh = 56,2 MWh × 209 = R$ 11.737. Os 196,2 MWh equivalem a ≈ 9,0 t de CO₂ (46 gCO₂/kWh).

**Fala:** "Fizemos a conta para cinco máquinas típicas de uma usina como esta. Só o exaustor da sinterização, com 10% a mais, joga fora 72 megawatts-hora em seis dias: 15 mil reais. Se os cinco casos acontecerem na mesma semana, são quase 200 megawatts-hora e 41 mil reais de energia desperdiçada. E isso não é raro: se um caso desses acontecer por mês em cada uma, são quase meio milhão de reais por ano. Tudo isso só porque a próxima ronda é na quarta."

## 5. Por que isso importa para o Pecém (2:10–2:30)
**Na tela:** frase do CEO do Pecém sobre aumentar o excedente; "1% de eficiência ≈ R$ 2–3 milhões/ano".

**Fala:** "Aqui no Pecém, cada quilowatt-hora economizado vira excedente vendido. A própria empresa diz que a melhoria operacional aumentou o excedente de energia. Pelos números públicos, cada 1% de eficiência elétrica vale de 2 a 3 milhões de reais por ano. O desperdício existe, só não está sendo visto."

## 6. A solução: a mesma quinta-feira, com o MapaVolt (2:30–3:15)
**Na tela:** celular do Chico vibrando: "⚠ Sobreuso · Ventilador de despoeiramento AC-02 · +15% há 5 min"; botão "Pegar chamado"; mapa com a rota.

**Fala:** "Agora a mesma quinta-feira, com o MapaVolt. Às 14h12, o sensor no painel do ventilador percebe que ele está puxando 15% acima do normal há 5 minutos. O app abre um chamado para o time da Aciaria, só para quem está no turno. O celular do Chico vibra. Ele toca em 'Pegar chamado', e o app mostra o caminho da portaria até a máquina: 180 metros, 3 minutos. Às 14h52, o rolamento está trocado. Em vez de seis dias, foram 40 minutos. Em vez de 11 mil reais, cerca de 50 reais."

## 7. O app (3:15–3:55)
**Na tela:** demo do protótipo, passando rápido pelas abas.

**Fala:** "O MapaVolt é um app para o celular de quem está no chão de fábrica. No painel, cada máquina aparece ao vivo, com potência, corrente e tensão. No mapa da unidade, a máquina com problema fica vermelha, a parada fica cinza, e dá para traçar a rota. Os chamados vão para o time ou cargo responsável e sobem para o gestor se ninguém pegar em 15 minutos. As preventivas continuam, e podem ser por horas de operação, que o próprio sensor conta. E a gestão vê, no Analytics, quanto a usina economizou no mês e quais máquinas mais desperdiçam."

## 8. Custos e assinatura (3:55–4:30)
**Na tela:** três planos lado a lado.

| Plano [Proposta] | O que inclui | Preço |
|---|---|---|
| **Piloto 90 dias** | 20 máquinas, instalação, app completo, relatório de economia no fim | Hardware a preço de custo (≈ R$ 900–1.500 por máquina em baixa tensão) · **sem licença** no piloto |
| **Indústria** | App, chamados, mapa, preventivas, analytics, governança, várias unidades, suporte | **R$ 89 por máquina/mês** (48 máquinas ≈ R$ 4,3 mil/mês) |
| **Economia compartilhada** | Mesmo app, sem mensalidade fixa | **20% da economia medida** no 1º ano |

Onde já houver medidor em rede no painel, o hardware sai quase de graça (só o gateway). Para pequenas empresas, o mesmo app pode ter um plano menor (ex.: R$ 39 por máquina/mês) [Proposta].

**Fala:** "O custo é baixo para o tamanho do problema. O sensor de baixa tensão sai de 900 a 1.500 reais por máquina, e onde já existe medidor no painel, a gente só lê. A assinatura é de 89 reais por máquina por mês. Ou, se preferirem, sem mensalidade: ficamos com 20% da economia medida. Um único caso como o do exaustor, pego a tempo, já paga a assinatura de três meses de quarenta e oito máquinas."

## 9. Próximo passo (4:30–4:50)
**Na tela:** "Piloto de 90 dias · 20 máquinas · Aciaria do Pecém".

**Fala:** "Propomos um piloto de 90 dias em 20 máquinas da Aciaria. No fim, entregamos a economia medida em megawatts-hora e em reais, com a mesma régua de energia que vocês usam no relatório de sustentabilidade."

## 10. Fechamento (4:50–5:00)
**Na tela:** o Chico com o celular na mão; logo do MapaVolt.

**Fala:** "O Chico continua fazendo a ronda toda quarta-feira. A diferença é que agora a máquina avisa na quinta."

---

### Checagem das contas
- 3 meses de assinatura de 48 máquinas: 48 × R$ 89 × 3 = R$ 12.816. O caso do exaustor sozinho evita R$ 15.048 → "paga três meses" confere.
- 40 min de sobreuso do ventilador: 390 kW × 0,67 h ≈ 260 kWh × R$ 0,209 ≈ R$ 54 → "cerca de 50 reais" confere.
- "Quase meio milhão por ano": R$ 41.006 × 12 = R$ 492.072.
