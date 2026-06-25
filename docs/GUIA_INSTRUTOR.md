# Guia do Instrutor — Workshop Bot Telegram B3

Workshop de **60 minutos** no Cursor. Repositório: [mateuscqueiros/telegram-stock-bot](https://github.com/mateuscqueiros/telegram-stock-bot)

| Branch | Uso |
|---|---|
| `starter` | Alunos clonam e constroem o bot na aula |
| `main` | Solução completa para consulta |

---

## Antes da turma (checklist 24h)

- [ ] Repo acessível: https://github.com/mateuscqueiros/telegram-stock-bot
- [ ] Branch `starter` como padrão no GitHub (Settings → Default branch)
- [ ] Enviar [CHECKLIST_ALUNOS.md](CHECKLIST_ALUNOS.md) por e-mail/Slack
- [ ] Token de demo do BotFather (backup)
- [ ] Testar brapi com e sem `BRAPI_TOKEN`
- [ ] Testar clone limpo da branch `starter` (ver seção abaixo)

---

## Claude Code no Cursor (Bloco 1 — explicar em 2 min)

Na aula **não se instala** o Claude Code da Anthropic. O fluxo é no **Agent do Cursor**:

| Conceito | No Cursor |
|---|---|
| Agent | **Agent mode** — edita arquivos e roda terminal |
| Planejar | **Plan mode** — propõe passos sem alterar código |
| Contexto | `@AGENTS.md`, `@bot/config.py` |
| Validar | `python -m bot.main` + Telegram no celular |

Fluxo: **Plan → Agent → terminal → Telegram → iterar com `@arquivo`**

---

## Roteiro da aula (60 min)

### Bloco 1 — Abertura (0–5 min)

1. Mostrar estrutura do repo `starter` (só `config.py` + `AGENTS.md`)
2. Plan mode: *"O que falta para o bot responder /start?"*
3. Agent mode: *"Implemente o que planejamos"*
4. Explicar `@AGENTS.md`

### Bloco 2 — Bot vivo (5–20 min)

**Prompt (copiar no chat):**

> Leia @AGENTS.md. Implemente `/start` e `/help` em `bot/handlers/commands.py` e registre em `bot/main.py`. Use o token de `bot/config.py`.

**Validar:**

```bash
python -m bot.main
```

Testar `/start` e `/help` no Telegram.

### Bloco 3 — `/cotacao` (20–40 min)

**Prompt 1:**

> Crie `bot/quotes.py` com `async def get_quote(ticker: str)` usando httpx e `https://brapi.dev/api/quote/{ticker}`. Trate ticker inválido e erro 401 com mensagem clara.

**Prompt 2:**

> Adicione `/cotacao` em `commands.py`: recebe o ticker, chama `get_quote` e responde com nome, preço em R$ e variação %.

**Validar:** `/cotacao PETR4`, `/cotacao VALE3`, `/cotacao XXXX`

### Bloco 4 — Alerta (40–55 min)

**Prompt:**

> Adicione `/alerta TICKER PRECO` em `bot/handlers/alerts.py`. Guarde 1 alerta por chat em memória. Use JobQueue para checar a cada 60s; quando preço >= limite, envie mensagem no chat. Registre em `main.py`.

**Validar:** `/alerta PETR4 0.01` (limite baixo para demo rápida)

### Bloco 5 — Fechamento (55–60 min)

1. Recapitular: Plan → Agent → terminal → Telegram
2. Mostrar branch `main` no GitHub
3. Q&A

---

## Troubleshooting (slide ou quadro)

| Problema | Solução |
|---|---|
| `KeyError: TELEGRAM_TOKEN` | Criar `.env` a partir de `.env.example` |
| `InvalidToken` | Token errado no `.env` |
| Bot não responde | `python -m bot.main` precisa estar rodando |
| brapi 401 (ex: RANI3) | Adicionar `BRAPI_TOKEN` ou usar PETR4/VALE3/MGLU3/ITUB4 |
| JobQueue desativado | `pip install "python-telegram-bot[job-queue]"` |

---

## Teste do clone starter (instrutor)

```bash
cd /tmp
rm -rf telegram-stock-bot-test
git clone -b starter git@github.com:mateuscqueiros/telegram-stock-bot.git telegram-stock-bot-test
cd telegram-stock-bot-test
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -c "import telegram, httpx; print('OK')"
```

Resultado esperado: `OK` e ausência de `bot/main.py`.

---

## Material de apoio

| Arquivo | Uso |
|---|---|
| [CHECKLIST_ALUNOS.md](CHECKLIST_ALUNOS.md) | E-mail 48h antes |
| [README starter](https://github.com/mateuscqueiros/telegram-stock-bot/blob/starter/README.md) | Alunos seguem na aula |
| [README main](https://github.com/mateuscqueiros/telegram-stock-bot/blob/main/README.md) | Referência da solução |
| [AGENTS.md](../AGENTS.md) | Contexto para o Agent |

## Plano B (se faltar tempo)

Prioridade: **`/cotacao` funcionando** > alerta > Q&A

Com 45 min: bot + `/cotacao` + testar no celular.
