# Radar de IA & Tecnologia — guia para o Claude

Podcast semanal pessoal do Volmar (São Paulo, comunica-se em português). Toda segunda às 8h13 (America/Sao_Paulo) uma tarefa agendada do Claude pesquisa as notícias de IA da semana, publica um documento escrito e envia ao repositório o roteiro do episódio: uma conversa de ~18 minutos entre dois apresentadores virtuais (Rafa e Camila), em dois blocos (visão geral da IA e aprofundamento em engenharia de software e arquitetura empresarial). O programa é um treinamento para os executive partners, colegas do Volmar, entregarem valor aos clientes: por isso a conversa marca os insights para levar aos clientes. O resto é automático.

Documentação completa: `README.md` (visão geral e status), `docs/arquitetura.md` (componentes, decisões, limites) e `docs/operacao.md` (configuração, ajustes, solução de problemas, custos). Ao mudar o pipeline, atualize esses arquivos no mesmo commit.

## Fluxo

1. **Tarefa agendada "Resumo semanal de IA e tecnologia"** (Claude Code remoto, cron `13 8 * * 1`, fuso America/Sao_Paulo). O prompt completo fica na própria tarefa. Para mudar escopo, tom, tamanho ou horário, altere a tarefa (update_trigger), não este repositório.
2. A tarefa cria `episodes/AAAA-MM-DD/roteiro.txt` (diálogo no formato descrito em "Formato do episódio") e `episodes/AAAA-MM-DD/notas.md` (notas com links e glossário) e faz push na `main`.
3. O push em `episodes/**` dispara `.github/workflows/episodio.yml`:
   - `scripts/tts.py` gera o áudio com Google Cloud Text-to-Speech, uma voz Chirp 3 HD pt-BR por locutor (RAFA e CAMILA), insere pausas entre falas e entre blocos, junta tudo, normaliza o volume (~-19 LUFS) e codifica em MP3 mono 64 kbps;
   - cria a Release `ep-AAAA-MM-DD` com o MP3 (arquivo permanente; o git não guarda áudio);
   - `scripts/build_feed.py` monta `feed.xml`, a página do podcast (`index.html`, com player, assinar e compartilhar) e uma página por episódio (`ep/<tag>/`, com notas e links) com os últimos 12 episódios, e o GitHub Pages publica.
4. O app Podcasts (iPhone/Apple Watch) segue o feed e baixa os episódios novos sozinho.

Feed: `https://volmarsegundo-source.github.io/radar-ia/feed.xml` · Página para compartilhar: `https://volmarsegundo-source.github.io/radar-ia/`

## Formato do episódio

- **Estrutura:** abertura (apresentação, aviso de que os apresentadores são virtuais e combinado do formato) → Bloco 1, visão geral da IA no mundo (4 a 6 notícias) → Bloco 2, aprofundamento em engenharia de software e em arquitetura empresarial (6 a 9 notícias) → Fechamento com os 3 a 4 insights principais da semana para levar aos clientes. Tamanho: 2.400 a 3.000 palavras (16 a 20 minutos).
- **Papéis:** RAFA conduz, apresenta as notícias e pergunta o que o ouvinte perguntaria. CAMILA explica cada conceito, sigla ou tecnologia nova (o que é, para que serve e, se a fonte permitir, quem usa), em linguagem simples.
- **Insights para clientes:** de 5 a 8 vezes por episódio, RAFA pergunta o recado para o cliente e CAMILA responde numa fala que começa com "Insight para levar ao cliente:" (sempre a mesma expressão). Insight é leitura editorial, prática e acionável, baseada em fatos da fonte; a abertura avisa que não é posição oficial de nenhuma empresa. Só fontes públicas, nada interno ou confidencial. O fechamento (marcador `# Fechamento — O que levar para os clientes`) resume os 3 a 4 principais, e `notas.md` traz a seção `## Insights para levar aos clientes`.
- **Fontes:** citar oralmente a fonte e a data de cada notícia e as ressalvas (dado só da empresa, alegação contestada, informação de agregador). Os links ficam em `notas.md` e aparecem no app Podcasts. Nunca inventar links nem "quem usa" sem fonte.
- **`roteiro.txt` (o gerador de áudio depende disto):** cada fala numa linha que começa com `RAFA: ` ou `CAMILA: `, linha em branco entre falas, falas de no máximo ~90 palavras. Linhas que começam com `# ` marcam a mudança de bloco (não são faladas; geram pausa longa). Linhas sem rótulo continuam a fala anterior. Um roteiro sem nenhum rótulo é lido por uma única voz (modo narrador).
- **Pronúncia:** as vozes são sintéticas; escrever por extenso o que soaria mal ("GPT seis ponto um"), sem URLs, símbolos ou markdown.
- **`notas.md`:** 1ª linha `# Radar de IA — semana de DD a DD/MM/AAAA`; frase de apresentação; `## Bloco 1 — Visão geral da IA no mundo`, `## Bloco 2 — Engenharia de software`, `## Bloco 2 — Arquitetura empresarial e governança` com itens `- **Título (empresa)**, data: resumo — [Fonte](URL)`; `## Insights para levar aos clientes` com `- **Insight curto:** explicação e pergunta de abertura`; `## Conceitos explicados no episódio` com `- **Termo:** explicação`. O feed converte esse markdown em HTML (listas, negrito e links).

## Regras

- Episódio já publicado (Release existente) é ignorado: reenviar a mesma pasta não gera áudio de novo. Para refazer um episódio, crie o arquivo vazio `episodes/AAAA-MM-DD/refazer` junto com a correção e dê push: o workflow apaga a Release e a tag, regera o áudio e remove o marcador (a sessão do Claude não consegue apagar Releases pela API).
- Nunca commitar MP3 nem chaves. O secret `GOOGLE_TTS_API_KEY` fica em Settings › Secrets and variables › Actions.
- Vozes e velocidade: variáveis do repositório `TTS_VOICE_RAFA` (padrão `pt-BR-Chirp3-HD-Charon`), `TTS_VOICE_CAMILA` (padrão `pt-BR-Chirp3-HD-Kore`), `TTS_VOICE` (voz do modo narrador) e `TTS_RATE` (padrão `1.0`).
- O repositório e o site são públicos (necessário para Pages gratuito). O feed tem `itunes:block`. Não colocar conteúdo confidencial.
- Custo: ~17 mil caracteres por episódio; o nível gratuito do Google TTS é 1 milhão de caracteres por mês nas vozes Chirp 3 HD. O Higgsfield não é mais usado.
- O episódio `2026-10-30` é o episódio 1 (os testes anteriores foram apagados). Para mudar o visual da página web, edite `scripts/build_feed.py` (CSS e templates no próprio arquivo).

## Limitações do ambiente do Claude

- A sessão do Claude só acessa o repositório depois de `add_repo` (owner `volmarsegundo-source`, repo `radar-ia`, access `push`). Não consegue criar repositórios, ativar Pages nem disparar workflows pela API; só o push dispara o workflow, e ele roda em qualquer push que mude `episodes/**`, `scripts/**`, `assets/**` ou o workflow.
- A sessão não alcança `github.io` nem `cloudfront.net`: para conferir o feed, o Volmar abre no navegador.
