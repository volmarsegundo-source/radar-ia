# Radar de IA — semana de 09 a 16/11/2026

Resumo da semana em IA, com os insights para levar aos clientes; os insights são leitura editorial do programa, não a posição oficial de nenhuma empresa. Fontes públicas; ressalvas indicadas em cada item.

## Bloco 1 — Visão geral da IA no mundo

- **Claude Fable 5.2 e Mythos 5.2 (Anthropic)**, 09/11: mesmo modelo base; o Fable é aberto a todos com travas de segurança e o Mythos fica para organizações verificadas; preço de 8 dólares por milhão de tokens de entrada e 40 de saída; benchmarks são da empresa — [Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- **Gemini 4 Carbon disponível para todos (Google)**, 10/11: preço introdutório de 2 e 10 dólares por milhão de tokens até 30/11, depois o dobro; rankings e custos são alegações do Google. O Gemini 4 Hydrogen, de 12/11, aparece só em agregadores; o anúncio original não foi lido — [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) · [Resumo semanal](https://note.com/masahiko_studio/n/nd05750f7c299?hl=en)
- **Roadshow do IPO da Anthropic**, 10/11: faixa de 70 a 78 dólares por ação, até 1,4 trilhão de valor de mercado; receita anualizada perto de 81 bilhões de dólares segundo a emenda ao prospecto (dado da empresa) — [Fortune](https://fortune.com/2026/11/10/anthropic-ipo-price-range-ai-stock-sell-off/)
- **Jensen Huang deixa o cargo de CEO (Nvidia)**, 12/11: saída em meio a investigação sobre relacionamento pessoal; a CBS diz não ter verificado as acusações; Colette Kress é CEO interina — [CBS News](https://www.cbsnews.com/news/nvidia-ceo-jensen-huang-resigns/)
- **Cúpula de IA da União Europeia**, 13/11: sete gigafábricas de IA e cerca de 30 bilhões de euros "mobilizados"; declarações políticas, não decisões; o pacote de soberania de nuvem (CADA) ainda é proposta — [Sofia Globe](https://sofiaglobe.com/2026/11/14/eu-to-mobilise-billions-of-euro-for-ai-gigafactories-europes-tech-sovereignty/) · [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/the-eus-technological-sovereignty-package-new-rules-for-cloud-and-chip-procurem-102nzxy)

## Bloco 2 — Engenharia de software

- **Fable 5.2 e a verificação do código (Anthropic)**, 09/11: a empresa afirma que mais de 90% das mudanças no código principal são escritas pelo Claude e mostra mil agentes formalizando um teorema em Lean em 30 horas; alegações da empresa — [Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- **Orquestração de agentes no Antigravity (Google)**, 10/11: comando /swarm em prévia com o Carbon; o Orchestrator do Hydrogen vem só de agregador — [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) · [Resumo semanal](https://note.com/masahiko_studio/n/nd05750f7c299?hl=en)
- **Extensão maliciosa do Claude Code no marketplace da Cursor**, 14/11: chave roubada de um fornecedor levou a duas versões falsas no ar por cerca de 11 horas; até 5.000 usuários podem ter baixado; números da Cursor — [BleepingComputer](https://bleepingcomputer.com/news/security/cursor-confirms-security-breach-led-to-malicious-claude-code-extension)

## Bloco 2 — Arquitetura empresarial e governança

- **Imagine Enterprise (IBM e Microsoft)**, 10/11: plataforma de agentes por setor, começando por finanças, seguros e varejo; "mais de 6.000" agentes e ativos pré-construídos é alegação da IBM; sem preço nem data de disponibilidade geral — [IBM](https://newsroom.ibm.com/2026-11-10-ibm-and-microsoft-announce-a-new-ai-agent-platform-designed-for-industry-specific-transformation)
- **OpenAI e Databricks com dados governados**, 13/11: ChatGPT com plugin Genie, Codex com gateway e modelos GPT dentro da plataforma; camada de contexto chamada Genie Ontology — [Databricks](https://www.databricks.com/blog/openai-and-databricks-enterprise-ai-your-governed-data)
- **"MCP e A2A sozinhos não escalam agentes"**, 11/11: artigo de opinião; quatro camadas além dos protocolos; a projeção de mais de 150.000 agentes por empresa é da Gartner, citada pelo texto — [InfoWorld](https://www.infoworld.com/article/4246624/mcp-and-a2a-alone-wont-scale-ai-agents.html)
- **ChatGPT Wallet (OpenAI)**, 13/11: agente paga sem ver o número do cartão, com aprovação a cada compra; informação de agregador, o anúncio original não abriu na leitura — [Resumo de agentes](https://aiagentstore.ai/ai-agent-news/this-week)
- **Claude Meetings em beta (Anthropic)**, 12/11: Claude entra no Google Meet como participante visível, em planos Team e Enterprise — [Central de ajuda do Claude](https://support.claude.com/en/articles/12138966-release-notes)

## Insights para levar aos clientes

- **Preço promocional não é orçamento:** o Carbon dobra de preço depois de 30/11. Pergunta: qual seria o custo do projeto se o preço do modelo dobrasse no mês seguinte, e quem monitora isso?
- **Fornecedor de IA é uma cadeia com pontos únicos de falha:** IPO, mudança de comando na Nvidia e proposta europeia de soberania mostram risco de oferta, de governança e de jurisdição. Pergunta: qual é o plano de contingência se o provedor de modelo ou de chips entrar em crise?
- **Extensão de editor e registro de agente são cadeia de suprimento de software:** Pergunta: quem aprova as extensões que os desenvolvedores instalam, as versões são travadas e os registros de sessão passam por varredura de segredos?
- **Plataforma de agentes por setor mistura produto e serviço:** Pergunta: o que vem pronto, o que é projeto, quem opera depois e onde ficam a identidade e a auditoria dos agentes?
- **Dicionário de negócio e identidade antes de multiplicar agentes:** Pergunta: onde estão as definições oficiais das métricas que os agentes usam e quem aprova mudanças?
- **Defina o que o agente faz sozinho e o que exige aprovação:** Pergunta: qual é o limite de valor sem aprovação humana e existe trilha de auditoria de cada ação?

## Conceitos explicados no episódio

- **Mythos e Fable:** o mesmo modelo base com permissões diferentes; o acesso mais amplo fica com quem foi verificado.
- **Acesso por confiança:** liberar um modelo perigoso primeiro a clientes verificados.
- **Token:** pedaço de texto que o modelo lê ou escreve; é a unidade de cobrança.
- **Preço introdutório:** preço promocional com data para acabar.
- **Roadshow:** turnê de apresentação a investidores antes de abrir o capital.
- **Receita anualizada (run rate):** receita do mês atual multiplicada por doze.
- **Gigafábrica de IA:** centro de computação em larga escala para treinar e rodar modelos.
- **Lean:** linguagem em que uma prova matemática é conferida por máquina.
- **Marketplace de extensões:** loja de plugins de um editor de código.
- **Ontologia (camada de contexto):** dicionário de negócio com definições e métricas oficiais da empresa.
- **MCP e A2A:** padrões de conexão de agentes a ferramentas e entre si; não resolvem governança sozinhos.
