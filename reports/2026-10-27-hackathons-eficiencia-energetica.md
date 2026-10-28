# Hackathons vencedores em eficiência energética — referências para o desafio 8

Pesquisa de 27/10/2026. Foco: o que construíram, como, e métricas. **Aviso:** a imprensa quase nunca publica métricas de economia; onde não achei número, está escrito "não informado". Nada foi inventado.

---

## 0. O hackathon anterior da ArcelorMittal (confirmado: 1º e 2º lugar foram energia)

**1ª Trilha da Inovação — Sebrae/CE + ArcelorMittal Pecém, outubro/2025.** É o mesmo formato do edital atual (Ideathons em Pecém, Paracuru e Caucaia, depois Hackathon em 18–19/10/2025).

Números do evento: 225 inscritos · 18 times formados nos Ideathons · 11 finalistas · R$ 12 mil em prêmios.

| Colocação | Time | Prêmio | O que propôs | Tema |
|---|---|---|---|---|
| 1º | **WeVoltz** (7 integrantes) | R$ 5 mil | Monitoramento inteligente de energia para reduzir desperdícios e custos. Sensores + inteligência artificial + plataforma online que identifica onde ocorre a falha. | Energia / redução de custos |
| 2º | **Enerlize** (4 integrantes) | R$ 4 mil | Monitoramento inteligente do consumo de energia industrial. | Eficiência energética |
| 3º | Tecseg Industrial (4 integrantes) | R$ 3 mil | Sensores + câmeras térmicas + pulseiras de monitoramento. | Segurança do trabalho |

- Métricas de economia: **não informado.** Só há o descritivo acima, sem arquitetura, sem percentuais.
- Detalhe importante: as duas equipes de topo fizeram **o mesmo conceito** (monitoramento de consumo com sensores + IA). Isso sinaliza o que a banca (Sebrae + ArcelorMittal) premia — e também que a ideia "genérica" já foi usada. Para se diferenciar, é preciso um ângulo específico (ver seção final).
- Fontes: [SGA Notícias, 10/2025](https://www.sganoticias.com.br/2025/10/arcelormittal-sebraece-e-ifces-premiam.html) · [Sebrae/CE, lançamento 2026](https://ce.agenciasebrae.com.br/inovacao-e-tecnologia/sebrae-ce-e-arcelormittal-lancam-trilha-da-inovacao-para-400-estudantes-do-ifce/). A página da AECIPP sobre o mesmo evento retornou 404.
- Observação: o "Hackathon Ideia Voluntária" da ArcelorMittal (setembro/2024) era de projetos sociais, sem relação com energia ([SGA Notícias](https://www.sganoticias.com.br/2024/09/hackathon-da-arcelormittal-premiou.html)).

---

## 1. NexoWatt — Hackathon Insted (Campo Grande/MS, Brasil)

- **Desafio:** produtividade e eficiência energética, com parceiros Dale Sorvetes e BEM Inteligência de Dados. ~70 alunos de Análise e Desenvolvimento de Sistemas.
- **O que construíram:** monitoramento em tempo real de uma **câmara fria industrial**: compressores e abertura de portas.
- **Como:** sensoriamento + IA + análise de dados. Usa cálculos de termodinâmica para converter consumo de energia em **gasto real em reais** e aponta falhas operacionais ("uma porta aberta gera prejuízo alto").
- **Prêmio:** R$ 3 mil + disputa por vaga de estágio na BEM.
- **Métricas:** não informado.
- **Lição:** traduzir kWh em R$ e ligar o consumo a um **evento operacional concreto** (porta aberta) torna a ideia tangível para a banca.
- Fontes: [A Crítica](https://acritica.net/educacao/hackathon-do-insted-premia-projeto-de-eficiencia-energetica-para-a-industria/) · [Diário Digital](https://www.diariodigital.com.br/geral/hackathon-no-insted-conecta-academicos-ao-mercado-de-trabalho-na-capital)

## 2. Solução de refrigeração de cremas e sopas (time AIRE) — Hackathon ESG València (Espanha)

- **Desafio:** da empresa La Línea Verde (DimmidiSì): otimizar o resfriamento na produção de cremas e sopas (fase com impacto em energia, tempo e sustentabilidade). Organização: Innova&acción / Fundación Politécnica de la Comunitat Valenciana.
- **O que construíram:** proposta técnica de resfriamento (mecanismo **não detalhado** na matéria).
- **Métrica:** reduz **até 80% do tempo de resfriamento** (meta inicial era 50%). Atenção: o título da matéria fala em "80% de consumo energético", mas o corpo do texto só comprova **tempo**; economia de energia não está demonstrada.
- **Lição:** meta inicial clara (50%) e resultado que a supera (80%) é uma ótima narrativa de pitch.
- Fonte: [Valencia Plaza](https://valenciaplaza.com/valenciaplaza/tierra-de-empresas/una-solucion-que-reduce-un-80-el-consumo-energetico-y-optimiza-costes-industriales-gana-el-hackathon-esg-valencia)

## 3. Monitoramento de contêineres refrigerados (reefers) — Valenciaport Hackathon, 5ª edição (Espanha, 2025)

- **O que construíram:** dispositivo **IoT de baixo custo** que mede o consumo de cada contêiner reefer + sistema que decide **quando ligar/desligar** os contêineres.
- **Como:** princípios de termodinâmica + análise de grande volume de dados; detecta anomalias; painel de controle com o estado de todos os equipamentos.
- **Evento:** 9–11/05/2025, 45 participantes em 9 equipes, organizado pela Opentop; prêmio de €3.000.
- **Métricas:** não informado.
- **Lição:** hardware barato + otimização de liga/desliga + painel é um pacote completo e demonstrável.
- Fonte: [Diario El Canal](https://www.diarioelcanal.com/una-solucion-que-monitoriza-el-consumo-energetico-de-reefers-se-lleva-el-valenciaport-hackathon/)

## 4. Predicta (time Atanora) — Hackathon IA 2026, COPPE/UFRJ (Rio de Janeiro)

- **O que construíram:** IA que **antecipa picos de demanda** de energia e indica os horários de consumo mais barato/eficiente; sugere **tarifas dinâmicas**.
- **Benefício declarado:** alivia a rede para as distribuidoras e reduz a conta do consumidor.
- **Time:** 5 estudantes (UFRJ, UFF, UERJ, Cefet/RJ). Prêmio: R$ 10 mil + US$ 10 mil em créditos AWS + 2 semanas no supercomputador Santos Dumont (LNCC).
- **Outros colocados:** CapiWatt (2º; IA que organiza processos regulatórios da ANEEL) e GPU Team (3º; usa dados do ONS para achar gargalos de transmissão e recuperar energia eólica/solar desperdiçada).
- **Métricas:** não informado; a matéria não descreve a arquitetura.
- Fontes: [UFRJ/CT](https://ct.ufrj.br/hackathon-ia-2026-transforma-desafios-reais-da-energia-em-solucoes-tecnologicas/) · [Brasil em Folhas](https://www.brasilemfolhas.com.br/2026/10/hackathon-no-rio-premia-solucoes-de-ia-para-transicao-energetica/)

## 5. Wall-Energy — Hackathon Viewnext, Universidade de Salamanca (Espanha, 2026)

- **O que construíram:** app com **agentes de IA** que otimizam em tempo real o consumo de energia de **edifícios inteligentes**, com previsões e recomendações.
- **Time:** 5 estudantes. 1º prêmio, organizado pela Viewnext (Cátedra Viewnext-USAL).
- **Métricas e stack:** não informado.
- Fontes: [El Diario de Salamanca](https://eldiariodesalamanca.com/usal/2026/05/15/ganadora-del-hackathon-app-para-mejorar-la-eficiencia-energetica/) · [Facultad de Ciencias USAL](https://fciencias.usal.es/en/ganadora-del-hackathon-de-viewnext-app-wall-energy-para-mejorar-la-eficiencia-energetica)

## 6. CooL-LLM (Ooredoo Group) — GCC Sustainability Hackathon 2025, categoria Eficiência Energética

- **O que construíram:** engine baseada em **LLM que prevê a necessidade futura de refrigeração** de data centers, com um modelo menor (SLM) especializado que se adapta a cada instalação.
- **Evento:** hospedado pela stc (GCC ESG Telecommunications Alliance); 310 submissões, 15 finalistas.
- **Métrica:** o release da empresa cita **economia de 20–30%** de energia no data center. É **autodeclarada** (não verifiquei: a página oficial retornou 403) — tratar como não verificada.
- Fonte: [Ooredoo (release)](https://www.ooredoo.com/en/media/news_view/ooredoo-group-wins-first-place-for-ai-driven-energy-efficiency-at-gcc-sustainability-hackathon-2025/)

## 7. "Agents of S.H.I.E.L.D" — Energy Hackathon FSU + NextEra Energy (EUA, 2024)

- **O que construíram:** dispositivo residencial + app com **dados de circuito em tempo real** para o morador acompanhar o consumo e a saúde dos eletrodomésticos.
- **Contexto:** 24 h, 50 estudantes em 10 times, design thinking; pitch de 3 min + 2 min de perguntas, com demo do protótipo. Meta do evento: ajudar moradores da Flórida a reduzir o consumo em **10%**.
- **Outros:** ShadE (2º; persiana adaptável com IA que ajusta por nível de UV) e AEGIS (3º; monitora eletrodomésticos e prevê falhas com IA).
- **Métricas dos projetos:** não informado.
- Fonte: [The Invading Sea](https://www.theinvadingsea.com/2024/11/21/florida-state-university-energy-hackathon-nextera-energy-ai-appliances-electric-vehicles/)

## 8. OptiWatt — Digital Innovators Student AI Hackathon (Guernsey, 2025)

- **O que construíram:** plano de IA para prever e reduzir consumo em escolas e casas, com foco em **"vampire devices"** (aparelhos em standby que consomem energia à toa).
- **Time:** 6 alunos do Year 10, 4 horas de prazo. Métricas: não informado.
- Fonte: [Digital Greenhouse](https://digitalgreenhouse.gg/news/skills-education/students-tackle-energy-efficiency-with-ai-at-2025-hackathon/)

---

## O que se repete nos vencedores

1. **Sensor/IoT barato + painel + IA** aparece em quase todos (WeVoltz, Enerlize, NexoWatt, Valenciaport, FSU).
2. **Caso específico e mensurável** ganha de "monitoramento genérico": câmara fria, reefers, resfriamento de sopa, data center, standby.
3. **Dinheiro na frente:** NexoWatt converte kWh em R$; Predicta fala em tarifa; os critérios da banca no edital incluem monetização e viabilidade.
4. **Meta numérica no pitch** (50% → 80% no caso de València; 10% na Flórida; 20–30% no CooL-LLM) — mesmo sendo só estimativa.
5. Prototipar rápido com hardware simples (ESP32 + sensor de corrente, por exemplo) costuma ser mais convincente do que só slides. *(Sugestão minha, não vem das fontes.)*

## Para o time do Luan (sugestão, não fonte)

Como WeVoltz e Enerlize já ocuparam o "monitoramento de energia industrial" em 2025, vale procurar um ângulo mais específico ligado à realidade de Pecém/ArcelorMittal e dos critérios da banca (problemática, proposta de valor, cliente, receita, viabilidade): por exemplo um nicho de pequenas indústrias/comércios do Complexo do Pecém, ou escolas (o desafio 8 inclui escolas e pequenos negócios), com estimativa de payback.
