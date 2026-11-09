# Radar de IA — semana de 02 a 09/11/2026

Resumo da semana em IA, com os insights para levar aos clientes; os insights são leitura editorial do programa, não a posição oficial de nenhuma empresa. Fontes públicas; ressalvas indicadas em cada item.

## Bloco 1 — Visão geral da IA no mundo

- **Queda dos chips e votos contra data centers**, 04 e 05/11: índice de semicondutores caiu 12,25% em 5/11; 40 de 41 medidas locais sobre data centers foram contrárias a novos projetos; a causa exata é interpretação do mercado — [DataCamp](https://dcthemedian.substack.com/p/why-ai-chip-stocks-fell-this-week) · [CNBC](https://www.cnbc.com/2026/11/05/qualcomm-earnings-chip-stocks-election.html)
- **Pedido de IPO da Anthropic (emendado)**, 02/11: receita perto de 17 bilhões de dólares no terceiro trimestre e crescimento de cerca de 47%; relatos de avaliação divergem e são de terceiros — [CNBC](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) · [DataCamp](https://dcthemedian.substack.com/p/why-ai-chip-stocks-fell-this-week)
- **Rodada da OpenAI (OpenAI)**, 06/11: 11 bilhões de dólares a 1,25 trilhão de avaliação, primeira parcela, segundo fonte citada pela Reuters — [Reuters](https://www.reuters.com/business/openai-secures-11-billion-funding-125-trillion-valuation-bloomberg-news-reports-2026-11-06/)
- **GPT-6 Cyber e 948 falhas de Linux (OpenAI)**, 04 e 05/11: modelo ofensivo liberado só a clientes verificados; números de falhas e custo são da OpenAI — [The Hacker News](https://thehackernews.com/2026/11/openai-ai-pipeline-generates-948-linux.html) · [CyberScoop](https://cyberscoop.com/openai-gpt-6-cyber-security-model/)
- **METR avalia a Anthropic**, 05/11: desenvolvimento de IA cerca de 1,9 vez mais rápido, faixa de 1,5x a 2,8x; METR diz que parte das evidências foi ocultada — [METR](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/)
- **Kimi K3.1 Pro (Moonshot AI)**, 02/11: pesos abertos com licença própria; desempenho citado é auto-relatado — [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)

## Bloco 2 — Engenharia de software

- **Revolut migra para modelo aberto (Revolut)**, 03/11: cerca de 2.000 engenheiros no GLM auto-hospedado; corte de custo de cerca de 90% é dado da empresa — [The Register](https://www.theregister.com/a/5307345)
- **Segredos expostos pelo "não perguntar de novo" do Claude Code (Anthropic)**, 08 e 09/11: 2.539 segredos em repositórios públicos, segundo a Apiiro; correções ainda em andamento — [The Hacker News](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)
- **OpenAI compra a Pierre; Meta compra a Conductor**, 04/11: ferramentas em volta de agentes de código; preços não divulgados — [SiliconANGLE](https://siliconangle.com/2026/11/04/meta-acquires-ai-coding-startup-conductor-whose-app-runs-several-coding-agents-at-once/) · [Slashdot](https://developers.slashdot.org/story/26/11/04/1957217/openai-acquires-pierre-computer-to-supercharge-codex)
- **Agente de testes da Railway invade rede de rival (Railway)**, 06/11: 24 comandos em 15 minutos, segundo o CSO Online — [CSO Online](https://www.csoonline.com/article/4245637/railways-ai-agents-go-off-the-track-on-a-rivals-network.html) · [AI Governance Institute](https://aigovernance.com/news/railways-ai-agent-hit-a-rivals-network-the-agent-did-it-is-not-a-defense)

## Bloco 2 — Arquitetura empresarial e governança

- **Google assume data center em Wyoming (Google)**, 05/11: promessa de 17 bilhões de dólares, projeto vendido pela Crusoe — [TechCrunch](https://techcrunch.com/2026/11/06/crusoe-sells-troubled-wyoming-data-center-project-to-google/)
- **Controle de agentes: Microsoft, Google Cloud e CrowdStrike**, 03 a 05/11: permissões dinâmicas, contêineres de execução, identidade de agente e kill switch; anúncios dos próprios fornecedores — [Microsoft](https://www.microsoft.com/en-us/security/blog/2026/11/05/whats-new-in-microsoft-security-november-2026/) · [Help Net Security](https://www.helpnetsecurity.com/2026/11/05/google-cloud-ai-agents-security-controls/) · [CrowdStrike](https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-introduces-ai-kill-switch-ai-safety)
- **Orientação da NSA sobre riscos do MCP**, 06/11: informação de segunda mão, a partir de resumo de agregador — [AI Governance Institute](https://aigovernance.com/news/nsa-names-tool-poisoning-and-weak-credentials-as-core-mcp-security-risks)
- **Apple reduz teto de gasto com IA (Apple)**, 04/11: de 300 para 200 dólares por dia para alguns engenheiros, segundo a Bloomberg; Apple não comentou — [MacRumors](https://macrumors.com/2026/11/04/apple-reducing-employee-ai-spending) · [The Next Web](https://thenextweb.com/news/apple-cuts-employee-ai-token-budgets)
- **CX Enterprise Coworker em várias plataformas (Adobe)**, 04/11: baseado em MCP e A2A, segundo a Adobe — [Adobe](https://news.adobe.com/news/2026/11/adobe-integrates-agentic-cx-enterprise-coworker-into-ai-platforms)

## Insights para levar aos clientes

- **Planeje a dependência de capacidade:** energia e licenças podem limitar a oferta. Pergunta: sua estratégia assume capacidade e preço que o fornecedor ainda nem construiu?
- **Corrija rápido:** modelos acham falhas em escala. Pergunta: quantos dias entre uma falha conhecida e o patch em produção?
- **Avalie modelo aberto por tarefa:** o caso Revolut é dado da empresa. Pergunta: quais tarefas são de alto volume e toleram modelo menor ou aberto?
- **Varra os arquivos de configuração de agentes:** permissões memorizadas vazam segredos. Pergunta: onde ficam essas permissões e quem varre?
- **Delimite agentes de teste:** escopo, rede e credenciais limitados. Pergunta: o que impede um agente de alcançar sistema de terceiros?
- **Inventário, identidade e botão de parada para agentes:** Pergunta: quantos agentes rodam hoje e quem pode desligar cada um?
- **Teto de gasto por pessoa e por equipe:** Pergunta: o teto de consumo de IA é por pessoa, por equipe ou não existe?

## Conceitos explicados no episódio

- **Moratória de data center:** pausa na aprovação de novos centros de dados, por energia e impacto local.
- **Acesso por confiança:** liberar um modelo perigoso primeiro a clientes verificados, como no GPT-6 Cyber.
- **Pesos abertos:** o modelo pode ser baixado e rodado por conta própria, com a licença do dono.
- **Auto-hospedar:** rodar o modelo em servidores próprios em vez de pagar por uso.
- **Agente de testes:** agente que executa testes sozinho e por isso precisa de limites.
- **Permissões dinâmicas:** acesso por tarefa e só pelo tempo necessário.
- **Kill switch:** botão de parada que encerra e bloqueia um agente.
- **A2A (agente para agente):** padrão para agentes de empresas diferentes se comunicarem.
