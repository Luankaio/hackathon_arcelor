# Protótipo do Claude Design × documento da solução

> 29/10/2026. Protótipo do Luan: `Monitoramento.dc.html` no projeto "Monitoramento de máquinas industriais" do Claude Design (https://claude.ai/design/p/22b249b9-c4bc-432b-98e8-f7bb340800c9). Visto pelo Chrome; nada foi alterado nem salvo lá.
> Atenção: o Claude Design standalone fecha em **14/12/2026** (aviso na própria página); vale exportar ou migrar para Artifacts antes disso.
> Comparação com `solucao.md`.

## O que o protótipo já tem
Celular, tema claro, dados simulados ao vivo de uma siderúrgica (setores tipo Pecém). Barra inferior com 3 abas: **Painel**, **Mapa** e **Dispositivos**.

| Tela | Conteúdo |
|---|---|
| **Painel** | Cabeçalho "Pecém · Turno B · hora"; demanda total da usina (MW) com gráfico; contadores Críticos / Atenção / Normais; **Alertas ativos** (pico de energia, queda de tensão, consumo acima do normal) com "Localizar no mapa" e "Detalhes"; lista de máquinas com status, mini-gráfico e kW (filtro Todas / Com alerta) |
| **Detalhe da máquina** | Status (ex.: Crítico); potência agora com gráfico (alterna Potência/Tensão), linha de limite, janela "últimos 48 s"; tensão (com mínimo), corrente por fase, consumo hoje vs. limite diário; ocorrências ativas; ficha (fabricante/modelo, setor, responsável, sensor, limite de pico); "Assumir chamado" e "Localizar no mapa" |
| **Mapa** | Grade fixa de 6 setores (Alto-Forno, Aciaria, Lingotamento, Laminação, Utilidades, Subestação), corredor central e ruas A/B/C; chips das máquinas em falha; máquina crítica pulsa em vermelho; **rota a partir da Portaria** desenhada no mapa, com passos, distância e tempo a pé (ex.: 180 m, ~3 min) |
| **Dispositivos** | "6 gateways IoT online"; sensores detectados e ainda sem máquina (medidor trifásico, sensor de corrente), com gateway, setor, leitura ao vivo e sinal; "Procurar", "Cadastrar máquina", "Ignorar" |
| **Cadastro (2 etapas)** | 1) nome, tipo (motor, bomba, compressor, ventilador, ponte rolante, prensa, forno, transformador), fabricante, modelo, setor (pré-selecionado pelo gateway), limites (pico kW, tensão mínima, consumo diário) **sugeridos a partir da leitura do sensor**, responsável (pessoa); 2) posição no mapa |

**O que o protótipo traz e o documento não tinha:** a tela de **Dispositivos**, em que o sensor aparece na rede e vira máquina com limites sugeridos. Vou levar isso para o `solucao.md` (§5.1).

## O que falta no protótipo (pelo `solucao.md`)
Ordem: do mais importante para o menos.

| # | Falta | No documento | Sugestão para o protótipo |
|---|---|---|---|
| 1 | **Times, funcionários, cargos, turno e gestor** | §5.4 e §5.5 | Nova aba "Equipe" (ou dentro de Perfil): lista de times, membros com cargo e turno, gestor de cada time |
| 2 | **Responsável = time ou cargo** (hoje é uma pessoa) | §5.1 e §5.5 | No cadastro, escolher "Time" ou "Cargo" no lugar de uma pessoa, e o gestor responsável |
| 3 | **Fluxo do chamado** | §5.5 | Aba ou caixa "Chamados" com Abertos / Meus / Resolvidos; "Pegar chamado" → "Pego por X às 14:07"; ao resolver, escolher a causa; selo de escalado para o gestor; aviso dentro do app (já existe um contador na aba Painel, falta a caixa) |
| 4 | **Editor do mapa** (hoje a grade é fixa) | §5.6 | Modo "Editar mapa": desenhar linhas e formas, criar áreas e sub-áreas, **arrastar máquinas**, criar **pontos de referência** e desenhar os caminhos |
| 5 | **Cinza para parada** e estado "sem sinal" | §5.2 | Hoje só há Crítico (vermelho), Atenção (amarelo) e Normal (verde). Falta Parada (cinza) e Sem sinal (cinza tracejado) na lista, no mapa e nos contadores |
| 6 | **Escolher o ponto de partida da rota** (hoje é sempre a Portaria) | §5.7 | Seletor "Saindo de: Portaria ▾" com os pontos de referência criados no mapa |
| 7 | **Dados nominais e potência esperada** no cadastro | §5.1 | Campos de tensão, corrente, potência e FP nominais, potência média esperada e faixa normal, horário de operação e criticidade |
| 8 | **Um gráfico por métrica e períodos** | §5.3 | Hoje: potência/tensão, últimos 48 s. Acrescentar corrente por fase, FP, kWh e Hz; períodos ao vivo / 1 h / 24 h / 7 d / 30 d; faixa esperada sombreada |
| 9 | **Regras de sobreuso com tempo mínimo** | §6 | Hoje o alerta é por limite fixo (pico kW, tensão mínima, consumo diário). Faltam: sobreuso vs. esperado por X min, parada inesperada, ligada fora de horário, desbalanço, FP baixo e sem sinal |
| 10 | **Energia gasta acima do esperado (kWh e R$)** | §5.3 | Um cartão no detalhe e um total no painel: é o número que mostra o desperdício |

## Detalhe para ajustar
- AC-02 mostra tensão de 6.566 V (média tensão) e LC-02 mostra 400 V. As duas fazem sentido na usina, mas vale exibir a tensão nominal junto ("6,6 kV nominal") para não parecer erro.
