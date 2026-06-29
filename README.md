# Workshop: Bot Telegram B3 — Claude Code

**Você não vai digitar código.** Seu papel é **dirigir o Claude Code**: enviar prompts, aprovar as mudanças e validar no terminal e no Telegram.

## O que você vai aprender

- Instalar e usar o **Claude Code CLI** (`claude`)
- Dar contexto com **`CLAUDE.md`**
- Pedir implementações em linguagem natural
- Iterar: Claude Code → terminal → Telegram → corrigir com novo prompt

O bot de cotações da B3 é o **projeto de prática**, não o foco da aula.

---

## Pré-requisitos

| Item | Obrigatório |
|---|---|
| **Claude Code** (Pro, Max ou API) | Sim — [code.claude.com/docs](https://code.claude.com/docs) |
| Python 3.11+ | Sim |
| Git | Sim |
| Token Telegram ([@BotFather](https://t.me/BotFather)) | Sim |
| Token [brapi.dev](https://brapi.dev) | Recomendado |
| Editor de código (VS Code, Cursor, etc.) | Opcional — para ver os diffs |

---

## Regra de ouro da aula

```
Você NÃO escreve código → você ESCREVE PROMPTS no Claude Code
Você NÃO decora Python   → você VALIDA no terminal e no Telegram
```

---

## Instalar Claude Code

**Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**macOS / Linux:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Na primeira vez, rode `claude` e faça login na conta Anthropic.

---

## Setup do projeto (antes da aula)

```bash
git clone -b starter git@github.com:mateuscqueiros/telegram-stock-bot.git
cd telegram-stock-bot

python -m venv .venv
pip install -r requirements.txt

cp .env.example .env               # Windows CMD: copy .env.example .env
```

Ative o venv **antes** do `pip install` (escolha conforme seu terminal):

| Terminal | Comando |
|---|---|
| **Git Bash** (Windows) | `source .venv/Scripts/activate` |
| **PowerShell** (Windows) | `.venv\Scripts\Activate.ps1` |
| **CMD** (Windows) | `.venv\Scripts\activate.bat` |
| **Mac / Linux** | `source .venv/bin/activate` |

Edite o **`.env`**:
```env
TELEGRAM_TOKEN=seu_token_do_botfather
BRAPI_TOKEN=seu_token_brapi
```

Smoke test: `python -c "import telegram, httpx; print('OK')"`

---

## O que já vem pronto

| Arquivo | Descrição |
|---|---|
| `CLAUDE.md` | **Leia primeiro.** Regras que o Claude Code segue |
| `bot/config.py` | Leitura do `.env` |
| `requirements.txt` | Dependências |
| `.env.example` | Modelo de configuração |

## O que o Claude Code constrói na aula

| Arquivo | Bloco |
|---|---|
| `bot/main.py` | 2 e 4 |
| `bot/handlers/commands.py` | 2 e 3 |
| `bot/quotes.py` | 3 |
| `bot/handlers/alerts.py` | 4 |

---

## Roteiro — prompts para o Claude Code

Abra o terminal **na pasta do projeto** e use `claude` (modo interativo) ou `claude "prompt"` (one-shot).

### Bloco 1 (0–5 min) — Primeiro contato

```bash
cd telegram-stock-bot
claude
```

No chat interativo:
> O que falta neste projeto para ter um bot Telegram com /start? Leia CLAUDE.md.

Depois:
> Implemente o que descreveu, seguindo CLAUDE.md.

### Bloco 2 (5–20 min) — Bot vivo

One-shot ou no chat:

```bash
claude "Leia CLAUDE.md e bot/config.py. Crie bot/handlers/commands.py com /start e /help e bot/main.py registrando os handlers. Use async, python-telegram-bot v21, token de config. Implemente tudo."
```

Validar:
```bash
python -m bot.main
```
Teste `/start` e `/help` no Telegram.

Se der erro:
```bash
claude "O bot falhou com este erro: [cole o erro]. Corrija seguindo CLAUDE.md."
```

### Bloco 3 (20–40 min) — `/cotacao`

```bash
claude "Leia CLAUDE.md. Crie bot/quotes.py com get_quote(ticker) via httpx e brapi.dev. Adicione /cotacao em commands.py formatando preço (R$) e variação (%). Trate erro 401 e ticker inválido em português. Implemente tudo."
```

Teste: `/cotacao PETR4` · `/cotacao VALE3` · `/cotacao XXXX`

### Bloco 4 (40–55 min) — Alerta

```bash
claude "Leia CLAUDE.md e bot/main.py. Crie bot/handlers/alerts.py com /alerta TICKER PRECO (1 alerta por chat, memória). JobQueue a cada 60s; quando preço >= limite, envie mensagem. Registre em main.py. Implemente tudo."
```

Teste: `/alerta PETR4 0.01`

### Bloco 5 (55–60 min) — Fechamento

Recapitular: **prompt → Claude Code → aprovar diff → terminal → Telegram**

Solução: [branch main](https://github.com/mateuscqueiros/telegram-stock-bot/tree/main)

---

## Comandos úteis do Claude Code

| Comando | O que faz |
|---|---|
| `claude` | Modo interativo |
| `claude "tarefa"` | One-shot |
| `claude -c` | Continuar conversa anterior |
| `/help` | Ajuda dentro da sessão |
| `/clear` | Limpar histórico |

Docs: [code.claude.com/docs](https://code.claude.com/docs)

---

## Troubleshooting

| Problema | Solução |
|---|---|
| `claude` não encontrado | Reinstale ou reinicie o terminal |
| Limite de uso atingido | Aguarde reset ou use plano Max |
| `KeyError: TELEGRAM_TOKEN` | Crie `.env` a partir de `.env.example` |
| Bot não responde | `python -m bot.main` precisa estar rodando |
| brapi 401 | Adicione `BRAPI_TOKEN` ou use PETR4/VALE3/MGLU3/ITUB4 |
