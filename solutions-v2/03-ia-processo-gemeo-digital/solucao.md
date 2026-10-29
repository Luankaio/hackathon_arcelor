# TonaZero: copiloto de IA que recomenda setpoints para baixar kWh/t e GJ/t

> Pesquisa de 28/10/2026. **[VALIDADO]** = fonte lida/buscada, citada abaixo. **[PREMISSA]** = estimativa nossa. Não repete as soluções 01 (equipamento ocioso), 02 (demanda/PLD) e 03 (ar comprimido).

## 1. Problema
- Siderúrgica integrada gasta energia por tonelada de placa em processos de **combustão e aquecimento** (coqueria, sinterização, alto-forno, aciaria, lingotamento) e no balanço de gases/termelétrica. O operador ajusta setpoints (razão ar/combustível, temperatura, ritmo) por experiência e com margem de segurança "gorda".
- Contexto (dados/00-indice.md): Pecém ≈ 500 kWh/t de placa [DERIVADO pelo time]; 1% de eficiência ≈ 12-14 GWh/ano ≈ R$ 2-3 mi/ano; intensidade energética do Grupo piorou (22,03 -> 23,00 GJ/t). Kcal poupada = gás de processo que vira excedente de energia vendido (tese da própria ArcelorMittal).
- Ninguém vê, em tempo real, "quanto deveria gastar por tonelada nestas condições" e o que mudar para chegar lá.

## 2. Como funciona
1. **Dados** (já existem no PIMS/historiador, sem hardware novo): vazões de gás/ar/O2, temperaturas, carga, mix de produto, kWh/GJ por área, clima.
2. **Gêmeo digital leve** por unidade: modelo físico simplificado (balanço de energia) + ML (gradient boosting; depois aprendizado por reforço em simulador) que prevê consumo específico esperado (baseline "dinâmico" de kWh/t ou GJ/t).
3. **Detector de desvio**: compara real x esperado; desvio persistente = desperdício (ex.: excesso de ar, temperatura acima do necessário, tempo de espera entre etapas).
4. **Recomendador**: sugere setpoint dentro de limites de segurança e qualidade (restrições duras), mostra ganho esperado em kWh/t, GJ/t, R$ e CO2 (46 g/kWh, fator ArcelorMittal Brasil).
5. **App/dashboard para operador** (modo conselheiro, humano decide; fase 2 = malha fechada): alerta, "o que mudar", feedback "apliquei/não apliquei" que realimenta o modelo e mede o ganho (antes/depois contra baseline).

## 3. Referências validadas
| # | Quem / país | O que fazem | Evidência e limites | URL |
|---|---|---|---|---|
| 1 | **Energiency x ArcelorMittal Belval** (França/Luxemburgo) | IA sobre >1.600 sinais do forno de reaquecimento (1 s, 1 ano) para achar novos setpoints; modelo atualizado regularmente | Site economizou **>3% da fatura de energia**, acima da meta; contrato de 3 anos com meta >=5%/ano; potencial inicial estimado 2%/ano (€100 mil). Mesmo grupo da empresa-alvo. Vendor afirma "até 15%" (claim comercial) | https://innoenergy.com/uploads/2023/01/success-story-arcelormittal-energiency-eng.pdf |
| 2 | **Deep.Meta** (Reino Unido, spin-out do Imperial College) | Gêmeo digital Deep.Optimiser-PhyX (física + ML), prevê temperatura de placa no forno e otimiza ciclo/escalonamento | Venceu a trilha Energia e Ambiente do Venture Catalyst Challenge (Imperial); finalista (10 times) do 2º **Manchester Prize** (IA para o bem público, £100 mil seed). Piloto na Spartan UK: modelagem indica **até 10% de redução de CO2**, **sujeito a validação** (sem resultado medido publicado) | https://www.imperial.ac.uk/news/265233/ai-startup-deepmeta-shortlisted-million-manchester/ e https://spartan.metinvestholding.com/en-us/news/spartan-uk-pilots-ai-technology-to-cut-emissions-and-energy-use/ |
| 3 | **Carbon Re** (Reino Unido) | IA por aprendizado por reforço profundo para forno de cimento, em cima do controle ABB existente; sem hardware novo; "Delta Zero Steel" em desenvolvimento | Piloto Heidelberg Materials (Mokra, Rep. Tcheca): **-4,1% de custo de combustível** e ~-2% de emissões no 1º mês; estimativa da empresa ~5% de emissões de combustível/ano. É cimento, não aço: prova a abordagem, não o setor | https://www.enterprise.cam.ac.uk/news/heidelberg-materials-adopts-carbon-res-ai-and-abb-ability-for-improved-kiln-operations/ |
| 4 | **Smart Steel Technologies x ArcelorMittal Duisburg** (Alemanha) | Software "SST Temperature Optimization AI" contratado pela ArcelorMittal | Só confirmei a contratação (via busca), **sem número de ganho lido** | https://eurometal.net/ai-solution-to-reduce-arcelormittal-duisburg-costs/ |
| 5 | **Imubit** (EUA) | Otimização em malha fechada por aprendizado por reforço para fornos | Apenas texto de produto, sem número verificado | https://imubit.com |

Não achei **hackathon** premiando exatamente "IA de setpoints para siderurgia com ganho por tonelada medido". A validação mais próxima de competição é a Deep.Meta (item 2). Números de blogs de fornecedor (ex.: oxmaint.com "5-12%", "18-25%") **foram descartados** por não terem fonte primária.

## 4. Adaptação ao Pecém
- **[PREMISSA]** Pecém é siderúrgica de placas (sem laminação a quente, a confirmar), então o forno de reaquecimento do Belval não existe 1:1. Alvos equivalentes: **sinterização, coqueria, alto-forno (ar quente/estufas), conversor, e o balanço de gases da termelétrica de 218 MW** (gás de processo é combustível; cada GJ poupado pode virar excedente vendido).
- Abordagem em dois níveis: (a) **kWh/t por área** (ventiladores, sopradores, compressores: reduz carga elétrica, ligado a dados de GRI 302); (b) **GJ/t térmico** nos processos de combustão.
- Valor de venda: mostrar tudo em R$ e MWh de "excedente adicional", linguagem do CEO do Pecém.
- Critério de compra do grupo (Belval): app simples para operador, mede impacto, ROI < 2 anos. O TonaZero é desenhado para isso.

## 5. Estimativa de ganho (todas as contas abaixo são ESTIMATIVAS)
- Base [DERIVADO]: 1% de consumo elétrico ≈ 12-14 GWh/ano ≈ R$ 2-3 mi/ano.
- Faixa conservadora **[PREMISSA]**: 1-3% do consumo específico nas áreas cobertas, apoiada nos 3% medidos no Belval (1 site, forno de reaquecimento) e nos 4,1% de combustível da Carbon Re (cimento, 1 mês). Não é garantia de transferência para outro processo.
- Cenário: cobrindo ~30% do consumo e ganhando 3% nessa fatia => ~0,9% do total => **~R$ 1,8-2,7 mi/ano** e ~11-13 GWh/ano. Parte térmica (GJ) não está contabilizada aqui.
- CO2 [ESTIMATIVA]: 12 GWh x 46 g/kWh ≈ 550 t CO2/ano (fator baixo por causa do gás de processo; o ganho real depende do que o excedente substitui no SIN).
- Resultados reais exigem medição antes/depois com baseline (feito pela própria ferramenta).

## 6. Monetização
- **SaaS por planta/processo** (assinatura anual) + implantação; ou **shared savings** (% da economia medida), modelo usado no Vanderbijlpark/ArcelorMittal SA (dados/projetos-eficiencia-ja-feitos.md).
- Escalável para outras indústrias do Pecém (cimento, vidro, química, alimentos) e para as unidades do Grupo.
- Meta de ROI < 2 anos, conforme critério da ArcelorMittal.

## 7. Viabilidade e riscos
- **Dados**: acesso ao historiador/OT, qualidade de sensores, sincronismo de tempo. Maior risco de cronograma real.
- **Segurança e qualidade**: recomendação só dentro de limites; começar em modo conselheiro (sem escrever no PLC). Ciber/OT exige TI/automação da empresa.
- **Confiança do operador**: modelo de caixa preta é rejeitado; mostrar o porquê (explicabilidade, física + ML, como a Deep.Meta).
- **Concorrência**: Energiency, Imubit, Smart Steel Technologies e integradores já atuam; nosso diferencial é o foco local, custo menor e o traduzir em R$/excedente.
- **Transferência de resultados**: ganhos de outros processos/plantas podem não valer no Pecém.

## 8. MVP em hackathon (5 dias, 3-5 alunos)
- **Dia 1**: escolher 1 processo e definir baseline; gerar dados sintéticos realistas (ou usar dataset público, ex.: consumo de energia industrial) e declarar que são simulados.
- **Dia 2**: modelo de consumo específico esperado (gradient boosting + regras físicas), com validação cruzada temporal.
- **Dia 3**: detector de desvio + recomendador de setpoint com restrições (otimização simples, busca em grade/Bayesiana) sobre o modelo.
- **Dia 4**: app web (Streamlit/React) com painel do operador: kWh/t real x esperado, ação sugerida, ganho em R$ e CO2, botão "apliquei".
- **Dia 5**: simulação antes/depois, pitch com os números do Pecém (500 kWh/t, 1% = R$ 2-3 mi) e plano de piloto de 90 dias.
- Papéis: dados/ML (2), backend/integração (1), front/UX operador (1), negócio/pitch (1).

## 9. Perguntas a validar (mentores)
1. Quais processos do Pecém consomem mais kWh/t e GJ/t, e existe laminação a quente ou reaquecimento?
2. Que dados o historiador (PIMS) exporta e com que frequência? Dá para um recorte anonimizado para o hackathon?
3. Há metas de kWh/t por área hoje e como são medidas (baseline)?
4. Quais setpoints o operador pode mudar sem gerar risco de qualidade/segurança?
5. Já usam IA de terceiros (Energiency, Smart Steel Technologies) em outra unidade do grupo? Podem ser parceiros?
6. Qual o valor de MWh/GJ de gás de processo excedente para o cálculo de ROI?
7. Qual o processo de piloto/compra via Açolab/iNO.VC e prazo típico?
