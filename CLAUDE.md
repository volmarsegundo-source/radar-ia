# Radar de IA & Tecnologia — guia para o Claude

Podcast semanal pessoal do Volmar (São Paulo, comunica-se em português). Toda segunda às 8h13 (America/Sao_Paulo) uma tarefa agendada do Claude pesquisa as notícias de IA da semana, publica um documento escrito e envia ao repositório o roteiro do episódio. O resto é automático.

## Fluxo

1. **Tarefa agendada "Resumo semanal de IA e tecnologia"** (Claude Code remoto, cron `13 8 * * 1`, fuso America/Sao_Paulo). O prompt completo fica na própria tarefa. Para mudar escopo, tom, tamanho ou horário, altere a tarefa (update_trigger), não este repositório.
2. A tarefa cria `episodes/AAAA-MM-DD/roteiro.txt` (texto falado, 900–1.100 palavras, parágrafos separados por linha em branco) e `episodes/AAAA-MM-DD/notas.md` (1ª linha `# título`; depois markdown simples com links) e faz push na `main`.
3. O push em `episodes/**` dispara `.github/workflows/episodio.yml`:
   - `scripts/tts.py` gera o áudio com Google Cloud Text-to-Speech (voz Chirp 3 HD pt-BR; divide em blocos de até 4.500 bytes, junta com ffmpeg em MP3 mono 64 kbps);
   - cria a Release `ep-AAAA-MM-DD` com o MP3 (arquivo permanente; o git não guarda áudio);
   - `scripts/build_feed.py` monta `feed.xml` e `index.html` com os últimos 12 episódios e o GitHub Pages publica.
4. O app Podcasts (iPhone/Apple Watch) segue o feed e baixa os episódios novos sozinho.

Feed: `https://volmarsegundo-source.github.io/radar-ia/feed.xml`

## Regras

- Episódio já publicado (Release existente) é ignorado: reenviar a mesma pasta não gera áudio de novo. Para refazer um episódio, apague a Release e a tag `ep-AAAA-MM-DD` e dê push de novo.
- Nunca commitar MP3 nem chaves. O secret `GOOGLE_TTS_API_KEY` fica em Settings › Secrets and variables › Actions.
- Voz e velocidade: variáveis do repositório `TTS_VOICE` (padrão `pt-BR-Chirp3-HD-Charon`) e `TTS_RATE` (padrão `1.0`).
- O repositório e o site são públicos (necessário para Pages gratuito). O feed tem `itunes:block`. Não colocar conteúdo confidencial.
- Custo: ~7 mil caracteres por episódio; o nível gratuito do Google TTS é 1 milhão de caracteres por mês nas vozes Chirp 3 HD. O Higgsfield não é mais usado.
- Primeiro episódio (`2026-10-30`) foi uma edição de teste.

## Limitações do ambiente do Claude

- A sessão do Claude só acessa o repositório depois de `add_repo` (owner `volmarsegundo-source`, repo `radar-ia`, access `push`). Não consegue criar repositórios, ativar Pages nem disparar workflows pela API; só o push dispara o workflow.
- A sessão não alcança `github.io` nem `cloudfront.net`: para conferir o feed, o Volmar abre no navegador.
