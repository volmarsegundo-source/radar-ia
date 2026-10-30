# Prompt: criar um novo podcast semanal nos moldes do Radar de IA

Como usar: abra uma conversa nova do Claude (Claude Code, com acesso ao GitHub e à criação de tarefas agendadas), preencha os campos `[PREENCHER]` da seção "Briefing" e cole **tudo a partir da linha "Início do prompt"**. O Claude reaproveita o código do repositório `radar-ia` em vez de reescrever.

---

## Início do prompt

Quero criar um novo podcast semanal automatizado, **muito parecido com o meu "Radar de IA & Tecnologia"**, mas com outro escopo. A arquitetura, os scripts e as lições aprendidas já existem no repositório `volmarsegundo-source/radar-ia` e na tarefa agendada "Resumo semanal de IA e tecnologia". Reaproveite esse trabalho; não reinvente.

### Briefing (decisões minhas)

- **Nome do podcast:** [PREENCHER, ex.: "Radar de Regulação & Privacidade"]
- **Subtítulo/escopo curto (vai no título e na descrição do feed):** [PREENCHER, ex.: "LGPD, Open Finance e IA regulada"]
- **Nome do repositório novo:** [PREENCHER, ex.: radar-regulacao] (conta `volmarsegundo-source`, público, sem README inicial)
- **Assunto e domínios de aprofundamento:** [PREENCHER: o que entra, o que fica de fora]
- **Estrutura em blocos:** [PREENCHER, ex.: Bloco 1 visão geral; Bloco 2 aprofundamento em X e Y; Fechamento]
- **Público e objetivo (por que alguém ouve):** [PREENCHER, ex.: treinamento para colegas que atendem clientes]
- **Periodicidade e horário:** [PREENCHER, ex.: toda quinta, 7h40, America/Sao_Paulo; escolha um minuto "quebrado" e um horário diferente do Radar]
- **Duração e tamanho do roteiro:** [PREENCHER, ex.: ~15 min = 2.000 a 2.600 palavras]
- **Fontes preferidas e fontes a evitar:** [PREENCHER]
- **Apresentadores virtuais (nomes e papéis):** [PREENCHER, ex.: LUCAS conduz; MARINA explica conceitos e dá os insights]. Vozes Chirp 3 HD pt-BR; use vozes diferentes das do Radar se quiser distinguir os programas.
- **Elemento editorial fixo (equivalente aos "insights para clientes"):** [PREENCHER ou "nenhum"]
- **Despedida padrão:** [PREENCHER]
- **Idioma:** português do Brasil.

### O que construir (replicar do Radar)

1. **Repositório** com: `.github/workflows/episodio.yml`, `scripts/tts.py`, `scripts/build_feed.py`, `assets/cover.png`, `episodes/`, `docs/` (arquitetura e operação), `README.md`, `CLAUDE.md`, `.gitignore`. Comece clonando `radar-ia` (adicione-o com `add_repo`, acesso read) e adapte: nomes, vozes, `SHOW_TITLE`, `SHOW_DESC`, `AUTHOR`, URLs, textos fixos das páginas e rótulos dos locutores no `tts.py`.
2. **Pipeline:** push em `episodes/**`, `scripts/**`, `assets/**` ou no workflow → Google Cloud TTS (Chirp 3 HD, uma voz por locutor, pausas, ffmpeg, loudnorm ~-19 LUFS, MP3 mono 64 kbps) → Release `ep-AAAA-MM-DD` → `feed.xml` + página web (player, assinar, compartilhar, uma página por episódio) → GitHub Pages. Mantenha o marcador `refazer` para regerar episódios.
3. **Tarefa agendada** própria (create_trigger, fuso America/Sao_Paulo) que pesquisa, publica o documento escrito, escreve `roteiro.txt` + `notas.md` e dá push. Para escrevê-la, **leia o prompt completo da tarefa "Resumo semanal de IA e tecnologia"** (list_triggers, campo prompt) e o `CLAUDE.md` do radar-ia, e adapte o escopo, a estrutura, as fontes e o tom ao meu briefing. Mantenha as regras de ouro: citar fonte e data oralmente, não inventar links nem "quem usa", sinalizar dado só da empresa, alegação contestada, agregador e projeção.
4. **Capa** 1400x1400 própria, gerada por código (Pillow), com identidade visual diferente da do Radar.
5. **Documentação** completa (README, arquitetura, operação, CLAUDE.md), no mesmo commit de qualquer mudança de pipeline.
6. **Episódio 1:** pesquise e escreva um episódio real (não de teste) já no formato final, para validar tudo de ponta a ponta.

### Lições aprendidas (aplique desde o início)

- **Você não consegue** criar o repositório, ativar o Pages, cadastrar secrets, apagar Releases, disparar workflows pela API nem abrir `github.io`/`cloudfront.net`. Só o **push** dispara o workflow. Peça-me essas ações com o passo a passo exato de cliques, **uma vez, em lista numerada**, e continue o resto.
- **Passos meus (manuais):** (a) criar o repositório vazio e público; (b) Settings › Pages › Source: GitHub Actions; (c) secret `GOOGLE_TTS_API_KEY` em Settings › Secrets and variables › Actions (posso reutilizar a mesma chave do Radar; o nível gratuito de 1 milhão de caracteres por mês é compartilhado entre os podcasts, cada episódio usa ~13 a 17 mil); (d) aprovar o ambiente `github-pages` se a execução ficar em "Waiting"; (e) seguir o feed por URL no app Podcasts. **Nunca peça nem imprima a chave no chat.**
- No XML, `&` no título deve ser `&amp;`. O limite do Google TTS é 5.000 bytes por requisição (divida por frase) e há 429/5xx transitórios (retry com backoff). `gh release view/download` usa GraphQL e falha aqui: use a API REST. Episódio com Release existente é ignorado; para refazer, use o marcador `refazer`.
- O Apple Podcasts não recebe aviso do feed: atualiza por consulta periódica; o título do programa demora mais. Se travar, deixar de seguir e seguir de novo por URL.
- Repositório e site são **públicos**: feed com `itunes:block`, páginas com `noindex`, nenhum conteúdo confidencial ou interno de empresa. Os apresentadores são virtuais e a abertura de cada episódio avisa isso.
- Pronúncia: escrever por extenso o que as vozes sintéticas leem mal (siglas, números, "GPT seis ponto um"), sem URLs, símbolos nem markdown. Cada fala numa linha, até ~90 palavras; linhas `# ` marcam troca de bloco.

### Como quero que você trabalhe

- Faça as perguntas bloqueantes **de uma vez só** (só se o briefing deixar algo realmente em aberto) e depois execute sem pedir confirmações intermediárias.
- Use uma lista de tarefas e termine com uma verificação: sintaxe do workflow (`bash -n`), parse do roteiro, geração local do site com áudio de teste, XML do feed válido e conferência do estado do workflow e da Release pela API REST.
- Ao final, entregue: o que foi criado, a **lista curta dos passos manuais que dependem de mim** (com cliques exatos), o que será conferido na primeira execução agendada e a URL do feed e da página.
- Não altere o repositório `radar-ia` nem a tarefa do Radar, e não mexa na tarefa "Monitor diário de preços de IA".

## Fim do prompt
