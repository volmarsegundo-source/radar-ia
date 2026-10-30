# Radar de IA & Tecnologia — podcast semanal

Briefing semanal de notícias de IA e tecnologia (engenharia de software, aplicações corporativas, arquitetura empresarial), pensado para ouvir offline no iPhone e no Apple Watch no deslocamento e na academia.

Toda segunda-feira às 8h13 (horário de São Paulo) uma tarefa agendada do Claude pesquisa a semana e publica dois produtos:

- um **documento escrito** com destaques, resumos e links (publicado pelo Claude);
- um **episódio de podcast** de 7 a 10 minutos, gerado automaticamente por este repositório.

**Feed (para colar no app Podcasts):** `https://volmarsegundo-source.github.io/radar-ia/feed.xml`

## Status

| Item | Situação |
|---|---|
| Tarefa agendada "Resumo semanal de IA e tecnologia" | Ativa, segundas 8h13 (America/Sao_Paulo) |
| Geração de áudio (Google Cloud TTS, Chirp 3 HD) | Funcionando; validada com o episódio de teste |
| Publicação (Releases + GitHub Pages) | Funcionando |
| Episódios | `2026-10-30` (edição de teste); o primeiro automático sai em 02/11/2026 |

## Documentação

| Arquivo | Conteúdo |
|---|---|
| [`docs/arquitetura.md`](docs/arquitetura.md) | Componentes, fluxo de dados, decisões e alternativas descartadas, limites |
| [`docs/operacao.md`](docs/operacao.md) | Configuração inicial, uso no iPhone/Watch, ajustes, solução de problemas, custos |
| [`CLAUDE.md`](CLAUDE.md) | Guia para o Claude: regras do projeto e limitações do ambiente |

## Visão geral

```
Tarefa agendada do Claude (segunda 8h13) ──push──▶ episodes/AAAA-MM-DD/{roteiro.txt, notas.md}
                                                        │
                                      GitHub Actions ◀──┘
                                      1. Google Cloud TTS (Chirp 3 HD, pt-BR) → MP3 único
                                      2. Release "ep-AAAA-MM-DD" (arquivo permanente)
                                      3. GitHub Pages: feed.xml + últimos 12 episódios
                                                        │
                                      App Podcasts (iPhone / Apple Watch) ◀── segue o feed
```

## Estrutura do repositório

```
.github/workflows/episodio.yml   workflow: gera áudio, cria Release, publica o feed
scripts/tts.py                   roteiro → MP3 (Google TTS + ffmpeg)
scripts/build_feed.py            Releases → feed.xml + index.html
assets/cover.png                 capa do podcast (1400×1400)
episodes/AAAA-MM-DD/             um diretório por episódio (roteiro.txt, notas.md)
docs/                            documentação
CLAUDE.md                        guia para o Claude
```

## Adicionar um episódio manualmente

1. Crie `episodes/AAAA-MM-DD/roteiro.txt` (texto falado; parágrafos separados por linha em branco).
2. Crie `episodes/AAAA-MM-DD/notas.md` (1ª linha `# Título do episódio`; o restante são as notas com links).
3. Faça push na `main`. O workflow gera o áudio e atualiza o feed em poucos minutos.

Mais detalhes, configuração inicial e solução de problemas: [`docs/operacao.md`](docs/operacao.md).
