# Mapa de exemplo: ArcelorMittal Pecém (CSP)

> 29/10/2026. Base para desenhar o mapa da unidade no protótipo.
> **Não achei planta/layout oficial publicado.** O EIA/RIMA da CSP está na Semace, mas só em partes e algumas só na biblioteca física. A GEM Wiki só traz equipamentos e a área (571 ha). O que existe aberto é o **OpenStreetMap (OSM)**, onde a usina está mapeada como "CSP – Companhia Siderúrgica do Pecém" (way 299910787).
> Dados © OpenStreetMap contributors, licença ODbL. Ao usar a imagem no pitch/protótipo, manter a linha de crédito "© OpenStreetMap contributors".

## Arquivos
| Arquivo | O que é |
|---|---|
| `csp_osm.png` / `.svg` | Desenho só com o que está no OSM: limite do terreno, ~110 prédios, vias internas, ferrovia interna, correia tubular de carvão vinda do porto, portaria, subestações e chaminés. Escala de 500 m |
| `csp_zonas.png` / `.svg` | O mesmo desenho com as **áreas da usina sobrepostas** (contorno laranja tracejado). As marcadas com `*` são **inferidas** |
| `csp_osm_dados.json` | Dados brutos do OSM (Overpass API, 29/10/2026) |
| `render_osm.py` | Script que gera os desenhos: `python3 -I render_osm.py csp_osm_dados.json saida.svg [zonas]` |

## O que é confirmado e o que é inferido
| Elemento | Situação |
|---|---|
| Limite do terreno, prédios, vias, ferrovia | **OSM** (o OSM está incompleto: faltam vários prédios grandes que existem na usina) |
| Alto-Forno 1 (100 m de altura) | **OSM**, com nome |
| Portaria da CSP, Portaria ZPE | **OSM** |
| Subestação UTE CSP e Subestação Pecém (Enel) | **OSM** |
| Correia tubular fechada (carvão), entrando pelo norte | **OSM** |
| Pátio de Matérias-Primas (o grande retângulo vazio ao norte, onde chega a correia do porto) | **Inferido** |
| Sinterização e Coqueria (entre o pátio e o alto-forno; prédios longos e finos parecem baterias de coque) | **Inferido** |
| Termelétrica/Utilidades (ao lado da Subestação UTE CSP, com chaminé) | **Inferido** |
| Aciaria + Lingotamento (o maior prédio, ao sul, para onde vai a ferrovia que sai do alto-forno) | **Inferido** |
| Pátio de Placas (galpão ao sul-leste) | **Inferido** |

As inferências seguem o fluxo de uma usina integrada (pátio → sínter/coqueria → alto-forno → aciaria/lingotamento → placas) e a posição dos elementos confirmados. Para o protótipo serve; **para o pitch, dizer "layout ilustrativo baseado em dados abertos"** e, se possível, pedir o arranjo real no Ideathon.

## Como usar no protótipo
- Usar `csp_zonas.png` como **imagem de fundo** do mapa da unidade Pecém (o app já prevê fundo opcional), ou redesenhar as áreas como formas por cima.
- **Pontos de referência** sugeridos: Portaria da CSP (OSM), Sala de Controle do Alto-Forno, Oficina Central, Portaria ZPE.
- **Caminhos para a rota:** seguir as vias internas do OSM (linhas claras); a rua leste-oeste que passa ao norte do alto-forno e a via que desce para a aciaria são bons eixos.
- Escala real: o desenho tem ~3,4 km × 5,1 km (1.400 px de largura ≈ 2,4 m por pixel). No Claude Design, dá para ajustar o `metersPerCell` do mapa para bater com isso.

## Fontes
- OpenStreetMap, way 299910787 e elementos dentro dele (consulta Overpass de 29/10/2026): https://www.openstreetmap.org/way/299910787
- Semace, página do EIA/RIMA da CSP: https://www.semace.ce.gov.br/2012/10/11/companhia-siderurgica-do-pecem-2/
- GEM Wiki, ArcelorMittal Pecém steel plant: https://www.gem.wiki/ArcelorMittal_Pec%C3%A9m_steel_plant
- CEPAL (2020), caso CSP (layout preparado para a 2ª fase): https://archivo.cepal.org/pdfs/bigpushambiental/Caso19-CSPCeara.pdf
