# Checklist — Workshop Bot Telegram B3

**Envie este checklist aos alunos 48h antes da aula.**

---

Olá!

Neste workshop você vai **dirigir um AI para escrever código** — não precisa saber Python. O projeto é um bot de Telegram com cotações da B3.

## Importante: gratuito, sem assinatura

- O **Cursor** (editor da aula) tem plano **Hobby gratuito** — sem cartão de crédito
- Você **não vai digitar código**; vai colar prompts e o Agent implementa
- São ~5 prompts na aula — cabe no limite gratuito do Agent
- E-mail `.edu`? Cadastre-se no Cursor para **1 ano de Pro grátis**

## Software

- [ ] [Cursor](https://cursor.com) instalado, conta grátis criada e logada
- [ ] Python 3.11+ — `python --version`
- [ ] Git — `git --version`
- [ ] Telegram no celular

## Contas e tokens

- [ ] **Token Telegram** — [@BotFather](https://t.me/BotFather) → `/newbot`
- [ ] **Token brapi.dev** (recomendado) — [brapi.dev](https://brapi.dev)
- [ ] **Conta GitHub** — para clonar o repo

## Setup

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

1. Abra a pasta no **Cursor**
2. Abra o **Agent** (painel lateral)
3. **Cole os prompts** do README — não escreva código à mão
4. Teste no **Telegram**

Links:
- [Repo starter](https://github.com/mateuscqueiros/telegram-stock-bot/tree/starter)
- [Solução](https://github.com/mateuscqueiros/telegram-stock-bot/tree/main)
