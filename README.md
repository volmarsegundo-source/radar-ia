# Radar de IA & Tecnologia — podcast semanal

Pipeline que transforma o roteiro semanal (escrito pela tarefa agendada do Claude) num episódio de podcast que o app Podcasts do iPhone e do Apple Watch baixam sozinhos.

```
Claude (segunda 8h13) ──commit──▶ episodes/AAAA-MM-DD/{roteiro.txt, notas.md}
                                         │
                       GitHub Actions ◀──┘
                       1. Google Cloud TTS (Chirp 3 HD, pt-BR) → MP3 único
                       2. Release "ep-AAAA-MM-DD" (arquivo permanente de todos os episódios)
                       3. GitHub Pages: feed.xml + últimos 12 episódios
                                         │
                       App Podcasts (iPhone/Watch) ◀── segue o feed
```

## Configuração (uma vez)

1. **Chave do Google Cloud TTS**
   - Em console.cloud.google.com: crie um projeto, ative a **Cloud Text-to-Speech API** e vincule uma conta de faturamento (o uso fica dentro do nível gratuito: 1 milhão de caracteres/mês nas vozes Chirp 3 HD; um episódio tem cerca de 7 mil).
   - APIs e serviços › Credenciais › Criar credenciais › **Chave de API**. Restrinja a chave à Cloud Text-to-Speech API.
   - Recomendado: crie um alerta de orçamento de US$ 1 em Faturamento › Orçamentos.
2. **Secret no GitHub**: Settings › Secrets and variables › Actions › New repository secret › nome `GOOGLE_TTS_API_KEY`.
3. **GitHub Pages**: Settings › Pages › Source: **GitHub Actions**.
4. Rode a primeira vez: aba Actions › "Gerar episódio e publicar feed" › Run workflow.
5. **No iPhone**: Podcasts › Biblioteca › ⋯ / Editar › **Seguir programa por URL** › `https://volmarsegundo-source.github.io/radar-ia/feed.xml`.
6. **No Apple Watch** (app Watch no iPhone › Podcasts): deixe o programa em "Personalizado" com download dos episódios mais recentes. O Watch baixa quando está carregando.

## Ajustes opcionais (Settings › Secrets and variables › Actions › Variables)

| Variável | Padrão | Exemplo |
|---|---|---|
| `TTS_VOICE` | `pt-BR-Chirp3-HD-Charon` (masculina) | `pt-BR-Chirp3-HD-Kore` (feminina), `pt-BR-Chirp3-HD-Orus` |
| `TTS_RATE` | `1.0` | `1.1` para ouvir um pouco mais rápido |

## Armazenamento

- Cada episódio ≈ 3,5 MB (64 kbps mono). Um ano ≈ 200 MB.
- Os MP3s ficam como anexos das **Releases** (não entram no histórico do git; limite de 2 GB por arquivo), então o repositório continua pequeno.
- O site (Pages) é reconstruído a cada execução só com os últimos 12 episódios.
- O feed tem `itunes:block` para não aparecer no diretório da Apple, mas o repositório e o site são públicos: não coloque conteúdo confidencial aqui.
