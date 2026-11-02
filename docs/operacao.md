# Operação

## Configuração inicial (feita em 30/10/2026)

1. **Chave do Google Cloud TTS**
   - console.cloud.google.com: criar o projeto `radar-ia`, vincular uma conta de faturamento e ativar a **Cloud Text-to-Speech API**.
   - APIs e serviços › Credenciais › Criar credenciais › **Chave de API**. Restrição de API: somente *Cloud Text-to-Speech API*. Restrição de aplicativo: nenhuma (o GitHub Actions usa IPs variáveis).
   - Faturamento › Orçamentos e alertas: orçamento de **US$ 1** para avisar se o uso sair do previsto.
2. **Secret no GitHub:** Settings › Secrets and variables › Actions › New repository secret, nome `GOOGLE_TTS_API_KEY`.
3. **GitHub Pages:** Settings › Pages › Build and deployment › Source: **GitHub Actions**.
4. **Primeira execução:** push em `episodes/**` ou aba Actions › "Gerar episódio e publicar feed" › Run workflow.
5. **iPhone:** Podcasts › Biblioteca › ⋯ › **Seguir Programa por URL** › `https://volmarsegundo-source.github.io/radar-ia/feed.xml`.
6. **Apple Watch:** app Watch no iPhone › Podcasts › Personalizado › ativar o programa. O Watch baixa os episódios enquanto carrega; depois toca com AirPods, sem o iPhone e sem internet.

## Rotina semanal

Nada a fazer. Na segunda-feira:

- 8h13: a tarefa agendada roda e você recebe uma notificação no celular com os destaques.
- Poucos minutos depois: o episódio (uma conversa de cerca de 18 minutos, com os insights para levar aos clientes) aparece no app Podcasts, com as notas e os links na descrição.
- A página do podcast (`https://volmarsegundo-source.github.io/radar-ia/`) mostra o episódio com player e notas.
- O documento escrito, com todos os links, fica na lista de artefatos do Claude.

## Verificar a automação

Estado em 30/10/2026: workflow, Release, feed e páginas validados com o episódio 1; a tarefa agendada ainda não rodou sozinha. Na segunda-feira, depois das 8h13:

1. Notificação da tarefa chegou e o documento escrito foi publicado (artefatos do Claude).
2. Repositório: existe a pasta `episodes/AAAA-MM-DD` com `roteiro.txt` e `notas.md` e o commit `Episódio AAAA-MM-DD` na `main`.
3. Actions: a execução de "Gerar episódio e publicar feed" terminou com ✓ (3 a 5 minutos). Se ficar em "Waiting", aprove o ambiente `github-pages`.
4. Releases: existe `ep-AAAA-MM-DD` com o MP3 (cerca de 9 MB).
5. A página e o `feed.xml` mostram o episódio; no app Podcasts, puxe a tela para atualizar.

Se algo falhar, veja "Solução de problemas". Para repetir a tarefa fora do horário, peça ao Claude para executá-la; se a pasta do dia já existir, use o marcador `refazer`.

## Novo podcast com o mesmo pipeline

`docs/prompt-novo-podcast.md` traz um prompt pronto para criar outro podcast (outro repositório, feed, escopo e tarefa agendada), reaproveitando os scripts deste repositório.

## Compartilhar com colegas

- **Link da página do podcast** (`https://volmarsegundo-source.github.io/radar-ia/`) ou da página de um episódio (`.../ep/ep-AAAA-MM-DD/`): abre no navegador com player, notas e links, e tem os botões Assinar e Compartilhar. Funciona bem no WhatsApp e no Teams (com prévia da capa).
- **Quem quer ouvir no app:** botão "Assinar no Apple Podcasts" da página (iPhone/Mac), ou "Copiar endereço do feed" e "Seguir por URL" em outros apps.
- **Alcance maior (opcional):** retirar `itunes:block` do feed e cadastrar o programa no Apple Podcasts Connect e no Spotify gera links públicos e páginas web nativas, mas o programa fica público e passa por revisão das plataformas; confira antes as regras de conteúdo gerado por IA e a política da sua empresa.
- **Endereço mais curto (opcional):** domínio próprio no GitHub Pages (Settings › Pages › Custom domain).

## Ajustes

Em Settings › Secrets and variables › Actions › **Variables**:

| Variável | Padrão | Exemplos |
|---|---|---|
| `TTS_VOICE_RAFA` | `pt-BR-Chirp3-HD-Charon` (masculina) | `pt-BR-Chirp3-HD-Orus`, `pt-BR-Chirp3-HD-Fenrir` |
| `TTS_VOICE_CAMILA` | `pt-BR-Chirp3-HD-Kore` (feminina) | `pt-BR-Chirp3-HD-Aoede`, `pt-BR-Chirp3-HD-Leda` |
| `TTS_VOICE` | igual à do Rafa | voz do modo narrador (roteiro sem rótulos) |
| `TTS_RATE` | `1.0` | `1.1` para ouvir um pouco mais rápido |

Em `.github/workflows/episodio.yml`: `KEEP_EPISODES` (padrão 12) define quantos episódios ficam no feed.

Título e descrição do podcast ficam em `SHOW_TITLE` e `SHOW_DESC` no `scripts/build_feed.py` (mudam o feed e a página; rode o workflow manualmente para publicar, porque só alterações em `episodes/**` o disparam).

Escopo, tom, tamanho do roteiro e horário mudam na **tarefa agendada** (pedir ao Claude para atualizá-la), não neste repositório.

## Formato do roteiro

O arquivo `episodes/AAAA-MM-DD/roteiro.txt` é um diálogo:

```
# Bloco 1 — Visão geral da IA no mundo
RAFA: Bom dia! Você está ouvindo o Radar de IA e Tecnologia...

CAMILA: E eu sou a Camila. Um aviso rápido: nós dois somos apresentadores virtuais...

# Bloco 2 — Aprofundamento: engenharia de software e arquitetura empresarial
RAFA: ...

# Fechamento — O que levar para os clientes
CAMILA: Insight para levar ao cliente: ...
```

- Cada fala fica numa linha que começa com `RAFA: ` ou `CAMILA: `, com linha em branco entre falas.
- Linhas que começam com `# ` são marcadores de bloco: não são faladas e geram uma pausa longa.
- Linhas sem rótulo continuam a fala anterior. Um roteiro sem nenhum rótulo é lido inteiro por uma voz (modo narrador).
- Escreva para ser ouvido: frases curtas, números e siglas como devem ser lidos, sem URLs nem markdown.
- O arquivo `notas.md` traz as notas do episódio (1ª linha = nome da Release; o título no app é montado pelo `build_feed.py` com número e período, veja `docs/arquitetura.md`; o resto vira a descrição no app, com listas, negrito e links).
- Tamanho e marcação dos insights ("Insight para levar ao cliente:", fechamento) são definidos na tarefa agendada e em `CLAUDE.md`.
- Para trocar as vozes, use as variáveis `TTS_VOICE_RAFA` e `TTS_VOICE_CAMILA` (seção Ajustes). As vozes Chirp 3 HD disponíveis estão na documentação do Google Cloud Text-to-Speech.

## Solução de problemas

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| Episódio não aparece no app | Workflow falhou ou o app ainda não atualizou | Veja a aba Actions; se passou, no app Podcasts puxe a tela para atualizar o programa |
| Workflow falha em "Gerar áudio dos episódios novos" | Chave ausente, inválida ou sem a API ativada; cota estourada | Confira o secret `GOOGLE_TTS_API_KEY`, a API ativada e o log da etapa |
| Workflow falha em "deploy-pages" | Pages não está em Source: GitHub Actions | Ajuste em Settings › Pages e dê push de novo |
| A tarefa agendada não publicou o roteiro | Falha de acesso ao repositório | A mensagem final da tarefa traz o erro e o roteiro em anexo; copie para `episodes/` e faça push |
| Áudio cortado ou com pronúncia estranha | Texto com siglas, URLs ou símbolos | Reescreva o trecho em `roteiro.txt` (números por extenso, sem URLs) e refaça o episódio |
| Uma fala saiu com a voz errada ou o locutor não troca | Rótulo ausente, com erro de digitação ou em minúsculas fora do padrão `RAFA:` / `CAMILA:` | Corrija o rótulo no `roteiro.txt` e refaça o episódio |
| Workflow falha com erro HTTP 429 do Google | Limite de taxa da API (o script já tenta de novo até 6 vezes) | Rode de novo pouco depois; se persistir, verifique a cota no Google Cloud |
| Quero ouvir o MP3 sem o app | — | Baixe da Release `ep-AAAA-MM-DD` na página de Releases do repositório |

## Refazer um episódio

O workflow ignora episódios que já têm Release. Para regerar, sem abrir o GitHub:

1. Edite `episodes/AAAA-MM-DD/roteiro.txt` (se necessário) e crie um arquivo vazio `episodes/AAAA-MM-DD/refazer`.
2. Faça push na `main`. O workflow apaga a Release e a tag, gera o áudio de novo, publica e remove o marcador sozinho.

(Alternativa manual: apague a Release `ep-AAAA-MM-DD` e a tag em Releases/Tags e rode o workflow em Actions.)

## Quando o workflow roda

Em todo push na `main` que altere `episodes/**`, `scripts/**`, `assets/**` ou o próprio workflow. Mudar título, descrição ou visual da página (`scripts/build_feed.py`) republica o site sem gerar áudio novo, porque episódios com Release são ignorados.

## Rotação da chave do Google

1. No Google Cloud, crie uma nova chave de API com a mesma restrição e apague a antiga.
2. Atualize o secret `GOOGLE_TTS_API_KEY` no GitHub.
3. Dê um push em `episodes/**` ou rode o workflow manualmente para confirmar.

## Custos

| Item | Custo |
|---|---|
| Google Cloud TTS (Chirp 3 HD) | Grátis até 1 milhão de caracteres/mês; um episódio usa ~17 mil (cerca de 1,7% da cota) |
| GitHub (repositório público, Actions, Releases, Pages) | Grátis |
| Tarefa agendada do Claude | Consome o uso normal da sua assinatura do Claude |

## Testar localmente

```bash
export GOOGLE_TTS_API_KEY=...            # chave de API do Google
python3 scripts/tts.py episodes/AAAA-MM-DD   # gera episodes/AAAA-MM-DD/episodio.mp3 (não versionado)
```

Requer Python 3 e ffmpeg. O arquivo `episodio.mp3` está no `.gitignore`.
