# Workshop: Bot Telegram B3 — Claude Code

**Você não vai digitar código.** Seu papel é **pilotar o Claude Code**: gerenciar a sessão, enviar prompts, aprovar mudanças e validar no terminal e no Telegram.

## O que você vai aprender

| Parte | Tempo | Foco |
|---|---|---|
| **1** | 15 min | Claude Code: sessão, atalhos, arquivos `.md`, subagentes |
| **2** | 15 min | Construir o bot via prompts |
| **3** | Aberta | Arquitetura, produção, prompt mestre |

O bot de cotações da B3 é o **projeto de prática**. O foco é **pilotar o Claude Code**.

---

## Pré-requisitos

| Item | Obrigatório |
|---|---|
| **Claude Code** (Pro, Max ou API) | Sim — [code.claude.com/docs](https://code.claude.com/docs) |
| Python 3.11+ | Sim |
| Git | Sim |
| Token Telegram ([@BotFather](https://t.me/BotFather)) | Sim |
| Token [brapi.dev](https://brapi.dev) | Recomendado |
| Cursor (ou VS Code) | Sim — terminal integrado |

---

## Regra de ouro da aula

```
Você NÃO escreve código → você PILOTA A SESSÃO do Claude Code
Você NÃO decora Python   → você VALIDA no terminal e no Telegram
Tarefa nova              → /clear (sessão nova)
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

No **Cursor**, terminal (**`` Ctrl+` ``**):

```bash
git clone -b starter git@github.com:mateuscqueiros/telegram-stock-bot.git
cd telegram-stock-bot
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env
python -c "import telegram, httpx; print('OK')"
```

Edite o **`.env`** no Cursor com seus tokens:
```env
TELEGRAM_TOKEN=seu_token_do_botfather
BRAPI_TOKEN=seu_token_brapi
```

---

## O que já vem pronto

| Arquivo | Descrição |
|---|---|
| `requirements.txt` | Dependências Python |
| `.env.example` | Modelo de configuração |
| `README.md` | Este roteiro |

**Não tem código do bot.** Você constrói na Parte 2 com o Claude Code.

---

# Parte 1 — Claude Code (15 min)

O palestrante explica conceitos. Siga na tela e experimente:

| Comando | O que faz |
|---|---|
| `claude` | Sessão interativa |
| `claude "tarefa"` | One-shot |
| `/context` | Ver o que ocupa a janela de contexto |
| `/clear` | Nova tarefa, sessão limpa |
| `/compact` | Resumir sessão longa sem perder o fio |
| `/rewind` | Voltar no tempo (código e/ou conversa) |
| `claude --continue` | Retomar última sessão |
| `claude --resume` | Escolher sessão anterior |

**Arquivos `.md`:** `CLAUDE.md` (regras permanentes), memórias escopadas como `telegram.md`.

Cheat-sheet completo: [docs/CLAUDE_CODE.md na main](https://github.com/mateuscqueiros/telegram-stock-bot/blob/main/docs/CLAUDE_CODE.md)

Ao final da Parte 1, o palestrante pede `/clear`.

---

# Parte 2 — Construir o bot (15 min)

**Cursor** → **File → Open Folder** → `telegram-stock-bot`  
Terminal — mantenha o venv ativo (`(.venv)` no prompt).

### Passo 1 — Criar CLAUDE.md

```bash
source .venv/Scripts/activate
claude "Leia o README.md. Crie um arquivo CLAUDE.md com as regras do nosso bot de cotações da B3 no Telegram. Inclua: mensagens em português, preço em reais com vírgula, usar a API brapi.dev, token do Telegram no .env, e os comandos /start, /help, /cotacao e /alerta. Crie só o CLAUDE.md por agora."
```

### Passo 2 — Bot vivo

```bash
claude "Leia CLAUDE.md. Faça o bot responder /start e /help no Telegram. O token está no .env. Implemente tudo."
python -m bot.main
```

Teste `/start` e `/help` no celular.

### Passo 3 — Cotação

```bash
claude "Leia CLAUDE.md. Faça o comando /cotacao PETR4 mostrar o nome da ação, o preço em reais e a variação do dia. Implemente tudo."
```

Teste: `/cotacao PETR4` · `/cotacao VALE3` · `/cotacao XXXX`

### Passo 4 — Alerta (se couber)

```bash
claude "Leia CLAUDE.md. Faça o comando /alerta PETR4 35 avisar no Telegram quando a ação atingir esse preço. Implemente tudo."
```

Teste: `/alerta PETR4 0.01`

### Se der erro

```bash
claude "Deu erro ao rodar o bot: [cole o erro]. Corrija seguindo CLAUDE.md."
```

Ao final da Parte 2, o palestrante pede `/clear`.

---

# Parte 3 — Arquitetura e prompt mestre (aberta)

Conduzida pelo palestrante:

- Documentar arquitetura do bot
- Pensar em ambiente de produção (Docker, env, polling vs webhook)
- **Reverse prompt engineering** — reconstruir o prompt que gera o bot inteiro

Referência: [docs/PROMPT_MESTRE.md na main](https://github.com/mateuscqueiros/telegram-stock-bot/blob/main/docs/PROMPT_MESTRE.md)

---

## Solução completa

[branch main](https://github.com/mateuscqueiros/telegram-stock-bot/tree/main)

---

## Troubleshooting

| Problema | Solução |
|---|---|
| `claude` não encontrado | Reinstale ou reinicie o terminal |
| Claude "esqueceu" uma regra | `/context` → `/clear` e reler `CLAUDE.md` |
| Limite de uso atingido | Aguarde reset ou use `claude --continue` |
| `KeyError: TELEGRAM_TOKEN` | Crie `.env` a partir de `.env.example` |
| Bot não responde | `python -m bot.main` precisa estar rodando |
| brapi 401 | Adicione `BRAPI_TOKEN` ou use PETR4/VALE3/MGLU3/ITUB4 |
