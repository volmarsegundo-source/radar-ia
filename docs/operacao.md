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
- Poucos minutos depois: o episódio aparece no app Podcasts.
- O documento escrito, com todos os links, fica na lista de artefatos do Claude.

## Ajustes

Em Settings › Secrets and variables › Actions › **Variables**:

| Variável | Padrão | Exemplos |
|---|---|---|
| `TTS_VOICE` | `pt-BR-Chirp3-HD-Charon` (masculina) | `pt-BR-Chirp3-HD-Orus` (masculina), `pt-BR-Chirp3-HD-Kore` (feminina) |
| `TTS_RATE` | `1.0` | `1.1` para ouvir um pouco mais rápido |

Em `.github/workflows/episodio.yml`: `KEEP_EPISODES` (padrão 12) define quantos episódios ficam no feed.

Escopo, tom, tamanho do roteiro e horário mudam na **tarefa agendada** (pedir ao Claude para atualizá-la), não neste repositório.

## Solução de problemas

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| Episódio não aparece no app | Workflow falhou ou o app ainda não atualizou | Veja a aba Actions; se passou, no app Podcasts puxe a tela para atualizar o programa |
| Workflow falha em "Gerar áudio dos episódios novos" | Chave ausente, inválida ou sem a API ativada; cota estourada | Confira o secret `GOOGLE_TTS_API_KEY`, a API ativada e o log da etapa |
| Workflow falha em "deploy-pages" | Pages não está em Source: GitHub Actions | Ajuste em Settings › Pages e dê push de novo |
| A tarefa agendada não publicou o roteiro | Falha de acesso ao repositório | A mensagem final da tarefa traz o erro e o roteiro em anexo; copie para `episodes/` e faça push |
| Áudio cortado ou com pronúncia estranha | Texto com siglas, URLs ou símbolos | Reescreva o trecho em `roteiro.txt` (números por extenso, sem URLs) e refaça o episódio |
| Quero ouvir o MP3 sem o app | — | Baixe da Release `ep-AAAA-MM-DD` na página de Releases do repositório |

## Refazer um episódio

O workflow ignora episódios que já têm Release. Para regerar:

1. Em Releases, apague a Release `ep-AAAA-MM-DD` e também a tag com o mesmo nome (Tags › apagar).
2. Edite `episodes/AAAA-MM-DD/roteiro.txt` (se necessário) e faça push na `main`; qualquer alteração em `episodes/**` dispara o workflow.

## Rotação da chave do Google

1. No Google Cloud, crie uma nova chave de API com a mesma restrição e apague a antiga.
2. Atualize o secret `GOOGLE_TTS_API_KEY` no GitHub.
3. Dê um push em `episodes/**` ou rode o workflow manualmente para confirmar.

## Custos

| Item | Custo |
|---|---|
| Google Cloud TTS (Chirp 3 HD) | Grátis até 1 milhão de caracteres/mês; um episódio usa ~7 mil (cerca de 0,7% da cota) |
| GitHub (repositório público, Actions, Releases, Pages) | Grátis |
| Tarefa agendada do Claude | Consome o uso normal da sua assinatura do Claude |

## Testar localmente

```bash
export GOOGLE_TTS_API_KEY=...            # chave de API do Google
python3 scripts/tts.py episodes/AAAA-MM-DD   # gera episodes/AAAA-MM-DD/episodio.mp3 (não versionado)
```

Requer Python 3 e ffmpeg. O arquivo `episodio.mp3` está no `.gitignore`.
