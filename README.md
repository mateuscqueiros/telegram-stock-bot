# Workshop: Bot Telegram B3 — Claude Code

**Você não vai digitar código.** Seu papel é **dirigir o Claude Code**: enviar prompts, aprovar as mudanças e validar no terminal e no Telegram.

## O que você vai aprender

- Criar **`CLAUDE.md`** — as regras do seu projeto (memória do Claude Code)
- Usar o **Claude Code CLI** (`claude`)
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
| Cursor (ou VS Code) | Sim — terminal integrado |

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

No **Cursor**, abra o terminal integrado (**`` Ctrl+` ``**) e rode na ordem:

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

**Não tem código do bot.** Você constrói tudo na aula com o Claude Code.

## O que você constrói na aula

| O quê | Bloco |
|---|---|
| `CLAUDE.md` | 0 — regras do projeto |
| Bot com `/start` e `/help` | 1 |
| Comando `/cotacao` | 2 |
| Comando `/alerta` | 3 |

---

## Roteiro — prompts para o Claude Code

**Cursor** → **File → Open Folder** → `telegram-stock-bot`  
Terminal (**`` Ctrl+` ``**) — mantenha o venv ativo (`(.venv)` no prompt).

> **Dica:** descreva **o que o bot deve fazer**. Depois do Bloco 0, o `CLAUDE.md` guarda as regras — basta pedir "Leia CLAUDE.md".

### Bloco 0 (0–10 min) — Criar as regras do projeto

Primeiro passo: **criar o `CLAUDE.md`** (você define como o bot deve funcionar).

```bash
source .venv/Scripts/activate
claude "Leia o README.md. Crie um arquivo CLAUDE.md com as regras do nosso bot de cotações da B3 no Telegram. Inclua: mensagens em português, preço em reais com vírgula, usar a API brapi.dev, token do Telegram no .env, e os comandos /start, /help, /cotacao e /alerta. Crie só o CLAUDE.md por agora."
```

Revise o arquivo gerado. Esse é **o seu** contexto — o Claude Code vai ler em toda a aula.

### Bloco 1 (10–25 min) — Bot vivo

```bash
claude "Leia CLAUDE.md. Faça o bot responder /start e /help no Telegram. O token está no .env. Implemente tudo."
python -m bot.main
```

Teste `/start` e `/help` no celular.

Se der erro:
```bash
claude "Deu erro ao rodar o bot: [cole o erro]. Corrija seguindo CLAUDE.md."
```

### Bloco 2 (25–42 min) — `/cotacao`

```bash
claude "Leia CLAUDE.md. Faça o comando /cotacao PETR4 mostrar o nome da ação, o preço em reais e a variação do dia. Implemente tudo."
```

Teste: `/cotacao PETR4` · `/cotacao VALE3` · `/cotacao XXXX`

### Bloco 3 (42–55 min) — Alerta

```bash
claude "Leia CLAUDE.md. Faça o comando /alerta PETR4 35 avisar no Telegram quando a ação atingir esse preço. Implemente tudo."
```

Teste: `/alerta PETR4 0.01` (limite baixo para disparar rápido)

### Bloco 4 (55–60 min) — Fechamento

Recapitular: **criar CLAUDE.md → prompt → Claude Code → terminal → Telegram**

Solução completa: [branch main](https://github.com/mateuscqueiros/telegram-stock-bot/tree/main)

**Professor:** [docs/GUIA_PROFESSOR.md](docs/GUIA_PROFESSOR.md) · [docs/GUIA_INSTRUTOR.md](docs/GUIA_INSTRUTOR.md)

---

## Comandos úteis do Claude Code

| Comando | O que faz |
|---|---|
| `claude` | Modo interativo |
| `claude "tarefa"` | One-shot |
| `claude -c` | Continuar conversa anterior |
| `/help` | Ajuda dentro da sessão |

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
