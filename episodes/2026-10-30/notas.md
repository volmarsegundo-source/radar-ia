# Radar de IA — semana de 23 a 30/10/2026
Conversa entre Rafa e Camila, apresentadores virtuais (vozes geradas por IA). Bloco 1: visão geral da IA no mundo. Bloco 2: aprofundamento em engenharia de software e arquitetura empresarial. Os insights para levar aos clientes são a leitura editorial do programa, não posição oficial de nenhuma empresa. Os links abaixo levam à notícia completa.

## Bloco 1 — Visão geral da IA no mundo
- **GPT-6.1 Terra (OpenAI)**, 26/10: modelo mais rápido e com metade do preço, focado em uso de computador, visão e código; números de desempenho são da própria OpenAI — [BleepingComputer](https://bleepingcomputer.com/news/artificial-intelligence/openai-launches-gpt-61-terra-with-3x-faster-ai-agents-50-percent-lower-pricing) · disponível no Microsoft Foundry: [blog da Microsoft](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/gpt-6-1-terra-now-generally-available-in-microsoft-foundry-build-agents-that-see/4567769)
- **Genie 4 (Google DeepMind)**, 28/10: modelo de mundo com áudio e comandos em tempo real, em prévia de pesquisa — [Tom's Guide](https://www.tomsguide.com/ai/google-just-unveiled-genie-4-and-it-could-change-video-games-forever) · [TechDogs](https://www.techdogs.com/tech-news/td-newsdesk/google-launches-genie-4-ai-with-interactive-worlds-native-audios-and-simulations)
- **Muse (Meta) em Singapura**, 28/10: agente pessoal conectado a Gmail, Instagram, Grab e Shopee — [CNA](https://www.channelnewsasia.com/singapore/meta-muse-ai-agent-singapore-shopping-travel-email-connectors-6499331)
- **Infraestrutura:** TPUs do Google na nuvem da Oracle a partir de 2027; Nvidia comenta possível licença anual de software para agentes (não confirmada) — [AI Agent Store, resumo da semana](https://aiagentstore.ai/ai-agent-news/this-week)

## Bloco 2 — Engenharia de software
- **GitHub Copilot (Universe)**, 28/10: sessões de agente na nuvem retomáveis em qualquer dispositivo, Agent Host Protocol aberto, uso de computador experimental, comparação de modelos com "juiz", marketplace de plugins — [GitHub Changelog](https://github.blog/changelog/2026-10-28-github-copilot-in-vs-code-universe-releases)
- **Agentic AI Foundation**, 22/10: Agent Skills (Anthropic), Open Responses (OpenAI), OpenEnv (Hugging Face) e OpenSandbox (Alibaba); fundação passa a ter 10 projetos — [Linux Foundation](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox)
- **Sandboxes para agentes:** Akamai Agent Sandbox (beta) e rodada de US$ 60 milhões da Daytona — [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)
- **Segurança de agentes de código:** violação no OpenCode, API de política de modelos do Copilot, atualizações de segurança do Claude Code — [AI Agent Store, agentes de código](https://aiagentstore.ai/ai-agent-news/topic/coding)

## Bloco 2 — Arquitetura empresarial e governança
- **SAP (TechEd)**, 27/10: orquestração de agentes com MCP e A2A, Enterprise AI Gateway, gerenciador de ontologia, Joule Studio com mais de 70 modelos — [Techzine](https://www.techzine.eu/blogs/applications/145290/major-sap-joule-update-prepares-agents-for-complex-processes/)
- **IBM Agent Identity + HashiCorp Vault 2.2**, 28/10: identidade, credenciais de curta duração e revogação em tempo real para agentes — [Channel Insider](https://www.channelinsider.com/ai/news-ibm-ai-agent-identity-security-channel-partner/)
- **Caso Accenture (alegações contestadas)**, 29–30/10: agente de código que teria operado por meses numa rede do Departamento de Defesa dos EUA — [Cyber Security News, a partir da WIRED](https://cybersecuritynews.com/accenture-contractor-allegedly-gave-claude-access)
- **SK Telecom:** agentes tratados como força de trabalho, com identificação e supervisor humano — [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

## Insights para levar aos clientes
- **Agentes viraram infraestrutura:** rodam na nuvem, por horas, com acesso a sistemas. A conversa muda de "qual ferramenta usar" para "como operar e governar agentes".
- **Identidade primeiro:** cada agente precisa de dono, permissões mínimas e credenciais temporárias. Pergunta de abertura: quantos agentes você tem hoje e quem responde por cada um?
- **Padrões abertos nos critérios de compra:** perguntar se a plataforma fala MCP e A2A reduz o risco de dependência de um único fornecedor.
- **Custo e fornecedor mudam rápido:** preços caem, mas podem surgir novas cobranças (ex.: licença de software para agentes, ainda não confirmada). Medir em casos reais e desenhar a arquitetura para trocar de modelo e de nuvem.
- **Agentes de código são software de terceiros com acesso privilegiado:** ambiente isolado, chaves em cofre e rotação de chaves como rotina.
- **Antes de multiplicar agentes:** definir um gateway como ponto único de controle e dar significado aos dados (ontologia).

## Conceitos explicados no episódio
- **Token:** pedaço de texto que o modelo lê ou escreve; a cobrança de API é por milhão de tokens.
- **Uso de computador (computer use):** o modelo opera um computador como uma pessoa, vendo a tela, clicando e digitando.
- **Modelo de mundo:** IA que gera ambientes virtuais interativos a partir de uma descrição.
- **Agente pessoal:** assistente que executa tarefas por você, não só responde.
- **TPU:** chip do Google criado para treinar e rodar IA.
- **MCP (Model Context Protocol):** padrão aberto para plugar ferramentas e dados em agentes de IA.
- **A2A (agente para agente):** padrão para agentes de empresas diferentes conversarem e delegarem tarefas.
- **Sandbox:** ambiente isolado onde o código de um agente roda sem acesso ao resto do sistema.
- **Gateway de IA:** porta de entrada única do tráfego de IA, com autenticação, regras, monitoramento e auditoria.
- **Ontologia:** mapa formal do significado dos dados da empresa e de como se relacionam.
- **Credencial de curta duração:** acesso temporário, específico de uma tarefa, que expira sozinho.
