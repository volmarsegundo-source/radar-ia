# Radar de IA & Tecnologia — podcast semanal

Conversa semanal de cerca de 15 minutos sobre IA, pensada para ouvir offline no iPhone e no Apple Watch no deslocamento e na academia. Dois apresentadores virtuais (vozes geradas por IA), Rafa e Camila, conversam em dois blocos:

1. **Visão geral da IA no mundo:** as principais notícias da semana.
2. **Aprofundamento:** o que está acontecendo, e qual o impacto da IA, em **engenharia de software** e em **arquitetura empresarial**.

A Camila explica cada conceito novo (o que é e quem já usa), e as fontes são citadas durante a conversa. As notas de cada episódio, com todos os links, aparecem no próprio app Podcasts.

Toda segunda-feira às 8h13 (horário de São Paulo) uma tarefa agendada do Claude pesquisa a semana e publica dois produtos:

- um **documento escrito** com destaques, resumos e links (publicado pelo Claude);
- um **episódio de podcast**, gerado automaticamente por este repositório.

**Feed (para colar no app Podcasts):** `https://volmarsegundo-source.github.io/radar-ia/feed.xml`

## Status

| Item | Situação |
|---|---|
| Tarefa agendada "Resumo semanal de IA e tecnologia" | Ativa, segundas 8h13 (America/Sao_Paulo) |
| Geração de áudio (Google Cloud TTS, Chirp 3 HD, duas vozes) | Funcionando; validada com o episódio de teste em formato conversa |
| Publicação (Releases + GitHub Pages) | Funcionando |
| Episódios | `2026-10-30` (teste, narrador único) e `2026-10-30-dialogo` (teste, formato conversa); o primeiro automático sai em 02/11/2026 |

## Documentação

| Arquivo | Conteúdo |
|---|---|
| [`docs/arquitetura.md`](docs/arquitetura.md) | Componentes, fluxo de dados, decisões e alternativas descartadas, limites |
| [`docs/operacao.md`](docs/operacao.md) | Configuração inicial, uso no iPhone/Watch, formato do roteiro, ajustes, solução de problemas, custos |
| [`CLAUDE.md`](CLAUDE.md) | Guia para o Claude: regras do projeto, formato do episódio e limitações do ambiente |

## Visão geral

```
Tarefa agendada do Claude (segunda 8h13) ──push──▶ episodes/AAAA-MM-DD/{roteiro.txt, notas.md}
                                                        │
                                      GitHub Actions ◀──┘
                                      1. Google Cloud TTS: uma voz por locutor (RAFA, CAMILA) → MP3 único
                                      2. Release "ep-AAAA-MM-DD" (arquivo permanente)
                                      3. GitHub Pages: feed.xml (notas com links) + últimos 12 episódios
                                                        │
                                      App Podcasts (iPhone / Apple Watch) ◀── segue o feed
```

## Estrutura do repositório

```
.github/workflows/episodio.yml   workflow: gera áudio, cria Release, publica o feed
scripts/tts.py                   roteiro (diálogo) → MP3 (Google TTS, duas vozes, pausas, ffmpeg)
scripts/build_feed.py            Releases → feed.xml (notas em HTML) + index.html
assets/cover.png                 capa do podcast (1400×1400)
episodes/AAAA-MM-DD/             um diretório por episódio (roteiro.txt, notas.md)
docs/                            documentação
CLAUDE.md                        guia para o Claude
```

## Formato do roteiro (resumo)

```
# Bloco 1 — Visão geral da IA no mundo
RAFA: fala do Rafa, numa linha.

CAMILA: fala da Camila, numa linha.

# Bloco 2 — Aprofundamento: engenharia de software e arquitetura empresarial
RAFA: ...
```

Linhas com `# ` marcam a mudança de bloco (não são faladas; geram uma pausa longa). Detalhes em [`docs/operacao.md`](docs/operacao.md).

## Adicionar um episódio manualmente

1. Crie `episodes/AAAA-MM-DD/roteiro.txt` no formato acima.
2. Crie `episodes/AAAA-MM-DD/notas.md` (1ª linha `# Título do episódio`; o restante são as notas com links).
3. Faça push na `main`. O workflow gera o áudio e atualiza o feed em poucos minutos.

Configuração inicial, ajustes e solução de problemas: [`docs/operacao.md`](docs/operacao.md).
