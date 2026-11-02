# Radar de IA — semana de 26/10 a 02/11/2026

Resumo da semana em IA, com os insights para levar aos clientes; os insights são leitura editorial do programa, não a posição oficial de nenhuma empresa. Fontes públicas; ressalvas indicadas em cada item.

## Bloco 1 — Visão geral da IA no mundo

- **GPT-6.1 Terra (OpenAI)**, 26/10: liberado na API, no ChatGPT Work e no Codex, fora da aba de chat comum; preço de API informado de 1 dólar por milhão de tokens de entrada e 5 de saída — [Resumo semanal](https://note.com/masahiko_studio/n/n37b4960e0104?hl=en) · [Notas de versão da OpenAI](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Gemini 4 Carbon (Google)**, 28/10: modelo com foco em segurança e tarefas longas de código, liberado de início a defensores via programa Fairwind; benchmarks são alegações do Google — [Blog do Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)
- **Genie 4 (Google DeepMind)**, 27/10: modelo de mundo com áudio sincronizado e cerca de dois minutos de consistência de cena; sem benchmarks na fonte — [Boletim de Rupak Ganguly](https://rupakganguly.substack.com/p/latest-in-ai-news-anthropic-ipo-gemini)
- **Balanços de Alphabet, Microsoft e Amazon**, 28 e 29/10: nuvem acelerando, mas fluxo de caixa livre negativo em Alphabet e Amazon e mais de 740 bilhões de dólares de capex planejados — [TechCrunch](https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom) · [Boletim](https://rupakganguly.substack.com/p/latest-in-ai-news-anthropic-ipo-gemini)
- **Pedido de IPO da Anthropic**, semana de 26/10: pedido confirmado pelo TechCrunch; números financeiros vêm de boletim não verificado e o alerta da Blackstone é relato do Financial Times citado por terceiros — [TechCrunch](https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom) · [Boletim](https://rupakganguly.substack.com/p/latest-in-ai-news-anthropic-ipo-gemini)

## Bloco 2 — Engenharia de software

- **Copilot Fusion disponível para todos (GitHub)**, 28/10: escolhe modelos e orquestração por tarefa; comparação de custo com o Claude Code é alegação do GitHub — [Beri.net](https://beri.net/article/github-universe-2026-recap-enterprise-includes-copilot-no-ai-credits-fusion-ga-30-percent-discount-standalone-10-dollars)
- **Super-Agent (DeepSeek)**, 01/11: protótipo de código aberto de agente proativo para código, sem dados de confiabilidade — [Digital Trends](https://digitaltrends.com/computing/deepseek-wants-to-steal-claude-code-and-codexs-lunch-with-an-ai-agent-that-does-not-wait-around)
- **Project Quarry (Cisco)**, 28/10: código aberto que detecta comportamento de risco na sessão inteira do agente; análise do incidente citado é hipotética e não há avaliação independente — [The Register](https://www.theregister.com/a/5305867)
- **Uso de computador do Gemini (Google)**, 30/10: disponibilidade geral nas APIs Interactions e GenerateContent — [Notas da API Gemini](https://ai.google.dev/gemini-api/docs/changelog) · [Resumo semanal](https://note.com/masahiko_studio/n/n37b4960e0104?hl=en)

## Bloco 2 — Arquitetura empresarial e governança

- **Pacote Copilot Enterprise (GitHub)**, 28/10: assento a zero, sem créditos incluídos e com consumo medido; limites de orçamento exigem ativação (análise de veículo secundário) — [Beri.net](https://beri.net/article/github-universe-2026-recap-enterprise-includes-copilot-no-ai-credits-fusion-ga-30-percent-discount-standalone-10-dollars)
- **Parceria ServiceNow e OpenAI**, 28/10: plugin no ChatGPT para ações governadas; boa parte das entregas é plano para 2027 e termos financeiros não foram divulgados — [Comunicado da ServiceNow](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-and-OpenAI-accelerate-enterprise-AI-from-models-and-operations-to-cybersecurity-and-agentic-development/default.aspx)
- **API de análise de uso e custo (Anthropic)**, 29/10: beta com custo por modelo, workspace, chave e usuário — [Notas de versão da Claude Platform](https://platform.claude.com/docs/en/release-notes/overview)
- **Cotas compartilhadas de ChatGPT e Codex (OpenAI)**, 31/10: a partir de dezembro nos planos Plus, Pro e Business — [Limites de uso da OpenAI](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits)
- **Pedidos de agentes no DoorDash**, 30/10: poucas centenas de pedidos de agentes de terceiros ante cerca de 3 milhões de entregas diárias; janela de tempo não informada — [Boletim](https://rupakganguly.substack.com/p/latest-in-ai-news-anthropic-ipo-gemini)

## Insights para levar aos clientes

- **Não amarre a solução a um único modelo:** preço e disponibilidade mudam rápido. Pergunta: se o preço do seu modelo principal mudasse em 30 dias, o que você refaria?
- **Encurte o ciclo de correção de vulnerabilidades:** modelos bons em achar falhas ajudam defensores e atacantes. Pergunta: quanto tempo passa entre uma falha conhecida e o patch em produção?
- **Planeje para fornecedores sob pressão financeira:** preço, capacidade ou prioridade podem mudar. Pergunta: qual é o plano B se um fornecedor reajustar ou limitar o serviço?
- **Documente a saída de cada provedor crítico:** concentração em fornecedor de modelo é risco. Pergunta: existe um plano de saída documentado?
- **Meça qualidade e custo nas suas próprias tarefas:** roteamento multimodelo vira padrão. Pergunta: o time tem tarefas reais para comparar ferramentas?
- **Monitore a sessão inteira do agente:** segurança é observabilidade de comportamento. Pergunta: os registros permitem reconstruir uma sessão do início ao fim?
- **FinOps de IA desde o dia um:** consumo medido só é barato com teto ativo. Pergunta: você vê o gasto por equipe e sabe quem aprova o teto?
- **Defina quem valida permissão e guarda a trilha de auditoria:** quando agentes alteram registros, alguém responde. Pergunta: qual sistema faz isso hoje?

## Conceitos explicados no episódio

- **Token:** pedaço de texto que o modelo lê ou escreve; é a unidade de cobrança.
- **Acesso escalonado por confiança:** liberar um modelo poderoso primeiro a grupos verificados.
- **Modelo de mundo:** modelo que gera ambientes interativos, como o Genie 4.
- **Capex:** gasto de capital em data centers, chips e energia.
- **Fluxo de caixa livre:** caixa que sobra depois da operação e dos investimentos.
- **Orquestração multimodelo (Fusion):** sistema que escolhe qual modelo faz cada tarefa e se outro revisa.
- **Agente proativo:** agente que age sem ser acionado.
- **Regras estilo Snort e YARA:** formato de regras de detecção, aplicado pelo Quarry a agentes.
- **MCP (Model Context Protocol):** padrão aberto para conectar agentes a ferramentas e sistemas.
- **Uso de computador (computer use):** o modelo vê a tela e opera mouse e teclado.
- **FinOps de IA:** gestão financeira do consumo de IA.
