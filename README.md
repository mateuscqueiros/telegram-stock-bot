# Workshop: Bot Telegram B3 — 1 hora no Cursor

Template do workshop HCode. **O código do bot ainda não existe** — você vai construí-lo na aula usando o **Agent** do Cursor.

## O que já vem pronto

| Arquivo | Descrição |
|---|---|
| `AGENTS.md` | Regras e convenções para o Agent |
| `bot/config.py` | Leitura de variáveis de ambiente |
| `requirements.txt` | Dependências Python |
| `.env.example` | Modelo de configuração |

## O que você constrói na aula

| Arquivo | Bloco | O que faz |
|---|---|---|
| `bot/main.py` | 2 e 4 | Inicia o bot e registra handlers |
| `bot/handlers/commands.py` | 2 e 3 | `/start`, `/help`, `/cotacao` |
| `bot/quotes.py` | 3 | Consulta cotações na brapi.dev |
| `bot/handlers/alerts.py` | 4 | `/alerta` + JobQueue |

## Pré-requisitos (faça ANTES da aula)

### Software

- [Cursor](https://cursor.com) instalado e logado (com **Agent** habilitado)
- Python 3.11+ — `python --version`
- Git — `git --version`
- Telegram no celular (para testar o bot)

### Contas e tokens

| Item | Como obter | Obrigatório |
|---|---|---|
| Token Telegram | [@BotFather](https://t.me/BotFather) → `/newbot` | Sim |
| Token brapi.dev | [brapi.dev](https://brapi.dev) → dashboard | Recomendado |
| Conta GitHub | Para clonar este repo | Sim |

## Passo a passo — download e setup

### 1. Clonar

```bash
git clone -b starter git@github.com:mateuscqueiros/telegram-stock-bot.git
cd telegram-stock-bot
```

### 2. Abrir no Cursor

**File → Open Folder** → selecione a pasta clonada.

### 3. Ambiente Python

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Configurar `.env`

```bash
cp .env.example .env               # Windows: copy .env.example .env
```

Edite o `.env` (nunca o `.env.example`):

```env
TELEGRAM_TOKEN=seu_token_do_botfather
BRAPI_TOKEN=seu_token_brapi
ALERT_INTERVAL_SECONDS=60
```

### 5. Smoke test

```bash
python -c "import telegram, httpx; print('OK')"
```

Se aparecer `OK`, o ambiente está pronto. O bot **ainda não roda** — você constrói o código na aula.

## Claude Code no Cursor

Na aula você usa o **Agent** do Cursor (não é um app separado):

| Conceito | No Cursor |
|---|---|
| Agent | **Agent mode** — edita arquivos e roda terminal |
| Planejar | **Plan mode** — propõe passos sem alterar código |
| Contexto | `@AGENTS.md`, `@bot/config.py` |
| Validar | `python -m bot.main` + testar no Telegram |

Fluxo: **Plan → Agent → terminal → Telegram → iterar com `@arquivo`**

## Roteiro da aula (60 min)

### Bloco 1 — Abertura (0–5 min)

- Explorar a estrutura do repo
- Plan mode: *"O que falta para o bot responder /start?"*
- Agent mode: *"Implemente o que planejamos"*

### Bloco 2 — Bot vivo (5–20 min)

> Leia @AGENTS.md. Implemente `/start` e `/help` em `bot/handlers/commands.py` e registre em `bot/main.py`. Use o token de `bot/config.py`.

```bash
python -m bot.main
```

Testar `/start` e `/help` no Telegram.

### Bloco 3 — `/cotacao` (20–40 min)

> Crie `bot/quotes.py` com `async def get_quote(ticker: str)` usando httpx e `https://brapi.dev/api/quote/{ticker}`. Trate ticker inválido e erro 401 com mensagem clara.

> Adicione `/cotacao` em `commands.py`: recebe o ticker, chama `get_quote` e responde com nome, preço em R$ e variação %.

Testar: `/cotacao PETR4`, `/cotacao VALE3`, `/cotacao XXXX`

### Bloco 4 — Alerta (40–55 min)

> Adicione `/alerta TICKER PRECO` em `bot/handlers/alerts.py`. Guarde 1 alerta por chat em memória. Use JobQueue para checar a cada 60s; quando preço >= limite, envie mensagem no chat. Registre em `main.py`.

Testar: `/alerta PETR4 0.01`

### Bloco 5 — Fechamento (55–60 min)

- Recapitular: Plan → Agent → terminal → Telegram
- Q&A

## Solução

Se travar, consulte a branch `main`:

```bash
git fetch origin
git checkout main
```

Ou veja direto no GitHub: [branch main](https://github.com/mateuscqueiros/telegram-stock-bot/tree/main)

## Troubleshooting

| Problema | Solução |
|---|---|
| `KeyError: TELEGRAM_TOKEN` | Crie `.env` a partir de `.env.example` |
| `InvalidToken` | Token errado no `.env` |
| Bot não responde | `python -m bot.main` precisa estar rodando |
| brapi 401 | Adicione `BRAPI_TOKEN` ou use PETR4/VALE3/MGLU3/ITUB4 |
| JobQueue desativado | `pip install "python-telegram-bot[job-queue]"` |
