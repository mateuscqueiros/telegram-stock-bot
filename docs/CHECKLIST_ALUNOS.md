# Checklist — Workshop Bot Telegram B3 (Claude Code)

**Envie este checklist aos alunos 48h antes da aula.**

---

Olá!

Neste workshop você vai **pilotar o Claude Code** para construir um bot de Telegram — não precisa saber Python.

O foco é aprender **gerenciamento de sessão**, atalhos e arquivos `.md` do Claude Code. O bot é o projeto de prática.

## Pré-requisitos

- [ ] **Claude Code** ativo (plano Pro, Max ou API Anthropic)
- [ ] Python 3.11+ — `python --version`
- [ ] Git — `git --version`
- [ ] **Cursor** (ou VS Code) — terminal integrado
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

## Na aula

O workshop tem **3 partes**:

| Parte | Tempo | O quê |
|---|---|---|
| 1 | 15 min | Claude Code: sessão, atalhos, arquivos `.md` |
| 2 | 15 min | Construir o bot via prompts |
| 3 | Aberta | Arquitetura, produção, prompt mestre |

### Durante a aula

1. **Cursor** → **File → Open Folder** → pasta `telegram-stock-bot`
2. Terminal (**`` Ctrl+` ``**) — confirme `(.venv)` no prompt
3. Rode `claude` ou `claude "prompt"`
4. **Aprove os diffs** que o Claude Code propõe
5. Valide com `python -m bot.main` e teste no Telegram

### Dica importante — gerenciamento de sessão

Entre cada parte, o palestrante vai pedir `/clear` no Claude Code.

> **Tarefa nova, sessão nova.** Isso evita que o contexto de uma parte atrapalhe a outra.

Comandos úteis: `/context`, `/clear`, `/compact`, `/rewind`

Referência: [docs/CLAUDE_CODE.md](https://github.com/mateuscqueiros/telegram-stock-bot/blob/main/docs/CLAUDE_CODE.md)

## Links

- [Repo starter](https://github.com/mateuscqueiros/telegram-stock-bot/tree/starter)
- [Solução](https://github.com/mateuscqueiros/telegram-stock-bot/tree/main)
- [Cheat-sheet Claude Code](https://github.com/mateuscqueiros/telegram-stock-bot/blob/main/docs/CLAUDE_CODE.md)
- [Docs Claude Code](https://code.claude.com/docs)
