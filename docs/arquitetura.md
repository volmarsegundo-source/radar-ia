# Arquitetura

## Objetivo

Título do podcast: **Radar de IA & Tecnologia: Engenharia de Software e Arquitetura**. O subtítulo delimita os dois domínios de aprofundamento; outros domínios poderão virar podcasts próprios no futuro (outro repositório/feed).

Entregar toda segunda de manhã um briefing das notícias de IA e tecnologia, em texto (com links) e em áudio, para ouvir offline no iPhone e no Apple Watch, com custo zero e sem intervenção manual. O programa é um treinamento para os executive partners entregarem valor aos clientes. O áudio é uma conversa de ~18 minutos entre dois apresentadores virtuais, em dois blocos: visão geral da IA no mundo e aprofundamento em engenharia de software e arquitetura empresarial.

## Componentes

| Componente | Papel | Onde vive |
|---|---|---|
| Tarefa agendada "Resumo semanal de IA e tecnologia" | Pesquisa as notícias da semana, escreve o documento, o roteiro e as notas, e faz push no repositório | Claude (Claude Code remoto), cron `13 8 * * 1`, fuso America/Sao_Paulo |
| Repositório `radar-ia` | Guarda roteiros, notas, scripts e documentação | GitHub (público) |
| Workflow `episodio.yml` | Gera o áudio, cria a Release e publica o feed | GitHub Actions |
| `scripts/tts.py` | Converte o diálogo de `roteiro.txt` em um MP3 único, com uma voz por locutor | Google Cloud Text-to-Speech + ffmpeg |
| `scripts/build_feed.py` | Monta `feed.xml` (notas em HTML, com links), a página do podcast (`index.html`) e uma página por episódio (`ep/<tag>/`) a partir das Releases | Python (biblioteca padrão) + ffprobe |
| Releases (`ep-AAAA-MM-DD`) | Arquivo permanente dos MP3 | GitHub Releases |
| GitHub Pages | Serve o feed e os últimos 12 episódios | `volmarsegundo-source.github.io/radar-ia` |
| App Podcasts | Segue o feed e baixa os episódios (iPhone e Apple Watch) | Dispositivos do usuário |

## Fluxo de dados

1. **Segunda 8h13.** A tarefa agendada pesquisa as notícias dos últimos 7 dias, publica o documento escrito com links e cria `episodes/AAAA-MM-DD/roteiro.txt` e `notas.md`. Faz commit e push na `main` (mensagem `Episódio AAAA-MM-DD`).
2. **Gatilho.** O push em `episodes/**` dispara o workflow. Ele também pode ser disparado manualmente (`workflow_dispatch`) pela aba Actions.
3. **Áudio.** Para cada pasta em `episodes/` sem Release correspondente, `tts.py` lê o roteiro fala por fala (`RAFA:` / `CAMILA:`), sintetiza cada fala com a voz do locutor (falas acima de 4.500 bytes são divididas por frase; o limite da API é 5.000), decodifica tudo para PCM, insere pausas (0,35 s entre falas; 1,4 s entre blocos), normaliza o volume (~-19 LUFS, padrão de podcast mono) e codifica um MP3 mono, 44,1 kHz, 64 kbps. Roteiros sem rótulos são lidos por uma única voz (modo narrador).
4. **Release.** O MP3 é anexado a uma Release `ep-AAAA-MM-DD`. O título vem da 1ª linha de `notas.md` e o corpo da Release são as notas.
5. **Feed.** O workflow baixa os MP3 das 12 Releases mais recentes, `build_feed.py` gera `feed.xml` (RSS com tags iTunes, duração e tamanho reais) e `index.html`, e o GitHub Pages publica.
6. **Escuta.** O app Podcasts já segue o feed e baixa o episódio novo automaticamente; o Apple Watch baixa os programas seguidos para uso offline.

## Decisões

### Hospedagem dos áudios: GitHub (Releases + Pages)

- Cada episódio tem ~3,5 MB (~200 MB por ano). Commitar MP3 faria o repositório crescer para sempre; as **Releases** guardam os arquivos fora do histórico do git (limite de 2 GB por arquivo).
- O **Pages** serve só os 12 episódios mais recentes, e o site é reconstruído a cada execução.
- Alternativas descartadas:
  - **Vercel:** funcionaria, mas adiciona outro serviço e outra conta para um caso que o GitHub já cobre sem custo.
  - **Google Drive / OneDrive:** os links de download passam por redirecionamentos e telas de verificação; o app Podcasts costuma falhar ao baixar ou tocar. Podem servir como cópia de backup, nunca como origem do feed.

### Geração de voz: Google Cloud Text-to-Speech (Chirp 3 HD)

- Nível gratuito de 1 milhão de caracteres por mês nas vozes Chirp 3 HD; um episódio usa ~7 mil.
- Qualidade natural em pt-BR, API estável e chamada simples (HTTP com chave de API), adequada para rodar em CI.
- Alternativas descartadas:
  - **Higgsfield (ElevenLabs):** usado no primeiro teste; custa ~20 créditos por episódio e o plano básico acabaria em poucas semanas.
  - **Gemini TTS (API):** boa qualidade, mas pago (~US$ 0,10 por episódio) e sem relação com a assinatura Gemini Pro.
  - **NotebookLM / Resumo em Áudio:** incluído na assinatura, mas manual e não automatizável.
  - **ChatGPT / Claude:** API de voz cobrada à parte (ChatGPT) ou sem geração de áudio (Claude).

### Formato conversa com dois apresentadores

- **Por quê:** o ouvinte é um profissional ocupado, em deslocamento ou na academia; a conversa é mais fácil de acompanhar que um noticiário corrido. Um segundo interlocutor permite explicar cada conceito novo (o que é, para que serve, quem usa) sem interromper a narrativa, o que atende a ouvintes que ainda não conhecem a tecnologia.
- **Papéis fixos:** RAFA conduz e pergunta; CAMILA explica e contextualiza. A estrutura em dois blocos (visão geral → aprofundamento em engenharia de software e arquitetura empresarial) é parte do prompt da tarefa agendada.
- **Transparência:** os apresentadores são virtuais; a abertura de cada episódio e a descrição do podcast dizem isso.
- **Fontes:** citadas oralmente (nome e data) e listadas com links nas notas do episódio, que o app Podcasts exibe. O feed converte o markdown das notas em HTML limitado (parágrafos, listas, negrito, itálico, links), o que o app suporta.
- **Implementação:** o Google TTS sintetiza um locutor por requisição, então cada fala é uma chamada; o script monta o áudio no próprio PCM (sem depender de concatenar MP3 de taxas diferentes). A síntese multilocutor do Gemini TTS foi descartada por ser paga. Não há fala sobreposta nem interrupções, apenas turnos, o que é adequado para um briefing.
- **Insights para clientes:** o público são executive partners que conversam com clientes. De 5 a 8 vezes por episódio, a CAMILA dá um recado prático começando por "Insight para levar ao cliente:", e o fechamento resume os 3 a 4 principais. São leitura editorial (avisada na abertura), baseada em fatos da fonte, com fontes públicas apenas; também aparecem em `notas.md`.
- **Tamanho:** 2.400 a 3.000 palavras (~17 mil caracteres, 16 a 20 minutos, ~9 MB); usa ~1,7% do nível gratuito mensal do Google TTS por episódio.

### Roteiro pelo Claude, áudio pelo GitHub

O Claude escreve o texto; a geração de áudio fica no GitHub Actions. Motivos: o ambiente do Claude não consegue baixar arquivos de áudio de provedores externos nem juntar partes de forma confiável, e o Actions permite reprocessar, versionar e inspecionar cada execução.

### Página web do podcast

O app Podcasts não tem página web própria para um feed privado, então `build_feed.py` gera uma: `index.html` (episódio mais recente com player, botões de assinar e lista de episódios) e `ep/<tag>/index.html` (player com voltar 15 s, avançar 30 s e velocidade, notas completas com links, botões de compartilhar). As páginas têm metadados Open Graph (capa, título e descrição), então o link aparece com prévia no WhatsApp, Teams e LinkedIn. É HTML estático, sem dependências; a posição de reprodução fica no navegador do ouvinte. O link de cada episódio também vai no `<link>` do item do feed.

### Feed público, sem listagem

O repositório e o site são públicos (Pages gratuito exige repositório público). O feed tem `itunes:block` e as páginas têm `noindex`, para não aparecer em diretórios nem em buscadores, mas qualquer pessoa com o endereço pode acessá-los. O conteúdo são notícias públicas; nada confidencial deve entrar aqui.

## Limites e restrições conhecidos

- A sessão do Claude só acessa o repositório depois de `add_repo` (owner `volmarsegundo-source`, repo `radar-ia`, acesso `push`). Não cria repositórios, não ativa o Pages e não dispara workflows pela API; só o push dispara.
- A sessão do Claude não alcança `github.io` nem `cloudfront.net`; a conferência do feed é feita pelo usuário no navegador.
- Limite de 5.000 bytes por requisição do Google TTS (falas maiores são divididas por frase). Cada fala é uma requisição; o script repete automaticamente em caso de limite de taxa (HTTP 429) ou erro transitório do servidor.
- As vozes são sintéticas e não interrompem uma à outra; a naturalidade depende do texto do roteiro (frases curtas, pronúncia escrita por extenso).
- Um episódio já publicado (Release existente) nunca é regerado automaticamente.
- O feed mostra só os 12 episódios mais recentes (`KEEP_EPISODES` no workflow); os demais continuam nas Releases.
- Se o Google TTS falhar, o workflow falha e nada é publicado; o roteiro permanece no repositório e o episódio pode ser reprocessado (ver `operacao.md`).
