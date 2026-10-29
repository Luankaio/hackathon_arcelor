# 05 - SolMatch Pecém: despacho inteligente de cargas flexíveis + bateria + energia renovável contratada

> Tema: fontes renováveis, armazenamento, mercado livre/PPA e cargas flexíveis. Tudo que for número é [ESTIMATIVA] salvo indicação. Contexto da planta: `dados/00-indice.md` e `dados/RANKING-DADOS-POR-IMPORTANCIA.md`.

## Problema
- O Pecém gera ~1.367 GWh/ano (gases do processo) e consome quase tudo; o excedente vendido é estreito. Logo, "kWh poupado = kWh vendido" (CEO, 2024).
- O Ceará tem solar e vento baratos, mas intermitentes (vento forte à noite, sol ao meio-dia). O PLD do Nordeste oscila por hora e há curtailment (corte) de renováveis no NE.
- Hoje cargas que podem esperar (bombeamento de água, ar de baixa pressão, sopradores, britagem/moagem de insumos, carregamento de empilhadeiras e frota elétrica, futura eletrólise) funcionam sem olhar o preço nem a oferta renovável hora a hora.
- A empresa mira aço verde (CEO: solar/eólica + H2V do hub do Pecém) e vai precisar provar "energia renovável hora a hora", não só em média anual.

## Solução
**SolMatch Pecém**: um software (com medidores IoT baratos) que decide, a cada hora, quando ligar cargas flexíveis e quando carregar/descarregar uma bateria (ou o autoconsumo da TRT/termelétrica) para consumir mais nas horas de energia renovável barata e menos nas horas caras/sujas, sem tocar na produção de placas.

### Como funciona
1. **Dados**: medidores/CLPs de cargas candidatas (potência, estado), curva de PLD/CCEE por hora, previsão de sol/vento (INMET, Open-Meteo, ONS), contrato de PPA (curva de energia contratada) e, se houver, estado de carga da bateria.
2. **Modelo**: previsão de 24-48 h (gradient boosting/LSTM simples) + otimização linear mista (MILP, ex.: PuLP/OR-Tools) que minimiza custo e maximiza o "casamento hora a hora" com a energia renovável, respeitando restrições de processo (janelas mínimas, tanques-pulmão, tempo máximo parado).
3. **Ação**: o operador vê no app/web uma agenda sugerida ("ligar bomba B3 entre 11h e 14h; adiar sopragem para 21h") com ganho em R$ e kgCO2; fase 2 envia setpoint ao SCADA/CLP apenas com aprovação.
4. **Medição e verificação**: compara custo real x linha de base (sem otimização), no mesmo padrão "app fácil + medir impacto + ROI < 2 anos" que a ArcelorMittal cobrou em Belval.
5. **Relatório de PPA hora a hora**: % de consumo coberto por geração contratada (base para certificado 24/7 e aço verde).

## Referências validadas
Nenhuma é uma "solução idêntica" à nossa; cada uma valida uma peça. Não achei vencedor de hackathon específico para indústria siderúrgica.

| Nome / país | O que faz (verificado nas páginas) | Peça que valida | URL |
|---|---|---|---|
| GridBeyond / Irlanda (origem; opera em UK, EUA, Austrália, Japão) | Plataforma que monetiza cargas flexíveis de fábricas, baterias financiadas no cliente, microgrid + solar, FlexPilot (otimizador de processo), PPA e hedge. Alega 1.500+ sites e 4+ GW de carga gerida | Produto completo: carga flexível + bateria em indústria | https://gridbeyond.com |
| FlexiDAO / Espanha (Barcelona) | Operação de energia limpa para compradores: monitora performance de PPA virtual, contabilidade Scope 2 horária; clientes: Google, Microsoft, P&G, Danone | Casamento hora a hora e prova de renovável | https://www.flexidao.com |
| Pexapark / Europa | Plataforma de preços e benchmarks de PPA e de bateria; 250+ empresas de energia (Iberdrola, Shell, TotalEnergies...). Sede não confirmada na página | Precificar PPA/armazenamento | https://pexapark.com |
| MIT Energy Hack (EUA), 1º lugar 2021 "Feeling AMPowered" | Estudantes criaram usina virtual para a Smartflower (solar), 1º lugar US$ 2.000; 2º lugar "Crown Joules": microgrid solar + bateria para ChargePoint | Hackathon premia solar + armazenamento + software | https://trienens-institute.northwestern.edu/news-events/news/2021/northwestern-energy-and-sustainability-graduate-students-win-mit-energy-hack.html |
| MIT Energy and Climate Hackathon (EUA), time Harvard/MIT | Ferramenta de otimização linear para decidir bateria em planta renovável da Avangrid; estimaram >= US$ 200 mil/ano de economia. A fonte não diz que ficaram em 1º | Mesmo método (otimização linear) | https://mccormick.northwestern.edu/engineering-management/inside-our-program/stories/2025/seeing-mem-in-a-more-holistic-way.html (só trecho de busca, página não aberta) |
| Hub H2V Pecém (Fortescue, ZPE Ceará), Brasil | Projeto de 1,2 GW renovável para ~500 t H2/dia, autorizado na ZPE; CEO da ArcelorMittal Pecém disse que comprará H2 verde do hub | Contexto local e futura carga flexível (eletrolisador) | https://eixos.com.br/hidrogenio/projeto-de-hidrogenio-da-fortescue-recebe-autorizacao-para-se-instalar-na-zpe-do-ceara/ ; https://diariodonordeste.verdesmares.com.br/opiniao/colunistas/egidio-serpa/hidrogenio-verde-do-pecem-ja-tem-comprador-a-arcelormittal-1.3435177 |

Observação: o caso Avangrid (linha 5) veio só de trecho de busca; confirmar antes de citar no pitch. Um estudo acadêmico (arXiv 2606.24183) trata eletrolisador e planta de aço como cargas flexíveis em mercado, mas é pesquisa, não produto.

## Adaptação ao Pecém
- **Cargas candidatas** (a confirmar com mentores): estação de bombeamento/água industrial, ventiladores e sopradores com VSD, moagem/preparo de insumos com silo-pulmão, compressores de baixa criticidade, carregadores de frota, usina de oxigênio com tanque criogênico (carga clássica de deslocamento).
- **Alvo não é o forno/laminador**: criticidade alta; manter fora do escopo.
- **Termelétrica própria**: pode servir de "bateria" (reduzir geração/consumir mais renovável quando o PLD está baixo e vender quando alto), o que exige validar com a operação.
- **Renovável**: usa PPA/contrato do mercado livre (ou solar de autoprodução) como curva de referência; o relatório hora a hora serve ao projeto de aço verde.
- **Fator de CO2**: usar 46 gCO2/kWh da ArcelorMittal Brasil; o ganho de CO2 é pequeno se a rede já é limpa, então o argumento principal é custo e comprovação hora a hora.

## Estimativa de ganho [ESTIMATIVAS, não confirmadas]
Premissas: 10 MW de carga flexível identificada (~2% do consumo de ~150 MW); deslocamento de 30% dessa energia (~26 GWh/ano) para horas com diferença média de R$ 60/MWh entre pico e vale; custo médio de referência R$ 180-250/MWh (dados/precos-e-tarifas.md).
- Economia por arbitragem: 26 GWh x R$ 60 = ~R$ 1,6 mi/ano.
- Bateria opcional 5 MW/10 MWh: ~1 ciclo/dia x 365 x 10 MWh x R$ 80/MWh de spread = ~R$ 0,3 mi/ano (não paga o capex sozinha; só faz sentido com serviços de rede ou evitar demanda de ponta).
- Evitar curtailment/ganho de "casamento" PPA: depende do contrato; não quantificado.
- Faixa realista para o piloto: R$ 0,5-2 mi/ano; comparável a ~0,3-1% de eficiência (cada 1% = R$ 2-3 mi/ano).

## Monetização
- SaaS por MW de carga gerenciada (ex.: R$ 5-10 mil/MW/mês) ou **shared savings** (20-30% da economia verificada), modelo que a ArcelorMittal já usou em Vanderbijlpark.
- Receita adicional: relatório hora a hora (certificação 24/7) e venda para outras indústrias do Complexo do Pecém e comercializadoras do mercado livre.

## Viabilidade e riscos
- Dados de carga e SCADA de acesso restrito; começar só com medição e recomendação (sem comando).
- Spread horário no Brasil é menor que na Europa; se o PLD do NE estiver achatado, o ganho cai. Comparar com a solução 02 (HoraCerta/PLD) para não duplicar escopo.
- Bateria tem capex alto e regulação (ANEEL) ainda em evolução; tratar como módulo opcional.
- Processo siderúrgico tem restrições de qualidade e segurança; qualquer carga precisa de aval da operação.
- Sobreposição parcial com demanda/PLD (solução 02): diferenciar pelo foco em renovável hora a hora e cargas flexíveis novas (H2V).

## MVP em hackathon (5 dias, 3-5 alunos)
- Dia 1: levantar dados públicos (PLD horário CCEE, geração solar/eólica NE do ONS, previsão Open-Meteo) e montar 5 cargas sintéticas com restrições realistas.
- Dia 2: modelo de previsão simples + otimizador MILP (Python/PuLP).
- Dia 3: dashboard web (Streamlit/React) com agenda sugerida, R$ economizados e % hora a hora coberto por renovável.
- Dia 4: simulação de 30 dias históricos comparando linha de base x otimizado; simulador de bateria opcional.
- Dia 5: pitch com 1 demo ao vivo, números marcados como estimativa e roteiro de piloto de 30 dias com 1 carga real.
- Papéis: dados/IA, otimização, front-end, negócio/pitch, (opcional) hardware com medidor ESP32 + sensor de corrente.

## Perguntas a validar com mentores da ArcelorMittal
1. Quais cargas do Pecém toleram deslocamento de 2-6 h e já têm tanque/silo-pulmão?
2. A energia comprada/contratada tem curva horária? Há PPA, autoprodução ou apenas PLD/ACL?
3. A termelétrica pode modular geração para acompanhar o preço sem perder a operação do processo?
4. Qual o valor interno do MWh excedente e o preço intragrupo?
5. Existe interesse em comprovar energia renovável hora a hora (aço verde) e para qual cliente?
6. Permissão para acessar dados de medição (sem comando) em piloto?
7. O hub H2V prevê eletrolisador flexível ligado à planta, e em que prazo?
