# Checklist — Workshop Bot Telegram B3 (Claude Code)

**Envie este checklist aos alunos 48h antes da aula.**

---

Olá!

Neste workshop você vai **dirigir o Claude Code** para construir um bot de Telegram — não precisa saber Python.

## Pré-requisitos

- [ ] **Claude Code** ativo (plano Pro, Max ou API Anthropic)
- [ ] Python 3.11+ — `python --version`
- [ ] Git — `git --version`
- [ ] Token Telegram — [@BotFather](https://t.me/BotFather) → `/newbot`
- [ ] Token brapi.dev (recomendado) — [brapi.dev](https://brapi.dev)
- [ ] Telegram no celular

## Instalar Claude Code

**Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**macOS / Linux:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Teste: `claude --version` (faça login na primeira execução)

## Setup do projeto

```bash
git clone -b starter git@github.com:mateuscqueiros/telegram-stock-bot.git
cd telegram-stock-bot

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env               # Windows: copy .env.example .env
```

Edite o **`.env`**:
```env
TELEGRAM_TOKEN=seu_token_do_botfather
BRAPI_TOKEN=seu_token_brapi
```

Smoke test: `python -c "import telegram, httpx; print('OK')"`

## Na aula

1. Abra o terminal **na pasta do projeto**
2. Rode `claude` ou `claude "prompt"`
3. **Aprove os diffs** que o Claude Code propõe
4. Valide com `python -m bot.main` e teste no Telegram

Links:
- [Repo starter](https://github.com/mateuscqueiros/telegram-stock-bot/tree/starter)
- [Solução](https://github.com/mateuscqueiros/telegram-stock-bot/tree/main)
- [Docs Claude Code](https://code.claude.com/docs)
