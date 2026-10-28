# Lacunas e perguntas prontas para mentores e representantes da ArcelorMittal

> Ordem = importância para metrificar as soluções. Marcar na hora: [OK] respondeu · [FAIXA] deu uma faixa · [X] confidencial.
> Dica: perguntar **faixas** ("é mais perto de 5, 20 ou 50 MW?") aumenta a chance de resposta quando o dado é confidencial.

---

## A. Energia da planta (crítico para as três soluções)
1. **Consumo elétrico interno do Pecém hoje:** "Dos ~1.367 GWh que a termelétrica gerou em 2024, quanto a usina consome e quanto sobra? É mais perto de 5, 20 ou 50 MW médios de excedente?" (Público: geração de 1.367 GWh em 2024; consumo de 138 MW em 2017 e 168 MW por volta de 2019–2020.)
2. **Valor do MWh poupado:** "Para vocês, 1 MWh economizado vale quanto: o PLD, o preço do contrato de venda, ou o preço de transferência para outras unidades do grupo? Uma faixa basta (R$ 150, 250 ou 400?)."
3. **Para onde vai o excedente hoje:** SIN (CCEE, curto prazo), contrato bilateral ou intragrupo (Vega, aços longos)? Qual a proporção?
4. **Horas de importação:** "Quantas horas por ano a usina compra energia (geração abaixo do consumo)? Quanto custa uma hora dessas?"
5. **Quebra do consumo elétrico por área:** sínter, alto-forno/sopradores, aciaria, lingotamento, utilidades (ar, água, bombas), correias/porto, coqueria.
6. **Existe medição por área ou por equipamento?** Qual o sistema (PI, historian, EMS, SCADA)? Dá para exportar CSV de 15 min?
7. **ISO 50001:** o Pecém tem ou planeja? Quem é o dono do Plano Diretor de energia no Pecém?

## B. Equipamentos (para calibrar as soluções 01 e 03)
8. **Ar comprimido:** quantas centrais e compressores, potência total (kW), tipo (parafuso ou centrífugo), controle (carga/alívio, VSD), pressão de rede (6 ou 7 bar?), há medidor de vazão e de energia, horímetros de carga/alívio?
9. "O ar comprimido do Pecém é gerado por vocês ou por terceiros (White Martins/Linde)?" (O RS 2024 da ArcelorMittal Brasil reporta 845.705 GJ de ar comprimido, ≈ 837 milhões de m³/ano no Brasil.)
10. **Existe programa de caça a vazamentos?** Frequência, ferramenta (ultrassom?), último percentual de vazamento medido.
11. **Motores acima de 100 kW sem medição individual** em utilidades: bombas de água de resfriamento, exaustores de despoeiramento, ventiladores de sínter, correias.
12. **Bombas redundantes:** há sistemas com 2 bombas rodando onde 1 bastaria (como no caso "Power of 1")? Há bombas em bypass ou recirculação longa (como em Vanderbijlpark)?
13. **Correias:** a correia até o porto e as de pátio ficam rodando vazias? Há controle de velocidade?
14. Sopradores do alto-forno: motor elétrico ou turbina a vapor?
15. O oxigênio vem da White Martins ou de planta própria? (O escopo ResponsibleSteel 2026 cita "gas plant for O2, argon".)
16. Unidades da termelétrica: a unidade de 18 MW é a TRT?

## C. Operação, compra e regras (viabilidade e monetização)
17. **Quem seria o dono de um piloto** (Gerência de Energia/Utilidades, Manutenção, Digital/iNO.VC)? Qual o caminho de contratação de startup no Pecém (Açolab, iNO.VC, Habitat FIEC)?
18. **Critério de payback para projetos de eficiência:** é o "ROI menor que 2 anos" de Belval? Há valor mínimo?
19. **TI/OT:** é permitido sensor de terceiros com 4G/LoRa isolado da rede de automação? Precisa de homologação?
20. **NR-10 e permissão de trabalho:** quem instala medidor em CCM (eletricista da planta)?
21. **Shared savings:** a ArcelorMittal Brasil aceita contratos de economia compartilhada (como em Vanderbijlpark)?
22. Paradas programadas: quando é a próxima (para teste de vazamento CAC/DOE e linha de base)?
23. Quais dos **"12 projetos de eficiência energética (R$ 63 mi/ano)"** do RS 2024 estão no Pecém? Algum em ar comprimido ou motores?
24. O **laminador de tiras a quente** (decisão no fim de 2026): já há estimativa de demanda elétrica? Isso muda o excedente?

## D. Linguagem e métricas (para o pitch)
25. "Qual indicador vocês usam no dia a dia: kWh/t de placa, MW médios de excedente, GJ/t, R$?" Usar a mesma unidade no slide.
26. "Qual fator de CO₂ vocês usam para a energia: os 46 g/kWh do inventário 2024 ou o fator do Grupo (52,8)?"
27. "O que já tentaram em eficiência elétrica que **não** deu certo, e por quê?"

---

## Lacunas que a pesquisa **não** conseguiu fechar (registro)
| Lacuna | Onde procuramos | Resultado |
|---|---|---|
| Consumo elétrico atual e excedente do Pecém | RS 2024 (sem quebra por unidade), imprensa 2024–2026, ABM, CEPAL | Só dados de 2017 e ~2020 |
| Preço de venda/transferência do excedente | Imprensa, CCEE (bloqueado), ANEEL | Não público |
| Demonstrações financeiras da ArcelorMittal Pecém S.A. com nota de receita de energia | Busca, Central de Balanços | Não localizadas |
| Equipamentos de utilidades do Pecém | ABM, GEM, POSCO E&C, fornecedores | Nada público |
| ISO 50001 no Pecém | Certificados ArcelorMittal Brasil, GEM | Não encontrada |
| RS 2025 da ArcelorMittal Brasil (PDF) | Site oficial (página dinâmica; padrão de URL antigo dá 404) | Só notícias com destaques |
| Texto completo dos artigos ABM do Pecém | ABM Proceedings (download exige login) | Só resumos |
| PLD horário e médias 2026 oficiais | CCEE (HTTP 403 para robôs) | Fontes secundárias |
| Fator oficial do SIN 2025 anual | MCTI/SIRENE | Não localizado; usar o da empresa |
