# Radar de IA — semana de 16 a 23/11/2026

Resumo da semana em IA, com os insights para levar aos clientes; os insights são leitura editorial do programa, não a posição oficial de nenhuma empresa. Fontes públicas; ressalvas indicadas em cada item.

## Bloco 1 — Visão geral da IA no mundo

- **Anthropic estreia na Nasdaq (Anthropic)**, 19/11: ações vendidas a 83 dólares, acima da faixa inicial de 70 a 78; captação de cerca de 81 bilhões de dólares; abriu a 111,50 e fechou a 97,17; prospecto cita prejuízo líquido de 104 bilhões nos nove primeiros meses de 2026, segundo o relato — [Al Jazeera/Reuters](https://www.aljazeera.com/economy/2026/11/19/anthropic-starts-trading-in-the-us-after-blockbuster-ipo)
- **Resultados da Nvidia e debate sobre financiamento (Nvidia)**, 17 a 22/11: receita de 115,8 bilhões de dólares, alta de 103%, segundo a empresa citada pela Fortune; a coluna do JoongAng Daily sobre financiamento circular é opinião — [Fortune](https://fortune.com/2026/11/22/nvidia-next-ceo-international-business-reorganization-ai-equilibrium/) · [JoongAng Daily](https://www.koreajoongangdaily.com/opinion/global-ai-industry-faces-nvidia-taper-tantrum/12984857)
- **Token mais barato, GPU mais cara (Nvidia)**, 17/11: preço dos tokens caiu quase 60% desde maio e o aluguel de GPUs sobe, segundo a CFO e CEO interina; alegação da empresa, relatada por veículo de terceiros — [Storm Media](https://world.storm.mg/articles/1183013)
- **GPT-6.2 Astra e Sol (OpenAI)**, 17/11 (data via agregadores): Astra a 8 e 40 dólares por milhão de tokens, Sol a 2 e 10; benchmarks são da OpenAI — [OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol)
- **Gemini 4 Neon (Google)**, 18/11: 3 e 15 dólares por milhão de tokens, contexto de 1 milhão; "32% mais barato por tarefa que o Carbon" e rankings são alegações do Google — [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)
- **Gemini no Mac com computer use (Google)**, 19/11: agente clica e digita em apps e sites, com aprovação do usuário; EUA, inglês, planos pagos e Apple Silicon — [Google](https://blog.google/innovation-and-ai/products/gemini-app/computer-use-mac/)

## Bloco 2 — Engenharia de software

- **Nadella diz que o IDE "desbotou" (Microsoft)**, 16/11: opiniões dele em entrevista; recomenda desacoplar harness, memória e modelo — [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes) · [Windows Latest](https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/)
- **VS Code 1.147 (Microsoft)**, 18/11: roteadores de modelo e envio agendado (experimentais), Browser Use em prévia, habilidades via MCP por padrão; harnesses do Claude e do Codex rodam sem os controles gerenciados do Copilot — [Notas da versão](https://code.visualstudio.com/updates/v1_147)

## Bloco 2 — Arquitetura empresarial e governança

- **Entra Agent ID e firewall de MCP (Microsoft)**, 17/11: identidade para agentes, desativação de agentes inativos por 60 dias e firewall de MCP em prévia; anúncios da própria Microsoft — [Microsoft Entra](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/ai-is-changing-access-see-how-microsoft-entra-helps-you-stay-ahead-/4556456)
- **Microsoft e SAP no Ignite (Microsoft)**, 17/11: servidores MCP deixam o Copilot ler e escrever no ERP da SAP; vários itens em prévia limitada — [Microsoft Tech Community](https://techcommunity.microsoft.com/blog/SAPApplications/microsoft-and-sap-at-ignite-2026-connecting-sap-customers-to-ai-agents-data-and-/4573931)
- **Autorização segura entre A2A e MCP (AAIF)**, 19/11: artigo de blog recomenda perfil equivalente ao do MCP, com OAuth 2.1, para o A2A; é recomendação, não norma — [AAIF](https://aaif.io/blog/designing-secure-authorization-across-a2a-and-mcp)
- **Orçamento de IA sem visibilidade (CIO)**, 23/11: artigo de opinião que cita estudos de terceiros (IBM, Deloitte, Cloud Security Alliance), não verificados por nós — [CIO](https://www.cio.com/article/4251456/claude-copilot-and-agentforce-are-ready-are-your-sap-and-servicenow-platforms-ready.html)

## Insights para levar aos clientes

- **Preço de token não é custo de IA:** o token ficou mais barato, segundo a Nvidia, mas a capacidade aluga-se mais cara. Pergunta: o orçamento separa preço unitário, volume e capacidade, e quem revisa quando um muda?
- **Desacople modelo, memória e ferramentas:** Nadella recomenda não ficar preso, e o VS Code já traz roteadores de modelo. Pergunta: se trocássemos de modelo amanhã, o que precisaria ser refeito?
- **Decida quais agentes de código entram e com quais controles:** o VS Code avisa que harnesses externos rodam sem os controles gerenciados do Copilot. Pergunta: quais ferramentas estão liberadas e que regras de permissão e isolamento valem para cada uma?
- **Quando o agente usa o computador, delimite o alcance:** Gemini no Mac e Browser Use dão controle de interface ao agente. Pergunta: quais aplicativos e dados ele pode tocar, e qual ação exige aprovação humana?
- **Agente precisa de identidade, dono e prazo de validade:** a Microsoft lança Agent ID e desativa agentes inativos. Pergunta: quantos agentes existem, quem é dono de cada um e quem os desativa?
- **A fronteira entre sistemas é onde a autorização falha:** agentes do Copilot acessando o SAP e a recomendação de OAuth 2.1 para o A2A. Pergunta: como credenciais e escopo passam de um agente para os sistemas centrais, e onde fica a trilha de auditoria?

## Conceitos explicados no episódio

- **Financiamento circular:** fornecedor que financia ou garante crédito a clientes que depois compram dele.
- **Token:** pedaço de texto que o modelo lê ou escreve; é a unidade de cobrança.
- **Computer use:** o agente opera o computador como uma pessoa, clicando e digitando.
- **IDE:** editor onde o programador escreve código.
- **Harness:** conjunto de ferramentas e controles em volta do modelo que forma o agente de código.
- **Roteador de modelos:** regra que escolhe qual modelo atende cada tarefa, equilibrando custo e qualidade.
- **Agent ID:** identidade própria de um agente, com dono, permissões e auditoria.
- **Firewall de MCP:** filtro que controla quais ferramentas um agente pode chamar pelo MCP.
- **A2A:** padrão para agentes de empresas diferentes se comunicarem.
- **OAuth 2.1 e token:** padrão de autorização; o token deve valer só para o destino previsto.
