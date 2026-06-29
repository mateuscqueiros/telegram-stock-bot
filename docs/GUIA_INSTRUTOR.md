# Guia do Instrutor — Workshop Bot Telegram B3 (Claude Code)

Workshop de **60 minutos** com **Claude Code CLI** como ferramenta principal.

Repositório: [mateuscqueiros/telegram-stock-bot](https://github.com/mateuscqueiros/telegram-stock-bot)

| Branch | Uso |
|---|---|
| `starter` | Alunos clonam — Claude Code constrói o bot na aula |
| `main` | Solução completa |

---

## Mensagem central

> **Alunos não digitam código. Eles dirigem o Claude Code no terminal.**

- Enviam prompts (prontos no README)
- Aprovam diffs propostos pelo Claude Code
- Rodam `python -m bot.main` e testam no Telegram
- Se falhar: `claude "O bot falhou com: [erro]. Corrija seguindo CLAUDE.md."`

---

## Pré-requisito assumido

Cada aluno tem **Claude Code** (Pro, Max ou API). Não é necessário Cursor.

Arquivo de contexto do projeto: **`CLAUDE.md`** (equivalente ao que Cursor chama de AGENTS.md).

---

## Antes da turma

- [ ] Enviar [CHECKLIST_ALUNOS.md](CHECKLIST_ALUNOS.md)
- [ ] Confirmar que alunos instalaram `claude` e fizeram login
- [ ] Token de demo BotFather (backup)
- [ ] Testar clone da branch `starter`
- [ ] Demo ao vivo no projetor com `claude` na pasta do projeto

---

## Bloco 1 — Abertura (0–5 min)

1. **"Vocês não vão digitar Python"** — vão usar o Claude Code no terminal
2. Mostrar: `cd telegram-stock-bot && claude`
3. Mostrar `CLAUDE.md` — regras que o Claude lê automaticamente
4. Perguntar no chat: *"O que falta para o bot responder /start?"*
5. Pedir: *"Implemente seguindo CLAUDE.md"*

---

## Bloco 2 — Bot vivo (5–20 min)

```bash
claude "Leia CLAUDE.md e bot/config.py. Crie bot/handlers/commands.py com /start e /help e bot/main.py registrando os handlers. Use async, python-telegram-bot v21, token de config. Implemente tudo."
```

Validar: `python -m bot.main` → `/start`, `/help`

---

## Bloco 3 — `/cotacao` (20–40 min)

```bash
claude "Leia CLAUDE.md. Crie bot/quotes.py com get_quote(ticker) via httpx e brapi.dev. Adicione /cotacao em commands.py formatando preço (R$) e variação (%). Trate erro 401 e ticker inválido em português. Implemente tudo."
```

Validar: `/cotacao PETR4`, `/cotacao VALE3`, `/cotacao XXXX`

---

## Bloco 4 — Alerta (40–55 min)

```bash
claude "Leia CLAUDE.md e bot/main.py. Crie bot/handlers/alerts.py com /alerta TICKER PRECO (1 alerta por chat, memória). JobQueue a cada 60s; quando preço >= limite, envie mensagem. Registre em main.py. Implemente tudo."
```

Validar: `/alerta PETR4 0.01`

---

## Bloco 5 — Fechamento (55–60 min)

1. Recapitular: **prompt → Claude Code → diff → terminal → Telegram**
2. Mostrar branch `main` no GitHub
3. Mencionar outros ambientes: VS Code extension, claude.ai/code, desktop app
4. Q&A

---

## Troubleshooting

| Problema | Solução |
|---|---|
| `claude` não encontrado | Reinstalar; reiniciar terminal |
| Aluno sem Claude Code | Pair programming ou demo no projetor |
| Limite de uso | `claude -c` para continuar; ou mostrar solução na `main` |
| Aluno editando à mão | Redirecionar para `claude "..."` |
| brapi 401 | `BRAPI_TOKEN` ou tickers gratuitos |

---

## Plano B (45 min)

Um prompt único para blocos 2+3:

```bash
claude "Leia CLAUDE.md e bot/config.py. Implemente bot com /start, /help, /cotacao (brapi.dev) em commands.py, quotes.py e main.py. Async, python-telegram-bot v21."
```

---

## Outros ambientes Claude Code (mencionar no fechamento)

| Ambiente | Uso |
|---|---|
| **Terminal CLI** | Principal na aula (`claude`) |
| **VS Code extension** | Mesmo fluxo, diffs inline |
| **claude.ai/code** | Web, sem instalação local |
| **Desktop app** | Interface visual |
| **GitHub Actions** | Automação CI/CD |
