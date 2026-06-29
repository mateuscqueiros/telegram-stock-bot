# Guia do Instrutor — Workshop Bot Telegram B3

Workshop de **60 minutos** focado em **Claude Code no Cursor** (não em Python).

Repositório: [mateuscqueiros/telegram-stock-bot](https://github.com/mateuscqueiros/telegram-stock-bot)

| Branch | Uso |
|---|---|
| `starter` | Alunos clonam — Agent constrói o código na aula |
| `main` | Solução completa para consulta |

---

## Mensagem central da aula

> **Alunos não digitam código. Eles dirigem o Agent.**

- Colam prompts prontos do README
- Clicam **Accept** nas edições propostas
- Rodam `python -m bot.main` e testam no Telegram
- Se falhar, colam prompt de correção com o erro

---

## Cursor gratuito — o que dizer à turma

| Pergunta do aluno | Resposta |
|---|---|
| Preciso pagar? | **Não.** Plano Hobby grátis, sem cartão |
| Preciso do Cursor? | **Sim** — é a ferramenta da aula (alternativa ao VS Code + extensões) |
| O Agent funciona grátis? | Sim, com limite mensal — ~5 prompts cabem na aula |
| Bateu o limite? | Use Chat do Cursor, pair programming, ou mostre no projetor |
| Sou estudante? | E-mail `.edu` → 1 ano de Pro grátis no Cursor |

**Não exija assinatura paga.** Avise sobre o limite do Agent no início.

---

## Antes da turma (checklist 24h)

- [ ] Repo acessível
- [ ] Branch `starter` como padrão no GitHub
- [ ] Enviar [CHECKLIST_ALUNOS.md](CHECKLIST_ALUNOS.md)
- [ ] Token de demo do BotFather (backup)
- [ ] Testar brapi com e sem `BRAPI_TOKEN`
- [ ] Testar clone limpo da branch `starter`
- [ ] Preparar projetor com Agent aberto (demo ao vivo)

---

## Bloco 1 — Abertura (0–5 min)

1. **"Vocês não vão digitar Python hoje"** — vão aprender a dirigir o AI
2. Mostrar repo `starter` (só `config.py` + `AGENTS.md`)
3. Plan mode: *"O que falta para o bot responder /start?"*
4. Agent mode: *"Implemente seguindo @AGENTS.md"*
5. Explicar: Cursor gratuito, limite do Agent, `@AGENTS.md`

---

## Bloco 2 — Bot vivo (5–20 min)

**Um prompt só (cole no Agent):**

> Leia @AGENTS.md e @bot/config.py. Crie `bot/handlers/commands.py` com `/start` e `/help` e `bot/main.py` registrando os handlers. Use async, python-telegram-bot v21, token de config. Implemente tudo sem pedir confirmação.

**Validar:** `python -m bot.main` → `/start`, `/help`

**Prompt de correção (se necessário):**

> O bot falhou com este erro: [erro]. Corrija seguindo @AGENTS.md.

---

## Bloco 3 — `/cotacao` (20–40 min)

**Um prompt só:**

> Leia @AGENTS.md. Crie `bot/quotes.py` com `get_quote(ticker)` via httpx e brapi.dev. Adicione `/cotacao` em `commands.py` formatando preço (R$) e variação (%). Trate erro 401 e ticker inválido em português. Implemente tudo.

**Validar:** `/cotacao PETR4`, `/cotacao VALE3`, `/cotacao XXXX`

---

## Bloco 4 — Alerta (40–55 min)

**Um prompt só:**

> Leia @AGENTS.md e @bot/main.py. Crie `bot/handlers/alerts.py` com `/alerta TICKER PRECO` (1 alerta por chat, memória). JobQueue a cada 60s; quando preço >= limite, envie mensagem. Registre em `main.py`. Implemente tudo.

**Validar:** `/alerta PETR4 0.01`

---

## Bloco 5 — Fechamento (55–60 min)

1. Recapitular: **prompt → Agent → Accept → terminal → Telegram**
2. Mostrar branch `main` no GitHub
3. Q&A

---

## Troubleshooting

| Problema | Solução |
|---|---|
| Aluno sem Cursor | Instalar na hora (plano grátis) ou pair programming |
| Limite do Agent atingido | Chat do Cursor, colega, ou projetor do instrutor |
| Aluno editando código à mão | Redirecionar: "cole um prompt no Agent" |
| `KeyError: TELEGRAM_TOKEN` | Criar `.env` |
| brapi 401 | `BRAPI_TOKEN` ou tickers gratuitos |
| Bot não responde | `python -m bot.main` rodando |

---

## Plano B (45 min)

Prioridade: **`/cotacao`** > alerta > Q&A

Um prompt único para blocos 2+3 se a turma for lenta:

> Leia @AGENTS.md e @bot/config.py. Implemente bot completo com /start, /help, /cotacao (brapi.dev) em commands.py, quotes.py e main.py. Async, python-telegram-bot v21.

---

## Material de apoio

| Arquivo | Uso |
|---|---|
| [CHECKLIST_ALUNOS.md](CHECKLIST_ALUNOS.md) | E-mail 48h antes |
| [README starter](https://github.com/mateuscqueiros/telegram-stock-bot/blob/starter/README.md) | Prompts para colar |
| [AGENTS.md](../AGENTS.md) | Contexto do Agent |
